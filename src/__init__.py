"""
Genesis Programming Language - Reference Implementation

This package provides a reference parser and interpreter for the Genesis
declarative programming language, designed for the creation of Artificial
Superintelligence on the contemporary Agent Operating System (AOS).

Modules:
    genesis_parser: Lexer and Parser for Genesis source code
    genesis_interpreter: Runtime interpreter with resonance-based logic
    genesis_cli: Command-line interface for executing Genesis programs

Usage:
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
    GenesisRuntime,
    ResonanceEngine,
    PotentialityEngine,
    MCPAdapter,
    run_genesis_program
)

__version__ = '1.0.0'
__all__ = [
    'Lexer', 'Parser', 'Program',
    'GenesisRuntime', 'ResonanceEngine', 'PotentialityEngine',
    'MCPAdapter', 'run_genesis_program'
]
