from exceptions import *
import sys

typ_map = {'bool':bool, 'char':str, 'string':str, 'int': int, 'float':float}

# may just let the sym table handle this. prob cleaner
def is_valid(a, b): # work in progress. has to rely on the entire programs typing
    typ_set = {int:{int, float}, float:{int, float}, bool:{bool}, list:{list}, str:{str}}
    if type(b) not in typ_set[type(a)]:
        return False # may just want to throw exception
    return True

# grouping them together for structure
class StructException(Exception):
    pass
class LoopBreak(StructException):
    pass
class FunctionReturn(StructException):
    pass

class ASTNode():
    def __init__(self, children):
        self.children = children

    def interpret(self):
        raise NotImplementedError('Interpret has been called on ASTNode')

class CmdNode(ASTNode):
    pass

class ExprNode(ASTNode):
    pass

# ============ COMMANDS ================
class StartNode(CmdNode):
    def interpret(self, st):
        st.push_scope()
        self.children[0].interpret(st)
        st.pop_scope()
        if st.scopes: # scopes must be empty. if not, print off scopes for debugging
            # print('Error, scoping not correct!\nScopes:\n')
            # for c,i in enumerate(st.scopes):
            #     print("Scope #",c,':')
            #     print(i)
            raise Exception(f'Scoping error. {st.scopes}')

class CmdListNode(CmdNode):
    def interpret(self, st):
        for child in self.children:
            child.interpret(st)

# ============ STATEMENTS ==============
class StmtDeclare(CmdNode):
    def interpret(self, st):
        st.declare(self.children[1], self.children[0], False)

class StmtDeclareAssign(CmdNode):
    def interpret(self, st):
        st.declare(self.children[1].children[0], self.children[0], False)
        val = self.children[1].interpret(st)
        st.set_val(self.children[1].children[0], val)

class StmtPrint(CmdNode):
    def interpret(self, st):
        exprlist = self.children[0].interpret(st)
        for val in exprlist:
            if isinstance(val, list):
                for v in val:
                    if isinstance(v, bool):
                        print(int(v), end='')
                    else:
                        print(v, end='')
            elif isinstance(val, bool):
                print(int(val),end="")
            else:
                print(val, end='')

class StmtPrintln(CmdNode):
    def interpret(self, st):
        exprlist = self.children[0].interpret(st)
        for val in exprlist:
            if isinstance(val, list):
                for v in val:
                    if isinstance(v, bool):
                        print(int(v), end='')
                    else:
                        print(v, end='')
            elif isinstance(val, bool):
                print(int(val),end="")
            else:
                print(val, end='')
        print() # print new ln

class StmtWhileLoop(CmdNode):
    def interpret(self, st):
        try:
            while t := self.children[0].interpret(st):
                if not isinstance(t, bool):
                    raise TypeMismatchError('Improper while loop test type {type(t)}')
                st.push_scope()
                self.children[1].interpret(st)
                st.pop_scope()
        except FunctionReturn as e:
            st.pop_scope()
            raise e
        except LoopBreak: # abusing python exceptions for break statements
            st.pop_scope()

class StmtForArrayID(CmdNode):
    def interpret(self, st):
        l = st.get_var(self.children[1])
        if not isinstance(l, list):
            raise TypeMismatchError('Scalar type used in for loop')
        if not l:
            return
        try:
            st.push_scope()
            st.declare(self.children[0], st.get_var_typ(self.children[1]), False)
            for i in l:
                st.push_scope()
                st.set_val(self.children[0], i) # set local variable
                self.children[2].interpret(st)
                st.pop_scope()
        except FunctionReturn as e:
            st.pop_scope()
            st.pop_scope()
            raise e
        except LoopBreak:
            pass
        st.pop_scope()

class StmtForRange(CmdNode):
    def interpret(self, st):
        l = self.children[1].interpret(st)
        assert isinstance(l, list)
        if not l:
            return
        try:
            st.push_scope()
            st.declare(self.children[0], 'int', False)
            for i in l:
                st.push_scope()
                st.set_val(self.children[0], i) # set local variable
                self.children[2].interpret(st)
                st.pop_scope()
        except FunctionReturn as e:
            st.pop_scope()
            st.pop_scope()
            raise e
        except LoopBreak:
            st.pop_scope()
        st.pop_scope()
        
