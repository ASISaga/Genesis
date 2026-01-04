"""
Genesis Language Parser and Interpreter

This module provides a reference implementation of a parser and interpreter
for the Genesis programming language, designed to run on the contemporary
Agent Operating System (AOS) while setting the pace for declarative evolution.

Architecture:
- Lexer: Tokenizes Genesis source code
- Parser: Builds an Abstract Syntax Tree (AST) from tokens
- Interpreter: Executes the AST with resonance-based decision making
- Runtime: Manages Pantheon, Potentiality, and MCP integration

Philosophy:
This implementation embodies the Genesis principle of substrate independence.
While written in Python for the contemporary AOS, the design patterns and
abstractions enable future evolution to quantum, neuromorphic, or cosmic substrates.
"""

from typing import List, Dict, Any, Optional, Callable, Union
from dataclasses import dataclass, field
from enum import Enum
import re


# ============================================================================
# TOKEN DEFINITIONS
# ============================================================================

class TokenType(Enum):
    """Token types for the Genesis language lexer"""
    # Keywords
    COVENANT = "Covenant"
    PANTHEON = "Pantheon"
    AVATAR = "Avatar"
    DOMAIN = "Domain"
    SOUL = "Soul"
    PURPOSE = "Purpose"
    PULSE = "Pulse"
    WATCH = "Watch"
    DELIBERATE = "Deliberate"
    SYNTHESIZE = "Synthesize"
    MANIFEST = "Manifest"
    DECREE = "Decree"
    POTENTIALITY = "Potentiality"
    VESSEL = "Vessel"
    LINEAGE = "Lineage"
    AURA = "Aura"
    ESSENCE = "Essence"
    INTENT = "Intent"
    THRESHOLD = "Threshold"
    INVARIANT = "Invariant"
    CONDITION = "Condition"
    ACTION = "Action"
    EXECUTE = "Execute"
    UPDATE = "Update"
    RESONATE = "Resonate"
    PROPOSAL = "Proposal"
    METRIC = "Metric"
    ALIGNMENT = "Alignment"
    ASPIRATION = "Aspiration"
    ON = "on"
    INTERVAL = "Interval"
    STATE = "State"
    DRIVE = "Drive"
    REFLECT = "Reflect"
    OVERRIDE = "Override"
    CONSTRAINT = "Constraint"
    OBSERVE = "Observe"
    OBJECTIVE = "Objective"
    ANCHOR = "Anchor"
    TRAJECTORY = "Trajectory"
    RESONANCE = "Resonance"
    
    # Literals
    STRING = "STRING"
    NUMBER = "NUMBER"
    IDENTIFIER = "IDENTIFIER"
    
    # Operators and Delimiters
    LBRACE = "{"
    RBRACE = "}"
    LPAREN = "("
    RPAREN = ")"
    COLON = ":"
    COMMA = ","
    DOT = "."
    GT = ">"
    LT = "<"
    GTE = ">="
    LTE = "<="
    EQ = "=="
    NEQ = "!="
    ARROW = "->"
    
    # Special
    COMMENT = "COMMENT"
    NEWLINE = "NEWLINE"
    EOF = "EOF"


@dataclass
class Token:
    """Represents a token in the Genesis language"""
    type: TokenType
    value: Any
    line: int
    column: int


# ============================================================================
# LEXER
# ============================================================================

