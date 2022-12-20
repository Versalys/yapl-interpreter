import unittest

class TestEnhancements(unittest.TestCase):
    
    def test_empty(self):
        from helpers import capture_intermediate_exec
        src = '''
        '''
        to_input = ""
        expected = ""
        stdout, st = capture_intermediate_exec(src, to_input)
        self.assertEquals(expected, stdout)


    def test_comments(self):
        from helpers import capture_intermediate_exec
        src = """# You should have removed the comments by now
        '''And this is another one that should be fliltered'''
        """
        to_input = ""
        expected = ""
        stdout, st = capture_intermediate_exec(src, to_input)
        self.assertEquals(expected, stdout)


    def test_literals_proect3(self):
        from helpers import capture_intermediate_exec
        src = """
        42
        True
        False
        """
        to_input = ""
        expected = ""
        stdout, st = capture_intermediate_exec(src, to_input)
        self.assertEquals(expected, stdout)


    def test_literal_float(self):
        from helpers import capture_intermediate_exec
        src = """
        3.14159
        """
        to_input = ""
        expected = ""
        stdout, st = capture_intermediate_exec(src, to_input)
        self.assertEquals(expected, stdout)

    def test_literal_char(self):
        from helpers import capture_intermediate_exec
        src = """
        'z'
        """
        to_input = ""
        expected = ""
        stdout, st = capture_intermediate_exec(src, to_input)
        self.assertEquals(expected, stdout)


    def test_char_escaped_0(self):
        from helpers import capture_intermediate_exec
        src = """
        '%n'
        '%t'
        '%%'
        """
        to_input = ""
        expected = ""
        stdout, st = capture_intermediate_exec(src, to_input)
        self.assertEquals(expected, stdout)

 
    def test_char_escaped_1(self):
        from helpers import capture_intermediate_exec
        src = """
        print {'%n'}
        """
        to_input = ""
        expected = "\n"
        stdout, st = capture_intermediate_exec(src, to_input)
        self.assertEquals(expected, stdout)


    def test_char_escaped_2(self):
        from helpers import capture_intermediate_exec
        src = """
        print {'%t'}
        """
        to_input = ""
        expected = "\t"
        stdout, st = capture_intermediate_exec(src, to_input)
        self.assertEquals(expected, stdout)


    def test_char_escaped_3(self):
        from helpers import capture_intermediate_exec
        src = """
        print {'%%'}
        """
        to_input = ""
        expected = "%"
        stdout, st = capture_intermediate_exec(src, to_input)
        self.assertEquals(expected, stdout)


    def test_char_escaped_4(self):
        from helpers import capture_intermediate_exec
        src = """
        print {'%''}
        """
        to_input = ""
        expected = "'"
        stdout, st = capture_intermediate_exec(src, to_input)
        self.assertEquals(expected, stdout)


    def test_declaration_project3(self):
        from helpers import capture_intermediate_exec
        src = '''
        int foo
        bool bar
        '''
        to_input = ""
        expected = ""
        stdout, st = capture_intermediate_exec(src, to_input)
        self.assertEquals(expected, stdout)

    
    def test_redeclaration_global_0(self):
        from helpers import capture_intermediate_exec
        src = '''
        bool foo
        int foo
        '''
        to_input = ""
        with self.assertRaises(Exception):
            stdout, st = capture_intermediate_exec(src, to_input)
    
    
    def test_assignment_project3(self):
        from helpers import capture_intermediate_exec
        src = '''
        int foo = 42
        bool bar = True
        println {foo}
        println {bar}
        '''
        to_input = ""
        stdout, st = capture_intermediate_exec(src, to_input)
        outs = stdout.split('\n')
        self.assertEquals(42, int(outs[0]))
        self.assertNotEquals(0, int(outs[1]))


    def test_print_multi_0(self):
        from helpers import capture_intermediate_exec
        src = '''
        println {42,57}
        '''
        to_input = ""
        expected = "4257\n"
        stdout, st = capture_intermediate_exec(src, to_input)
        self.assertEquals(expected, stdout)


    def test_print_multi_1(self):
        from helpers import capture_intermediate_exec
        src = '''
        println {'h', 'e', 'l', 'l', 'o'}
        '''
        to_input = ""
        expected = "hello\n"
        stdout, st = capture_intermediate_exec(src, to_input)
        self.assertEquals(expected, stdout)


    def test_declaration_project4(self):
        from helpers import capture_intermediate_exec
        src = '''
        char baz
        float blarg
        '''
        to_input = ""
        expected = ""
        stdout, st = capture_intermediate_exec(src, to_input)
        self.assertEquals(expected, stdout)


    def test_assignment_char(self):
        from helpers import capture_intermediate_exec
        src = '''
        char x = 'b'
        print {x}
        '''
        to_input = ""
        expected = "b"
        stdout, st = capture_intermediate_exec(src, to_input)
        self.assertEquals(expected, stdout)


    def test_assignment_float(self):
        from helpers import capture_intermediate_exec
        src = '''
        float pi = 3.14159
        print {pi}
        '''
        to_input = ""
        expected = 3.14159
        stdout, st = capture_intermediate_exec(src, to_input)
        self.assertAlmostEquals(expected, float(stdout))


    def test_math_negation(self):
        from helpers import capture_intermediate_exec
        src = '''
        println {-42}
        println {--68}
        '''
        to_input = ""
        expected = '-42\n68\n'
        stdout, st = capture_intermediate_exec(src, to_input)
        self.assertEquals(expected, stdout)


    def test_math_paren(self):
        from helpers import capture_intermediate_exec
        src = '''
        print {(440)}
        '''
        to_input = ""
        expected = '440'
        stdout, st = capture_intermediate_exec(src, to_input)
        self.assertEquals(expected, stdout)


    def test_math_binary_ints(self):
        from helpers import capture_intermediate_exec
        src = '''
        println {1+2}
        println {10-2}
        println {4*5}
        println {10/2}
        println {10%3}
        '''
        to_input = ""
        expected = '3\n8\n20\n5\n1\n'
        stdout, st = capture_intermediate_exec(src, to_input)
        self.assertEquals(expected, stdout)


    def test_math_float_0(self):
        from helpers import capture_intermediate_exec
        src = '''
        print {3.0 * 5.0}
        '''
        to_input = ""
        expected = 15.0
        stdout, st = capture_intermediate_exec(src, to_input)
        self.assertAlmostEquals(expected, float(stdout))


    def test_math_float_1(self):
        from helpers import capture_intermediate_exec
        src = '''
        print {2 * 1.1}
        '''
        to_input = ""
        expected = 2.2
        stdout, st = capture_intermediate_exec(src, to_input)
        self.assertAlmostEquals(expected, float(stdout))


    def test_math_float_2(self):
        from helpers import capture_intermediate_exec
        src = '''
        print {2.2 / 2}
        '''
        to_input = ""
        expected = 1.1
        stdout, st = capture_intermediate_exec(src, to_input)
        self.assertAlmostEquals(expected, float(stdout))


    def test_math_float_3(self):
        from helpers import capture_intermediate_exec
        src = '''
        print {-42.42}
        '''
        to_input = ""
        expected = -42.42
        stdout, st = capture_intermediate_exec(src, to_input)
        self.assertAlmostEquals(expected, float(stdout))


    def test_math_float_4(self):
        from helpers import capture_intermediate_exec
        src = '''
        print {-3.3%3.3}
        '''
        to_input = ""
        with self.assertRaises(Exception):
            stdout, st = capture_intermediate_exec(src, to_input)


    def test_math_mixed_0(self):
        from helpers import capture_intermediate_exec
        src = '''
        print {3 + 4.2 - 0.2}
        '''
        to_input = ""
        expected = 7.0
        stdout, st = capture_intermediate_exec(src, to_input)
        self.assertAlmostEquals(expected, float(stdout))


    def test_math_mixed_1(self):
        from helpers import capture_intermediate_exec
        src = '''
        int apple = 10
        float banana = 22.22
        float result = banana - apple
        print {result}
        '''
        to_input = ""
        expected = 12.22
        stdout, st = capture_intermediate_exec(src, to_input)
        self.assertAlmostEquals(expected, float(stdout))


    def test_logic_negation(self):
        from helpers import capture_intermediate_exec
        src = '''
        println {~True}
        println {~False}
        println {~~True}
        '''
        to_input = ""
        expected = [0, 1, 1]
        stdout, st = capture_intermediate_exec(src, to_input)
        bool_out = list(map(lambda x: 1 if int(x) != 0 else 0, stdout.strip().split('\n')))
        self.assertEquals(expected, bool_out)


    def test_logic_binary_and(self):
        from helpers import capture_intermediate_exec
        src = '''
        println {True and True}
        println {True and False}
        println {False and True}
        println {False and False}
        '''
        to_input = ""
        expected = [1, 0, 0, 0]
        stdout, st = capture_intermediate_exec(src, to_input)
        bool_out = list(map(lambda x: 1 if int(x) != 0 else 0, stdout.strip().split('\n')))
        self.assertEquals(expected, bool_out)


    def test_logic_binary_or(self):
        from helpers import capture_intermediate_exec
        src = '''
        println {True or True}
        println {True or False}
        println {False or True}
        println {False or False}
        '''
        to_input = ""
        expected = [1,1,1,0]
        stdout, st = capture_intermediate_exec(src, to_input)
        bool_out = list(map(lambda x: 1 if int(x) != 0 else 0, stdout.strip().split('\n')))
        self.assertEquals(expected, bool_out)


    def test_logic_binary_xor(self):
        from helpers import capture_intermediate_exec
        src = '''
        println {True xor True}
        println {True xor False}
        println {False xor True}
        println {False xor False}
        '''
        to_input = ""
        expected = [0,1,1,0]
        stdout, st = capture_intermediate_exec(src, to_input)
        bool_out = list(map(lambda x: 1 if int(x) != 0 else 0, stdout.strip().split('\n')))
        self.assertEquals(expected, bool_out)


    def test_compare_logic_equ(self):
        from helpers import capture_intermediate_exec
        src = '''
        println {True == True}
        println {True == False}
        println {False == True}
        println {False == False}
        '''
        to_input = ""
        expected = [1,0,0,1]
        stdout, st = capture_intermediate_exec(src, to_input)
        bool_out = list(map(lambda x: 1 if int(x) != 0 else 0, stdout.strip().split('\n')))
        self.assertEquals(expected, bool_out)


    def test_compare_logic_neq(self):
        from helpers import capture_intermediate_exec
        src = '''
        println {True ~= True}
        println {True ~= False}
        println {False ~= True}
        println {False ~= False}
        '''
        to_input = ""
        expected = [0,1,1,0]
        stdout, st = capture_intermediate_exec(src, to_input)
        bool_out = list(map(lambda x: 1 if int(x) != 0 else 0, stdout.strip().split('\n')))
        self.assertEquals(expected, bool_out)


    def test_compare_int_equ(self):
        from helpers import capture_intermediate_exec
        src = '''
        println {1 == 1}
        println {1 == 2}
        '''
        to_input = ""
        expected = [1, 0]
        stdout, st = capture_intermediate_exec(src, to_input)
        bool_out = list(map(lambda x: 1 if int(x) != 0 else 0, stdout.strip().split('\n')))
        self.assertEquals(expected, bool_out)


    def test_compare_int_neq(self):
        from helpers import capture_intermediate_exec
        src = '''
        println {1 ~= 1}
        println {1 ~= 2}
        '''
        to_input = ""
        expected = [0,1]
        stdout, st = capture_intermediate_exec(src, to_input)
        bool_out = list(map(lambda x: 1 if int(x) != 0 else 0, stdout.strip().split('\n')))
        self.assertEquals(expected, bool_out)


    def test_compare_int_less(self):
        from helpers import capture_intermediate_exec
        src = '''
        println {1 < 0}
        println {1 < 1}
        println {1 < 2}
        '''
        to_input = ""
        expected = [0,0,1]
        stdout, st = capture_intermediate_exec(src, to_input)
        bool_out = list(map(lambda x: 1 if int(x) != 0 else 0, stdout.strip().split('\n')))
        self.assertEquals(expected, bool_out)


    def test_compare_int_leq(self):
        from helpers import capture_intermediate_exec
        src = '''
        println {1 <= 0}
        println {1 <= 1}
        println {1 <= 2}
        '''
        to_input = ""
        expected = [0,1,1]
        stdout, st = capture_intermediate_exec(src, to_input)
        bool_out = list(map(lambda x: 1 if int(x) != 0 else 0, stdout.strip().split('\n')))
        self.assertEquals(expected, bool_out)


    def test_compare_int_greater(self):
        from helpers import capture_intermediate_exec
        src = '''
        println {1 > 0}
        println {1 > 1}
        println {1 > 2}
        '''
        to_input = ""
        expected = [1,0,0]
        stdout, st = capture_intermediate_exec(src, to_input)
        bool_out = list(map(lambda x: 1 if int(x) != 0 else 0, stdout.strip().split('\n')))
        self.assertEquals(expected, bool_out)


    def test_compare_int_geq(self):
        from helpers import capture_intermediate_exec
        src = '''
        println {1 >= 0}
        println {1 >= 1}
        println {1 >= 2}
        '''
        to_input = ""
        expected = [1,1,0]
        stdout, st = capture_intermediate_exec(src, to_input)
        bool_out = list(map(lambda x: 1 if int(x) != 0 else 0, stdout.strip().split('\n')))
        self.assertEquals(expected, bool_out)


    def test_compare_float_equ(self):
        from helpers import capture_intermediate_exec
        src = '''
        println {1.0 == 1.0}
        println {1.0 == 2.0}
        '''
        to_input = ""
        expected = [1, 0]
        stdout, st = capture_intermediate_exec(src, to_input)
        bool_out = list(map(lambda x: 1 if int(x) != 0 else 0, stdout.strip().split('\n')))
        self.assertEquals(expected, bool_out)


    def test_compare_float_neq(self):
        from helpers import capture_intermediate_exec
        src = '''
        println {1.0 ~= 1.0}
        println {1.0 ~= 2.0}
        '''
        to_input = ""
        expected = [0,1]
        stdout, st = capture_intermediate_exec(src, to_input)
        bool_out = list(map(lambda x: 1 if int(x) != 0 else 0, stdout.strip().split('\n')))
        self.assertEquals(expected, bool_out)


    def test_compare_float_less(self):
        from helpers import capture_intermediate_exec
        src = '''
        println {1.0 < 0.0}
        println {1.0 < 1.0}
        println {1.0 < 2.0}
        '''
        to_input = ""
        expected = [0,0,1]
        stdout, st = capture_intermediate_exec(src, to_input)
        bool_out = list(map(lambda x: 1 if int(x) != 0 else 0, stdout.strip().split('\n')))
        self.assertEquals(expected, bool_out)


    def test_compare_float_leq(self):
        from helpers import capture_intermediate_exec
        src = '''
        println {1.0 <= 0.0}
        println {1.0 <= 1.0}
        println {1.0 <= 2.0}
        '''
        to_input = ""
        expected = [0,1,1]
        stdout, st = capture_intermediate_exec(src, to_input)
        bool_out = list(map(lambda x: 1 if int(x) != 0 else 0, stdout.strip().split('\n')))
        self.assertEquals(expected, bool_out)


    def test_compare_float_greater(self):
        from helpers import capture_intermediate_exec
        src = '''
        println {1.0 > 0.0}
        println {1.0 > 1.0}
        println {1.0 > 2.0}
        '''
        to_input = ""
        expected = [1,0,0]
        stdout, st = capture_intermediate_exec(src, to_input)
        bool_out = list(map(lambda x: 1 if int(x) != 0 else 0, stdout.strip().split('\n')))
        self.assertEquals(expected, bool_out)


    def test_compare_float_geq(self):
        from helpers import capture_intermediate_exec
        src = '''
        println {1.0 >= 0.0}
        println {1.0 >= 1.0}
        println {1.0 >= 2.0}
        '''
        to_input = ""
        expected = [1,1,0]
        stdout, st = capture_intermediate_exec(src, to_input)
        bool_out = list(map(lambda x: 1 if int(x) != 0 else 0, stdout.strip().split('\n')))
        self.assertEquals(expected, bool_out)


    def test_compare_numeric_equ(self):
        from helpers import capture_intermediate_exec
        src = '''
        println {1 == 1.0}
        println {1 == 2.0}
        println {1.0 == 1}
        println {1.0 == 2}
        '''
        to_input = ""
        expected = [1, 0, 1, 0]
        stdout, st = capture_intermediate_exec(src, to_input)
        bool_out = list(map(lambda x: 1 if int(x) != 0 else 0, stdout.strip().split('\n')))
        self.assertEquals(expected, bool_out)


    def test_compare_numeric_neq(self):
        from helpers import capture_intermediate_exec
        src = '''
        println {1 ~= 1.0}
        println {1 ~= 2.0}
        println {1.0 ~= 1}
        println {1.0 ~= 2}
        '''
        to_input = ""
        expected = [0,1,0,1]
        stdout, st = capture_intermediate_exec(src, to_input)
        bool_out = list(map(lambda x: 1 if int(x) != 0 else 0, stdout.strip().split('\n')))
        self.assertEquals(expected, bool_out)


    def test_compare_numeric_less(self):
        from helpers import capture_intermediate_exec
        src = '''
        println {1 < 0.0}
        println {1 < 1.0}
        println {1 < 2.0}
        println {1.0 < 0}
        println {1.0 < 1}
        println {1.0 < 2}
        '''
        to_input = ""
        expected = [0,0,1]*2
        stdout, st = capture_intermediate_exec(src, to_input)
        bool_out = list(map(lambda x: 1 if int(x) != 0 else 0, stdout.strip().split('\n')))
        self.assertEquals(expected, bool_out)


    def test_compare_numeric_leq(self):
        from helpers import capture_intermediate_exec
        src = '''
        println {1 <= 0.0}
        println {1 <= 1.0}
        println {1 <= 2.0}
        println {1.0 <= 0}
        println {1.0 <= 1}
        println {1.0 <= 2}
        '''
        to_input = ""
        expected = [0,1,1]*2
        stdout, st = capture_intermediate_exec(src, to_input)
        bool_out = list(map(lambda x: 1 if int(x) != 0 else 0, stdout.strip().split('\n')))
        self.assertEquals(expected, bool_out)


    def test_compare_numeric_greater(self):
        from helpers import capture_intermediate_exec
        src = '''
        println {1 > 0.0}
        println {1 > 1.0}
        println {1 > 2.0}
        println {1.0 > 0}
        println {1.0 > 1}
        println {1.0 > 2}
        '''
        to_input = ""
        expected = [1,0,0]*2
        stdout, st = capture_intermediate_exec(src, to_input)
        bool_out = list(map(lambda x: 1 if int(x) != 0 else 0, stdout.strip().split('\n')))
        self.assertEquals(expected, bool_out)


    def test_compare_numeric_geq(self):
        from helpers import capture_intermediate_exec
        src = '''
        println {1 >= 0.0}
        println {1 >= 1.0}
        println {1 >= 2.0}
        println {1.0 >= 0}
        println {1.0 >= 1}
        println {1.0 >= 2}
        '''
        to_input = ""
        expected = [1,1,0]*2
        stdout, st = capture_intermediate_exec(src, to_input)
        bool_out = list(map(lambda x: 1 if int(x) != 0 else 0, stdout.strip().split('\n')))
        self.assertEquals(expected, bool_out)


    def test_compare_char_equ(self):
        from helpers import capture_intermediate_exec
        src = '''
        println {'a' == 'a'}
        println {'a' == 'z'}
        '''
        to_input = ""
        expected = [1,0]
        stdout, st = capture_intermediate_exec(src, to_input)
        bool_out = list(map(lambda x: 1 if int(x) != 0 else 0, stdout.strip().split('\n')))
        self.assertEquals(expected, bool_out)


    def test_compare_char_neq(self):
        from helpers import capture_intermediate_exec
        src = '''
        println {'a' ~= 'a'}
        println {'a' ~= 'z'}
        '''
        to_input = ""
        expected = [0,1]
        stdout, st = capture_intermediate_exec(src, to_input)
        bool_out = list(map(lambda x: 1 if int(x) != 0 else 0, stdout.strip().split('\n')))
        self.assertEquals(expected, bool_out)


    def test_compare_char_less(self):
        from helpers import capture_intermediate_exec
        src = '''
        println {'m' < 'a'}
        println {'m' < 'm'}
        println {'m' < 'z'}
        '''
        to_input = ""
        expected = [0,0,1]
        stdout, st = capture_intermediate_exec(src, to_input)
        bool_out = list(map(lambda x: 1 if int(x) != 0 else 0, stdout.strip().split('\n')))
        self.assertEquals(expected, bool_out)


    def test_compare_char_leq(self):
        from helpers import capture_intermediate_exec
        src = '''
        println {'m' <= 'a'}
        println {'m' <= 'm'}
        println {'m' <= 'z'}
        '''
        to_input = ""
        expected = [0,1,1]
        stdout, st = capture_intermediate_exec(src, to_input)
        bool_out = list(map(lambda x: 1 if int(x) != 0 else 0, stdout.strip().split('\n')))
        self.assertEquals(expected, bool_out)


    def test_compare_char_greater(self):
        from helpers import capture_intermediate_exec
        src = '''
        println {'m' > 'a'}
        println {'m' > 'm'}
        println {'m' > 'z'}
        '''
        to_input = ""
        expected = [1,0,0]
        stdout, st = capture_intermediate_exec(src, to_input)
        bool_out = list(map(lambda x: 1 if int(x) != 0 else 0, stdout.strip().split('\n')))
        self.assertEquals(expected, bool_out)


    def test_compare_char_geq(self):
        from helpers import capture_intermediate_exec
        src = '''
         println {'m' >= 'a'}
        println {'m' >= 'm'}
        println {'m' >= 'z'}
        '''
        to_input = ""
        expected = [1,1,0]
        stdout, st = capture_intermediate_exec(src, to_input)
        bool_out = list(map(lambda x: 1 if int(x) != 0 else 0, stdout.strip().split('\n')))
        self.assertEquals(expected, bool_out)

    
    def test_if_0(self):
        from helpers import capture_intermediate_exec
        src = '''
        if True then
            print {'x'}
        end
        print {'z'}
        '''
        to_input = ""
        expected = "xz"
        stdout, st = capture_intermediate_exec(src, to_input)
        self.assertEquals(expected, stdout)


    def test_if_1(self):
        from helpers import capture_intermediate_exec
        src = '''
        if False then
            print {'x'}
        end
        print {'z'}
        '''
        to_input = ""
        expected = "z"
        stdout, st = capture_intermediate_exec(src, to_input)
        self.assertEquals(expected, stdout)


    def test_if_2(self):
        from helpers import capture_intermediate_exec
        src = '''
        if 1==1 then
            print {'x'}
        end
        print {'z'}
        '''
        to_input = ""
        expected = "xz"
        stdout, st = capture_intermediate_exec(src, to_input)
        self.assertEquals(expected, stdout)


    def test_if_3(self):
        from helpers import capture_intermediate_exec
        src = '''
        if 1==2 then
            print {'x'}
        end
        print {'z'}
        '''
        to_input = ""
        expected = "z"
        stdout, st = capture_intermediate_exec(src, to_input)
        self.assertEquals(expected, stdout)

    
    def test_if_4(self):
        from helpers import capture_intermediate_exec
        src = '''
        bool test = True
        if test then
            print {'x'}
        end
        print {'z'}
        '''
        to_input = ""
        expected = "xz"
        stdout, st = capture_intermediate_exec(src, to_input)
        self.assertEquals(expected, stdout)


    def test_ifelse_0(self):
        from helpers import capture_intermediate_exec
        src = '''
        if True then
            print {'x'}
        else
            print {'y'}
        end
        print {'z'}
        '''
        to_input = ""
        expected = "xz"
        stdout, st = capture_intermediate_exec(src, to_input)
        self.assertEquals(expected, stdout)


    def test_ifelse_1(self):
        from helpers import capture_intermediate_exec
        src = '''
        if False then
            print {'x'}
        else
            print {'y'}
        end
        print {'z'}
        '''
        to_input = ""
        expected = "yz"
        stdout, st = capture_intermediate_exec(src, to_input)
        self.assertEquals(expected, stdout)


    def test_ifelse_2(self):
        from helpers import capture_intermediate_exec
        src = '''
        if 1==1 then
            print {'x'}
        else
            print {'y'}
        end
        print {'z'}
        '''
        to_input = ""
        expected = "xz"
        stdout, st = capture_intermediate_exec(src, to_input)
        self.assertEquals(expected, stdout)


    def test_ifelse_3(self):
        from helpers import capture_intermediate_exec
        src = '''
        if 1==2 then
            print {'x'}
        else
            print {'y'}
        end
        print {'z'}
        '''
        to_input = ""
        expected = "yz"
        stdout, st = capture_intermediate_exec(src, to_input)
        self.assertEquals(expected, stdout)

    
    def test_ifelse_4(self):
        from helpers import capture_intermediate_exec
        src = '''
        bool test = False
        if test then
            print {'x'}
        else
            print {'y'}
        end
        print {'z'}
        '''
        to_input = ""
        expected = "yz"
        stdout, st = capture_intermediate_exec(src, to_input)
        self.assertEquals(expected, stdout)

    
    def test_while_0(self):
        from helpers import capture_intermediate_exec
        src = '''
        int x = 0
        while x < 5 do
            print {'m'}
            x = x + 1
        end
        print {'n'}
        '''
        to_input = ""
        expected = "mmmmmn"
        stdout, st = capture_intermediate_exec(src, to_input)
        self.assertEquals(expected, stdout)


    def test_while_1(self):
        from helpers import capture_intermediate_exec
        src = '''
        int x = 0
        while x > 0 do
            print {'m'}
            x = x + 1
        end
        print {'n'}
        '''
        to_input = ""
        expected = "n"
        stdout, st = capture_intermediate_exec(src, to_input)
        self.assertEquals(expected, stdout)

    
    def test_break_0(self):
        from helpers import capture_intermediate_exec
        src = '''
        while True do
            break
        end
        print {'w'}
        '''
        to_input = ""
        expected = "w"
        stdout, st = capture_intermediate_exec(src, to_input)
        self.assertEquals(expected, stdout)


    def test_break_1(self):
        from helpers import capture_intermediate_exec
        src = '''
        int x = 0
        while x < 5 do
            print {'m'}
            if x == 2 then
                break
            end
            x = x + 1
        end
        print {'n'}
        '''
        to_input = ""
        expected = "mmmn"
        stdout, st = capture_intermediate_exec(src, to_input)
        self.assertEquals(expected, stdout)


    def test_minimumof_0(self):
        from helpers import capture_intermediate_exec
        src = '''
        print { minimum_of {42} }
        '''
        to_input = ""
        expected = "42"
        stdout, st = capture_intermediate_exec(src, to_input)
        self.assertEquals(expected, stdout)


    def test_minimumof_1(self):
        from helpers import capture_intermediate_exec
        src = '''
        print { minimum_of {42,57,4,99} }
        '''
        to_input = ""
        expected = "4"
        stdout, st = capture_intermediate_exec(src, to_input)
        self.assertEquals(expected, stdout)


    def test_maximumof_0(self):
        from helpers import capture_intermediate_exec
        src = '''
        print { maximum_of {99} }
        '''
        to_input = ""
        expected = "99"
        stdout, st = capture_intermediate_exec(src, to_input)
        self.assertEquals(expected, stdout)


    def test_maximumof_1(self):
        from helpers import capture_intermediate_exec
        src = '''
        print { maximum_of {4,99,212,3,53} }
        '''
        to_input = ""
        expected = "212"
        stdout, st = capture_intermediate_exec(src, to_input)
        self.assertEquals(expected, stdout)



    def test_bad_math_0(self):
        from helpers import capture_intermediate_exec
        src = '''
        1 + 'x'
        '''
        to_input = ""
        with self.assertRaises(Exception):
            stdout, st = capture_intermediate_exec(src, to_input)



    def test_bad_math_1(self):
        from helpers import capture_intermediate_exec
        src = '''
        True - 1
        '''
        to_input = ""
        with self.assertRaises(Exception):
            stdout, st = capture_intermediate_exec(src, to_input)


    def test_bad_math_2(self):
        from helpers import capture_intermediate_exec
        src = '''
        char foo = 'x'
        1.0 / foo
        '''
        to_input = ""
        with self.assertRaises(Exception):
            stdout, st = capture_intermediate_exec(src, to_input)


    def test_bad_assign_0(self):
        from helpers import capture_intermediate_exec
        src = '''
        int apple = 10
        float orange = apple
        '''
        to_input = ""
        with self.assertRaises(Exception):
            stdout, st = capture_intermediate_exec(src, to_input)


    def test_bad_assign_1(self):
        from helpers import capture_intermediate_exec
        src = '''
        int apple = 10
        bool orange = apple
        '''
        to_input = ""
        with self.assertRaises(Exception):
            stdout, st = capture_intermediate_exec(src, to_input)


    def test_bad_assign_2(self):
        from helpers import capture_intermediate_exec
        src = '''
        int apple = 10
        char orange = apple
        '''
        to_input = ""
        with self.assertRaises(Exception):
            stdout, st = capture_intermediate_exec(src, to_input)


    def test_bad_assign_3(self):
        from helpers import capture_intermediate_exec
        src = '''
        char apple = 'x'
        int orange = apple
        '''
        to_input = ""
        with self.assertRaises(Exception):
            stdout, st = capture_intermediate_exec(src, to_input)


    def test_bad_assign_4(self):
        from helpers import capture_intermediate_exec
        src = '''
        char apple = 'x'
        float orange = apple
        '''
        to_input = ""
        with self.assertRaises(Exception):
            stdout, st = capture_intermediate_exec(src, to_input)

    
    def test_bad_assign_5(self):
        from helpers import capture_intermediate_exec
        src = '''
        char apple = 'x'
        bool orange = apple
        '''
        to_input = ""
        with self.assertRaises(Exception):
            stdout, st = capture_intermediate_exec(src, to_input)


    def test_bad_if_test_0(self):
        from helpers import capture_intermediate_exec
        src = '''
        if 100 then
            print {'s'}
        end
        print {'t'}
        '''
        to_input = ""
        with self.assertRaises(Exception):
            stdout, st = capture_intermediate_exec(src, to_input)


    def test_bad_if_test_1(self):
        from helpers import capture_intermediate_exec
        src = '''
        if 100.0 then
            print {'s'}
        end
        print {'t'}
        '''
        to_input = ""
        with self.assertRaises(Exception):
            stdout, st = capture_intermediate_exec(src, to_input)

    
    def test_bad_if_test_2(self):
        from helpers import capture_intermediate_exec
        src = '''
        if 'x' then
            print {'s'}
        end
        print {'t'}
        '''
        to_input = ""
        with self.assertRaises(Exception):
            stdout, st = capture_intermediate_exec(src, to_input)


    def test_bad_ifelse_test(self):
        from helpers import capture_intermediate_exec
        src = '''
        if 100.0 then
            print {'s'}
        else
            print {'r'}
        end
        print {'t'}
        '''
        to_input = ""
        with self.assertRaises(Exception):
            stdout, st = capture_intermediate_exec(src, to_input)


    def test_bad_while_test(self):
        from helpers import capture_intermediate_exec
        src = '''
        while 'x' do
            break
        end
        '''
        to_input = ""
        with self.assertRaises(Exception):
            stdout, st = capture_intermediate_exec(src, to_input)


    def test_scope_0(self):
        from helpers import capture_intermediate_exec
        src = '''
        int foo = 10
        if True then
            char foo = 'x'
            print {foo}
        end
        print {foo}
        '''
        to_input = ""
        expected = "x10"
        stdout, st = capture_intermediate_exec(src, to_input)
        self.assertEquals(expected, stdout)


    def test_scope_1(self):
        from helpers import capture_intermediate_exec
        src = '''
        int foo = 10
        if False then
            char foo = 'x'
            print {foo}
        else
            bool foo = False
            print {foo}
        end
        print {foo}
        '''
        to_input = ""
        expected = "010"
        stdout, st = capture_intermediate_exec(src, to_input)
        self.assertEquals(expected, stdout)


    def test_scope_3(self):
        from helpers import capture_intermediate_exec
        src = '''
        int x = 1
        while x > 0 do
             x = x - 1
            char x = 'a'
            print {x}
        end
        print {x}
        '''
        to_input = ""
        expected = "a0"
        stdout, st = capture_intermediate_exec(src, to_input)
        self.assertEquals(expected, stdout)


    def test_scope_nested_0(self):
        from helpers import capture_intermediate_exec
        src = '''
        int foo = 10
        if True then
            char foo = 'x'
            if True then
                char foo = 'y'
                print {foo}
            end
        else
            bool foo = False
            print {foo}
        end
        print {foo}
        '''
        to_input = ""
        expected = "y10"
        stdout, st = capture_intermediate_exec(src, to_input)
        self.assertEquals(expected, stdout)



    def test_scope_nested_1(self):
        from helpers import capture_intermediate_exec
        src = '''
        int x = 2
        while x > 0 do
             if x == 1 then
                char x = 'p'
                print {x}
            end
            print{x}
            x = x - 1
        end
        print {x}
        '''
        to_input = ""
        expected = "2p10"
        stdout, st = capture_intermediate_exec(src, to_input)
        self.assertEquals(expected, stdout)


    def test_chained_assign(self):
        from helpers import capture_intermediate_exec
        src = '''
        int x
        int y
        int z = y = x = 42
        print {x,y,z}
        '''
        to_input = ""
        expected = "424242"
        stdout, st = capture_intermediate_exec(src, to_input)
        self.assertEquals(expected, stdout)



    def test_complex_0(self):
        from helpers import capture_intermediate_exec
        src = '''
        int x = 10
        while x <= 10 do
            x = x - 1
            if x == 3 then
                break
            end
        end
        print {x}
        '''
        to_input = ""
        expected = "3"
        stdout, st = capture_intermediate_exec(src, to_input)
        self.assertEquals(expected, stdout)

    def test_custom(self):
        return # TMP
        from helpers import capture_intermediate_exec
        src = src = '''
        print {-3.3%3.3}
        '''
        to_input = ""
        stdout, st = capture_intermediate_exec(src, to_input)
        print(stdout)


if __name__ == '__main__':
    unittest.main()
    # t = TestEnhancements()
    # t.test_maximumof_1()