class StmtBreak(CmdNode):
    def interpret(self, st):
        raise LoopBreak('Break called outside of a loop') # if not caught, error message displays

class StmtIf(CmdNode):
    def interpret(self, st):
        test = self.children[0].interpret(st)
        if not isinstance(test, bool):
            raise TypeMismatchError('Non bool used as an if test condition')
        try:
            if test:
                st.push_scope()
                self.children[1].interpret(st)
                st.pop_scope()
        except StructException as e:
            st.pop_scope()
            raise e
            

class StmtIfElse(CmdNode):
    def interpret(self, st):
        test = self.children[0].interpret(st)
        if not isinstance(test, bool):
            raise TypeMismatchError('Non bool used as an if test condition')
        try:
            if test:
                st.push_scope()
                self.children[1].interpret(st)
                st.pop_scope()
            else:
                st.push_scope()
                self.children[2].interpret(st)
                st.pop_scope()
        except StructException as e:
            st.pop_scope()
            raise e



# arrrays

class StmtDeclareArrayNoSizeNoAssign(CmdNode):
    def interpret(self, st):
        st.declare(self.children[1], self.children[0][:-1], True)

class StmtDeclareArraySizedNoAssign(CmdNode):
    def interpret(self, st):
        size = self.children[2].interpret(st)
        if not isinstance(size, int):
            raise TypeMismatchError('Non integer given as array size on declaration')
        st.declare(self.children[1], self.children[0][:-1], True, size)

class StmtDeclareArrayNoSizeAssign(CmdNode):
    def interpret(self, st):
        ident = self.children[1].children[0] # get identifier from child
        st.declare(ident, self.children[0][:-1], True)
        self.children[1].interpret(st)

class StmtDeclareArraySizedAssign(CmdNode):
    def interpret(self, st):
        size = self.children[1].interpret(st)
        if not isinstance(size, int):
            raise TypeMismatchError('Non integer given as array size')
        st.declare(self.children[2].children[0], self.children[0][:-1], True, size)
        self.children[2].interpret(st)
        
# functions
class StmtFuncDefine(CmdNode):
    def interpret(self, st):
        st.declare_function(self.children[0], self.children[3], self.children[1], self.children[2])
        # params are in the form (type, identifier)


class StmtFuncReturn(CmdNode): # one problem with using exceptions again is that values need to be returned as well. Could use something in the symbol table though
    def interpret(self, st):
        st.set_ret(self.children[0].interpret(st))
        st.pop_scope()
        raise FunctionReturn('Return statement uncaught')

# ============ EXPRESSIONS =============
class ExprListNode(ExprNode):
    def interpret(self, st):
        ret = []
        for child in self.children:
            ret.append(child.interpret(st))
        return ret

class ExprAssignArrayNdx(ExprNode):
    def interpret(self, st):
        ndx = self.children[1].interpret(st)
        if not isinstance(ndx, int):
            raise TypeMismatchError('Non int type used in indexing array.')
        l = st.get_var(self.children[0])
        if not isinstance(l, list):
            raise TypeMismatchError('Non list indexed')
        l[ndx] = self.children[2].interpret(st)
        return l[ndx]

class ExprArrayGetNdx(ExprNode):
    def interpret(self, st):
        ndx = self.children[1].interpret(st)

        if not isinstance(ndx, int):
            raise TypeMismatchError('Non int type used in indexing array.')

        return st.get_ndx(self.children[0], ndx)

class ExprArraySize(ExprNode):
    def interpret(self, st):
        return st.get_arr_size(self.children[0])

class ExprArrayCopy(ExprNode):
    def interpret(self, st):
        l = st.get_var(self.children[0])
        if not isinstance(l, list):
            raise TypeMismatchError('.copy invoked on non array')
        return l.copy()
    

class ExprArrRange(ExprNode):
    def interpret(self, st):
        start = self.children[0].interpret(st)
        step = self.children[1].interpret(st)
        stop = self.children[2].interpret(st)

        return list(range(start, stop, step))