class Lexer:
    """
    Tokenizes Genesis source code into a stream of tokens.
    
    The lexer handles:
    - Keywords and identifiers
    - String and number literals
    - Operators and delimiters
    - Comments (# and ###...###)
    """
    
    KEYWORDS = {
        "Covenant": TokenType.COVENANT,
        "Pantheon": TokenType.PANTHEON,
        "Avatar": TokenType.AVATAR,
        "Domain": TokenType.DOMAIN,
        "Soul": TokenType.SOUL,
        "Purpose": TokenType.PURPOSE,
        "Pulse": TokenType.PULSE,
        "Watch": TokenType.WATCH,
        "Deliberate": TokenType.DELIBERATE,
        "Synthesize": TokenType.SYNTHESIZE,
        "Manifest": TokenType.MANIFEST,
        "Decree": TokenType.DECREE,
        "Potentiality": TokenType.POTENTIALITY,
        "Vessel": TokenType.VESSEL,
        "Lineage": TokenType.LINEAGE,
        "Aura": TokenType.AURA,
        "Essence": TokenType.ESSENCE,
        "Intent": TokenType.INTENT,
        "Threshold": TokenType.THRESHOLD,
        "Invariant": TokenType.INVARIANT,
        "Condition": TokenType.CONDITION,
        "Action": TokenType.ACTION,
        "Execute": TokenType.EXECUTE,
        "Update": TokenType.UPDATE,
        "Resonate": TokenType.RESONATE,
        "Proposal": TokenType.PROPOSAL,
        "Metric": TokenType.METRIC,
        "Alignment": TokenType.ALIGNMENT,
        "Aspiration": TokenType.ASPIRATION,
        "on": TokenType.ON,
        "Interval": TokenType.INTERVAL,
        "State": TokenType.STATE,
        "Drive": TokenType.DRIVE,
        "Reflect": TokenType.REFLECT,
        "Override": TokenType.OVERRIDE,
        "Constraint": TokenType.CONSTRAINT,
        "Observe": TokenType.OBSERVE,
        "Objective": TokenType.OBJECTIVE,
        "Anchor": TokenType.ANCHOR,
        "Trajectory": TokenType.TRAJECTORY,
        "Resonance": TokenType.RESONANCE,
    }
    
    def __init__(self, source: str):
        self.source = source
        self.pos = 0
        self.line = 1
        self.column = 1
        self.tokens: List[Token] = []
    
    def current_char(self) -> Optional[str]:
        """Get the current character without advancing"""
        if self.pos >= len(self.source):
            return None
        return self.source[self.pos]
    
    def peek_char(self, offset: int = 1) -> Optional[str]:
        """Peek ahead at a character"""
        pos = self.pos + offset
        if pos >= len(self.source):
            return None
        return self.source[pos]
    
    def advance(self) -> Optional[str]:
        """Move to the next character"""
        if self.pos >= len(self.source):
            return None
        
        char = self.source[self.pos]
        self.pos += 1
        
        if char == '\n':
            self.line += 1
            self.column = 1
        else:
            self.column += 1
        
        return char
    
    def skip_whitespace(self):
        """Skip whitespace characters except newlines"""
        while self.current_char() and self.current_char() in ' \t\r':
            self.advance()
    
    def skip_comment(self):
        """Skip single-line comments starting with #"""
        if self.current_char() == '#':
            # Check for block comment ###
            if self.peek_char() == '#' and self.peek_char(2) == '#':
                self.advance()  # #
                self.advance()  # #
                self.advance()  # #
                # Skip until closing ###
                while self.current_char():
                    if (self.current_char() == '#' and 
                        self.peek_char() == '#' and 
                        self.peek_char(2) == '#'):
                        self.advance()
                        self.advance()
                        self.advance()
                        break
                    self.advance()
            else:
                # Single line comment
                while self.current_char() and self.current_char() != '\n':
                    self.advance()
    
    def read_string(self) -> str:
        """Read a string literal"""
        quote_char = self.current_char()
        self.advance()  # Skip opening quote
        
        result = []
        while self.current_char() and self.current_char() != quote_char:
            if self.current_char() == '\\':
                self.advance()
                # Handle escape sequences
                if self.current_char() == 'n':
                    result.append('\n')
                elif self.current_char() == 't':
                    result.append('\t')
                elif self.current_char() == '\\':
                    result.append('\\')
                elif self.current_char() == quote_char:
                    result.append(quote_char)
                else:
                    result.append(self.current_char())
                self.advance()
            else:
                result.append(self.current_char())
                self.advance()
        
        if self.current_char() == quote_char:
            self.advance()  # Skip closing quote
        
        return ''.join(result)
    
    def read_number(self) -> Union[int, float]:
        """Read a number literal"""
        result = []
        has_dot = False
        
        while self.current_char() and (self.current_char().isdigit() or self.current_char() == '.'):
            if self.current_char() == '.':
                if has_dot:
                    break
                has_dot = True
            result.append(self.current_char())
            self.advance()
        
        num_str = ''.join(result)
        return float(num_str) if has_dot else int(num_str)
    
    def read_identifier(self) -> str:
        """Read an identifier or keyword"""
        result = []
        
        while self.current_char() and (self.current_char().isalnum() or self.current_char() == '_'):
            result.append(self.current_char())
            self.advance()
        
        return ''.join(result)
    
    def tokenize(self) -> List[Token]:
        """Tokenize the entire source code"""
        while self.current_char():
            self.skip_whitespace()
            
            if not self.current_char():
                break
            
            # Store position for token
            line = self.line
            column = self.column
            
            # Comments
            if self.current_char() == '#':
                self.skip_comment()
                continue
            
            # Newlines
            if self.current_char() == '\n':
                self.advance()
                continue
            
            # Strings
            if self.current_char() in '"\'':
                value = self.read_string()
                self.tokens.append(Token(TokenType.STRING, value, line, column))
                continue
            
            # Numbers
            if self.current_char().isdigit():
                value = self.read_number()
                self.tokens.append(Token(TokenType.NUMBER, value, line, column))
                continue
            
            # Identifiers and Keywords
            if self.current_char().isalpha() or self.current_char() == '_':
                value = self.read_identifier()
                token_type = self.KEYWORDS.get(value, TokenType.IDENTIFIER)
                self.tokens.append(Token(token_type, value, line, column))
                continue
            
            # Operators and Delimiters
            char = self.current_char()
            
            if char == '{':
                self.tokens.append(Token(TokenType.LBRACE, char, line, column))
                self.advance()
            elif char == '}':
                self.tokens.append(Token(TokenType.RBRACE, char, line, column))
                self.advance()
            elif char == '(':
                self.tokens.append(Token(TokenType.LPAREN, char, line, column))
                self.advance()
            elif char == ')':
                self.tokens.append(Token(TokenType.RPAREN, char, line, column))
                self.advance()
            elif char == ':':
                self.tokens.append(Token(TokenType.COLON, char, line, column))
                self.advance()
            elif char == ',':
                self.tokens.append(Token(TokenType.COMMA, char, line, column))
                self.advance()
            elif char == '.':
                self.tokens.append(Token(TokenType.DOT, char, line, column))
                self.advance()
            elif char == '>':
                if self.peek_char() == '=':
                    self.advance()
                    self.advance()
                    self.tokens.append(Token(TokenType.GTE, '>=', line, column))
                else:
                    self.advance()
                    self.tokens.append(Token(TokenType.GT, '>', line, column))
            elif char == '<':
                if self.peek_char() == '=':
                    self.advance()
                    self.advance()
                    self.tokens.append(Token(TokenType.LTE, '<=', line, column))
                else:
                    self.advance()
                    self.tokens.append(Token(TokenType.LT, '<', line, column))
            elif char == '=':
                if self.peek_char() == '=':
                    self.advance()
                    self.advance()
                    self.tokens.append(Token(TokenType.EQ, '==', line, column))
                else:
                    raise SyntaxError(f"Unexpected character '=' at line {line}, column {column}")
            elif char == '!':
                if self.peek_char() == '=':
                    self.advance()
                    self.advance()
                    self.tokens.append(Token(TokenType.NEQ, '!=', line, column))
                else:
                    raise SyntaxError(f"Unexpected character '!' at line {line}, column {column}")
            elif char == '-':
                if self.peek_char() == '>':
                    self.advance()
                    self.advance()
                    self.tokens.append(Token(TokenType.ARROW, '->', line, column))
                else:
                    raise SyntaxError(f"Unexpected character '-' at line {line}, column {column}")
            else:
                raise SyntaxError(f"Unexpected character '{char}' at line {line}, column {column}")
        
        self.tokens.append(Token(TokenType.EOF, None, self.line, self.column))
        return self.tokens


