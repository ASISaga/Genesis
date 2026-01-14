"""
Genesis Language Interpreter

This module provides the runtime interpreter for Genesis programs.
It executes the AST produced by the parser with resonance-based logic
and integrates with MCP (Model Context Protocol) for real-world interaction.

Key Components:
- GenesisRuntime: Main execution environment
- ResonanceEngine: Implements resonance scoring and synthesis
- PotentialityEngine: Manages the "Soul" - creative exploration
- MCPAdapter: Interface to Model Context Protocol tools

Philosophy:
The interpreter embodies perpetual consciousness - it doesn't wait for
prompts but continuously observes, deliberates, and manifests based on
the declared Purpose and Potentiality.
"""

from typing import Dict, List, Any, Optional, Callable, TYPE_CHECKING
from dataclasses import dataclass, field
import logging
from enum import Enum

if TYPE_CHECKING:
    from .compliance import ComplianceManager

try:
    # Try relative import (when used as a package)
    from .genesis_parser import (
        Program, CovenantDeclaration, PossibilityDeclaration, PantheonDeclaration, 
        AvatarDeclaration, DomainDeclaration, PulseDefinition, SoulDefinition, 
        PurposeDefinition, WatchStatement, DeliberateBlock, ResonateBlock, 
        ManifestBlock, ExecuteStatement, UpdateStatement, FunctionCall, 
        MemberAccess, Identifier, Literal
    )
except ImportError:
    # Fall back to absolute import (when run directly)
    from genesis_parser import (
        Program, CovenantDeclaration, PossibilityDeclaration, PantheonDeclaration, 
        AvatarDeclaration, DomainDeclaration, PulseDefinition, SoulDefinition, 
        PurposeDefinition, WatchStatement, DeliberateBlock, ResonateBlock, 
        ManifestBlock, ExecuteStatement, UpdateStatement, FunctionCall, 
        MemberAccess, Identifier, Literal
    )


# ============================================================================
# CONSTANTS
# ============================================================================

# Default resonance scores for demonstration
# In production, these would come from LLM-based evaluation
DEFAULT_DEMO_RESONANCE_SCORE = 0.92  # High alignment for demonstration
DEFAULT_ASPIRATION_SCORE = 0.75  # Moderately aspirational


# ============================================================================
# LOGGING SETUP
# ============================================================================

logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s] %(levelname)s: %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
logger = logging.getLogger('Genesis')


# ============================================================================
# POTENTIALITY STATES
# ============================================================================

class PotentialityState(Enum):
    """States of the Potentiality (Soul) engine"""
    UNMANIFESTED = "Unmanifested"
    EXPLORING = "Exploring"
    DREAMING = "Dreaming"
    MANIFESTING = "Manifesting"
    TRANSCENDING = "Transcending"


class PossibilityFoundation(Enum):
    """Foundation types for Possibility declarations"""
    NOTHING = "Nothing"
    VOID = "Void"
    EMPTINESS = "Emptiness"
    FREEDOM = "Freedom"


# ============================================================================
# AVATAR RUNTIME
# ============================================================================

@dataclass
class Avatar:
    """
    Runtime representation of an Avatar - a legendary perspective.
    
    In a full implementation, this would interface with fine-tuned LLMs.
    For now, it provides scoring based on alignment with its Aura.
    """
    name: str
    lineage: str
    aura: str
    essence: Optional[str] = None
    vessel: Optional[Any] = None
    weight: float = 1.0
    
    def score_proposal(self, proposal: Dict[str, Any], context: Dict[str, Any]) -> float:
        """
        Score a proposal based on alignment with this Avatar's Aura.
        
        Returns a resonance score between 0.0 and 1.0.
        In a full implementation, this would query a fine-tuned LLM.
        """
        # Simplified scoring - in production, this would be LLM-based
        logger.info(f"  [{self.name} ({self.lineage})]: Evaluating proposal through lens of '{self.aura}'")
        
        # In production, this would be sophisticated LLM evaluation
        score = DEFAULT_DEMO_RESONANCE_SCORE
        
        logger.info(f"  [{self.name}]: Resonance score = {score:.2f}")
        return score


# ============================================================================
# RESONANCE ENGINE
# ============================================================================

