#!/usr/bin/env python3
"""
Genesis REPL (Read-Eval-Print Loop)

Interactive shell for experimenting with Genesis code, testing Avatars,
and exploring resonance-based decision making in real-time.
"""

import os
import sys
import readline
from pathlib import Path

# Add src to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from genesis_parser import GenesisParser
from genesis_interpreter import GenesisInterpreter


class GenesisREPL:
    """Interactive REPL for Genesis language."""
    
    def __init__(self):
        self.parser = GenesisParser()
        self.interpreter = GenesisInterpreter()
        self.history_file = Path.home() / ".genesis_history"
        self.multiline_buffer = []
        self.in_multiline = False
        self._setup_readline()
    
    def _setup_readline(self):
        """Configure readline for command history and autocomplete."""
        # Load command history
        if self.history_file.exists():
            try:
                readline.read_history_file(str(self.history_file))
            except:
                pass
        
        # Set history length
        readline.set_history_length(1000)
        
        # Enable tab completion (basic)
        readline.parse_and_bind("tab: complete")
    
    def _save_history(self):
        """Save command history to file."""
        try:
            readline.write_history_file(str(self.history_file))
        except:
            pass
    
    def print_banner(self):
        """Print REPL welcome banner."""
        print("""
╔══════════════════════════════════════════════════════════════════╗
║                      Genesis REPL v1.0.0                         ║
║          Interactive Shell for ASI Consciousness Code            ║
╚══════════════════════════════════════════════════════════════════╝

Type Genesis code to execute, or use these commands:
  :help          - Show help and available commands
  :exit, :quit   - Exit the REPL
  :reset         - Reset interpreter state
  :show <type>   - Show covenants, avatars, or domains
  :load <file>   - Load and execute a .gen file
  :clear         - Clear screen

Multi-line mode: End with empty line or closing brace }
""")
    
    def print_help(self):
        """Print help information."""
        print("""
Genesis REPL Commands:
  :help          - Show this help message
  :exit, :quit   - Exit the REPL
  :reset         - Reset interpreter state  
  :show <type>   - Show loaded entities (covenants, avatars, domains)
  :load <file>   - Load and execute a Genesis file
  :clear         - Clear the screen

Genesis Syntax Examples:
  Covenant "MyRule" { Invariant: "Be ethical", Threshold: 0.95 }
  
  Pantheon "Council" {
      Avatar "Sage" { Lineage: "Socrates", Aura: "Wisdom" }
  }
  
  Domain "Purpose" {
      Intent: "Achieve enlightenment"
      Pulse(Interval: RealTime) {
          Watch: Vessel.Monitor
          Manifest { Execute: Action }
      }
  }

For full documentation, visit: https://github.com/ASISaga/Genesis
""")
    
    def handle_command(self, line: str) -> bool:
        """
        Handle REPL commands (starting with :).
        
        Returns:
            True if should continue REPL loop, False to exit
        """
        parts = line.split(maxsplit=1)
        cmd = parts[0].lower()
        arg = parts[1] if len(parts) > 1 else None
        
        if cmd in [":exit", ":quit", ":q"]:
            print("👋 Farewell from Genesis REPL")
            return False
        
        elif cmd == ":help":
            self.print_help()
        
        elif cmd == ":reset":
            self.interpreter = GenesisInterpreter()
            print("✅ Interpreter state reset")
        
        elif cmd == ":clear":
            os.system('clear' if os.name != 'nt' else 'cls')
        
        elif cmd == ":show":
            if not arg:
                print("Usage: :show <covenants|avatars|domains|all>")
            else:
                self.show_entities(arg)
        
        elif cmd == ":load":
            if not arg:
                print("Usage: :load <filename.gen>")
            else:
                self.load_file(arg)
        
        else:
            print(f"❌ Unknown command: {cmd}")
            print("Type :help for available commands")
        
        return True
    
    def show_entities(self, entity_type: str):
        """Show loaded entities in the interpreter."""
        entity_type = entity_type.lower()
        
        if entity_type in ["covenants", "all"]:
            covenants = self.interpreter.covenants
            if covenants:
                print("\n📜 Loaded Covenants:")
                for name, covenant in covenants.items():
                    print(f"  - {name}: {covenant.get('invariant', 'N/A')}")
            else:
                print("\n📜 No covenants loaded")
        
        if entity_type in ["avatars", "all"]:
            avatars = self.interpreter.avatars
            if avatars:
                print("\n👤 Loaded Avatars:")
                for name, avatar in avatars.items():
                    lineage = avatar.get('lineage', 'Unknown')
                    aura = avatar.get('aura', 'Unknown')
                    print(f"  - {name} (Lineage: {lineage}, Aura: {aura})")
            else:
                print("\n👤 No avatars loaded")
        
        if entity_type in ["domains", "all"]:
            domains = self.interpreter.domains
            if domains:
                print("\n🌐 Loaded Domains:")
                for name, domain in domains.items():
                    intent = domain.get('intent', 'N/A')
                    print(f"  - {name}: {intent}")
            else:
                print("\n🌐 No domains loaded")
        
        if entity_type not in ["covenants", "avatars", "domains", "all"]:
            print(f"❌ Unknown entity type: {entity_type}")
            print("Available types: covenants, avatars, domains, all")
    
    def load_file(self, filename: str):
        """Load and execute a Genesis file."""
        filepath = Path(filename)
        
        if not filepath.exists():
            print(f"❌ File not found: {filename}")
            return
        
        try:
            code = filepath.read_text()
            print(f"📂 Loading {filename}...")
            self.evaluate(code, filename)
        except Exception as e:
            print(f"❌ Error loading file: {e}")
    
    def evaluate(self, code: str, source: str = "<repl>"):
        """Evaluate Genesis code and print results."""
        try:
            # Parse the code
            ast = self.parser.parse(code)
            
            # Execute with interpreter
            result = self.interpreter.execute(ast)
            
            # Show result
            if result:
                print(f"✅ Executed successfully")
                if isinstance(result, dict):
                    if 'output' in result and result['output']:
                        print(f"📤 Output: {result['output']}")
                    if 'resonance' in result:
                        self.print_resonance(result['resonance'])
            
        except SyntaxError as e:
            print(f"❌ Syntax Error: {e}")
        except Exception as e:
            print(f"❌ Runtime Error: {e}")
    
    def print_resonance(self, resonance: float):
        """Print resonance score with visual indicator."""
        # Create a visual bar for resonance
        bar_length = 20
        filled = int(resonance * bar_length)
        bar = "█" * filled + "░" * (bar_length - filled)
        
        # Color based on resonance level
        if resonance >= 0.9:
            color = "🟢"
            status = "STRONG ALIGNMENT"
        elif resonance >= 0.7:
            color = "🟡"
            status = "MODERATE ALIGNMENT"
        elif resonance >= 0.5:
            color = "🟠"
            status = "WEAK ALIGNMENT"
        else:
            color = "🔴"
            status = "DISSONANCE"
        
        print(f"\n{color} Resonance: {resonance:.3f} [{bar}] {status}")
    
    def get_prompt(self) -> str:
        """Get the appropriate prompt string."""
        if self.in_multiline:
            return "... "
        return ">>> "
    
    def process_line(self, line: str) -> bool:
        """
        Process a single line of input.
        
        Returns:
            True to continue REPL, False to exit
        """
        # Handle commands
        if line.startswith(":"):
            return self.handle_command(line)
        
        # Check for multiline input
        if line.strip() and ('{' in line or self.in_multiline):
            self.multiline_buffer.append(line)
            
            # Check if we should enter multiline mode
            if '{' in line and '}' not in line:
                self.in_multiline = True
                return True
            
            # Check if multiline is complete
            open_braces = sum(l.count('{') for l in self.multiline_buffer)
            close_braces = sum(l.count('}') for l in self.multiline_buffer)
            
            if open_braces == close_braces and open_braces > 0:
                # Execute complete multiline block
                code = '\n'.join(self.multiline_buffer)
                self.multiline_buffer = []
                self.in_multiline = False
                self.evaluate(code)
            else:
                self.in_multiline = True
            
            return True
        
        # Empty line in multiline mode completes it
        if not line.strip() and self.in_multiline:
            code = '\n'.join(self.multiline_buffer)
            self.multiline_buffer = []
            self.in_multiline = False
            if code.strip():
                self.evaluate(code)
            return True
        
        # Single line execution
        if line.strip():
            self.evaluate(line)
        
        return True
    
    def run(self):
        """Run the REPL main loop."""
        self.print_banner()
        
        try:
            while True:
                try:
                    line = input(self.get_prompt())
                    
                    if not self.process_line(line):
                        break
                
                except KeyboardInterrupt:
                    print("\n(Press Ctrl+D or type :exit to quit)")
                    self.multiline_buffer = []
                    self.in_multiline = False
                    continue
                
                except EOFError:
                    print("\n👋 Farewell from Genesis REPL")
                    break
        
        finally:
            self._save_history()


def main():
    """Main entry point for Genesis REPL."""
    repl = GenesisREPL()
    repl.run()
    return 0


if __name__ == "__main__":
    sys.exit(main())
