from exceptions import *

class ImproperFunctionCall(Exception):
    pass

class SymbolTable:
    def __init__(self):
        self.scopes = []
        self.functions = {}
        self.stack = []
        self.typ_map = {'bool':bool, 'char':str, 'string':str, 'int': int, 'float':float}

    def declare(self, ident, typ, is_arr, size=0):
        defaults = {'int':0, 'float':0.0, 'bool':False, 'char':'\0'}
        if ident in self.scopes[-1]:
            raise RedeclarionError(f'Variable {ident} redeclared : {self.scopes}')
        self.scopes[-1][ident] = [defaults[typ] if not is_arr else [None]*size, typ, is_arr]

    def get_ndx(self, ident, index):
        l = self.get_var(ident)
        if not isinstance(l, list):
            raise TypeMismatchError('Attempt to subscript a scalar type')
        if index >= len(l):
            raise OutOfBoundsError(f'{index} index is out of bounds for {ident}:{len(l)}')

        return l[index]

    def set_ndx(self, ident, index, new):
        l = self.get_var(ident)
        if not isinstance(l, list):
            raise TypeMismatchError('Attempt to subscript a scalar type')
        if index >= len(self.scopes):
            raise OutOfBoundsError(f'{index} index is out of bounds for {ident}')

        l[index] = new # need to implement type checking for this... maybe ;)

    def get_arr_size(self, ident):
        l = self.get_var(ident)
        if not isinstance(l, list):
            raise TypeMismatchError('Size invoked on scalar variable')
        return len(l)

    def set_val(self, ident, val):
        for scope in reversed(self.scopes):
            if ident in scope:
                if not self.typ_map[scope[ident][1]] == type(val):
                    if not (isinstance(val, list) and scope[ident][2]):
                        raise TypeMismatchError(f'Improper assignment {scope[ident][1]} {type(val)}')
                    if scope[ident][0]: # if sized, fill to capactiy. If not, set capacity
                        for i in range(len(scope[ident][0])):
                            if len(val) > i:
                                scope[ident][0][i] = val[i]
                        return
                scope[ident][0] = val
                return
        raise UndeclaredError('Set val used on undeclared variable')

    def get_var(self, ident):
        for scope in reversed(self.scopes):
            if ident in scope:
                return scope[ident][0]
        print('scopes', self.scopes)
        for k,i in enumerate(self.scopes):
            print('scope:',k)
            for c,v in i.items():
                print('\t', c, v)
        raise UndeclaredError(f'Get var used on undeclared variable {ident}')
    

    def get_var_typ(self, ident):
        for scope in reversed(self.scopes):
            if ident in scope:
                return scope[ident][1]
        for k,i in enumerate(self.scopes):
            print('scope:',k)
            for c,v in i.items():
                print('\t', c, v)
        raise UndeclaredError(f'Get var used on undeclared variable {ident}')

    def declare_function(self, ident, start, params, ret_type):
        new_params = []
        for typ, name in params:
            if typ[-1] == '[': # converts between the two typing schemes
                new_params.append([name, typ[:-1], True, 0])
            else:
                new_params.append([name, typ, False, 0])
        self.functions[ident] = [start, ret_type, new_params]

    def call_function(self, fident, args):
        '''
        FUNCTION TOPOLOGY
        There will be a function declaration node with a function
        start node as its child. the funciton declaration node will
        declare with the symbol table the function but will not run 
        interpret on the child. The declaration node will pass on the
        start node to the st to be run from.
        '''
        self.push_scope() # push scopes
        if len(args) != len(self.functions[fident][2]):
            raise ImproperFunctionCall('Incorrect number of arguments passed to function')
        for c, (ident, typ, is_arr, size) in enumerate(self.functions[fident][2]): # declare params on scope
            if is_arr:
                if not isinstance(args[c], list):
                    raise ImproperFunctionCall('Scalar given as a vector argument')
                if args[c]:
                    if self.typ_map[typ] != type(args[c][0]):
                        raise ImproperFunctionCall('Improper vector type given as argument')
                self.declare(ident, typ, is_arr, len(args[c]))
            else:
                if self.typ_map[typ] != type(args[c]):
                    raise ImproperFunctionCall('Wrong scalar type given to function call')
                self.declare(ident, typ, is_arr, size)
            self.set_val(ident, args[c])
        self.functions[fident][0].interpret(self)
        self.pop_scope()

    def pop_scope(self):
        self.scopes.pop()

    def push_scope(self):
        self.scopes.append({})

    def set_ret(self, ret):
        self.ret = ret

    def get_ret(self):
        # if self.ret == None:
            # raise Exception('Function has no return value')
        ret = self.ret
        self.ret = None
        return ret