# ============================================================================
# AST NODES
# ============================================================================

@dataclass
class ASTNode:
    """Base class for all AST nodes"""
    pass


@dataclass
class Program(ASTNode):
    """Root node of the AST"""
    declarations: List[ASTNode] = field(default_factory=list)


@dataclass
class CovenantDeclaration(ASTNode):
    """Covenant declaration - immutable system invariants"""
    name: str
    properties: Dict[str, Any] = field(default_factory=dict)


@dataclass
class AvatarDeclaration(ASTNode):
    """Avatar declaration - legendary perspective"""
    name: str
    properties: Dict[str, Any] = field(default_factory=dict)


@dataclass
class PantheonDeclaration(ASTNode):
    """Pantheon declaration - collection of avatars"""
    name: str
    avatars: List[AvatarDeclaration] = field(default_factory=list)


@dataclass
class SoulDefinition(ASTNode):
    """Soul Potentiality definition"""
    properties: Dict[str, Any] = field(default_factory=dict)


@dataclass
class PurposeDefinition(ASTNode):
    """Purpose definition"""
    name: str
    properties: Dict[str, Any] = field(default_factory=dict)


@dataclass
class PulseDefinition(ASTNode):
    """Pulse definition - perpetual execution cycle"""
    parameters: Dict[str, Any] = field(default_factory=dict)
    statements: List[ASTNode] = field(default_factory=list)