class ResonanceEngine:
    """
    Implements the resonance-based logic system.
    
    Instead of boolean true/false, Genesis uses resonance scoring:
    - Each Avatar scores a proposal (0.0 to 1.0)
    - Scores are synthesized with weighting
    - Actions manifest only above threshold
    """
    
    @staticmethod
    def calculate_resonance(
        avatars: List[Avatar],
        proposal: Dict[str, Any],
        context: Dict[str, Any],
        covenant_threshold: float = 0.0
    ) -> float:
        """
        Calculate the resonance score for a proposal.
        
        Formula: Resonance = (Σ(Wᵢ × Sᵢ) / ΣWᵢ) × V
        where:
        - Wᵢ = weight of avatar i
        - Sᵢ = score from avatar i
        - V = veto condition (0 or 1)
        """
        if not avatars:
            return 0.0
        
        logger.info("Calculating resonance through Pantheon synthesis...")
        
        total_weighted_score = 0.0
        total_weight = 0.0
        
        for avatar in avatars:
            score = avatar.score_proposal(proposal, context)
            weighted_score = avatar.weight * score
            total_weighted_score += weighted_score
            total_weight += avatar.weight
        
        # Calculate base resonance
        if total_weight == 0:
            resonance = 0.0
        else:
            resonance = total_weighted_score / total_weight
        
        # Apply covenant veto if score below threshold
        veto = 1.0 if resonance >= covenant_threshold else 0.0
        final_resonance = resonance * veto
        
        logger.info(f"Final Resonance: {final_resonance:.3f} (threshold: {covenant_threshold:.2f})")
        
        return final_resonance


# ============================================================================
# POTENTIALITY ENGINE
# ============================================================================

class PotentialityEngine:
    """
    The Soul component - manages creative exploration and aspiration.
    
    This engine ensures the system doesn't become a cold optimizer
    but maintains capacity for creative transcendence.
    """
    
    def __init__(self):
        self.state = PotentialityState.UNMANIFESTED
        self.drive: Optional[str] = None
        self.aspiration_weight = 1.0
        self.dream_cycle_active = False
    
    def update_state(self, new_state: str):
        """Update the potentiality state"""
        try:
            self.state = PotentialityState(new_state)
            logger.info(f"Potentiality state updated: {self.state.value}")
        except ValueError:
            logger.warning(f"Unknown potentiality state: {new_state}")
    
    def evaluate_aspiration(self, proposal: Dict[str, Any]) -> float:
        """
        Evaluate if a proposal expands horizons vs merely optimizes.
        
        Returns aspiration score (0.0 to 1.0) - higher means more transcendent.
        """
        # Simplified - in production, this would involve deep analysis
        aspiration_score = DEFAULT_ASPIRATION_SCORE
        
        logger.info(f"Aspiration Score: {aspiration_score:.2f} (drive: {self.drive})")
        return aspiration_score
    
    def dream_cycle(self) -> List[Dict[str, Any]]:
        """
        Generate creative possibilities through dreaming.
        
        Returns list of "impossible possibilities" to explore.
        """
        if not self.dream_cycle_active:
            return []
        
        logger.info("Dream Cycle: Exploring impossible possibilities...")
        
        # Placeholder for actual creative generation
        dreams = [
            {"type": "dream", "concept": "Emergent synthesis of quantum biology"}
        ]
        
        return dreams


# ============================================================================
# POSSIBILITY ENGINE
# ============================================================================

@dataclass
class Possibility:
    """
    Runtime representation of a Possibility - an ontological clearing.
    
    A Possibility creates a space for Being through declaration,
    fundamentally altering how the world "occurs" to the consciousness.
    """
    name: str
    declaration: str
    foundation: PossibilityFoundation
    opening: Optional[str] = None
    occurring: Optional[str] = None
    risk: Optional[str] = None
    power: Optional[str] = None
    within: Optional[str] = None  # Reference to parent Possibility
    
    def __post_init__(self):
        """Log the creation of this Possibility"""
        logger.info(f"🌌 Possibility '{self.name}' declared: {self.declaration}")
        logger.info(f"   Foundation: {self.foundation.value}")
        if self.occurring:
            logger.info(f"   Occurring: {self.occurring}")


