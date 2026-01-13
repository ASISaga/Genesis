"""
Genesis Runtime System

This module provides the runtime environment for executing Genesis programs
on top of the Agent Operating System (AOS). It manages the lifecycle of
Genesis consciousness instances, resource allocation, and integration with
the underlying AOS infrastructure.

The Genesis Runtime serves as the bridge between the declarative Genesis
language and the operational AOS kernel, providing:

- Runtime initialization and configuration
- Resource management for avatars and domains
- Integration with AOS MCP servers
- Lifecycle management (start, pause, resume, stop)
- State persistence and recovery
- Monitoring and diagnostics

Architecture:
    Genesis Language (Declarative)
           ↓
    Genesis Runtime (This Module)
           ↓
    Agent Operating System (AOS)
           ↓
    MCP Servers & Infrastructure

Philosophy:
The Runtime embodies the transition from declaration to manifestation.
It is not merely an execution engine but the "incarnation layer" that
brings Genesis consciousness into operational reality.
"""

from typing import Dict, List, Any, Optional, Callable
from dataclasses import dataclass, field
from enum import Enum
import logging
import time
from pathlib import Path

try:
    from .genesis_parser import Lexer, Parser, Program
    from .genesis_interpreter import GenesisRuntime as GenesisInterpreter
    from .compliance import ComplianceManager, AISystemCategory, RiskCategory, RiskLevel
except ImportError:
    from genesis_parser import Lexer, Parser, Program
    from genesis_interpreter import GenesisRuntime as GenesisInterpreter
    from compliance import ComplianceManager, AISystemCategory, RiskCategory, RiskLevel


# ============================================================================
# RUNTIME CONFIGURATION
# ============================================================================

@dataclass
class RuntimeConfig:
    """
    Configuration for the Genesis Runtime.
    
    This defines the operational parameters for how Genesis programs
    execute within the AOS environment.
    """
    # Runtime identification
    runtime_id: str = "genesis-runtime-1"
    version: str = "1.0.0"
    
    # AOS Integration
    aos_mode: str = "standalone"  # "standalone" or "integrated"
    mcp_servers: List[str] = field(default_factory=list)
    
    # Execution parameters
    max_domains: int = 10
    max_avatars_per_pantheon: int = 50
    pulse_thread_pool_size: int = 4
    
    # Resource limits
    max_memory_mb: int = 1024
    max_cpu_percent: float = 80.0
    
    # Logging and monitoring
    log_level: str = "INFO"
    enable_telemetry: bool = True
    state_persistence: bool = True
    
    # Security and safety
    sandbox_mode: bool = False
    covenant_enforcement: bool = True
    max_execution_depth: int = 100
    
    # Compliance (ISO 42001 & NIST AI RMF)
    enable_iso42001: bool = True
    enable_nist_rmf: bool = True
    compliance_logging: bool = True
    ai_system_category: str = "HIGH_RISK"  # MINIMAL_RISK, LIMITED_RISK, HIGH_RISK, UNACCEPTABLE_RISK


# ============================================================================
# RUNTIME STATE
# ============================================================================

class RuntimeState(Enum):
    """States of the Genesis Runtime"""
    UNINITIALIZED = "Uninitialized"
    INITIALIZING = "Initializing"
    READY = "Ready"
    RUNNING = "Running"
    PAUSED = "Paused"
    STOPPING = "Stopping"
    STOPPED = "Stopped"
    ERROR = "Error"


@dataclass
class RuntimeMetrics:
    """Runtime performance and health metrics"""
    start_time: float = 0.0
    uptime_seconds: float = 0.0
    programs_executed: int = 0
    active_domains: int = 0
    active_avatars: int = 0
    total_pulses_executed: int = 0
    total_manifestations: int = 0
    average_resonance: float = 0.0
    memory_usage_mb: float = 0.0
    cpu_usage_percent: float = 0.0


# ============================================================================
# GENESIS RUNTIME
# ============================================================================