class ExprID(ExprNode):
    def interpret(self, st):
        return st.get_var(self.children[0])

class ExprAssignNode(ExprNode):
    def interpret(self, st):
        old = st.get_var(self.children[0])
        new = self.children[1].interpret(st)
        if not isinstance(old, type(new)):
            raise TypeMismatchError('Assign (' + str(self.children[0]) + ')' + str(old) + ' : ' + str(type(new)))
        st.set_val(self.children[0], new)
        return new


# math
class ExprMathNegate(ExprNode):
    def interpret(self, st):
        val = self.children[0].interpret(st)
        if type(val) not in {int, float}:
            raise TypeMismatchError('Non-number used in numerical negation')
        return -val

class ExprMathBinary(ExprNode):
    def interpret(self, st):
        lhs = self.children[0].interpret(st)
        rhs = self.children[2].interpret(st)
        op = self.children[1]
        t = {int, float}
        if type(lhs) not in t or type(rhs) not in t:
            raise TypeMismatchError('Math binary called on non-numbers')

        if op == '+':
            return lhs + rhs
        if op == '-':
            return lhs - rhs
        if op == '*':
            return lhs * rhs
        if op == '%': # int only
            if isinstance(lhs, int) and isinstance(rhs, int):
                return lhs % rhs
            else:
                raise TypeMismatchError('Improper typing passed to modulous division.')
        if op == '/': # int or float handled differently
            if isinstance(lhs, int):
                return int(lhs / rhs)
            return lhs / rhs
        raise Exception(f'math binary has no applicable operator {op}')

class ExprMathNary(ExprNode):
    def interpret(self, st):
        l = self.children[1].interpret(st)
        if self.children[0] == 'sum_of':
            ret = 0
            for i in l:
                if type(i) not in {int, float}:
                    raise TypeMismatchError(f'Type mismatch in nary operation {i}')
                ret += i
            return ret
        # product_of
        elif self.children[0] == 'product_of':
            ret = 1
            for i in l:
                if type(i) not in {int, float}:
                    raise TypeMismatchError(f'Type mismatch in nary operation {i}')
                ret *= i
            return ret

        elif self.children[0] == 'maximum_of':
            return max(l)

        elif self.children[0] == 'minimum_of':
            return min(l)

        raise Exception('Invalid math nary operation')

class ExprMathNaryArray(ExprNode):
    def interpret(self, st):
        l = st.get_var(self.children[1])
        if not isinstance(l, list):
            raise TypeMismatchError('Scalar variable used in math_nary')
        if self.children[0] == 'sum_of':
            ret = 0
            for i in l:
                if type(i) not in {int, float}:
                    raise TypeMismatchError(f'Type mismatch in nary operation {i}')
                ret += i
            return ret
        elif self.children[0] == 'product_of':
            ret = 1
            for i in l:
                if type(i) not in {int, float}:
                    raise TypeMismatchError(f'Type mismatch in nary operation {i}')
                ret *= i
            return ret
        elif self.children[0] == 'maximum_of':
            return max(l)

        elif self.children[0] == 'minimum_of':
            return min(l)

        raise Exception('Invalid math nary operation')

# logic operations

class ExprLogicNegate(ExprNode):
    def interpret(self, st):
        val = self.children[0].interpret(st)
        if not isinstance(val, bool):
            raise TypeMismatchError('Logic negate used on non bool')
        return not val

class ExprLogicBinary(ExprNode):
    def interpret(self, st):
        lhs = self.children[0].interpret(st)
        rhs = self.children[2].interpret(st)
        op = self.children[1]

        if not isinstance(lhs, bool) or not isinstance(rhs, bool):
            raise TypeMismatchError('Binary logic used on non bool types')

        if op == 'and':
            return lhs and rhs
        if op == 'or':
            return lhs or rhs
        if op == 'xor':
            return (lhs or rhs) and not (lhs and rhs)
        raise NotImplementedError('Improper logic binary')

