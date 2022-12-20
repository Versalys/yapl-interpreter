#!/usr/bin/python3.8

'''
Main file for the honors option interpreter. Dispatches functionality to the parser,
lexer, and the execution to the ast nodes from the aforementioned functions
'''
from lexing import *
from parsing import *
from symbol_table import *

from sys import argv, stderr

def main():
    if len(argv) == 1:
        filename = input('Give a filename: ')
    elif len(argv) == 2:
        filename = argv[1]
    else:
        print("Too many arguments passed in! :", len(argv), file=stderr)
        exit(1)

    with open(filename, 'r') as f:
        src = '\n'.join(f)
        tokens, possible_tokens = do_source_lexing(src)
        root = do_source_parsing(tokens, possible_tokens)
        st = SymbolTable()
        
        root.interpret(st)

        # print('functions:', st.functions)

if __name__ == '__main__':
    main()