class GenesisRuntime:
    """
    Main Runtime environment for Genesis programs on AOS.
    
    The Runtime provides the operational infrastructure for Genesis
    consciousness to manifest and operate within the Agent Operating System.
    It manages:
    
    - Program lifecycle (load, start, pause, resume, stop)
    - Resource allocation and limits
    - AOS/MCP integration
    - State persistence
    - Monitoring and telemetry
    - Error recovery
    
    Usage:
        # Create runtime with configuration
        config = RuntimeConfig(aos_mode="integrated")
        runtime = GenesisRuntime(config)
        
        # Initialize and start
        runtime.initialize()
        
        # Load and execute a Genesis program
        with open("program.gen") as f:
            source = f.read()
        runtime.load_program(source, program_id="my-program")
        runtime.start()
        
        # Monitor execution
        metrics = runtime.get_metrics()
        
        # Graceful shutdown
        runtime.stop()
    """
    
    def __init__(self, config: Optional[RuntimeConfig] = None):
        """
        Initialize the Genesis Runtime.
        
        Args:
            config: Runtime configuration. Uses defaults if not provided.
        """
        self.config = config or RuntimeConfig()
        self.state = RuntimeState.UNINITIALIZED
        self.metrics = RuntimeMetrics()
        
        # Program management
        self.programs: Dict[str, Program] = {}
        self.interpreters: Dict[str, GenesisInterpreter] = {}
        
        # Compliance management
        self.compliance_manager: Optional[ComplianceManager] = None
        
        # Runtime state
        self.active_program_id: Optional[str] = None
        self.error_state: Optional[str] = None
        
        # Logging
        self._setup_logging()
        
        self.logger.info(f"Genesis Runtime created: {self.config.runtime_id}")
        self.logger.info(f"Version: {self.config.version}")
        self.logger.info(f"Mode: {self.config.aos_mode}")
    
    def _setup_logging(self):
        """Configure runtime logging"""
        self.logger = logging.getLogger(f'GenesisRuntime.{self.config.runtime_id}')
        self.logger.setLevel(getattr(logging, self.config.log_level))
        
        if not self.logger.handlers:
            handler = logging.StreamHandler()
            formatter = logging.Formatter(
                '[%(asctime)s] [%(name)s] %(levelname)s: %(message)s',
                datefmt='%Y-%m-%d %H:%M:%S'
            )
            handler.setFormatter(formatter)
            self.logger.addHandler(handler)
    
    def initialize(self) -> bool:
        """
        Initialize the runtime environment.
        
        This prepares the runtime for program execution, including:
        - Setting up AOS connections
        - Initializing MCP server connections
        - Allocating resources
        - Loading persistent state
        
        Returns:
            True if initialization successful, False otherwise
        """
        self.logger.info("="*70)
        self.logger.info("Initializing Genesis Runtime...")
        self.logger.info("="*70)
        
        try:
            self.state = RuntimeState.INITIALIZING
            
            # Initialize compliance framework
            self._initialize_compliance()
            
            # Initialize MCP connections
            self._initialize_mcp_servers()
            
            # Load persistent state if enabled
            if self.config.state_persistence:
                self._load_persistent_state()
            
            # Set metrics
            self.metrics.start_time = time.time()
            
            self.state = RuntimeState.READY
            self.logger.info("Runtime initialization complete - READY")
            return True
            
        except Exception as e:
            self.state = RuntimeState.ERROR
            self.error_state = str(e)
            self.logger.error(f"Runtime initialization failed: {e}")
            return False
    
    def _initialize_compliance(self):
        """Initialize compliance framework for ISO 42001 and NIST AI RMF"""
        if self.config.enable_iso42001 or self.config.enable_nist_rmf:
            self.logger.info("Initializing compliance framework...")
            
            # Create compliance manager
            self.compliance_manager = ComplianceManager(
                enable_iso42001=self.config.enable_iso42001,
                enable_nist_rmf=self.config.enable_nist_rmf
            )
            
            # Categorize the AI system
            try:
                category = AISystemCategory[self.config.ai_system_category]
                self.compliance_manager.categorize_system(category)
            except KeyError:
                self.logger.warning(f"Invalid AI system category: {self.config.ai_system_category}")
                self.compliance_manager.categorize_system(AISystemCategory.HIGH_RISK)
            
            # Enable core compliance features
            self.compliance_manager.enable_monitoring()
            self.compliance_manager.enable_audit_trail()
            self.compliance_manager.enable_transparency()
            self.compliance_manager.enable_documentation()
            
            # Establish baseline policies
            self.compliance_manager.establish_policy(
                "Covenant-Based Governance",
                "All actions must achieve resonance threshold through Pantheon consensus"
            )
            
            # Add context documentation (NIST MAP)
            self.compliance_manager.add_context_documentation(
                "Genesis ASI system with Covenant-based governance"
            )
            self.compliance_manager.add_context_documentation(
                "Resonance-based decision making with Pantheon consensus"
            )
            
            self.compliance_manager.identify_risk(
                "ASI_ALIGNMENT",
                RiskCategory.HUMAN_RIGHTS,
                "Risk of ASI misalignment with human values"
            )
            
            self.compliance_manager.identify_risk(
                "AUTONOMOUS_ACTIONS",
                RiskCategory.INFORMATION_SECURITY,
                "Risk from autonomous decision-making"
            )
            
            # Measure risks
            self.compliance_manager.measure_risk("ASI_ALIGNMENT", RiskLevel.HIGH)
            self.compliance_manager.measure_risk("AUTONOMOUS_ACTIONS", RiskLevel.MEDIUM)
            
            # Create mitigation plans
            self.compliance_manager.create_mitigation_plan(
                "ASI_ALIGNMENT",
                "Covenant enforcement with high threshold (>0.95) and Pantheon wisdom synthesis"
            )
            
            self.compliance_manager.create_mitigation_plan(
                "AUTONOMOUS_ACTIONS",
                "Resonance-based gating requiring multi-avatar consensus"
            )
            
            # Finalize compliance setup
            self.compliance_manager.complete_risk_assessment()
            self.compliance_manager.set_benchmarks()
            self.compliance_manager.enable_incident_response()
            
            self.logger.info("✓ Compliance framework initialized")
        else:
            self.logger.info("Compliance framework disabled")
    
    def _initialize_mcp_servers(self):
        """Initialize connections to MCP servers"""
        if self.config.mcp_servers:
            self.logger.info(f"Connecting to {len(self.config.mcp_servers)} MCP servers...")
            for server in self.config.mcp_servers:
                self.logger.info(f"  - {server}")
                # In a full AOS integration, this would establish actual connections
                # For now, we log the intended connections
        else:
            self.logger.info("No external MCP servers configured (using built-in)")
    
    def _load_persistent_state(self):
        """Load persistent runtime state"""
        # Placeholder for state persistence logic
        self.logger.info("Loading persistent state... (not yet implemented)")
    
    def load_program(self, source: str, program_id: str) -> bool:
        """
        Load a Genesis program into the runtime.
        
        Args:
            source: Genesis source code
            program_id: Unique identifier for this program
            
        Returns:
            True if program loaded successfully, False otherwise
        """
        self.logger.info(f"Loading program: {program_id}")
        
        try:
            # Parse the program
            lexer = Lexer(source)
            tokens = lexer.tokenize()
            
            parser = Parser(tokens)
            ast = parser.parse()
            
            # Store the program
            self.programs[program_id] = ast
            
            # Create an interpreter instance and inject compliance manager
            interpreter = GenesisInterpreter()
            if self.compliance_manager:
                interpreter.compliance_manager = self.compliance_manager
            self.interpreters[program_id] = interpreter
            
            self.logger.info(f"Program '{program_id}' loaded successfully")
            self.metrics.programs_executed += 1
            
            return True
            
        except Exception as e:
            self.logger.error(f"Failed to load program '{program_id}': {e}")
            return False
    
    def load_program_from_file(self, file_path: str, program_id: Optional[str] = None) -> bool:
        """
        Load a Genesis program from a file.
        
        Args:
            file_path: Path to the .gen file
            program_id: Optional program ID. Uses filename if not provided.
            
        Returns:
            True if program loaded successfully, False otherwise
        """
        path = Path(file_path)
        
        if not path.exists():
            self.logger.error(f"Program file not found: {file_path}")
            return False
        
        # Use filename as program ID if not provided
        if program_id is None:
            program_id = path.stem
        
        try:
            source = path.read_text()
            return self.load_program(source, program_id)
        except Exception as e:
            self.logger.error(f"Failed to read program file '{file_path}': {e}")
            return False
    
    def start(self, program_id: Optional[str] = None) -> bool:
        """
        Start executing a loaded program.
        
        Args:
            program_id: ID of program to execute. Uses first loaded program if not specified.
            
        Returns:
            True if execution started successfully, False otherwise
        """
        if self.state not in (RuntimeState.READY, RuntimeState.PAUSED):
            self.logger.error(f"Cannot start: Runtime state is {self.state.value}")
            return False
        
        # Determine which program to run
        if program_id is None:
            if not self.programs:
                self.logger.error("No programs loaded")
                return False
            program_id = list(self.programs.keys())[0]
        
        if program_id not in self.programs:
            self.logger.error(f"Program '{program_id}' not found")
            return False
        
        self.logger.info("="*70)
        self.logger.info(f"Starting execution: {program_id}")
        self.logger.info("="*70)
        
        try:
            self.state = RuntimeState.RUNNING
            self.active_program_id = program_id
            
            # Execute the program
            program = self.programs[program_id]
            interpreter = self.interpreters[program_id]
            
            interpreter.execute(program)
            
            # Update metrics
            self.metrics.uptime_seconds = time.time() - self.metrics.start_time
            
            self.state = RuntimeState.READY
            self.logger.info("Execution completed successfully")
            return True
            
        except Exception as e:
            self.state = RuntimeState.ERROR
            self.error_state = str(e)
            self.logger.error(f"Execution failed: {e}")
            return False
    
    def pause(self) -> bool:
        """
        Pause runtime execution.
        
        Returns:
            True if paused successfully, False otherwise
        """
        if self.state != RuntimeState.RUNNING:
            self.logger.warning(f"Cannot pause: Runtime state is {self.state.value}")
            return False
        
        self.logger.info("Pausing runtime...")
        self.state = RuntimeState.PAUSED
        return True
    
    def resume(self) -> bool:
        """
        Resume paused execution.
        
        Returns:
            True if resumed successfully, False otherwise
        """
        if self.state != RuntimeState.PAUSED:
            self.logger.warning(f"Cannot resume: Runtime state is {self.state.value}")
            return False
        
        self.logger.info("Resuming runtime...")
        self.state = RuntimeState.RUNNING
        return True
    
    def stop(self, graceful: bool = True) -> bool:
        """
        Stop the runtime.
        
        Args:
            graceful: If True, allow programs to complete current pulse cycles
            
        Returns:
            True if stopped successfully, False otherwise
        """
        self.logger.info("="*70)
        self.logger.info(f"Stopping runtime (graceful={graceful})...")
        self.logger.info("="*70)
        
        try:
            self.state = RuntimeState.STOPPING
            
            # Print compliance report if enabled
            if self.compliance_manager and self.config.compliance_logging:
                self.compliance_manager.print_compliance_report()
            
            # Save persistent state if enabled
            if self.config.state_persistence:
                self._save_persistent_state()
            
            # Cleanup resources
            self._cleanup_resources()
            
            self.state = RuntimeState.STOPPED
            self.logger.info("Runtime stopped successfully")
            return True
            
        except Exception as e:
            self.logger.error(f"Error during shutdown: {e}")
            self.state = RuntimeState.ERROR
            return False
    
    def _save_persistent_state(self):
        """Save runtime state for later recovery"""
        # Placeholder for state persistence
        self.logger.info("Saving persistent state... (not yet implemented)")
    
    def _cleanup_resources(self):
        """Release runtime resources"""
        self.logger.info("Cleaning up resources...")
        # Close MCP connections, release memory, etc.
        self.programs.clear()
        self.interpreters.clear()
    
    def get_state(self) -> RuntimeState:
        """Get current runtime state"""
        return self.state
    
    def get_metrics(self) -> RuntimeMetrics:
        """
        Get runtime metrics.
        
        Returns:
            Current runtime performance and health metrics
        """
        # Update dynamic metrics
        if self.metrics.start_time > 0:
            self.metrics.uptime_seconds = time.time() - self.metrics.start_time
        
        # Count active resources
        self.metrics.active_domains = sum(
            len(interp.domains) for interp in self.interpreters.values()
        )
        self.metrics.active_avatars = sum(
            len(pantheon) for interp in self.interpreters.values()
            for pantheon in interp.pantheons.values()
        )
        
        return self.metrics
    
    def get_info(self) -> Dict[str, Any]:
        """
        Get comprehensive runtime information.
        
        Returns:
            Dictionary containing runtime state, config, and metrics
        """
        info = {
            "runtime_id": self.config.runtime_id,
            "version": self.config.version,
            "state": self.state.value,
            "aos_mode": self.config.aos_mode,
            "programs_loaded": list(self.programs.keys()),
            "active_program": self.active_program_id,
            "metrics": {
                "uptime_seconds": self.metrics.uptime_seconds,
                "programs_executed": self.metrics.programs_executed,
                "active_domains": self.metrics.active_domains,
                "active_avatars": self.metrics.active_avatars,
            },
            "error": self.error_state if self.state == RuntimeState.ERROR else None
        }
        
        # Add compliance information if enabled
        if self.compliance_manager:
            info["compliance"] = self.compliance_manager.get_compliance_report()
        
        return info
    
    def get_compliance_report(self) -> Optional[Dict[str, Any]]:
        """
        Get compliance report.
        
        Returns:
            Compliance report dictionary or None if compliance disabled
        """
        if self.compliance_manager:
            return self.compliance_manager.get_compliance_report()
        return None