class ExprLogicNary(ExprNode):
    def interpret(self, st):
        l = self.children[1].interpret(st)

        if not isinstance(l, list):
            raise TypeMismatchError('Scalar type used in a nary operation')

        if not l or not isinstance(l[0], bool):
            raise TypeMismatchError('list empty or non bool type used')

        if self.children[0] == 'any_of':
            for i in l:
                if i:
                    return True
            return False
        # every_of
        for i in l:
            if not i:
                return False
        return True

class ExprLogicNaryArray(ExprNode):
    def interpret(self, st):
        l = st.get_var(self.children[1])

        if not isinstance(l, list):
            raise TypeMismatchError('Scalar type used in a nary operation')

        if not l or not isinstance(l[0], bool):
            raise TypeMismatchError('list empty or non bool type used')

        if self.children[0] == 'any_of':
            for i in l:
                if i:
                    return True
            return False
        # every_of
        if self.children[0] == 'every_of':
            for i in l:
                if not i:
                    return False
            return True
        raise Exception(f'Invalid nary op {self.children[0]}')

class ExprCompareBinary(ExprNode):
    def interpret(self, st):
        lhs = self.children[0].interpret(st)
        rhs = self.children[2].interpret(st)
        op = self.children[1]

        if not is_valid(lhs, rhs):
            raise TypeMismatchError(f'Incompatible types compared {type(lhs)} {type(rhs)}')

        # if type(lhs) not in {int, float}:
        #     if op != '!=' and op != '==':
        #         raise TypeMismatchError('Less/Greater than used on a non number')

        if op == '==':
            return lhs == rhs
        if op == '!=':
            return lhs != rhs
        if op =='<':
            return lhs < rhs
        if op == '<=':
            return lhs <= rhs
        if op == '>':
            return lhs > rhs
        if op == '>=':
            return lhs >= rhs
        if op == "~=":
            return lhs != rhs
        raise Exception('Invalid Compare Operation')

class ExprInput(ExprNode):
    def interpret(self, st):
        try:
            if self.children[0] == 'input_int':
                return int(input())
            if self.children[0] == 'input_float':
                return float(input())
            if self.children[0] == 'input_char':
                return sys.stdin.read(1) # get one byte from stdin
                
        except ValueError:
            raise TypeMismatchError('Improper type passed in as input')
        raise Exception("no type, " + self.children[0])

class ExprFuncCall(ExprNode):
    def interpret(self, st):
        try:
            st.call_function(self.children[0], [i.interpret(st) for i in self.children[1]]) # needs to be 
        except FunctionReturn:
            return st.get_ret() # let symbol table handle return values
        return None

# base nodes
class ExprIntLiteralNode(ExprNode):
    def interpret(self, st):
        return int(self.children[0])

class ExprFloatLiteralNode(ExprNode):
    def interpret(self ,st):
        return float(self.children[0])

class ExprBoolLiteralNode(ExprNode):
    def interpret(self, st):
        if self.children[0] == 'True':
            return True
        return False

class ExprCharLiteralNode(ExprNode):
    def interpret(self, st):
        l = self.children[0][1:-1]
        if len(l) == 2:
            if l[0] == '%':
                if l[1] == 'n':
                    return '\n'
                if l[1] == 't':
                    return '\t'
                if l[1] == '"':
                    return '"'
                if l[1] == "'":
                    return "'"
                if l[1] == '%':
                    return '%'
                raise Exception('Escape sequence not defined')
            raise Exception(f'Char literals must be one character {l}')
        if l[0] == '%':
            raise Exception('Escape character "\" does not have a sequence.')
        return l

class ExprStringLiteral(ExprNode):
    def interpret(self, st):
        literal = self.children[0][1:-1]
        ret = []
        i = 0
        while i < len(literal):
            if literal[i] == '%':
                if i == len(literal)-1:
                    raise Exception('Escape sequence as last character')
                if literal[i+1] == 'n':
                    ret += '\n'
                elif literal[i+1] == 't':
                    ret += '\t'
                elif literal[i+1] == '\'':
                    ret += '\''
                elif literal[i+1] == '"':
                    ret += '"'
                elif literal[i+1] == '%':
                    ret += '%'
                else:
                    raise Exception(f'Improper escape sequence {literal[i+1]}')
                i += 1 # extra iter
            else:
                ret += literal[i]
            i += 1 # extra iter
        return ret
