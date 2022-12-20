from ast_nodes import *
from solution import *

import unittest

class TestInterpreting(unittest.TestCase):

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
        src = "# You should have removed the comments by now"
        to_input = ""
        expected = ""
        stdout, st = capture_intermediate_exec(src, to_input)
        self.assertEquals(expected, stdout)


    def test_declaration_0(self):
        from helpers import capture_intermediate_exec
        src = '''
        int foo
        '''
        to_input = ""
        expected = ""
        stdout, st = capture_intermediate_exec(src, to_input)
        self.assertEquals(expected, stdout)


    def test_declaration_1(self):
        from helpers import capture_intermediate_exec
        src = '''
        bool bar
        '''
        to_input = ""
        expected = ""
        stdout, st = capture_intermediate_exec(src, to_input)
        self.assertEquals(expected, stdout)


    def test_declaration_2(self):
        from helpers import capture_intermediate_exec
        src = '''
        int baz
        bool baz
        '''
        to_input = ""
        expected = ""
        with self.assertRaises(Exception):
            stdout, st = capture_intermediate_exec(src, to_input)

    
    def test_int_literal(self):
        from helpers import capture_intermediate_exec
        src = '''
        42
        '''
        to_input = ""
        expected = ""
        stdout, st = capture_intermediate_exec(src, to_input)
        self.assertEquals(expected, stdout)


    def test_bool_literal(self):
        from helpers import capture_intermediate_exec
        src = '''
        True
        False
        '''
        to_input = ""
        expected = ""
        stdout, st = capture_intermediate_exec(src, to_input)
        self.assertEquals(expected, stdout)


    def test_print_int(self):
        from helpers import capture_intermediate_exec
        src = '''
        print {43}
        '''
        to_input = ""
        expected = "43"
        stdout, st = capture_intermediate_exec(src, to_input)
        self.assertEquals(expected, stdout)


    def test_print_bool_0(self):
        from helpers import capture_intermediate_exec
        src = '''
        print {True}
        '''
        to_input = ""
        stdout, st = capture_intermediate_exec(src, to_input)
        assert(stdout[-1] != '\n')
        self.assertNotEqual(0, int(stdout))


    def test_print_bool_1(self):
        from helpers import capture_intermediate_exec
        src = '''
        print {False}
        '''
        to_input = ""
        stdout, st = capture_intermediate_exec(src, to_input)
        assert(stdout[-1] != '\n')
        self.assertEqual(0, int(stdout))


    def test_println_int(self):
        from helpers import capture_intermediate_exec
        src = '''
        println {57}
        '''
        to_input = ""
        expected = "57\n"
        stdout, st = capture_intermediate_exec(src, to_input)
        self.assertEquals(expected, stdout)


    def test_println_bool_0(self):
        from helpers import capture_intermediate_exec
        src = '''
        println {True}
        '''
        to_input = ""
        stdout, st = capture_intermediate_exec(src, to_input)
        assert(stdout[-1] == '\n')
        self.assertNotEqual(0, int(stdout))


    def test_println_bool_1(self):
        from helpers import capture_intermediate_exec
        src = '''
        println {False}
        '''
        to_input = ""
        stdout, st = capture_intermediate_exec(src, to_input)
        assert(stdout[-1] == '\n')
        self.assertEqual(0, int(stdout))


    def test_print_multi(self):
        from helpers import capture_intermediate_exec
        src = '''
        print {10, 20, 30}
        '''
        to_input = ""
        expected = '102030'
        stdout, st = capture_intermediate_exec(src, to_input)
        self.assertEquals(expected, stdout)


    def test_println_multi(self):
        from helpers import capture_intermediate_exec
        src = '''
        println {11, 22, 33, 44, 55}
        '''
        to_input = ""
        expected = '1122334455\n'
        stdout, st = capture_intermediate_exec(src, to_input)
        self.assertEquals(expected, stdout)


    def test_math_negation_0(self):
        from helpers import capture_intermediate_exec
        src = '''
        print {-44}
        '''
        to_input = ""
        expected = '-44'
        stdout, st = capture_intermediate_exec(src, to_input)
        self.assertEquals(expected, stdout)


    def test_math_negation_1(self):
        from helpers import capture_intermediate_exec
        src = '''
        print {--68}
        '''
        to_input = ""
        expected = '68'
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


    def test_math_add_0(self):
        from helpers import capture_intermediate_exec
        src = '''
        print {1+2}
        '''
        to_input = ""
        expected = '3'
        stdout, st = capture_intermediate_exec(src, to_input)
        self.assertEquals(expected, stdout)


    def test_math_sub_0(self):
        from helpers import capture_intermediate_exec
        src = '''
        print {22-10}
        '''
        to_input = ""
        expected = '12'
        stdout, st = capture_intermediate_exec(src, to_input)
        self.assertEquals(expected, stdout)


    def test_math_mul_0(self):
        from helpers import capture_intermediate_exec
        src = '''
        print {4*5}
        '''
        to_input = ""
        expected = '20'
        stdout, st = capture_intermediate_exec(src, to_input)
        self.assertEquals(expected, stdout)


    def test_math_div_0(self):
        from helpers import capture_intermediate_exec
        src = '''
        print {10/2}
        '''
        to_input = ""
        expected = '5'
        stdout, st = capture_intermediate_exec(src, to_input)
        self.assertEquals(expected, stdout)
    

    def test_math_div_1(self):
        from helpers import capture_intermediate_exec
        src = '''
        print {10/2}
        '''
        to_input = ""
        expected = '5'
        stdout, st = capture_intermediate_exec(src, to_input)
        self.assertEquals(expected, stdout)


    def test_math_idiv_0(self):
        from helpers import capture_intermediate_exec
        src = '''
        print {10%2}
        '''
        to_input = ""
        expected = '0'
        stdout, st = capture_intermediate_exec(src, to_input)
        self.assertEquals(expected, stdout)


    def test_logic_negation_0(self):
        from helpers import capture_intermediate_exec
        src = '''
        print {~True}
        '''
        to_input = ""
        stdout, st = capture_intermediate_exec(src, to_input)
        self.assertEquals(0, int(stdout))


    def test_logic_negation_1(self):
        from helpers import capture_intermediate_exec
        src = '''
        print {~False}
        '''
        to_input = ""
        stdout, st = capture_intermediate_exec(src, to_input)
        self.assertNotEquals(0, int(stdout))


    def test_logic_negation_2(self):
        from helpers import capture_intermediate_exec
        src = '''
        print {~~True}
        '''
        to_input = ""
        stdout, st = capture_intermediate_exec(src, to_input)
        self.assertNotEquals(0, int(stdout))
    

    def test_logic_and_0(self):
        from helpers import capture_intermediate_exec
        src = '''
        print {True and True}
        '''
        to_input = ""
        stdout, st = capture_intermediate_exec(src, to_input)
        self.assertNotEquals(0, int(stdout))


    def test_logic_and_1(self):
        from helpers import capture_intermediate_exec
        src = '''
        print {True and False}
        '''
        to_input = ""
        stdout, st = capture_intermediate_exec(src, to_input)
        self.assertEquals(0, int(stdout))


    def test_logic_and_2(self):
        from helpers import capture_intermediate_exec
        src = '''
        print {False and True}
        '''
        to_input = ""
        stdout, st = capture_intermediate_exec(src, to_input)
        self.assertEquals(0, int(stdout))


    def test_logic_and_3(self):
        from helpers import capture_intermediate_exec
        src = '''
        print {False and False}
        '''
        to_input = ""
        stdout, st = capture_intermediate_exec(src, to_input)
        self.assertEquals(0, int(stdout))


    def test_logic_or_0(self):
        from helpers import capture_intermediate_exec
        src = '''
        print {True or True}
        '''
        to_input = ""
        stdout, st = capture_intermediate_exec(src, to_input)
        self.assertNotEquals(0, int(stdout))


    def test_logic_or_1(self):
        from helpers import capture_intermediate_exec
        src = '''
        print {True or False}
        '''
        to_input = ""
        stdout, st = capture_intermediate_exec(src, to_input)
        self.assertNotEquals(0, int(stdout))


    def test_logic_or_2(self):
        from helpers import capture_intermediate_exec
        src = '''
        print {False or True}
        '''
        to_input = ""
        stdout, st = capture_intermediate_exec(src, to_input)
        self.assertNotEquals(0, int(stdout))


    def test_logic_or_3(self):
        from helpers import capture_intermediate_exec
        src = '''
        print {False and False}
        '''
        to_input = ""
        stdout, st = capture_intermediate_exec(src, to_input)
        self.assertEquals(0, int(stdout))


    def test_logic_xor_0(self):
        from helpers import capture_intermediate_exec
        src = '''
        print {True xor True}
        '''
        to_input = ""
        stdout, st = capture_intermediate_exec(src, to_input)
        self.assertEquals(0, int(stdout))


    def test_logic_xor_1(self):
        from helpers import capture_intermediate_exec
        src = '''
        print {True xor False}
        '''
        to_input = ""
        stdout, st = capture_intermediate_exec(src, to_input)
        self.assertNotEquals(0, int(stdout))


    def test_logic_xor_2(self):
        from helpers import capture_intermediate_exec
        src = '''
        print {False xor True}
        '''
        to_input = ""
        stdout, st = capture_intermediate_exec(src, to_input)
        self.assertNotEquals(0, int(stdout))


    def test_logic_xor_3(self):
        from helpers import capture_intermediate_exec
        src = '''
        print {False xor False}
        '''
        to_input = ""
        stdout, st = capture_intermediate_exec(src, to_input)
        self.assertEquals(0, int(stdout))


    def test_compare_nequ_0(self):
        from helpers import capture_intermediate_exec
        src = '''
        print {1 ~= 2}
        '''
        to_input = ""
        stdout, st = capture_intermediate_exec(src, to_input)
        self.assertNotEquals(0, int(stdout))


    def test_compare_nequ_1(self):
        from helpers import capture_intermediate_exec
        src = '''
        print {1 ~= 1}
        '''
        to_input = ""
        stdout, st = capture_intermediate_exec(src, to_input)
        self.assertEquals(0, int(stdout))


    def test_compare_equ_0(self):
        from helpers import capture_intermediate_exec
        src = '''
        print {1 == 2}
        '''
        to_input = ""
        stdout, st = capture_intermediate_exec(src, to_input)
        self.assertEquals(0, int(stdout))


    def test_compare_equ_1(self):
        from helpers import capture_intermediate_exec
        src = '''
        print {1 == 1}
        '''
        to_input = ""
        stdout, st = capture_intermediate_exec(src, to_input)
        self.assertNotEquals(0, int(stdout))


    def test_compare_less_0(self):
        from helpers import capture_intermediate_exec
        src = '''
        print {1 < 2}
        '''
        to_input = ""
        stdout, st = capture_intermediate_exec(src, to_input)
        self.assertNotEquals(0, int(stdout))


    def test_compare_less_1(self):
        from helpers import capture_intermediate_exec
        src = '''
        print {1 < 0}
        '''
        to_input = ""
        stdout, st = capture_intermediate_exec(src, to_input)
        self.assertEquals(0, int(stdout))


    def test_compare_less_2(self):
        from helpers import capture_intermediate_exec
        src = '''
        print {1 < 1}
        '''
        to_input = ""
        stdout, st = capture_intermediate_exec(src, to_input)
        self.assertEquals(0, int(stdout))


    def test_compare_greater_0(self):
        from helpers import capture_intermediate_exec
        src = '''
        print {1 > 2}
        '''
        to_input = ""
        stdout, st = capture_intermediate_exec(src, to_input)
        self.assertEquals(0, int(stdout))


    def test_compare_greater_1(self):
        from helpers import capture_intermediate_exec
        src = '''
        print {1 > 0}
        '''
        to_input = ""
        stdout, st = capture_intermediate_exec(src, to_input)
        self.assertNotEquals(0, int(stdout))


    def test_compare_greater_2(self):
        from helpers import capture_intermediate_exec
        src = '''
        print {1 > 1}
        '''
        to_input = ""
        stdout, st = capture_intermediate_exec(src, to_input)
        self.assertEquals(0, int(stdout))


    def test_compare_leq_0(self):
        from helpers import capture_intermediate_exec
        src = '''
        print {1 <= 2}
        '''
        to_input = ""
        stdout, st = capture_intermediate_exec(src, to_input)
        self.assertNotEquals(0, int(stdout))


    def test_compare_leq_1(self):
        from helpers import capture_intermediate_exec
        src = '''
        print {1 <= 0}
        '''
        to_input = ""
        stdout, st = capture_intermediate_exec(src, to_input)
        self.assertEquals(0, int(stdout))


    def test_compare_leq_2(self):
        from helpers import capture_intermediate_exec
        src = '''
        print {1 <= 1}
        '''
        to_input = ""
        stdout, st = capture_intermediate_exec(src, to_input)
        self.assertNotEquals(0, int(stdout))


    def test_compare_geq_0(self):
        from helpers import capture_intermediate_exec
        src = '''
        print {1 >= 2}
        '''
        to_input = ""
        stdout, st = capture_intermediate_exec(src, to_input)
        self.assertEquals(0, int(stdout))


    def test_compare_geq_1(self):
        from helpers import capture_intermediate_exec
        src = '''
        print {1 >= 0}
        '''
        to_input = ""
        stdout, st = capture_intermediate_exec(src, to_input)
        self.assertNotEquals(0, int(stdout))


    def test_compare_geq_2(self):
        from helpers import capture_intermediate_exec
        src = '''
        print {1 >= 1}
        '''
        to_input = ""
        stdout, st = capture_intermediate_exec(src, to_input)
        self.assertNotEquals(0, int(stdout))


    def test_math_sum_of(self):
        from helpers import capture_intermediate_exec
        src = '''
        print { sum_of {2,3,4} }
        '''
        to_input = ""
        expected = 9
        stdout, st = capture_intermediate_exec(src, to_input)
        self.assertEquals(expected, int(stdout))


    def test_math_product_of(self):
        from helpers import capture_intermediate_exec
        src = '''
        print { product_of {2,3,4} }
        '''
        to_input = ""
        expected = 24
        stdout, st = capture_intermediate_exec(src, to_input)
        self.assertEquals(expected, int(stdout))


    def test_logic_any_of_0(self):
        from helpers import capture_intermediate_exec
        src = '''
        print { any_of {True, False, False} }
        '''
        to_input = ""
        stdout, st = capture_intermediate_exec(src, to_input)
        self.assertNotEquals(0, int(stdout))


    def test_logic_any_of_1(self):
        from helpers import capture_intermediate_exec
        src = '''
        print { any_of {True, True, True} }
        '''
        to_input = ""
        stdout, st = capture_intermediate_exec(src, to_input)
        self.assertNotEquals(0, int(stdout))


    def test_logic_any_of_2(self):
        from helpers import capture_intermediate_exec
        src = '''
        print { any_of {False, False, False} }
        '''
        to_input = ""
        stdout, st = capture_intermediate_exec(src, to_input)
        self.assertEquals(0, int(stdout))


    def test_logic_every_of_0(self):
        from helpers import capture_intermediate_exec
        src = '''
        print { every_of {True, False, False} }
        '''
        to_input = ""
        stdout, st = capture_intermediate_exec(src, to_input)
        self.assertEquals(0, int(stdout))


    def test_logic_every_of_1(self):
        from helpers import capture_intermediate_exec
        src = '''
        print { every_of {True, True, True} }
        '''
        to_input = ""
        stdout, st = capture_intermediate_exec(src, to_input)
        self.assertNotEquals(0, int(stdout))


    def test_logic_every_of_2(self):
        from helpers import capture_intermediate_exec
        src = '''
        print { every_of {False, False, False} }
        '''
        to_input = ""
        stdout, st = capture_intermediate_exec(src, to_input)
        self.assertEquals(0, int(stdout))


    def test_declare_w_init_int(self):
        from helpers import capture_intermediate_exec
        src = '''
        int foo = 57
        print { foo }
        '''
        to_input = ""
        expected = 57
        stdout, st = capture_intermediate_exec(src, to_input)
        self.assertEquals(expected, int(stdout))


    def test_declare_w_init_bool_0(self):
        from helpers import capture_intermediate_exec
        src = '''
        bool bar = True
        print { bar }
        '''
        to_input = ""
        stdout, st = capture_intermediate_exec(src, to_input)
        self.assertNotEquals(0, int(stdout))


    def test_declare_w_init_bool_1(self):
        from helpers import capture_intermediate_exec
        src = '''
        bool baz = False
        print { baz }
        '''
        to_input = ""
        stdout, st = capture_intermediate_exec(src, to_input)
        self.assertEquals(0, int(stdout))


    def test_declare_w_init_chaining(self):
        from helpers import capture_intermediate_exec
        src = '''
        int foo
        int bar = foo = 27
        print { foo, bar }
        '''
        to_input = ""
        expected = '2727'
        stdout, st = capture_intermediate_exec(src, to_input)
        self.assertEquals(expected, stdout)


    def test_complex_0(self):
        from helpers import capture_intermediate_exec
        src = '''
        int is_even = 10 % 2
        int is_odd = 11 % 2
        print {is_even == is_odd}
        '''
        to_input = ""
        stdout, st = capture_intermediate_exec(src, to_input)
        self.assertEquals(0, int(stdout))


    def test_complex_1(self):
        from helpers import capture_intermediate_exec
        src = '''
        int sum = sum_of {10, 20, 30, 40}
        int product = product_of {11, 22, 33, 44}
        print {product > sum}
        '''
        to_input = ""
        stdout, st = capture_intermediate_exec(src, to_input)
        self.assertNotEquals(0, int(stdout))


    def test_complex_2(self):
        from helpers import capture_intermediate_exec
        src = '''
        int foo = product_of{1,2,3} + 4
        int bar = 12 * foo + 1
        print {bar == 12 * foo + 1}
        '''
        to_input = ""
        stdout, st = capture_intermediate_exec(src, to_input)
        self.assertNotEquals(0, int(stdout))


    def test_complex_3(self):
        from helpers import capture_intermediate_exec
        src = '''
        bool my_and = True and True and False
        bool my_or = False or False or True
        bool both = my_and and my_or
        print {both}
        '''
        to_input = ""
        stdout, st = capture_intermediate_exec(src, to_input)
        self.assertEquals(0, int(stdout))


    def test_complex_4(self):
        from helpers import capture_intermediate_exec
        src = '''
        int foo = (1 + ( (2*3+1) * 3 )) / 11
        int bar = 20
        print {foo*bar}
        '''
        to_input = ""
        expected = 40
        stdout, st = capture_intermediate_exec(src, to_input)
        self.assertEquals(40, int(stdout))


    def test_complex_5(self):
        from helpers import capture_intermediate_exec
        src = '''
        bool x
        x = (2*3 == 2+3+1) and any_of{False, True}
        print {x}
        '''
        to_input = ""
        stdout, st = capture_intermediate_exec(src, to_input)
        self.assertNotEquals(0, int(stdout))


    def test_complex_6(self):
        from helpers import capture_intermediate_exec
        src = '''
        int foo = 10
        int bar = 100
        bool lesser = foo < bar
        print {(lesser) and ~False}
        '''
        to_input = ""
        stdout, st = capture_intermediate_exec(src, to_input)
        self.assertNotEquals(0, int(stdout))


    def test_complex_7(self):
        from helpers import capture_intermediate_exec
        src = '''
        int foo = product_of {10,20}
        int bar = sum_of {10, 20}
        bool neq = foo ~= bar
        print {(neq) and False}
        '''
        to_input = ""
        stdout, st = capture_intermediate_exec(src, to_input)
        self.assertEquals(0, int(stdout))

    def test_custom(self):
        from helpers import capture_intermediate_exec
        code = '''
        bool x
        x = (2*3 == 2+3+1) and any_of{False, True}
        print {x}
        '''

        src = '''
        bool x
        x = 2*3 == 2+3+1
        print {x}
        '''
        to_input = ""
        stdout, st = capture_intermediate_exec(src, to_input)
        print(stdout)
        # self.assertNotEquals(0, int(stdout))


        
if __name__ == '__main__':
    unittest.main()
