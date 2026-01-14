#!/usr/bin/env python3
"""
Genesis Linter (genesis-lint)

Static analysis tool for Genesis programs, detecting potential issues,
style violations, and best practice deviations.
"""

import argparse
import re
import sys
from pathlib import Path
from typing import List, Tuple, Dict


class LintIssue:
    """Represents a linting issue found in code."""
    
    def __init__(self, severity: str, line: int, message: str, code: str):
        self.severity = severity  # 'error', 'warning', 'info'
        self.line = line
        self.message = message
        self.code = code  # Issue code like 'E001', 'W002'
    
    def __str__(self):
        icon = {'error': '❌', 'warning': '⚠️ ', 'info': 'ℹ️ '}[self.severity]
        return f"{icon} Line {self.line}: [{self.code}] {self.message}"


class GenesisLinter:
    """Lints Genesis code for style and potential issues."""
    
    def __init__(self):
        self.issues: List[LintIssue] = []
    
    def lint_code(self, code: str, filepath: str = "<string>") -> List[LintIssue]:
        """
        Lint Genesis code and return list of issues.
        
        Args:
            code: Genesis source code
            filepath: Path to file (for error reporting)
        
        Returns:
            List of LintIssue objects
        """
        self.issues = []
        lines = code.split('\n')
        
        for i, line in enumerate(lines, 1):
            self._check_line(line, i)
        
        # Whole-file checks
        self._check_structure(code)
        
        return self.issues
    
    def _check_line(self, line: str, line_num: int):
        """Check a single line for issues."""
        stripped = line.strip()
        
        # Check for trailing whitespace
        if line != stripped and line.endswith(' '):
            self.issues.append(LintIssue(
                'info', line_num,
                'Trailing whitespace',
                'W001'
            ))
        
        # Check for tabs instead of spaces
        if '\t' in line:
            self.issues.append(LintIssue(
                'warning', line_num,
                'Use spaces instead of tabs for indentation',
                'W002'
            ))
        
        # Check for inconsistent naming (PascalCase for entities)
        if stripped.startswith(('Covenant', 'Avatar', 'Domain', 'Pantheon')):
            # Extract name in quotes
            match = re.search(r'["\']([^"\']+)["\']', stripped)
            if match:
                name = match.group(1)
                if not self._is_pascal_case(name):
                    self.issues.append(LintIssue(
                        'info', line_num,
                        f'Consider using PascalCase for entity names: "{name}"',
                        'I001'
                    ))
        
        # Check for missing threshold in Covenant
        if stripped.startswith('Covenant') and '{' in stripped:
            # Note: Full validation would require complete parsing
            # This is a simple heuristic check
            # TODO: Enhance with full AST-based validation when parser is integrated
            pass
        
        # Check for very long lines
        if len(line) > 120:
            self.issues.append(LintIssue(
                'info', line_num,
                f'Line too long ({len(line)} > 120 characters)',
                'I002'
            ))
    
    def _check_structure(self, code: str):
        """Check overall code structure."""
        # Check for at least one Covenant
        if 'Covenant' not in code:
            self.issues.append(LintIssue(
                'warning', 0,
                'Genesis programs should define at least one Covenant',
                'W003'
            ))
        
        # Check for balanced braces
        open_braces = code.count('{')
        close_braces = code.count('}')
        if open_braces != close_braces:
            self.issues.append(LintIssue(
                'error', 0,
                f'Unbalanced braces: {open_braces} opening, {close_braces} closing',
                'E001'
            ))
    
    def _is_pascal_case(self, name: str) -> bool:
        """Check if a name follows PascalCase convention."""
        # Allow underscores for composite names
        parts = name.split('_')
        return all(part[0].isupper() if part else False for part in parts)
    
    def lint_file(self, filepath: Path) -> List[LintIssue]:
        """Lint a Genesis file."""
        if not filepath.exists():
            return [LintIssue('error', 0, f'File not found: {filepath}', 'E002')]
        
        try:
            code = filepath.read_text()
            return self.lint_code(code, str(filepath))
        except Exception as e:
            return [LintIssue('error', 0, f'Error reading file: {e}', 'E003')]


def main():
    """Main entry point for genesis-lint CLI."""
    parser = argparse.ArgumentParser(
        description="Genesis Linter - Static analysis for Genesis code"
    )
    
    parser.add_argument(
        'paths',
        nargs='+',
        help='Files or directories to lint'
    )
    
    parser.add_argument(
        '--severity',
        choices=['error', 'warning', 'info'],
        default='info',
        help='Minimum severity level to report (default: info)'
    )
    
    parser.add_argument(
        '--verbose',
        '-v',
        action='store_true',
        help='Verbose output'
    )
    
    args = parser.parse_args()
    
    linter = GenesisLinter()
    all_issues: List[Tuple[Path, List[LintIssue]]] = []
    
    severity_levels = {'error': 0, 'warning': 1, 'info': 2}
    min_severity = severity_levels[args.severity]
    
    for path_str in args.paths:
        path = Path(path_str)
        
        if not path.exists():
            print(f"❌ Path not found: {path}")
            continue
        
        gen_files = []
        if path.is_file() and path.suffix == '.gen':
            gen_files = [path]
        elif path.is_dir():
            gen_files = list(path.rglob('*.gen'))
        
        for gen_file in gen_files:
            issues = linter.lint_file(gen_file)
            
            # Filter by severity
            filtered_issues = [
                issue for issue in issues
                if severity_levels[issue.severity] <= min_severity
            ]
            
            if filtered_issues:
                all_issues.append((gen_file, filtered_issues))
    
    # Report issues
    if not all_issues:
        print("✅ No issues found")
        return 0
    
    total_issues = sum(len(issues) for _, issues in all_issues)
    print(f"\n🔍 Found {total_issues} issue(s) in {len(all_issues)} file(s):\n")
    
    for filepath, issues in all_issues:
        print(f"\n📄 {filepath}")
        for issue in issues:
            print(f"  {issue}")
    
    # Count by severity
    errors = sum(1 for _, issues in all_issues for i in issues if i.severity == 'error')
    warnings = sum(1 for _, issues in all_issues for i in issues if i.severity == 'warning')
    infos = sum(1 for _, issues in all_issues for i in issues if i.severity == 'info')
    
    print(f"\n📊 Summary: {errors} errors, {warnings} warnings, {infos} info")
    
    return 1 if errors > 0 else 0


if __name__ == "__main__":
    sys.exit(main())
