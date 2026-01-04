#!/usr/bin/env python3
"""
Genesis Language CLI

Command-line interface for running Genesis programs.
This provides the primary way to execute .gen files on the contemporary AOS.

Usage:
    python genesis_cli.py <file.gen>
    python genesis_cli.py --help
"""

import sys
import argparse
from pathlib import Path

try:
    from genesis_interpreter import run_genesis_program
except ImportError:
    # Add src directory to path
    sys.path.insert(0, str(Path(__file__).parent))
    from genesis_interpreter import run_genesis_program


def main():
    """Main CLI entry point"""
    parser = argparse.ArgumentParser(
        description='Genesis Programming Language Interpreter',
        epilog='Genesis: A declarative language for Artificial Superintelligence'
    )
    
    parser.add_argument(
        'file',
        type=str,
        help='Path to Genesis program file (.gen)'
    )
    
    parser.add_argument(
        '-v', '--verbose',
        action='store_true',
        help='Enable verbose output'
    )
    
    parser.add_argument(
        '--version',
        action='version',
        version='Genesis 1.0.0 - The Language of Superintelligence'
    )
    
    args = parser.parse_args()
    
    # Read the Genesis file
    file_path = Path(args.file)
    
    if not file_path.exists():
        print(f"Error: File not found: {file_path}", file=sys.stderr)
        sys.exit(1)
    
    if not file_path.suffix == '.gen':
        print(f"Warning: Expected .gen file extension", file=sys.stderr)
    
    try:
        source_code = file_path.read_text()
    except Exception as e:
        print(f"Error reading file: {e}", file=sys.stderr)
        sys.exit(1)
    
    # Execute the program
    try:
        print(f"\nLoading Genesis program: {file_path}")
        print(f"{'='*70}\n")
        
        run_genesis_program(source_code)
        
        print(f"\n{'='*70}")
        print("Program execution completed successfully")
        sys.exit(0)
        
    except SyntaxError as e:
        print(f"\nSyntax Error: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"\nRuntime Error: {e}", file=sys.stderr)
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == '__main__':
    main()
