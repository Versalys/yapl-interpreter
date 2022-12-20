from rply import LexerGenerator
from exceptions import *
import re

def do_source_lexing(src):
    """
    Build the lexer and perform the lexing

    Arguments
        src     source code source

    Returns
        A list of tokens
    """
    lg = build_source_lexer()
    lexer = lg.build()
    tokens = list(lexer.lex(src))

    possible_tokens = {rule.name  for rule in lg.rules}
    possible_tokens.remove('ERROR')
    possible_tokens.remove('COMMENT_MULTI')
    possible_tokens.remove('COMMENT_SINGLE')
    n_tokens = []
    for i in tokens:
        if not(i.name == 'COMMENT_SINGLE' or i.name == 'COMMENT_MULTI'):
            n_tokens.append(i)
    return n_tokens, possible_tokens



def build_source_lexer():
    """
    Configure a new instance of the LexerGenerator
    to handle the source language.

    The lists below will configure the lexer generator.
    
    The first element in the list is the token name.

    The second element in the list is a list of regular expressions
    that match the lexemes for the token.

    An optional third element in the list adds flags from the re library
    to handle things like multiple lines.
    """


    # The tokens identifying scalar types
    scalar_types = ['SCALAR_TYPE', [r'\bint\b', r'\bfloat\b', r'\bchar\b', r'\bbool\b']]
    array_types = ['ARRAY_TYPE', [r'\bint\[', r'\bfloat\[', r'\bchar\[', r'\bbool\[']]

    array_size = ['ARR_SIZE', [r'\.length\b']]
    array_copy = ['ARR_COPY', [r'\.copy\b']]

    # The tokens identifying literals   
    string_literal = ['STRING_LITERAL', [r'"(%[nt%"]|[^"])*"'] ]
    char_literal = ['CHAR_LITERAL', [r"'%[nt%']'", r"'.'" ] ]
    int_literal = ['INT_LITERAL', [r'\d+']]
    float_literal = ['FLOAT_LITERAL', [r'\d+\.\d+']]
    bool_literal = ['BOOL_LITERAL', [r'\bTrue\b|\bFalse\b']]

    # Declaration and assignment operator
    assignment = ['ASSIGN', [r'=']]

    # The tokens identifying single-operand math operations and minus
    math_minus = ['MATH_MINUS', [r'\-']]

    # Plus can be part of a numeric literal or the addition operator
    math_plus = ['MATH_PLUS', [r'\+']]

    # The tokens identifying double-operand math operations
    math_binary_ops = ['MATH_BINARY_OP', [r'/', r'%',r'\*']]

    # The tokens identifying math-nary operations
    math_nary_ops = ['MATH_NARY_OP', [r'\bsum_of\b', r'\bproduct_of\b', r'\bminimum_of\b', r'\bmaximum_of\b']]

    # The tokens identifying logic unary operations
    logic_unary_ops = ['LOGIC_UNARY_OP', [r'~']]

    # The tokens identifying binary logic operations
    logic_binary_ops = ['LOGIC_BINARY_OP', [r'\band\b', r'\bor\b', r'\bxor\b']]

    # The tokens identifying n-ary logic operations
    logic_nary_ops = ['LOGIC_NARY_OP', [r'\bevery_of\b', r'\bany_of\b']]

    # The tokens identifying comparison operations
    compare_binary_ops = ['COMPARE_BINARY_OP', [r'<=', r'>=', r'==', r'~=', r'<', r'>']]  # Note the ordering

    # The print commands
    printing = ['PRINTING', [r'\bprintln\b', r'\bprint\b']]


    # The input commands
    inputting = ['INPUTTING', [r'\binput_bool\b', r'\binput_char\b', r'\binput_float\b', r'\binput_int\b']]

    # Flow Control
    kw_if = ['IF', [r'\bif\b']]
    kw_then = ['THEN', [r'\bthen\b']]
    kw_else = ['ELSE', [r'\belse\b']]
    kw_end = ['END', [r'\bend\b']]
    kw_while = ['WHILE', [r'\bwhile\b']]
    kw_do = ['DO', [r'\bdo\b']]
    kw_break = ['BREAK', [r'\bbreak\b']]
    kw_for = ['FOR', [r'\bfor\b']]
    kw_in = ['IN', [r'\bin\b']]


    # Comments
    comment_single = ['COMMENT_SINGLE', [r'#.*']]
    comment_multi = ['COMMENT_MULTI', [r"'''.*'''"], re.M | re.DOTALL] # <-- requires re.M


    # Identifier
    identifier = ['IDENTIFIER', [r'\b[a-zA-Z][a-zA-Z_\d]*\b']]

    # Function TO
    kw_def = ['FUNC_DEF', [r'\bdef\b']]
    
    # Func call identifier
    func_call = ['FUNC_IDENTIFIER', [r'\b[a-zA-Z][a-zA-Z_\d]*\(']]

    kw_return = ['FUNC_RETURN', [r'\breturn\b']]

    func_out_op = ['FUNC_RETURN_OP', [r'\->']]



    # Parentheses
    paren_open = ['PAREN_OPEN', [r'\(']]
    paren_close = ['PAREN_CLOSE', [r'\)']]

     # Braces
    brace_open = ['BRACE_OPEN', [r'\{']]
    brace_close = ['BRACE_CLOSE', [r'\}']]

    # Bracket
    bracket_open = ['BRACKET_OPEN', [r'\['] ]
    bracket_close = ['BRACKET_CLOSE', [r'\]'] ]


    # Commas
    comma = ['COMMA', ',']

    # Colon
    colon = ['COLON', ':']

    # End of Statement
    eos = ['EOC', [r'\n']]

    # Error
    error = ['ERROR', [r'.']]

    
    # Actually configure the lexer generator
    lg = LexerGenerator()

    # Ignore spaces and tabs
    lg.ignore(r'[ \t]+')

    # Add our adds
    add_order = [
            comment_multi,
            comment_single,
            array_types,
            array_size, array_copy,
            scalar_types,
            compare_binary_ops,
            assignment,
            string_literal,
            float_literal, char_literal, bool_literal, int_literal,
            math_nary_ops, logic_nary_ops,
            func_out_op,
            math_minus, math_plus, math_binary_ops,
            logic_unary_ops, logic_binary_ops,
            printing,
            inputting,
            kw_if, kw_in, kw_then, kw_else, kw_while, kw_do, kw_end, kw_break, 
            kw_for,
            kw_def, func_call, kw_return,
            identifier,
            paren_open, paren_close,
            brace_open, brace_close,
            bracket_open, bracket_close,
            comma,
            colon,
            eos,
            error]

    for entry in add_order:
        if len(entry) == 3:
            tok_name, tok_patterns, tok_flags = entry
        else:
            tok_name, tok_patterns = entry
            tok_flags = 0   # No flags set
        for p in tok_patterns:
            lg.add(tok_name, p, tok_flags)
    
    return lg
    
    



