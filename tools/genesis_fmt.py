#!/usr/bin/env python3
"""
Genesis Formatter (genesis-fmt)

Automatic code formatter for Genesis programs, ensuring consistent
style and readability across the codebase.
"""

import argparse
import sys
from pathlib import Path
from typing import List


class GenesisFormatter:
    """Formats Genesis code according to style guidelines."""
    
    def __init__(self):
        self.indent_size = 4
        self.indent_level = 0
    
    def format_code(self, code: str) -> str:
        """Format Genesis code with proper indentation and spacing."""
        lines = code.split('\n')
        formatted_lines = []
        
        for line in lines:
            stripped = line.strip()
            
            # Skip empty lines but preserve them
            if not stripped:
                formatted_lines.append('')
                continue
            
            # Decrease indent for closing braces
            if stripped.startswith('}'):
                self.indent_level = max(0, self.indent_level - 1)
            
            # Add indentation
            formatted_line = ' ' * (self.indent_level * self.indent_size) + stripped
            formatted_lines.append(formatted_line)
            
            # Increase indent after opening braces
            if stripped.endswith('{'):
                self.indent_level += 1
        
        # Reset indent level
        self.indent_level = 0
        
        return '\n'.join(formatted_lines)
    
    def format_file(self, filepath: Path, check_only: bool = False) -> bool:
        """
        Format a Genesis file.
        
        Args:
            filepath: Path to the .gen file
            check_only: If True, only check if formatting is needed
        
        Returns:
            True if file is properly formatted (or was formatted), False otherwise
        """
        if not filepath.exists():
            print(f"❌ File not found: {filepath}")
            return False
        
        if filepath.suffix != '.gen':
            print(f"⚠️  Skipping non-Genesis file: {filepath}")
            return True
        
        try:
            original_code = filepath.read_text()
            formatted_code = self.format_code(original_code)
            
            if check_only:
                if original_code != formatted_code:
                    print(f"❌ {filepath} needs formatting")
                    return False
                else:
                    print(f"✅ {filepath} is properly formatted")
                    return True
            else:
                if original_code != formatted_code:
                    filepath.write_text(formatted_code)
                    print(f"✅ Formatted {filepath}")
                else:
                    print(f"✅ {filepath} already formatted")
                return True
        
        except Exception as e:
            print(f"❌ Error formatting {filepath}: {e}")
            return False
    
    def format_directory(self, dirpath: Path, check_only: bool = False) -> bool:
        """
        Format all Genesis files in a directory recursively.
        
        Returns:
            True if all files are properly formatted, False otherwise
        """
        all_formatted = True
        
        for gen_file in dirpath.rglob('*.gen'):
            if not self.format_file(gen_file, check_only):
                all_formatted = False
        
        return all_formatted


def main():
    """Main entry point for genesis-fmt CLI."""
    parser = argparse.ArgumentParser(
        description="Genesis Formatter - Format Genesis code for consistency"
    )
    
    parser.add_argument(
        'paths',
        nargs='+',
        help='Files or directories to format'
    )
    
    parser.add_argument(
        '--check',
        action='store_true',
        help='Check if files need formatting without modifying them'
    )
    
    parser.add_argument(
        '--verbose',
        '-v',
        action='store_true',
        help='Verbose output'
    )
    
    args = parser.parse_args()
    
    formatter = GenesisFormatter()
    all_formatted = True
    
    for path_str in args.paths:
        path = Path(path_str)
        
        if not path.exists():
            print(f"❌ Path not found: {path}")
            all_formatted = False
            continue
        
        if path.is_file():
            if not formatter.format_file(path, args.check):
                all_formatted = False
        elif path.is_dir():
            if not formatter.format_directory(path, args.check):
                all_formatted = False
        else:
            print(f"❌ Invalid path: {path}")
            all_formatted = False
    
    if args.check:
        if all_formatted:
            print("\n✅ All files are properly formatted")
            return 0
        else:
            print("\n❌ Some files need formatting")
            return 1
    else:
        print("\n✅ Formatting complete")
        return 0


if __name__ == "__main__":
    sys.exit(main())