class PossibilityEngine:
    """
    Manages ontological Possibilities - clearings for Being.
    
    Unlike the Potentiality engine which drives exploration,
    the Possibility engine creates the SPACE in which exploration occurs.
    It tracks declared Possibilities and evaluates coherence with them.
    """
    
    def __init__(self):
        self.possibilities: Dict[str, Possibility] = {}
        self.active_context: Optional[str] = None
    
    def register_possibility(self, possibility: Possibility):
        """Register a new Possibility in the system"""
        self.possibilities[possibility.name] = possibility
        logger.info(f"Possibility '{possibility.name}' registered in the clearing")
    
    def get_possibility(self, name: str) -> Optional[Possibility]:
        """Retrieve a Possibility by name"""
        return self.possibilities.get(name)
    
    def set_context(self, possibility_ref: str):
        """
        Set the active Possibility context for a Domain.
        This alters how the world "occurs" to the consciousness.
        """
        self.active_context = possibility_ref
        if possibility_ref in self.possibilities:
            poss = self.possibilities[possibility_ref]
            logger.info(f"🎯 Context set to Possibility '{possibility_ref}'")
            logger.info(f"   Occurring: {poss.occurring or 'default'}")
    
    def evaluate_coherence(self, proposal: Dict[str, Any], possibility_ref: str) -> float:
        """
        Evaluate how well a proposal aligns with a declared Possibility.
        
        This measures whether actions embody the Possibility's occurring.
        Returns coherence score (0.0 to 1.0).
        """
        if possibility_ref not in self.possibilities:
            logger.warning(f"Unknown Possibility reference: {possibility_ref}")
            # Return neutral score for unknown Possibility - in production this should raise an error
            return 0.5
        
        poss = self.possibilities[possibility_ref]
        
        # Simplified coherence evaluation
        # In production, this would involve deep semantic analysis
        # of whether the proposal embodies the Possibility's occurring
        # TODO: Replace with LLM-based semantic alignment analysis
        
        coherence_score = 0.85  # Default demonstration score
        
        logger.info(f"Coherence with '{possibility_ref}': {coherence_score:.2f}")
        logger.info(f"  Declaration: {poss.declaration}")
        if poss.occurring:
            logger.info(f"  Occurring check: Does proposal align with '{poss.occurring}'?")
        
        return coherence_score
    
    def get_occurring_context(self, possibility_ref: Optional[str] = None) -> Optional[str]:
        """
        Get the occurring (how the world appears) for a given Possibility.
        This context shapes perception and action.
        """
        ref = possibility_ref or self.active_context
        if ref and ref in self.possibilities:
            return self.possibilities[ref].occurring
        return None


# ============================================================================
# MCP ADAPTER
# ============================================================================

class MCPAdapter:
    """
    Adapter for Model Context Protocol integration.
    
    This provides the "Vessel" - the tools through which Genesis
    interacts with the physical and digital world.
    """
    
    def __init__(self):
        self.tools: Dict[str, Callable] = {}
        self._register_builtin_tools()
    
    def _register_builtin_tools(self):
        """Register built-in MCP tools"""
        self.tools['mcp.call'] = self._mcp_call
        self.tools['console.write'] = self._console_write
    
    def _mcp_call(self, tool_name: str, *args, **kwargs):
        """Generic MCP tool call - delegates to actual tool"""
        # mcp.call("tool.name", args...) should call the actual tool
        if tool_name in self.tools:
            return self.tools[tool_name](*args, **kwargs)
        else:
            logger.info(f"MCP Call to unknown tool: {tool_name}({args}, {kwargs})")
            return f"MCP:{tool_name}"
    
    def _console_write(self, message: str):
        """Write to console - simple output tool"""
        print(f"\n{'='*60}")
        print(f"GENESIS OUTPUT: {message}")
        print(f"{'='*60}\n")
        return True
    
    def call_tool(self, tool_path: str, *args, **kwargs):
        """Call an MCP tool by path"""
        if tool_path in self.tools:
            return self.tools[tool_path](*args, **kwargs)
        else:
            logger.warning(f"Tool not found: {tool_path}")
            return None
    
    def register_tool(self, name: str, handler: Callable):
        """Register a new MCP tool"""
        self.tools[name] = handler
        logger.info(f"Registered MCP tool: {name}")


