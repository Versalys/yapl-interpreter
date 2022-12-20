import unittest

class FunctionTest(unittest.TestCase):
    
    def test_empty(self):
        from helpers import capture_intermediate_exec
        src = """
        """
        to_input = ""
        expected = ""
        stdout, st = capture_intermediate_exec(src, to_input)
        self.assertEquals(expected, stdout)


    def test_def_ret_type_0(self):
        from helpers import capture_intermediate_exec
        src = """
        def some_funtion() -> int:
        end
        """
        to_input = ""
        expected = ""
        stdout, st = capture_intermediate_exec(src, to_input)
        self.assertEquals(expected, stdout)


    def test_def_ret_type_1(self):
        from helpers import capture_intermediate_exec
        src = """
        def another_function() -> float:
        end
        """
        to_input = ""
        expected = ""
        stdout, st = capture_intermediate_exec(src, to_input)
        self.assertEquals(expected, stdout)


    def test_def_ret_type_2(self):
        from helpers import capture_intermediate_exec
        src = """
        def so_many_functions() -> bool:
        end
        """
        to_input = ""
        expected = ""
        stdout, st = capture_intermediate_exec(src, to_input)
        self.assertEquals(expected, stdout)


    def test_def_ret_type_3(self):
        from helpers import capture_intermediate_exec
        src = """
        def too_many_functions() -> char:
        end
        """
        to_input = ""
        expected = ""
        stdout, st = capture_intermediate_exec(src, to_input)
        self.assertEquals(expected, stdout)


    def test_def_ret_type_4(self):
        from helpers import capture_intermediate_exec
        src = """
        def some_funtion() -> int[]:
        end
        """
        to_input = ""
        expected = ""
        stdout, st = capture_intermediate_exec(src, to_input)
        self.assertEquals(expected, stdout)


    def test_def_ret_type_5(self):
        from helpers import capture_intermediate_exec
        src = """
        def another_function() -> float[]:
        end
        """
        to_input = ""
        expected = ""
        stdout, st = capture_intermediate_exec(src, to_input)
        self.assertEquals(expected, stdout)


    def test_def_ret_type_6(self):
        from helpers import capture_intermediate_exec
        src = """
        def so_many_functions() -> bool[]:
        end
        """
        to_input = ""
        expected = ""
        stdout, st = capture_intermediate_exec(src, to_input)
        self.assertEquals(expected, stdout)


    def test_def_ret_type_7(self):
        from helpers import capture_intermediate_exec
        src = """
        def too_many_functions() -> char[]:
        end
        """
        to_input = ""
        expected = ""
        stdout, st = capture_intermediate_exec(src, to_input)
        self.assertEquals(expected, stdout)


    def test_def_one_arg_0(self):
        from helpers import capture_intermediate_exec
        src = """
        def one_argument(int:x) -> int:
        end
        """
        to_input = ""
        expected = ""
        stdout, st = capture_intermediate_exec(src, to_input)
        self.assertEquals(expected, stdout)


    def test_def_one_arg_1(self):
        from helpers import capture_intermediate_exec
        src = """
        def one_argument(float:y) -> int:
        end
        """
        to_input = ""
        expected = ""
        stdout, st = capture_intermediate_exec(src, to_input)
        self.assertEquals(expected, stdout)



    def test_def_one_arg_3(self):
        from helpers import capture_intermediate_exec
        src = """
        def one_argument(bool:B) -> int:
        end
        """
        to_input = ""
        expected = ""
        stdout, st = capture_intermediate_exec(src, to_input)
        self.assertEquals(expected, stdout)


    def test_def_one_arg_4(self):
        from helpers import capture_intermediate_exec
        src = """
        def one_argument(char:c) -> int:
        end
        """
        to_input = ""
        expected = ""
        stdout, st = capture_intermediate_exec(src, to_input)
        self.assertEquals(expected, stdout)


    def test_def_one_arg_5(self):
        from helpers import capture_intermediate_exec
        src = """
        def one_argument(int[]:x) -> int:
        end
        """
        to_input = ""
        expected = ""
        stdout, st = capture_intermediate_exec(src, to_input)
        self.assertEquals(expected, stdout)


    def test_def_one_arg_6(self):
        from helpers import capture_intermediate_exec
        src = """
        def one_argument(float[]:y) -> int:
        end
        """
        to_input = ""
        expected = ""
        stdout, st = capture_intermediate_exec(src, to_input)
        self.assertEquals(expected, stdout)



    def test_def_one_arg_7(self):
        from helpers import capture_intermediate_exec
        src = """
        def one_argument(bool[]:B) -> int:
        end
        """
        to_input = ""
        expected = ""
        stdout, st = capture_intermediate_exec(src, to_input)
        self.assertEquals(expected, stdout)


    def test_def_one_arg_4(self):
        from helpers import capture_intermediate_exec
        src = """
        def one_argument(char[]:c) -> int:
        end
        """
        to_input = ""
        expected = ""
        stdout, st = capture_intermediate_exec(src, to_input)
        self.assertEquals(expected, stdout)


    def test_call_not_defined(self):
        from helpers import capture_intermediate_exec
        src = """
        foo()
        """
        to_input = ""
        expected = ""
        with self.assertRaises(Exception):
            stdout, st = capture_intermediate_exec(src, to_input)


    def test_return_int(self):
        from helpers import capture_intermediate_exec
        src = """
        def return_one() -> int:
            return 1
        end
        print { return_one() }
        """
        to_input = ""
        expected = "1"
        stdout, st = capture_intermediate_exec(src, to_input)
        self.assertEquals(expected, stdout)


    
    def test_return_float(self):
        from helpers import capture_intermediate_exec
        src = """
        def return_one() -> float:
            return 1.0
        end
        print { return_one() }
        """
        to_input = ""
        expected = "1.0"
        stdout, st = capture_intermediate_exec(src, to_input)
        self.assertEquals(float(expected), float(stdout))


    def test_return_char(self):
        from helpers import capture_intermediate_exec
        src = """
        def return_one() -> char:
            return 'y'
        end
        print { return_one() }
        """
        to_input = ""
        expected = "y"
        stdout, st = capture_intermediate_exec(src, to_input)
        self.assertEquals(expected, stdout)


    def test_return_bool(self):
        from helpers import capture_intermediate_exec
        src = """
        def return_one() -> bool:
            return False
        end
        print { return_one() }
        """
        to_input = ""
        expected = "0"
        stdout, st = capture_intermediate_exec(src, to_input)
        self.assertEquals(int(expected), int(stdout))


    def test_return_arr_char(self):
        from helpers import capture_intermediate_exec
        src = """
        def return_one() -> char[]:
            return "It's almost break!"
        end
        print { return_one() }
        """
        to_input = ""
        expected = "It's almost break!"
        stdout, st = capture_intermediate_exec(src, to_input)
        self.assertEquals(expected, stdout)


    def test_return_arr_copy(self):
        from helpers import capture_intermediate_exec
        src = """
        def return_one() -> char[]:
            char[] foo = "Hello world"
            return foo.copy
        end
        print { return_one() }
        """
        to_input = ""
        expected = "Hello world"
        stdout, st = capture_intermediate_exec(src, to_input)
        self.assertEquals(expected, stdout)


    def test_return_arr_int(self):
        from helpers import capture_intermediate_exec
        src = """
        def return_one() -> int[]:
            int[] bar = {11, 22, 33}
            return bar
        end
        print { return_one() }
        """
        to_input = ""
        expected = "112233"
        stdout, st = capture_intermediate_exec(src, to_input)
        self.assertEquals(expected, stdout)


    def test_return_arr_float(self):
        from helpers import capture_intermediate_exec
        src = """
        def return_one() -> float[]:
            float[] bar = {3.14}
            return bar
        end
        print { return_one() }
        """
        to_input = ""
        expected = "3.14"
        stdout, st = capture_intermediate_exec(src, to_input)
        self.assertAlmostEquals(float(expected), float(stdout))


    def test_return_arr_bool(self):
        from helpers import capture_intermediate_exec
        src = """
        def return_one() -> bool[]:
            bool[] bar = {False}
            return bar
        end
        print { return_one() }
        """
        to_input = ""
        expected = "0"
        stdout, st = capture_intermediate_exec(src, to_input)
        self.assertAlmostEquals(int(expected), int(stdout))


    def test_return_assign_0(self):
        from helpers import capture_intermediate_exec
        src = """
        def return_one() -> char[]:
            return "Let it snow!  Or not."
        end
        char[] winter = return_one()
        print { winter }
        """
        to_input = ""
        expected = "Let it snow!  Or not."
        stdout, st = capture_intermediate_exec(src, to_input)
        self.assertEquals(expected, stdout)


    def test_return_assign_1(self):
        from helpers import capture_intermediate_exec
        src = """
        def return_one() -> int:
            int foo = 10 + 20 + 30 + 40
            return foo
        end
        int century = return_one()
        print { century }
        """
        to_input = ""
        expected = "100"
        stdout, st = capture_intermediate_exec(src, to_input)
        self.assertEquals(expected, stdout)


    def test_return_assign_2(self):
        from helpers import capture_intermediate_exec
        src = """
        def return_one() -> int:
            int foo = 1 + 1 + 2 + 3 + 5
            return foo
        end
        int fib = return_one() + 8 
        print { fib }
        """
        to_input = ""
        expected = "20"
        stdout, st = capture_intermediate_exec(src, to_input)
        self.assertEquals(expected, stdout)


    def test_return_assign_3(self):
        from helpers import capture_intermediate_exec
        src = """
        def return_one() -> int:
            int foo = 22
            return foo
        end
        int[] arr = {11, return_one(), 33, 44}
        print { arr[1] }
        """
        to_input = ""
        expected = "22"
        stdout, st = capture_intermediate_exec(src, to_input)
        self.assertEquals(expected, stdout)


    def test_return_assign_4(self):
        from helpers import capture_intermediate_exec
        src = """
        def return_one() -> int:
            int foo = 10
            return foo
        end
        int[] arr = return_one():2:21
        print { arr[0] }
        """
        to_input = ""
        expected = "10"
        stdout, st = capture_intermediate_exec(src, to_input)
        self.assertEquals(expected, stdout)


    def test_arg_return_0(self):
        from helpers import capture_intermediate_exec
        src = """
        def my_func(int:x) -> int:
            return 2 * x
        end
        print { my_func(10) }
        """
        to_input = ""
        expected = "20"
        stdout, st = capture_intermediate_exec(src, to_input)
        self.assertEquals(expected, stdout)


    def test_arg_return_1(self):
        from helpers import capture_intermediate_exec
        src = """
        def my_func(float:y) -> float:
            return y / 3.0
        end
        print { my_func(33.0) }
        """
        to_input = ""
        expected = "11.0"
        stdout, st = capture_intermediate_exec(src, to_input)
        self.assertAlmostEquals(float(expected), float(stdout))


    def test_arg_return_2(self):
        from helpers import capture_intermediate_exec
        src = """
        def wrapper(bool[]:truths) -> bool:
            return any_of truths
        end
        bool[] values = {True, False, False, True}
        print { wrapper(values) }
        """
        to_input = ""
        stdout, st = capture_intermediate_exec(src, to_input)
        self.assertNotEquals(0, int(stdout))


    def test_two_args_0(self):
        from helpers import capture_intermediate_exec
        src = """
        def add(int:x, int:y) -> int:
            return x+y
        end
        print { add(2,7) }
        """
        to_input = ""
        expected = "9"
        stdout, st = capture_intermediate_exec(src, to_input)
        self.assertEquals(expected, stdout)


    def test_two_args_1(self):
        from helpers import capture_intermediate_exec
        src = """
        def substitute(char[]:x, int:y) -> char[]:
            x[y] = 'b'
            return x
        end
        char[] foo = "more"
        print { substitute(foo, 0) }
        """
        to_input = ""
        expected = "bore"
        stdout, st = capture_intermediate_exec(src, to_input)
        self.assertEquals(expected, stdout)


    def test_two_args_2(self):
        from helpers import capture_intermediate_exec
        src = """
        def combine(int[]:one, int[]:two) -> int[]:
            int[one.length] retval
            for x in 0:one.length do
                retval[x] = one[x] + two[x]
            end
            return retval
        end
        int[] a = {0,   1,  2,  3}
        int[] b = {10, 20, 30, 40}
        print { combine(a,b) }
        """
        to_input = ""
        expected = "10213243"
        stdout, st = capture_intermediate_exec(src, to_input)
        self.assertEquals(expected, stdout)


    def test_three_args_0(self):
        from helpers import capture_intermediate_exec
        src = """
        def thrice(int:lesser, int:greater, bool:is_true) -> bool:
            if (lesser < greater) and (is_true) then
                return True
            else
                return False
            end
        end
        print { thrice(20,10,True) }
        """
        to_input = ""
        expected = "0"
        stdout, st = capture_intermediate_exec(src, to_input)
        self.assertEquals(int(expected), int(stdout))


    def test_more_args_0(self):
        from helpers import capture_intermediate_exec
        src = """
        def many(int:x, int:y, int:z, int:mult, int:div) -> int:
            return (x+y+z)*mult/div
        end
        print { many(7,2,3,10,5) }
        """
        to_input = ""
        expected = "24"
        stdout, st = capture_intermediate_exec(src, to_input)
        self.assertEquals(int(expected), int(stdout))


    def test_scope_0(self):
        from helpers import capture_intermediate_exec
        src = """
        int x = 99
        def ex(int:x) -> int:
            return x
        end
        println { ex(12) }
        println { x }
        """
        to_input = ""
        expected = "12\n99\n"
        stdout, st = capture_intermediate_exec(src, to_input)
        self.assertEquals(expected, stdout)


    def test_scope_1(self):
        from helpers import capture_intermediate_exec
        src = """
        int x = 99
        def ex(int:x) -> int:
            for x in 0:x do
                println {x}
            end
            return x
        end
        println { ex(3) }
        println { x }
        """
        to_input = ""
        expected = "0\n1\n2\n3\n99\n"
        stdout, st = capture_intermediate_exec(src, to_input)
        self.assertEquals(expected, stdout)



    def test_recursive_0(self):
        from helpers import capture_intermediate_exec
        src = """
        def fib(int:n) -> int:
            if n <= 2 then
                return 1
            end
            return fib(n-1) + fib(n-2)
        end
        println { fib(4) }
        """
        to_input = ""
        expected = "3\n"
        stdout, st = capture_intermediate_exec(src, to_input)
        self.assertEquals(expected, stdout)


    def test_recursive_1(self):
        from helpers import capture_intermediate_exec
        src = """
        def num_places(int:value) -> int:
            if value < 10 then
                return 1
            else
                return 1 + num_places(value/10)
            end
        end
        println { num_places(4213) }
        """
        to_input = ""
        expected = "4\n"
        stdout, st = capture_intermediate_exec(src, to_input)
        self.assertEquals(expected, stdout)


    def test_recursive_2(self):
        from helpers import capture_intermediate_exec
        src = """
        def pow(int:base, int:exp) -> int:
            if exp == 0 then
                return 1
            else
                if exp == 1 then
                    return base
                end
            end
            int half_exp = pow(base, exp/2)
            if exp % 2 == 1 then
                return half_exp * half_exp * base
            else
                return half_exp * half_exp
            end
        end
        println { pow(2, 9) }
        """
        to_input = ""
        expected = "512\n"
        stdout, st = capture_intermediate_exec(src, to_input)
        self.assertEquals(expected, stdout)



    def test_recursive_3(self):
        from helpers import capture_intermediate_exec
        src = """
        def find(int[]:arr, int:value, int:start, int:the_end) -> bool:     
            if (start > the_end) then
                return False
            else
                int mid = start + (the_end + 1 - start) / 2
                if arr[mid] == value then
                    return True
                end
                if arr[mid] > value then
                     return find(arr, value, start, mid-1)
                else
                    return find(arr, value, mid+1, the_end)
                end
            end
        end
        int[] arr = {10, 20, 30, 40, 50, 60, 70, 80}
        println {find(arr, 60, 0, arr.length-1)}
        println {find(arr, 42, 0, arr.length-1)}
        """
        to_input = ""
        stdout, st = capture_intermediate_exec(src, to_input)
        values = stdout.split('\n')
        self.assertNotEquals(0, int(values[0]))
        self.assertEquals(0, int(values[1]))

if __name__ == '__main__':
    # t = FunctionTest()
    # t.test_recursive_0()
    unittest.main()