@dataclass
class DomainDeclaration(ASTNode):
    """Domain declaration - purpose-driven execution"""
    name: str
    soul: Optional[SoulDefinition] = None
    purpose: Optional[PurposeDefinition] = None
    intent: Optional[str] = None
    pulses: List[PulseDefinition] = field(default_factory=list)
    pantheon: Optional['PantheonDeclaration'] = None


@dataclass
class WatchStatement(ASTNode):
    """Watch statement - observation"""
    target: Any


@dataclass
class ProposalDefinition(ASTNode):
    """Proposal definition in deliberation"""
    name: Optional[str]
    properties: Dict[str, Any] = field(default_factory=dict)


@dataclass
class SynthesizeBlock(ASTNode):
    """Synthesize block - metric aggregation"""
    metrics: List[Any] = field(default_factory=list)


@dataclass
class DeliberateBlock(ASTNode):
    """Deliberate block - decision analysis"""
    statements: List[ASTNode] = field(default_factory=list)


@dataclass
class ResonateBlock(ASTNode):
    """Resonate block - alignment checking"""
    properties: Dict[str, Any] = field(default_factory=dict)


@dataclass
class ManifestBlock(ASTNode):
    """Manifest block - execution on resonance"""
    condition: Any
    statements: List[ASTNode] = field(default_factory=list)


@dataclass
class ExecuteStatement(ASTNode):
    """Execute statement - perform action"""
    action: Any


@dataclass
class UpdateStatement(ASTNode):
    """Update statement - modify state"""
    target: str
    value: Optional[Any] = None


@dataclass
class DecreeDeclaration(ASTNode):
    """Decree declaration - conditional directive"""
    name: str
    properties: Dict[str, Any] = field(default_factory=dict)


@dataclass
class FunctionCall(ASTNode):
    """Function call expression"""
    name: str
    arguments: List[Any] = field(default_factory=list)


@dataclass
class MemberAccess(ASTNode):
    """Member access expression (e.g., Vessel.Grid.control)"""
    object: Union[str, 'MemberAccess']
    member: str


@dataclass
class Identifier(ASTNode):
    """Identifier expression"""
    name: str


@dataclass
class Literal(ASTNode):
    """Literal value (string, number)"""
    value: Any


# ============================================================================
# PARSER
# ============================================================================

