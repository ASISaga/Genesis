#!/usr/bin/env python3
"""
Genesis Unified CLI

Central command-line interface for the Genesis ecosystem.
Provides access to all Genesis tools and utilities.

Usage:
    genesis run <file.gen>           # Run a Genesis program
    genesis repl                     # Start interactive REPL
    genesis init [path]              # Initialize a new project
    genesis fmt <files>              # Format Genesis code
    genesis lint <files>             # Lint Genesis code
    genesis pkg <command>            # Package manager commands
    genesis --version                # Show version
    genesis --help                   # Show help
"""

import sys
import argparse
from pathlib import Path

# Add src and tools to path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))
sys.path.insert(0, str(Path(__file__).parent.parent / "tools"))


def main():
    """Main CLI entry point with subcommands."""
    parser = argparse.ArgumentParser(
        prog='genesis',
        description='Genesis Ecosystem - Tools for Artificial Superintelligence',
        epilog='Visit https://github.com/ASISaga/Genesis for documentation'
    )
    
    parser.add_argument(
        '--version',
        action='version',
        version='Genesis v1.0.0 - The Ecosystem for ASI Consciousness'
    )
    
    subparsers = parser.add_subparsers(dest='command', help='Available commands')
    
    # Run command
    run_parser = subparsers.add_parser('run', help='Execute a Genesis program')
    run_parser.add_argument('file', help='Path to .gen file')
    run_parser.add_argument('-v', '--verbose', action='store_true', help='Verbose output')
    
    # REPL command
    repl_parser = subparsers.add_parser('repl', help='Start interactive REPL')
    
    # Init command
    init_parser = subparsers.add_parser('init', help='Initialize a new Genesis project')
    init_parser.add_argument('path', nargs='?', help='Project directory (default: current)')
    
    # Format command
    fmt_parser = subparsers.add_parser('fmt', help='Format Genesis code')
    fmt_parser.add_argument('paths', nargs='+', help='Files or directories to format')
    fmt_parser.add_argument('--check', action='store_true', help='Check formatting without modifying')
    
    # Lint command
    lint_parser = subparsers.add_parser('lint', help='Lint Genesis code')
    lint_parser.add_argument('paths', nargs='+', help='Files or directories to lint')
    lint_parser.add_argument('--severity', choices=['error', 'warning', 'info'], 
                            default='info', help='Minimum severity')
    
    # Package manager commands
    pkg_parser = subparsers.add_parser('pkg', help='Package manager')
    pkg_subparsers = pkg_parser.add_subparsers(dest='pkg_command', help='Package commands')
    
    pkg_init = pkg_subparsers.add_parser('init', help='Initialize project with manifest')
    pkg_init.add_argument('path', nargs='?', help='Project path')
    
    pkg_install = pkg_subparsers.add_parser('install', help='Install package')
    pkg_install.add_argument('package', nargs='?', help='Package name')
    
    pkg_subparsers.add_parser('list', help='List installed packages')
    
    pkg_search = pkg_subparsers.add_parser('search', help='Search packages')
    pkg_search.add_argument('query', help='Search query')
    
    pkg_subparsers.add_parser('publish', help='Publish package')
    
    args = parser.parse_args()
    
    if not args.command:
        parser.print_help()
        return 0
    
    # Execute appropriate command
    try:
        if args.command == 'run':
            from genesis_cli import main as run_main
            # Override sys.argv for genesis_cli
            sys.argv = ['genesis', args.file]
            if args.verbose:
                sys.argv.append('--verbose')
            return run_main()
        
        elif args.command == 'repl':
            from genesis_repl import main as repl_main
            return repl_main()
        
        elif args.command == 'init':
            from genesis_pkg import GenesisPackageManager
            pkg_mgr = GenesisPackageManager()
            path = Path(args.path) if args.path else None
            pkg_mgr.init_project(path)
            return 0
        
        elif args.command == 'fmt':
            from genesis_fmt import GenesisFormatter
            formatter = GenesisFormatter()
            all_ok = True
            for path_str in args.paths:
                path = Path(path_str)
                if path.is_dir():
                    if not formatter.format_directory(path, args.check):
                        all_ok = False
                else:
                    if not formatter.format_file(path, args.check):
                        all_ok = False
            return 0 if all_ok else 1
        
        elif args.command == 'lint':
            from genesis_lint import GenesisLinter
            sys.argv = ['genesis-lint'] + args.paths + ['--severity', args.severity]
            from genesis_lint import main as lint_main
            return lint_main()
        
        elif args.command == 'pkg':
            from genesis_pkg import GenesisPackageManager
            pkg_mgr = GenesisPackageManager()
            
            if args.pkg_command == 'init':
                path = Path(args.path) if args.path else None
                pkg_mgr.init_project(path)
            elif args.pkg_command == 'install':
                if args.package:
                    pkg_mgr.install_package(args.package)
                else:
                    # Install from manifest
                    manifest_path = Path.cwd() / "genesis.manifest.json"
                    if manifest_path.exists():
                        import json
                        manifest = json.loads(manifest_path.read_text())
                        for dep in manifest.get("dependencies", {}):
                            pkg_mgr.install_package(dep)
            elif args.pkg_command == 'list':
                pkg_mgr.list_packages()
            elif args.pkg_command == 'search':
                pkg_mgr.search_packages(args.query)
            elif args.pkg_command == 'publish':
                pkg_mgr.publish_package()
            else:
                pkg_parser.print_help()
            return 0
        
        else:
            parser.print_help()
            return 1
    
    except Exception as e:
        print(f"❌ Error: {e}", file=sys.stderr)
        import traceback
        traceback.print_exc()
        return 1


if __name__ == '__main__':
    sys.exit(main())