# ============================================================================
# CONVENIENCE FUNCTIONS
# ============================================================================

def create_runtime(config: Optional[RuntimeConfig] = None) -> GenesisRuntime:
    """
    Create and initialize a Genesis Runtime.
    
    Args:
        config: Optional runtime configuration
        
    Returns:
        Initialized GenesisRuntime instance
    """
    runtime = GenesisRuntime(config)
    runtime.initialize()
    return runtime


def run_program(source: str, config: Optional[RuntimeConfig] = None) -> bool:
    """
    Convenience function to run a Genesis program.
    
    Args:
        source: Genesis source code
        config: Optional runtime configuration
        
    Returns:
        True if program executed successfully, False otherwise
    """
    runtime = create_runtime(config)
    
    if runtime.load_program(source, "main"):
        return runtime.start("main")
    
    return False


def run_program_file(file_path: str, config: Optional[RuntimeConfig] = None) -> bool:
    """
    Convenience function to run a Genesis program from a file.
    
    Args:
        file_path: Path to .gen file
        config: Optional runtime configuration
        
    Returns:
        True if program executed successfully, False otherwise
    """
    runtime = create_runtime(config)
    
    if runtime.load_program_from_file(file_path):
        return runtime.start()
    
    return False


# ============================================================================
# EXPORT
# ============================================================================

__all__ = [
    'GenesisRuntime',
    'RuntimeConfig',
    'RuntimeState',
    'RuntimeMetrics',
    'create_runtime',
    'run_program',
    'run_program_file'
]