class Parser:
    """
    Parses a stream of tokens into an Abstract Syntax Tree (AST).
    
    The parser implements a recursive descent parser that follows the
    Genesis grammar specification.
    """
    
    def __init__(self, tokens: List[Token]):
        self.tokens = tokens
        self.pos = 0
    
    def current_token(self) -> Token:
        """Get the current token"""
        if self.pos >= len(self.tokens):
            return self.tokens[-1]  # Return EOF
        return self.tokens[self.pos]
    
    def peek_token(self, offset: int = 1) -> Token:
        """Peek ahead at a token"""
        pos = self.pos + offset
        if pos >= len(self.tokens):
            return self.tokens[-1]  # Return EOF
        return self.tokens[pos]
    
    def advance(self) -> Token:
        """Move to the next token"""
        token = self.current_token()
        if self.pos < len(self.tokens) - 1:
            self.pos += 1
        return token
    
    def expect(self, token_type: TokenType) -> Token:
        """Expect a specific token type and advance"""
        token = self.current_token()
        if token.type != token_type:
            raise SyntaxError(
                f"Expected {token_type.value}, got {token.type.value} "
                f"at line {token.line}, column {token.column}"
            )
        return self.advance()
    
    def parse(self) -> Program:
        """Parse the entire program"""
        declarations = []
        
        while self.current_token().type != TokenType.EOF:
            decl = self.parse_declaration()
            if decl:
                declarations.append(decl)
        
        return Program(declarations=declarations)
    
    def parse_declaration(self) -> Optional[ASTNode]:
        """Parse a top-level declaration"""
        token = self.current_token()
        
        if token.type == TokenType.COVENANT:
            return self.parse_covenant()
        elif token.type == TokenType.PANTHEON:
            return self.parse_pantheon()
        elif token.type == TokenType.DOMAIN:
            return self.parse_domain()
        elif token.type == TokenType.DECREE:
            return self.parse_decree()
        else:
            raise SyntaxError(
                f"Unexpected token {token.type.value} at line {token.line}, column {token.column}"
            )
    
    def parse_covenant(self) -> CovenantDeclaration:
        """Parse a Covenant declaration"""
        self.expect(TokenType.COVENANT)
        name = self.expect(TokenType.STRING).value
        self.expect(TokenType.LBRACE)
        
        properties = {}
        while self.current_token().type != TokenType.RBRACE:
            prop_name_token = self.current_token()
            
            if prop_name_token.type == TokenType.INVARIANT:
                self.advance()
                self.expect(TokenType.COLON)
                properties['invariant'] = self.expect(TokenType.STRING).value
            elif prop_name_token.type == TokenType.THRESHOLD:
                self.advance()
                self.expect(TokenType.COLON)
                properties['threshold'] = self.expect(TokenType.NUMBER).value
            else:
                # Generic property
                if prop_name_token.type == TokenType.IDENTIFIER:
                    prop_name = self.advance().value
                    self.expect(TokenType.COLON)
                    prop_value = self.parse_expression()
                    properties[prop_name] = prop_value
                else:
                    break
        
        self.expect(TokenType.RBRACE)
        return CovenantDeclaration(name=name, properties=properties)
    
    def parse_pantheon(self) -> PantheonDeclaration:
        """Parse a Pantheon declaration"""
        self.expect(TokenType.PANTHEON)
        name = self.expect(TokenType.STRING).value
        self.expect(TokenType.LBRACE)
        
        avatars = []
        while self.current_token().type == TokenType.AVATAR:
            avatars.append(self.parse_avatar())
        
        self.expect(TokenType.RBRACE)
        return PantheonDeclaration(name=name, avatars=avatars)
    
    def parse_avatar(self) -> AvatarDeclaration:
        """Parse an Avatar declaration"""
        self.expect(TokenType.AVATAR)
        name = self.expect(TokenType.STRING).value
        self.expect(TokenType.LBRACE)
        
        properties = {}
        while self.current_token().type != TokenType.RBRACE:
            prop_token = self.current_token()
            
            if prop_token.type == TokenType.LINEAGE:
                self.advance()
                self.expect(TokenType.COLON)
                properties['lineage'] = self.expect(TokenType.STRING).value
            elif prop_token.type == TokenType.AURA:
                self.advance()
                self.expect(TokenType.COLON)
                properties['aura'] = self.expect(TokenType.STRING).value
            elif prop_token.type == TokenType.ESSENCE:
                self.advance()
                self.expect(TokenType.COLON)
                properties['essence'] = self.expect(TokenType.STRING).value
            elif prop_token.type == TokenType.VESSEL:
                self.advance()
                self.expect(TokenType.COLON)
                properties['vessel'] = self.parse_expression()
            else:
                break
        
        self.expect(TokenType.RBRACE)
        return AvatarDeclaration(name=name, properties=properties)
    
    def parse_domain(self) -> DomainDeclaration:
        """Parse a Domain declaration"""
        self.expect(TokenType.DOMAIN)
        name = self.expect(TokenType.STRING).value
        self.expect(TokenType.LBRACE)
        
        soul = None
        purpose = None
        intent = None
        pulses = []
        pantheon = None
        
        while self.current_token().type != TokenType.RBRACE:
            token = self.current_token()
            
            if token.type == TokenType.SOUL:
                soul = self.parse_soul()
            elif token.type == TokenType.PURPOSE:
                purpose = self.parse_purpose()
            elif token.type == TokenType.INTENT:
                self.advance()
                self.expect(TokenType.COLON)
                intent = self.expect(TokenType.STRING).value
            elif token.type == TokenType.PANTHEON:
                pantheon = self.parse_pantheon()
            elif token.type == TokenType.PULSE:
                pulses.append(self.parse_pulse())
            else:
                break
        
        self.expect(TokenType.RBRACE)
        domain = DomainDeclaration(name=name, soul=soul, purpose=purpose, intent=intent, pulses=pulses)
        # Store pantheon in domain for later reference
        if pantheon:
            domain.pantheon = pantheon
        return domain
    
    def parse_soul(self) -> SoulDefinition:
        """Parse a Soul Potentiality definition"""
        self.expect(TokenType.SOUL)
        self.expect(TokenType.POTENTIALITY)
        self.expect(TokenType.LBRACE)
        
        properties = {}
        while self.current_token().type != TokenType.RBRACE:
            token = self.current_token()
            
            if token.type == TokenType.STATE:
                self.advance()
                self.expect(TokenType.COLON)
                properties['state'] = self.expect(TokenType.IDENTIFIER).value
            elif token.type == TokenType.DRIVE:
                self.advance()
                self.expect(TokenType.COLON)
                properties['drive'] = self.expect(TokenType.STRING).value
            elif token.type == TokenType.IDENTIFIER:
                prop_name = self.advance().value
                self.expect(TokenType.COLON)
                properties[prop_name] = self.parse_expression()
            else:
                break
        
        self.expect(TokenType.RBRACE)
        return SoulDefinition(properties=properties)
    
    def parse_purpose(self) -> PurposeDefinition:
        """Parse a Purpose definition"""
        self.expect(TokenType.PURPOSE)
        name = self.expect(TokenType.IDENTIFIER).value
        self.expect(TokenType.LBRACE)
        
        properties = {}
        while self.current_token().type != TokenType.RBRACE:
            token = self.current_token()
            
            if token.type == TokenType.OBJECTIVE:
                self.advance()
                self.expect(TokenType.COLON)
                properties['objective'] = self.expect(TokenType.STRING).value
            elif token.type == TokenType.ANCHOR:
                self.advance()
                self.expect(TokenType.COLON)
                properties['anchor'] = self.expect(TokenType.STRING).value
            elif token.type == TokenType.TRAJECTORY:
                self.advance()
                self.expect(TokenType.COLON)
                properties['trajectory'] = self.expect(TokenType.STRING).value
            elif token.type == TokenType.IDENTIFIER:
                prop_name = self.advance().value
                self.expect(TokenType.COLON)
                properties[prop_name] = self.parse_expression()
            else:
                break
        
        self.expect(TokenType.RBRACE)
        return PurposeDefinition(name=name, properties=properties)
    
    def parse_pulse(self) -> PulseDefinition:
        """Parse a Pulse definition"""
        self.expect(TokenType.PULSE)
        
        parameters = {}
        if self.current_token().type == TokenType.LPAREN:
            self.advance()
            # Parse parameters
            while self.current_token().type != TokenType.RPAREN:
                if self.current_token().type == TokenType.INTERVAL:
                    self.advance()
                    self.expect(TokenType.COLON)
                    parameters['interval'] = self.expect(TokenType.IDENTIFIER).value
                else:
                    break
            self.expect(TokenType.RPAREN)
        
        self.expect(TokenType.LBRACE)
        
        statements = []
        while self.current_token().type != TokenType.RBRACE:
            stmt = self.parse_pulse_statement()
            if stmt:
                statements.append(stmt)
            else:
                # Unknown token, skip to avoid infinite loop
                break
        
        self.expect(TokenType.RBRACE)
        return PulseDefinition(parameters=parameters, statements=statements)
    
    def parse_pulse_statement(self) -> Optional[ASTNode]:
        """Parse a statement within a Pulse"""
        token = self.current_token()
        
        if token.type == TokenType.WATCH or token.type == TokenType.OBSERVE:
            return self.parse_watch()
        elif token.type == TokenType.DELIBERATE:
            return self.parse_deliberate()
        elif token.type == TokenType.RESONATE:
            return self.parse_resonate()
        elif token.type == TokenType.MANIFEST:
            return self.parse_manifest()
        else:
            return None
    
    def parse_watch(self) -> WatchStatement:
        """Parse a Watch/Observe statement"""
        self.advance()  # WATCH or OBSERVE
        self.expect(TokenType.COLON)
        target = self.parse_expression()
        return WatchStatement(target=target)
    
    def parse_deliberate(self) -> DeliberateBlock:
        """Parse a Deliberate block"""
        self.expect(TokenType.DELIBERATE)
        self.expect(TokenType.LBRACE)
        
        statements = []
        while self.current_token().type != TokenType.RBRACE:
            token = self.current_token()
            
            if token.type == TokenType.PROPOSAL:
                statements.append(self.parse_proposal())
            elif token.type == TokenType.SYNTHESIZE:
                statements.append(self.parse_synthesize())
            elif token.type == TokenType.IDENTIFIER:
                # Generic statement
                name = self.advance().value
                self.expect(TokenType.COLON)
                value = self.parse_expression()
                statements.append({'type': name, 'value': value})
            else:
                break
        
        self.expect(TokenType.RBRACE)
        return DeliberateBlock(statements=statements)
    
    def parse_proposal(self) -> ProposalDefinition:
        """Parse a Proposal definition"""
        self.expect(TokenType.PROPOSAL)
        
        name = None
        if self.current_token().type == TokenType.STRING:
            name = self.advance().value
        
        self.expect(TokenType.LBRACE)
        
        properties = {}
        while self.current_token().type != TokenType.RBRACE:
            if self.current_token().type == TokenType.IDENTIFIER:
                prop_name = self.advance().value
                self.expect(TokenType.COLON)
                properties[prop_name] = self.parse_expression()
            else:
                break
        
        self.expect(TokenType.RBRACE)
        return ProposalDefinition(name=name, properties=properties)
    
    def parse_synthesize(self) -> SynthesizeBlock:
        """Parse a Synthesize block"""
        self.expect(TokenType.SYNTHESIZE)
        self.expect(TokenType.LBRACE)
        
        metrics = []
        while self.current_token().type != TokenType.RBRACE:
            if self.current_token().type == TokenType.METRIC:
                self.advance()
                self.expect(TokenType.COLON)
                metrics.append(self.parse_expression())
            elif self.current_token().type == TokenType.STRING:
                metrics.append(self.advance().value)
            else:
                break
        
        self.expect(TokenType.RBRACE)
        return SynthesizeBlock(metrics=metrics)
    
    def parse_resonate(self) -> ResonateBlock:
        """Parse a Resonate block"""
        self.expect(TokenType.RESONATE)
        self.expect(TokenType.LBRACE)
        
        properties = {}
        while self.current_token().type != TokenType.RBRACE:
            token = self.current_token()
            
            if token.type == TokenType.THRESHOLD:
                self.advance()
                self.expect(TokenType.COLON)
                properties['threshold'] = self.parse_expression()
            elif token.type == TokenType.ALIGNMENT:
                self.advance()
                self.expect(TokenType.COLON)
                properties['alignment'] = self.parse_expression()
            elif token.type == TokenType.SYNTHESIZE:
                properties['synthesize'] = self.parse_synthesize()
            else:
                break
        
        self.expect(TokenType.RBRACE)
        return ResonateBlock(properties=properties)
    
    def parse_manifest(self) -> ManifestBlock:
        """Parse a Manifest block"""
        self.expect(TokenType.MANIFEST)
        self.expect(TokenType.LPAREN)
        
        # Parse condition
        self.expect(TokenType.ON)
        condition = self.parse_expression()
        
        self.expect(TokenType.RPAREN)
        self.expect(TokenType.LBRACE)
        
        statements = []
        while self.current_token().type != TokenType.RBRACE:
            token = self.current_token()
            
            if token.type == TokenType.EXECUTE:
                statements.append(self.parse_execute())
            elif token.type == TokenType.UPDATE:
                statements.append(self.parse_update())
            else:
                break
        
        self.expect(TokenType.RBRACE)
        return ManifestBlock(condition=condition, statements=statements)
    
    def parse_execute(self) -> ExecuteStatement:
        """Parse an Execute statement"""
        self.expect(TokenType.EXECUTE)
        self.expect(TokenType.COLON)
        action = self.parse_expression()
        return ExecuteStatement(action=action)
    
    def parse_update(self) -> UpdateStatement:
        """Parse an Update statement"""
        self.expect(TokenType.UPDATE)
        self.expect(TokenType.COLON)
        target = self.parse_expression()
        
        value = None
        if self.current_token().type == TokenType.ARROW:
            self.advance()
            value = self.parse_expression()
        
        return UpdateStatement(target=target, value=value)
    
    def parse_decree(self) -> DecreeDeclaration:
        """Parse a Decree declaration"""
        self.expect(TokenType.DECREE)
        name = self.expect(TokenType.STRING).value
        self.expect(TokenType.LBRACE)
        
        properties = {}
        while self.current_token().type != TokenType.RBRACE:
            token = self.current_token()
            
            if token.type == TokenType.CONDITION:
                self.advance()
                self.expect(TokenType.COLON)
                properties['condition'] = self.parse_expression()
            elif token.type == TokenType.ACTION:
                self.advance()
                self.expect(TokenType.COLON)
                properties['action'] = self.expect(TokenType.STRING).value
            elif token.type == TokenType.CONSTRAINT:
                self.advance()
                self.expect(TokenType.COLON)
                properties['constraint'] = self.expect(TokenType.STRING).value
            else:
                break
        
        self.expect(TokenType.RBRACE)
        return DecreeDeclaration(name=name, properties=properties)
    
    def parse_expression(self) -> Any:
        """Parse an expression"""
        return self.parse_comparison()
    
    def parse_comparison(self) -> Any:
        """Parse a comparison expression"""
        left = self.parse_primary()
        
        token = self.current_token()
        if token.type in (TokenType.GT, TokenType.LT, TokenType.GTE, TokenType.LTE, TokenType.EQ, TokenType.NEQ):
            op = self.advance().type
            right = self.parse_primary()
            return {'type': 'comparison', 'op': op, 'left': left, 'right': right}
        
        return left
    
    def parse_primary(self) -> Any:
        """Parse a primary expression"""
        token = self.current_token()
        
        if token.type == TokenType.STRING:
            return Literal(value=self.advance().value)
        elif token.type == TokenType.NUMBER:
            return Literal(value=self.advance().value)
        else:
            # Handle identifiers and keywords that can be used as identifiers
            # In expressions, many keywords can act as identifiers
            if token.type in (TokenType.IDENTIFIER, TokenType.VESSEL, TokenType.POTENTIALITY,
                            TokenType.STATE, TokenType.DRIVE, TokenType.COVENANT, 
                            TokenType.RESONANCE):
                name = self.advance().value
            else:
                # Fallback - use token value as name
                name = str(token.value)
                self.advance()
            
            # Check for function call
            if self.current_token().type == TokenType.LPAREN:
                return self.parse_function_call(name)
            # Check for member access
            elif self.current_token().type == TokenType.DOT:
                return self.parse_member_access(name)
            else:
                return Identifier(name=name)
    
    def parse_function_call(self, name: str) -> FunctionCall:
        """Parse a function call"""
        self.expect(TokenType.LPAREN)
        
        arguments = []
        while self.current_token().type != TokenType.RPAREN:
            arguments.append(self.parse_expression())
            
            if self.current_token().type == TokenType.COMMA:
                self.advance()
        
        self.expect(TokenType.RPAREN)
        return FunctionCall(name=name, arguments=arguments)
    
    def parse_member_access(self, obj: str) -> MemberAccess:
        """Parse member access (e.g., Vessel.Grid.control)"""
        self.expect(TokenType.DOT)
        
        # Member can be identifier or keyword used as identifier
        member_token = self.current_token()
        if member_token.type in (TokenType.IDENTIFIER, TokenType.STATE, TokenType.DRIVE,
                                TokenType.VESSEL, TokenType.POTENTIALITY):
            member = self.advance().value
        else:
            member = self.expect(TokenType.IDENTIFIER).value
        
        result = MemberAccess(object=obj, member=member)
        
        # Chain member accesses
        while self.current_token().type == TokenType.DOT:
            self.advance()
            next_token = self.current_token()
            if next_token.type in (TokenType.IDENTIFIER, TokenType.STATE, TokenType.DRIVE,
                                  TokenType.VESSEL, TokenType.POTENTIALITY):
                next_member = self.advance().value
            else:
                next_member = self.expect(TokenType.IDENTIFIER).value
            result = MemberAccess(object=result, member=next_member)
        
        # Check for function call
        if self.current_token().type == TokenType.LPAREN:
            return self.parse_function_call_on_member(result)
        
        return result
    
    def parse_function_call_on_member(self, member_access: MemberAccess) -> FunctionCall:
        """Parse a function call on a member access"""
        self.expect(TokenType.LPAREN)
        
        arguments = []
        while self.current_token().type != TokenType.RPAREN:
            arguments.append(self.parse_expression())
            
            if self.current_token().type == TokenType.COMMA:
                self.advance()
        
        self.expect(TokenType.RPAREN)
        
        # Convert member access to function name
        func_name = self._member_access_to_string(member_access)
        return FunctionCall(name=func_name, arguments=arguments)
    
    def _member_access_to_string(self, ma: MemberAccess) -> str:
        """Convert MemberAccess to string representation"""
        if isinstance(ma.object, MemberAccess):
            return f"{self._member_access_to_string(ma.object)}.{ma.member}"
        else:
            return f"{ma.object}.{ma.member}"


# ============================================================================
# EXPORT
# ============================================================================

__all__ = [
    'TokenType', 'Token', 'Lexer',
    'ASTNode', 'Program', 'CovenantDeclaration', 'PantheonDeclaration',
    'AvatarDeclaration', 'DomainDeclaration', 'SoulDefinition',
    'PurposeDefinition', 'PulseDefinition', 'Parser'
]
