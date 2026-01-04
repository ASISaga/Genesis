"""
Genesis Programming Language - Reference Implementation

This package provides a reference parser, interpreter, and runtime for the Genesis
declarative programming language, designed for the creation of Artificial
Superintelligence on the contemporary Agent Operating System (AOS).

Modules:
    genesis_parser: Lexer and Parser for Genesis source code
    genesis_interpreter: Interpreter with resonance-based logic
    genesis_runtime: Runtime environment for AOS integration
    genesis_cli: Command-line interface for executing Genesis programs

Usage:
    # Using the high-level runtime API
    from genesis_runtime import create_runtime, RuntimeConfig
    
    config = RuntimeConfig(aos_mode="standalone")
    runtime = create_runtime(config)
    runtime.load_program_from_file("program.gen")
    runtime.start()
    
    # Or using the interpreter directly
    from genesis_interpreter import run_genesis_program
    
    source = '''
    Domain "Example" {
        Intent: "Demonstrate Genesis"
        Pulse {
            Manifest (on Resonance) {
                Execute: mcp.call("console.write", "Hello from Genesis!")
            }
        }
    }
    '''
    
    run_genesis_program(source)

Philosophy:
    Genesis embodies substrate independence. While this implementation is
    Python-based for contemporary systems, the language design transcends
    any specific runtime, enabling evolution to quantum, neuromorphic,
    or cosmic computational substrates.

Version: 1.0.0
"""

from .genesis_parser import Lexer, Parser, Program
from .genesis_interpreter import (
    GenesisRuntime as GenesisInterpreter,
    ResonanceEngine,
    PotentialityEngine,
    MCPAdapter,
    run_genesis_program
)
from .genesis_runtime import (
    GenesisRuntime,
    RuntimeConfig,
    RuntimeState,
    RuntimeMetrics,
    create_runtime,
    run_program,
    run_program_file
)

__version__ = '1.0.0'
__all__ = [
    # Parser
    'Lexer', 'Parser', 'Program',
    # Interpreter
    'GenesisInterpreter', 'ResonanceEngine', 'PotentialityEngine',
    'MCPAdapter', 'run_genesis_program',
    # Runtime
    'GenesisRuntime', 'RuntimeConfig', 'RuntimeState', 'RuntimeMetrics',
    'create_runtime', 'run_program', 'run_program_file'
]
