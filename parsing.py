from typing import SupportsAbs
from rply import ParserGenerator
from ast_nodes import *

def do_source_parsing(toks, possible_tokens):
    parser = build_parser(possible_tokens)
    return parser.parse(iter(toks))



def build_parser(possible_tokens):
    precedence = [
        ('right', ['ASSIGN']),
        ('right', ['COLON']),
        ('left', ['COMPARE_BINARY_OP']),
        ('left', ['MATH_PLUS', 'MATH_MINUS', 'LOGIC_BINARY_OP']),
        ('left', ['MATH_BINARY_OP']),
        ('right', ['MATH_NEGATION', 'LOGIC_UNARY_OP']),
    ]

    pg = ParserGenerator(possible_tokens, precedence)

    @pg.error
    def on_error(p):
        print(f'There was an error processing token {p}')


    @pg.production('start : cmd_list')
    def start(p):
        return StartNode([ CmdListNode(p[0]) ])

    
    @pg.production('cmd_list : ')
    def cmd_list_empty(p):
        return []


    @pg.production('cmd_list : cmd EOC cmd_list')
    def cmd_list(p):
        return p[0] + p[2]



    # ==================================================================== COMMANDS
    @pg.production('cmd : ')
    def cmd_empty(p):
        return []

    @pg.production('cmd : stmt')
    @pg.production('cmd : all_expr')
    def cmd_not_empty(p):
        return [p[0]]

    
    @pg.production('all_expr : expr')
    @pg.production('all_expr : range')
    def all_expr_passthrough(p):
        return p[0]



    # ==================================================================== LISTS
    @pg.production('expr_list : BRACE_OPEN expr_list_head expr_list_tail BRACE_CLOSE')
    def expr_list(p):
        elist = p[1] + p[2]
        return ExprListNode(elist)

    @pg.production('expr_list_head : all_expr')
    def expr_list_head(p):
        return [p[0]]

    @pg.production('expr_list_tail : ')
    @pg.production('expr_list_tail : COMMA all_expr expr_list_tail')
    def expr_list_tail(p):
        if len(p) == 0:
            return []
        else:
            return [p[1]] + p[2]


    # ==================================================================== STATEMENTS
    @pg.production('stmt : SCALAR_TYPE IDENTIFIER')
    def stmt_declare_scalar_noassgn(p):
        dtype, ident = p
        return StmtDeclare([dtype.value, ident.value])
        

    @pg.production('stmt : SCALAR_TYPE assign')
    def stmt_declare_scalar_assgn(p):
        dtype, assign = p[0].value, p[1]
        return StmtDeclareAssign([dtype, assign])
    

    @pg.production('stmt : PRINTING expr_list')
    def stmt_printing(p):
        if p[0].value == 'print':
            return StmtPrint([p[1]])
        else:
            return StmtPrintln([p[1]])


    # ==================================================================== EXPRESSIONS

    @pg.production('expr : assign')
    def assign_passthrough(p):
        return p[0]


    @pg.production('assign : IDENTIFIER ASSIGN expr')
    @pg.production('assign : IDENTIFIER ASSIGN expr_list')
    @pg.production('assign : IDENTIFIER ASSIGN range')
    def assignment(p):
        id, expr = p[0].value, p[2]
        return ExprAssignNode([id, expr])

    @pg.production('assign : IDENTIFIER BRACKET_OPEN expr BRACKET_CLOSE ASSIGN expr')
    def assignment_array_ndx(p):
        ident, ndx, expr = p[0].value, p[2], p[5]
        return ExprAssignArrayNdx([ident, ndx, expr])


    @pg.production('expr : INT_LITERAL')
    def expr_literal_int(p):
        int_lexeme = p[0].value
        return ExprIntLiteralNode([int_lexeme])


    @pg.production('expr : BOOL_LITERAL')
    def expr_literal_bool(p):
        bool_lexeme = p[0].value
        return ExprBoolLiteralNode([bool_lexeme])


    @pg.production('expr : FLOAT_LITERAL')
    def expr_literal_float(p):
        bool_lexeme = p[0].value
        return ExprFloatLiteralNode([bool_lexeme])


    @pg.production('expr : CHAR_LITERAL')
    def expr_literal_char(p):
        char_lexeme = p[0].value
        return ExprCharLiteralNode([char_lexeme])


    @pg.production('expr : IDENTIFIER')
    def expr_id(p):
        ident = p[0].value
        return ExprID([ident])



    @pg.production('expr : PAREN_OPEN expr PAREN_CLOSE')
    def expr_parentheses(p):
        return p[1]


    @pg.production('expr : MATH_MINUS expr', precedence='MATH_NEGATION')
    def expr_math_negation(p):
        return ExprMathNegate([p[1]])


    @pg.production('expr : expr MATH_PLUS expr')
    @pg.production('expr : expr MATH_MINUS expr')
    @pg.production('expr : expr MATH_BINARY_OP expr')
    def expr_math_binary_ops(p):
        lhs, op, rhs = p[0], p[1].value, p[2]
        return ExprMathBinary([lhs, op, rhs])


    @pg.production('expr : MATH_NARY_OP expr_list')
    def expr_math_nary_ops(p):
        op, expr_list = p[0].value, p[1]
        return ExprMathNary([op, expr_list])


    @pg.production('expr : MATH_NARY_OP IDENTIFIER')
    def expr_math_nary_ops_arr(p):
        op, expr = p[0].value, p[1].value
        return ExprMathNaryArray([op, expr])

    
    @pg.production('expr : LOGIC_UNARY_OP expr')
    def expr_logic_negation(p):
        return ExprLogicNegate([p[1]])


    @pg.production('expr : expr LOGIC_BINARY_OP expr')
    def expr_logic_binary_ops(p):
        lhs, op, rhs = p[0], p[1].value, p[2]
        return ExprLogicBinary([lhs, op, rhs])


    @pg.production('expr : LOGIC_NARY_OP expr_list')
    def expr_logic_nary_ops(p):
        op, expr_list = p[0].value, p[1]
        return ExprLogicNary([op, expr_list])


    @pg.production('expr : LOGIC_NARY_OP IDENTIFIER')
    def expr_logic_nary_ops_arr(p):
        op, expr = p[0].value, p[1].value
        return ExprLogicNaryArray([op, expr])


    @pg.production('expr : expr COMPARE_BINARY_OP expr')
    def expr_compare_binary_ops(p):
        lhs, op, rhs = p[0], p[1].value, p[2]
        return ExprCompareBinary([lhs, op, rhs])


    @pg.production('expr : INPUTTING')
    def expr_input(p):
        return ExprInput([p[0].value])

    @pg.production('stmt : IF expr THEN cmd_list END')
    def stmt_if(p):
        test, true_block = p[1], CmdListNode(p[3])
        return StmtIf([test, true_block])


    @pg.production('stmt : IF expr THEN cmd_list ELSE cmd_list END')
    def stmt_if_else(p):
        test, true_block, else_block = p[1], CmdListNode(p[3]), CmdListNode(p[5])
        return StmtIfElse([test, true_block, else_block])


    @pg.production('stmt : WHILE expr DO cmd_list END')
    def stmt_while(p):
        test, block = p[1], CmdListNode(p[3])
        return StmtWhileLoop([test, block])


    @pg.production('stmt : BREAK')
    def stmt_break(p):
        return StmtBreak([])

    
    
    # ==================================================================== ARRAY

    @pg.production('stmt : ARRAY_TYPE BRACKET_CLOSE IDENTIFIER')
    def stmt_declare_array_nosz_noassgn(p):
        dtype, ident = p[0].value, p[2].value
        return StmtDeclareArrayNoSizeNoAssign([dtype, ident])

    
    @pg.production('stmt : ARRAY_TYPE expr BRACKET_CLOSE IDENTIFIER')
    def stmt_declare_array_wsz_noassign(p):
        dtype, size, ident = p[0].value, p[1], p[3].value
        return StmtDeclareArraySizedNoAssign([dtype, ident, size])

    
    @pg.production('stmt : ARRAY_TYPE BRACKET_CLOSE assign')
    def stmt_declare_array_nosz_assgn(p):
        dtype, assign = p[0].value, p[2]
        return StmtDeclareArrayNoSizeAssign([dtype, assign])

    
    @pg.production('stmt : ARRAY_TYPE expr BRACKET_CLOSE assign')
    def stmt_declare_array_wsz_assign(p):
        dtype, size, assign = p[0].value, p[1], p[3]
        return StmtDeclareArraySizedAssign([dtype, size, assign])


    @pg.production('expr : STRING_LITERAL')
    def expr_string_literal(p):
        return ExprStringLiteral([p[0].value])


    @pg.production('range : range_head range_tail')
    def expr_range_parts(p):
        first, second = p[0][0], p[0][1]
        third = p[1]
        if len(third) == 0:
            third = second
            second = ExprIntLiteralNode(['1'])
        else:
            third = third[0]
        start, step, stop = first, second, third
        return ExprArrRange([start, step, stop])


    @pg.production('range_head : expr COLON expr')
    def expr_range_head(p):
        first, second = p[0], p[2]
        return [first, second]


    @pg.production('range_tail : ')
    @pg.production('range_tail : COLON expr')
    def expr_range_tail(p):
        if len(p) == 0:
            return []
        return [p[1]]


    @pg.production('expr : IDENTIFIER BRACKET_OPEN expr BRACKET_CLOSE')
    def expr_arr_ndx(p):
        ident, ndx = p[0].value, p[2]
        return ExprArrayGetNdx([ident, ndx])


    @pg.production('expr : IDENTIFIER ARR_SIZE')
    def expr_arr_size(p):
        ident = p[0].value
        return ExprArraySize([ident])

    

    @pg.production('expr : IDENTIFIER ARR_COPY')
    def expr_arr_copy(p):
        ident = p[0].value
        return ExprArrayCopy([ident])


    @pg.production('stmt : FOR IDENTIFIER IN IDENTIFIER DO cmd_list END')
    def stmt_for_array(p):
        ident_local, ident_arr, cmd_list = p[1].value, p[3].value, CmdListNode(p[5])
        return StmtForArrayID([ident_local, ident_arr, cmd_list])


    @pg.production('stmt : FOR IDENTIFIER IN range DO cmd_list END')
    def stmt_for_range(p):
        ident_local, the_range, cmd_list = p[1].value, p[3], CmdListNode(p[5])
        return StmtForRange([ident_local, the_range, cmd_list])





    # ==================================================================== FUNCTION
    @pg.production('stmt : FUNC_DEF FUNC_IDENTIFIER type_list PAREN_CLOSE FUNC_RETURN_OP any_type COLON cmd_list END')
    def stmt_func_declare(p):
        ident, parameters, return_type, cmd_list = p[1].value[:-1], p[2], p[5], CmdListNode(p[7])
        return StmtFuncDefine([ident, parameters, return_type, cmd_list])


    @pg.production('expr : FUNC_IDENTIFIER arg_list PAREN_CLOSE')
    def expr_func_call(p):
        ident, expr_list = p[0].value[:-1], p[1]
        return ExprFuncCall([ident, expr_list])


    @pg.production('stmt : FUNC_RETURN all_expr')
    def stmt_func_return(p):
        expr = p[1]
        return StmtFuncReturn([expr])

    @pg.production('any_type : SCALAR_TYPE')
    @pg.production('any_type : ARRAY_TYPE BRACKET_CLOSE')
    def any_type(p):
        return p[0].value

    
    @pg.production('type_list : ')
    @pg.production('type_list : any_type COLON IDENTIFIER opt_type_list_tail')
    def type_list(p):
        if len(p) == 0:
            return []
        param_type, identifier, tail = p[0], p[2].value, p[3]
        return [(param_type, identifier)] + tail


    @pg.production('opt_type_list_tail : ')
    @pg.production('opt_type_list_tail : COMMA any_type COLON IDENTIFIER opt_type_list_tail')
    def type_list_tail(p):
        if len(p) == 0:
            return []
        param_type, identifier, tail = p[1], p[3].value, p[4]
        return [(param_type, identifier)] + tail


    
    @pg.production('arg_list : ')
    def arg_list_empty(p):
        return []

    @pg.production('arg_list : all_expr opt_arg_list_tail')
    def arg_list_not_empty(p):
        return [p[0]] + p[1]

    @pg.production('opt_arg_list_tail : COMMA all_expr opt_arg_list_tail')
    def arg_list_tail_notempty(p):
        return [p[1]] + p[2]

    @pg.production('opt_arg_list_tail : ')
    def arg_list_tail_empty(p):
        return []

        

    return pg.build()
    

