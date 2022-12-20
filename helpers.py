
def get_token_names(lex_retval):
    """
    Convert a list of tokens into a list of just the token names
    """
    tokens, possible_tokens = lex_retval
    return list(map(lambda x: x.name, tokens))


def test_rules(src):
    """
    Given a source, lex it and pass the token stream
    to the parser.
    """
    from solution import parse_source
    parse_source(src)


def capture_intermediate_exec(src_code, to_input=""):
    import io
    import contextlib
    import sys
    from solution import compile_source_intermediate

    old_stdin = sys.stdin

    sys.stdin = io.StringIO(to_input)

    f = io.StringIO()
    with contextlib.redirect_stdout(f):
        stable = compile_source_intermediate(src_code)
        # for c,v in stable.memory.items():
            # print(c, v.as_string())
    
    sys.stdin = old_stdin

    return f.getvalue(), stable