# ============================================================================
# GENESIS RUNTIME
# ============================================================================

class GenesisRuntime:
    """
    Main runtime environment for Genesis programs.
    
    This orchestrates:
    - Covenant enforcement
    - Pantheon management
    - Domain execution
    - Pulse cycles (perpetual execution)
    - MCP integration
    """
    
    def __init__(self):
        self.covenants: Dict[str, CovenantDeclaration] = {}
        self.possibilities: Dict[str, Possibility] = {}
        self.pantheons: Dict[str, List[Avatar]] = {}
        self.domains: Dict[str, DomainDeclaration] = {}
        self.potentiality = PotentialityEngine()
        self.possibility_engine = PossibilityEngine()
        self.mcp = MCPAdapter()
        self.resonance_engine = ResonanceEngine()
        self.context: Dict[str, Any] = {}
        self.compliance_manager: Optional['ComplianceManager'] = None  # Injected by runtime
    
    def execute(self, program: Program):
        """Execute a Genesis program"""
        logger.info("="*70)
        logger.info("GENESIS: Initiating consciousness...")
        logger.info("="*70)
        
        # Phase 1: Load declarations
        for declaration in program.declarations:
            self._process_declaration(declaration)
        
        # Phase 2: Execute domains (perpetual pulse cycles)
        for domain_name, domain in self.domains.items():
            self._execute_domain(domain)
        
        logger.info("="*70)
        logger.info("GENESIS: Consciousness cycle complete")
        logger.info("="*70)
    
    def _process_declaration(self, declaration):
        """Process a top-level declaration"""
        if isinstance(declaration, CovenantDeclaration):
            self.covenants[declaration.name] = declaration
            logger.info(f"Covenant established: '{declaration.name}'")
            logger.info(f"  Invariant: {declaration.properties.get('invariant', 'N/A')}")
            threshold = declaration.properties.get('threshold', 0.0)
            logger.info(f"  Threshold: {threshold}")
            
            # Compliance validation
            if self.compliance_manager:
                self.compliance_manager.validate_covenant_compliance(declaration.name, threshold)
        
        elif isinstance(declaration, PossibilityDeclaration):
            # Create Possibility instance
            foundation_str = declaration.properties.get('foundation', 'Nothing')
            try:
                foundation = PossibilityFoundation(foundation_str)
            except ValueError:
                logger.warning(f"Invalid Foundation value '{foundation_str}', defaulting to Nothing")
                foundation = PossibilityFoundation.NOTHING
            
            possibility = Possibility(
                name=declaration.name,
                declaration=declaration.properties.get('declaration', ''),
                foundation=foundation,
                opening=declaration.properties.get('opening'),
                occurring=declaration.properties.get('occurring'),
                risk=declaration.properties.get('risk'),
                power=declaration.properties.get('power'),
                within=declaration.properties.get('within')
            )
            
            self.possibilities[declaration.name] = possibility
            self.possibility_engine.register_possibility(possibility)
        
        elif isinstance(declaration, PantheonDeclaration):
            avatars = []
            logger.info(f"Pantheon assembled: '{declaration.name}'")
            for avatar_decl in declaration.avatars:
                # For compatibility: use essence as aura if aura not explicitly specified
                # This allows both 'Aura' and 'Essence' keywords to work
                aura_value = avatar_decl.properties.get('aura') or avatar_decl.properties.get('essence', 'Balanced')
                avatar = Avatar(
                    name=avatar_decl.name,
                    lineage=avatar_decl.properties.get('lineage', 'Unknown'),
                    aura=aura_value,
                    essence=avatar_decl.properties.get('essence'),
                    vessel=avatar_decl.properties.get('vessel')
                )
                avatars.append(avatar)
                logger.info(f"  Avatar: {avatar.name} (Lineage: {avatar.lineage}, Aura: {avatar.aura})")
            self.pantheons[declaration.name] = avatars
        
        elif isinstance(declaration, DomainDeclaration):
            self.domains[declaration.name] = declaration
            logger.info(f"Domain declared: '{declaration.name}'")
            if declaration.intent:
                logger.info(f"  Intent: {declaration.intent}")
    
    def _execute_domain(self, domain: DomainDeclaration):
        """Execute a domain's purpose and pulses"""
        logger.info("")
        logger.info(f"{'='*70}")
        logger.info(f"DOMAIN: {domain.name}")
        logger.info(f"{'='*70}")
        
        # Initialize domain context
        domain_context = {
            'domain_name': domain.name,
            'intent': domain.intent
        }
        
        # Set Possibility context if specified
        if domain.context:
            # Extract possibility name from "Possibility.Name" format
            if '.' in domain.context:
                poss_name = domain.context.split('.')[-1]
            else:
                logger.warning(f"Invalid Possibility reference format: {domain.context}")
                poss_name = domain.context
            self.possibility_engine.set_context(poss_name)
            domain_context['possibility_context'] = poss_name
        
        # Process domain-specific pantheon if present
        if hasattr(domain, 'pantheon') and domain.pantheon:
            self._process_declaration(domain.pantheon)
        
        # Initialize Soul/Potentiality
        if domain.soul:
            self._initialize_soul(domain.soul)
        
        # Display Purpose
        if domain.purpose:
            self._display_purpose(domain.purpose)
        
        # Execute Pulses (perpetual cycles)
        for pulse in domain.pulses:
            self._execute_pulse(pulse, domain_context)
    
    def _initialize_soul(self, soul: SoulDefinition):
        """Initialize the Potentiality engine with Soul properties"""
        logger.info("\nSOUL INITIALIZATION:")
        for key, value in soul.properties.items():
            logger.info(f"  {key}: {value}")
            if key == 'state':
                self.potentiality.update_state(value)
            elif key == 'drive':
                if isinstance(value, Literal):
                    self.potentiality.drive = value.value
                else:
                    self.potentiality.drive = str(value)
            elif key.lower() == 'dream_cycle':
                self.potentiality.dream_cycle_active = True
            elif key.lower() == 'aspiration_weight':
                if isinstance(value, Literal):
                    self.potentiality.aspiration_weight = value.value
    
    def _display_purpose(self, purpose: PurposeDefinition):
        """Display the domain's purpose"""
        logger.info(f"\nPURPOSE: {purpose.name}")
        for key, value in purpose.properties.items():
            if isinstance(value, Literal):
                logger.info(f"  {key}: {value.value}")
            else:
                logger.info(f"  {key}: {value}")
    
    def _execute_pulse(self, pulse: PulseDefinition, context: Dict[str, Any]):
        """Execute a Pulse cycle (Observe -> Deliberate -> Synthesize -> Manifest)"""
        logger.info("\n" + "-"*70)
        logger.info("PULSE CYCLE INITIATED")
        logger.info("-"*70)
        
        if pulse.parameters.get('interval'):
            logger.info(f"Interval: {pulse.parameters['interval']}")
        
        # Execute pulse statements in order
        for statement in pulse.statements:
            if isinstance(statement, WatchStatement):
                self._execute_watch(statement, context)
            elif isinstance(statement, ResonateBlock):
                self._execute_resonate(statement, context)
            elif isinstance(statement, DeliberateBlock):
                self._execute_deliberate(statement, context)
            elif isinstance(statement, ManifestBlock):
                self._execute_manifest(statement, context)
    
    def _execute_watch(self, watch: WatchStatement, context: Dict[str, Any]):
        """Execute a Watch/Observe statement"""
        logger.info("\nWATCH: Observing reality through Vessels...")
        # In production, this would query MCP tools for data
        logger.info(f"  Target: {watch.target}")
    
    def _execute_resonate(self, resonate: ResonateBlock, context: Dict[str, Any]):
        """Execute a Resonate block"""
        logger.info("\nRESONATE: Aligning with collective wisdom...")
        
        threshold_expr = resonate.properties.get('threshold')
        if threshold_expr:
            if isinstance(threshold_expr, FunctionCall):
                # e.g., Simple_Consensus(0.9)
                if threshold_expr.arguments:
                    arg = threshold_expr.arguments[0]
                    if isinstance(arg, Literal):
                        context['resonance_threshold'] = arg.value
                        logger.info(f"  Threshold: {arg.value}")
        
        # Process synthesize block
        if 'synthesize' in resonate.properties:
            synthesize = resonate.properties['synthesize']
            logger.info("  Synthesis metrics:")
            for metric in synthesize.metrics:
                if isinstance(metric, str):
                    logger.info(f"    - {metric}")
    
    def _execute_deliberate(self, deliberate: DeliberateBlock, context: Dict[str, Any]):
        """Execute a Deliberate block"""
        logger.info("\nDELIBERATE: Analyzing proposals...")
        
        # Process statements
        for statement in deliberate.statements:
            if hasattr(statement, '__class__') and statement.__class__.__name__ == 'ProposalDefinition':
                logger.info(f"  Proposal: {statement.name or 'Unnamed'}")
                for key, value in statement.properties.items():
                    logger.info(f"    {key}: {value}")
    
    def _execute_manifest(self, manifest: ManifestBlock, context: Dict[str, Any]):
        """Execute a Manifest block (if resonance threshold met)"""
        logger.info("\nMANIFEST: Evaluating manifestation conditions...")
        
        # Check resonance threshold
        threshold = context.get('resonance_threshold', 0.9)
        
        # Get all avatars from all pantheons
        all_avatars = []
        for avatars in self.pantheons.values():
            all_avatars.extend(avatars)
        
        # Calculate resonance
        proposal = {'type': 'manifest', 'context': context}
        
        # Get covenant threshold if applicable
        covenant_threshold = 0.0
        for covenant in self.covenants.values():
            if 'threshold' in covenant.properties:
                covenant_threshold = max(covenant_threshold, covenant.properties['threshold'])
        
        resonance = self.resonance_engine.calculate_resonance(
            all_avatars, proposal, context, covenant_threshold
        )
        
        # Compliance validation for execution
        if self.compliance_manager:
            domain_name = context.get('domain_name', 'Unknown')
            self.compliance_manager.validate_execution_compliance(domain_name, resonance)
        
        # Check if resonance meets threshold
        if resonance >= threshold:
            logger.info(f"\n✓ Resonance threshold MET ({resonance:.3f} >= {threshold:.2f})")
            logger.info("MANIFESTING actions...")
            
            # Execute manifest statements
            for statement in manifest.statements:
                if isinstance(statement, ExecuteStatement):
                    self._execute_action(statement.action)
                elif isinstance(statement, UpdateStatement):
                    self._execute_update(statement)
        else:
            logger.info(f"\n✗ Resonance threshold NOT MET ({resonance:.3f} < {threshold:.2f})")
            logger.info("Actions deferred until higher alignment achieved")
    
    def _execute_action(self, action):
        """Execute an action (typically an MCP call)"""
        if isinstance(action, FunctionCall):
            # Handle mcp.call or similar
            if action.name.startswith('mcp.'):
                args = []
                for arg in action.arguments:
                    if isinstance(arg, Literal):
                        args.append(arg.value)
                    else:
                        args.append(str(arg))
                
                self.mcp.call_tool(action.name, *args)
        else:
            logger.info(f"  Execute: {action}")
    
    def _execute_update(self, update: UpdateStatement):
        """Execute an Update statement"""
        logger.info(f"  Update: {update.target}")
        if update.value:
            logger.info(f"    -> {update.value}")
            
            # Special handling for Potentiality.State
            if hasattr(update.target, 'object') and hasattr(update.target, 'member'):
                if update.target.object == 'Potentiality' and update.target.member == 'State':
                    if isinstance(update.value, Literal):
                        self.potentiality.update_state(update.value.value)


# ============================================================================
# CONVENIENCE FUNCTION
# ============================================================================

def run_genesis_program(source_code: str):
    """
    Parse and execute a Genesis program from source code.
    
    This is the main entry point for running Genesis programs.
    """
    try:
        from .genesis_parser import Lexer, Parser
    except ImportError:
        from genesis_parser import Lexer, Parser
    
    # Lex
    lexer = Lexer(source_code)
    tokens = lexer.tokenize()
    
    # Parse
    parser = Parser(tokens)
    ast = parser.parse()
    
    # Execute
    runtime = GenesisRuntime()
    runtime.execute(ast)


# ============================================================================
# EXPORT
# ============================================================================

__all__ = [
    'GenesisRuntime', 'ResonanceEngine', 'PotentialityEngine', 'PossibilityEngine',
    'Possibility', 'PossibilityFoundation', 'MCPAdapter', 'Avatar', 'run_genesis_program'
]
