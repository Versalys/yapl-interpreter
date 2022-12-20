import unittest


class TestArrays(unittest.TestCase):


    def test_empty(self):
        from helpers import capture_intermediate_exec
        src = """
        """
        to_input = ""
        expected = ""
        stdout, st = capture_intermediate_exec(src, to_input)
        self.assertEquals(expected, stdout)



    def test_declare_arr_int(self):
        from helpers import capture_intermediate_exec
        src = """
        int[] foo
        """
        to_input = ""
        expected = ""
        stdout, st = capture_intermediate_exec(src, to_input)
        self.assertEquals(expected, stdout)


        
    def test_declare_arr_float(self):
        from helpers import capture_intermediate_exec
        src = """
        float[] bar
        """
        to_input = ""
        expected = ""
        stdout, st = capture_intermediate_exec(src, to_input)
        self.assertEquals(expected, stdout)



    def test_declare_arr_char(self):
        from helpers import capture_intermediate_exec
        src = """
        char[] baz
        """
        to_input = ""
        expected = ""
        stdout, st = capture_intermediate_exec(src, to_input)
        self.assertEquals(expected, stdout)



    def test_declare_arr_bool(self):
        from helpers import capture_intermediate_exec
        src = """
        bool[] blarg
        """
        to_input = ""
        expected = ""
        stdout, st = capture_intermediate_exec(src, to_input)
        self.assertEquals(expected, stdout)



    def test_declare_arr_int_sized(self):
        from helpers import capture_intermediate_exec
        src = """
        int[10] foo
        """
        to_input = ""
        expected = ""
        stdout, st = capture_intermediate_exec(src, to_input)
        self.assertEquals(expected, stdout)



    def test_declare_arr_float_sized(self):
        from helpers import capture_intermediate_exec
        src = """
        float[2+2] bar
        """
        to_input = ""
        expected = ""
        stdout, st = capture_intermediate_exec(src, to_input)
        self.assertEquals(expected, stdout)



    def test_declare_arr_char_sized(self):
        from helpers import capture_intermediate_exec
        src = """
        char[2-1] baz
        """
        to_input = ""
        expected = ""
        stdout, st = capture_intermediate_exec(src, to_input)
        self.assertEquals(expected, stdout)



    def test_declare_arr_bool_sized(self):
        from helpers import capture_intermediate_exec
        src = """
        bool[42/2] blarg
        """
        to_input = ""
        expected = ""
        stdout, st = capture_intermediate_exec(src, to_input)
        self.assertEquals(expected, stdout)



    def test_arr_size_0(self):
        from helpers import capture_intermediate_exec
        src = """
        int[3] foo
        print {foo.length}
        """
        to_input = ""
        expected = "3"
        stdout, st = capture_intermediate_exec(src, to_input)
        self.assertEquals(expected, stdout)


    def test_arr_size_1(self):
        from helpers import capture_intermediate_exec
        src = """
        bool[4] me_bools = {True, True, False, False, True}
        print {me_bools.length}
        """
        to_input = ""
        expected = "4"
        stdout, st = capture_intermediate_exec(src, to_input)
        self.assertEquals(expected, stdout)


    def test_arr_size_2(self):
        from helpers import capture_intermediate_exec
        src = """
        float[] me_floats = {2*3.14159, 42.0/2.0, 73.33}
        print {me_floats.length}
        """
        to_input = ""
        expected = "3"
        stdout, st = capture_intermediate_exec(src, to_input)
        self.assertEquals(expected, stdout)



    def test_arr_int_assign_0(self):
        from helpers import capture_intermediate_exec
        src = """
        int[] foo = {11, 22, 33}
        println {foo[1]}
        println {foo.length}
        """
        to_input = ""
        expected = "22\n3\n"
        stdout, st = capture_intermediate_exec(src, to_input)
        self.assertEquals(expected, stdout)



    def test_arr_char_assign_0(self):
        from helpers import capture_intermediate_exec
        src = """
        char[] foo = {'h','i','y','o'}
        println {foo[3]}
        println {foo.length}
        """
        to_input = ""
        expected = "o\n4\n"
        stdout, st = capture_intermediate_exec(src, to_input)
        self.assertEquals(expected, stdout)


    def test_arr_bool_assign_0(self):
        from helpers import capture_intermediate_exec
        src = """
        bool[] foo = {True and False}
        println {foo[0]}
        println {foo.length}
        """
        to_input = ""
        stdout, st = capture_intermediate_exec(src, to_input)
        result = stdout.split()
        self.assertEquals(0, int(result[0]))
        self.assertEquals(1, int(result[1]))



    def test_arr_float_assign_0(self):
        from helpers import capture_intermediate_exec
        src = """
        float[] foo = {3.14, 2.16, 42.42, 127.3, 22.1}
        println {foo[4]}
        println {foo.length}
        """
        to_input = ""
        stdout, st = capture_intermediate_exec(src, to_input)
        result = stdout.split()
        self.assertAlmostEqual(22.1, float(result[0]))
        self.assertEquals(5, int(result[1]))


    def test_arr_set_ndx_0(self):
        from helpers import capture_intermediate_exec
        src = """
        int[] blarg = {10, 20, 30, 40, 50}
        blarg[0] = 99
        println {blarg[0]}
        """
        to_input = ""
        expected = "99\n"
        stdout, st = capture_intermediate_exec(src, to_input)
        self.assertEquals(expected, stdout)


    def test_arr_set_ndx_1(self):
        from helpers import capture_intermediate_exec
        src = """
        int[] blarg = {10, 20, 30, 40, 50}
        blarg[4] = 98
        println {blarg[4]}
        """
        to_input = ""
        expected = "98\n"
        stdout, st = capture_intermediate_exec(src, to_input)
        self.assertEquals(expected, stdout)


    def test_arr_set_ndx_2(self):
        from helpers import capture_intermediate_exec
        src = """
        int[] blarg = {10, 20, 30, 40, 50}
        blarg[2] = 97
        println {blarg[2]}
        """
        to_input = ""
        expected = "97\n"
        stdout, st = capture_intermediate_exec(src, to_input)
        self.assertEquals(expected, stdout)


    def test_arr_set_ndx_3(self):
        from helpers import capture_intermediate_exec
        src = """
        char[] howdy = "Hello"
        howdy[1] = 'a'
        println {howdy[1]}
        """
        to_input = ""
        expected = "a\n"
        stdout, st = capture_intermediate_exec(src, to_input)
        self.assertEquals(expected, stdout)


    def test_arr_set_ndx_4(self):
        from helpers import capture_intermediate_exec
        src = """
        int[] blarg = {10, 20, 30, 40, 50}
        blarg[2] = blarg[2] + 12
        println {blarg[2]}
        """
        to_input = ""
        expected = "42\n"
        stdout, st = capture_intermediate_exec(src, to_input)
        self.assertEquals(expected, stdout)


    def test_arr_set_ndx_5(self):
        from helpers import capture_intermediate_exec
        src = """
        int[] blarg = {10, 20, 30, 40, 50}
        blarg[2] = blarg[0] = blarg[3] = 11
        println {blarg[0], blarg[2], blarg[3]}
        """
        to_input = ""
        expected = "111111\n"
        stdout, st = capture_intermediate_exec(src, to_input)
        self.assertEquals(expected, stdout)


    def test_print_arr_0(self):
        from helpers import capture_intermediate_exec
        src = """
        int[] foo = {10, 30, 50}
        println {foo}
        """
        to_input = ""
        expected = '103050\n'
        stdout, st = capture_intermediate_exec(src, to_input)
        self.assertEquals(expected, stdout)


    def test_print_arr_1(self):
        from helpers import capture_intermediate_exec
        src = """
        int[1] foo = {10, 30, 50}
        println {foo}
        """
        to_input = ""
        expected = '10\n'
        stdout, st = capture_intermediate_exec(src, to_input)
        self.assertEquals(expected, stdout)



    def test_print_arr_2(self):
        from helpers import capture_intermediate_exec
        src = """
        char[] foo = {'h', 'e', 'l', 'l', 'o'}
        println {foo}
        """
        to_input = ""
        expected = 'hello\n'
        stdout, st = capture_intermediate_exec(src, to_input)
        self.assertEquals(expected, stdout)



    def test_print_arr_3(self):
        from helpers import capture_intermediate_exec
        src = """
        int[] foo = {10, 30, 50}
        char[] bar = {'c', 'a', 't'}
        println {foo, bar}
        """
        to_input = ""
        expected = '103050cat\n'
        stdout, st = capture_intermediate_exec(src, to_input)
        self.assertEquals(expected, stdout)



    def test_sum_of_0(self):
        from helpers import capture_intermediate_exec
        src = """
        int[] foo = {1, 2, 3, 4}
        print {sum_of foo}
        """
        to_input = ""
        expected = "10"
        stdout, st = capture_intermediate_exec(src, to_input)
        self.assertEquals(expected, stdout)   


    def test_sum_of_1(self):
        from helpers import capture_intermediate_exec
        src = """
        float[] foo = {11.1, 22.2, 33.3, 33.33}
        print {sum_of foo}
        """
        to_input = ""
        stdout, st = capture_intermediate_exec(src, to_input)
        self.assertAlmostEquals(99.9, float(stdout), places=1)   



    def test_product_of_0(self):
        from helpers import capture_intermediate_exec
        src = """
        int[] foo = {1, 2, 3, 4}
        print {product_of foo}
        """
        to_input = ""
        expected = "24"
        stdout, st = capture_intermediate_exec(src, to_input)
        self.assertEquals(expected, stdout)   


    def test_product_of_1(self):
        from helpers import capture_intermediate_exec
        src = """
        float[] foo = {11.0, 22.2, 33.0}
        print {product_of foo}
        """
        to_input = ""
        stdout, st = capture_intermediate_exec(src, to_input)
        self.assertAlmostEquals(8058.6, float(stdout), places=1)   



    def test_minimum_of_0(self):
        from helpers import capture_intermediate_exec
        src = """
        int[] elements = {10, -20, 30, 100, 0}
        print {minimum_of elements}
        """
        to_input = ""
        expected = "-20"
        stdout, st = capture_intermediate_exec(src, to_input)
        self.assertEquals(expected, stdout)


    def test_minimum_of(self):
        from helpers import capture_intermediate_exec
        src = """
        float[] elements = {72.3, 2.0, 2.0, 30.0, 40.0, 100.1}
        print {minimum_of elements}
        """
        to_input = ""
        stdout, st = capture_intermediate_exec(src, to_input)
        self.assertAlmostEquals(2.0, float(stdout))


    def test_maximum_of_0(self):
        from helpers import capture_intermediate_exec
        src = """
        int[] elements = {10, -20, 30, -2, 0, 63}
        print {maximum_of elements}
        """
        to_input = ""
        expected = "63"
        stdout, st = capture_intermediate_exec(src, to_input)
        self.assertEquals(expected, stdout)


    def test_maximum_of_1(self):
        from helpers import capture_intermediate_exec
        src = """
        float[] elements = {0.1, -22.0, 33.1, 23.1, -2.0}
        print {maximum_of elements}
        """
        to_input = ""
        stdout, st = capture_intermediate_exec(src, to_input)
        self.assertAlmostEquals(33.1, float(stdout))


    def test_any_of_0(self):
        from helpers import capture_intermediate_exec
        src = """
        bool[] elements = {True, False}
        print {any_of elements}
        """
        to_input = ""
        stdout, st = capture_intermediate_exec(src, to_input)
        self.assertNotEquals(0, int(stdout))


    def test_any_of_1(self):
        from helpers import capture_intermediate_exec
        src = """
        bool[] elements = {True, True, True}
        print {any_of elements}
        """
        to_input = ""
        stdout, st = capture_intermediate_exec(src, to_input)
        self.assertNotEquals(0, int(stdout))    


    def test_any_of_2(self):
        from helpers import capture_intermediate_exec
        src = """
        bool[] elements = {False, False, False}
        print {any_of elements}
        """
        to_input = ""
        stdout, st = capture_intermediate_exec(src, to_input)
        self.assertEquals(0, int(stdout)) 


    def test_any_of_3(self):
        from helpers import capture_intermediate_exec
        src = """
        bool[] elements = {True, True, True}
        print {any_of elements}
        """
        to_input = ""
        stdout, st = capture_intermediate_exec(src, to_input)
        self.assertNotEquals(0, int(stdout))          


    def test_every_of_0(self):
        from helpers import capture_intermediate_exec
        src = """
        bool[] elements = {True, False}
        print {every_of elements}
        """
        to_input = ""
        stdout, st = capture_intermediate_exec(src, to_input)
        self.assertEquals(0, int(stdout))


    def test_every_of_1(self):
        from helpers import capture_intermediate_exec
        src = """
        bool[] elements = {True, True, True, True, True}
        print {every_of elements}
        """
        to_input = ""
        stdout, st = capture_intermediate_exec(src, to_input)
        self.assertNotEquals(0, int(stdout))


    def test_every_of_2(self):
        from helpers import capture_intermediate_exec
        src = """
        bool[] elements = {False, False}
        print {every_of elements}
        """
        to_input = ""
        stdout, st = capture_intermediate_exec(src, to_input)
        self.assertEquals(0, int(stdout))


    def test_every_of_3(self):
        from helpers import capture_intermediate_exec
        src = """
        bool[] elements = {False, True}
        print {every_of elements}
        """
        to_input = ""
        stdout, st = capture_intermediate_exec(src, to_input)
        self.assertEquals(0, int(stdout))


    def test_arr_copy_0(self):
        from helpers import capture_intermediate_exec
        src = """
        int[] foo = {10, 20, 30}
        int[] bar = foo.copy
        foo[1] = 22
        println{foo[1]}
        println{bar[1]}
        """
        to_input = ""
        expected = '22\n20\n'
        stdout, st = capture_intermediate_exec(src, to_input)
        self.assertEquals(expected, stdout)


    def test_arr_copy_1(self):
        from helpers import capture_intermediate_exec
        src = """
        bool[] foo = {True, False, True}
        bool[] bar = foo.copy
        foo[1] = True
        println{foo[1]}
        println{bar[1]}
        """
        to_input = ""
        stdout, st = capture_intermediate_exec(src, to_input)
        stdout = stdout.split()
        self.assertNotEquals(0, int(stdout[0]))
        self.assertEquals(0, int(stdout[1]))



    def test_range_0(self):
        from helpers import capture_intermediate_exec
        src = """
        1:10
        """
        to_input = ""
        expected = ""
        stdout, st = capture_intermediate_exec(src, to_input)
        self.assertEquals(expected, stdout)


    def test_range_1(self):
        from helpers import capture_intermediate_exec
        src = """
        1:2:10
        """
        to_input = ""
        expected = ""
        stdout, st = capture_intermediate_exec(src, to_input)
        self.assertEquals(expected, stdout)


    def test_range_print_0(self):
        from helpers import capture_intermediate_exec
        src = """
        print {1:2:10}
        """
        to_input = ""
        expected = "13579"
        stdout, st = capture_intermediate_exec(src, to_input)
        self.assertEquals(expected, stdout)


    def test_range_print_1(self):
        from helpers import capture_intermediate_exec
        src = """
        print {-2:4}
        """
        to_input = ""
        expected = "-2-10123"
        stdout, st = capture_intermediate_exec(src, to_input)
        self.assertEquals(expected, stdout)


    def test_range_print_2(self):
        from helpers import capture_intermediate_exec
        src = """
        print {10+5:10+5+4}
        """
        to_input = ""
        expected = "15161718"
        stdout, st = capture_intermediate_exec(src, to_input)
        self.assertEquals(expected, stdout)


    def test_range_print_3(self):
        from helpers import capture_intermediate_exec
        src = """
        print {10-10:1+3:3*5}
        """
        to_input = ""
        expected = "04812"
        stdout, st = capture_intermediate_exec(src, to_input)
        self.assertEquals(expected, stdout)


    def test_range_assign_0(self):
        from helpers import capture_intermediate_exec
        src = """
        int[] foo = 1:2:12
        println {foo[2]}
        println {foo.length}
        """
        to_input = ""
        stdout, st = capture_intermediate_exec(src, to_input)
        result = stdout.split()
        self.assertEquals(5, int(result[0]))
        self.assertEquals(6, int(result[1]))


    def test_range_assign_1(self):
        from helpers import capture_intermediate_exec
        src = """
        int[] foo = 0:7
        println {foo[3]}
        println {foo.length}
        """
        to_input = ""
        stdout, st = capture_intermediate_exec(src, to_input)
        result = stdout.split()
        self.assertEquals(3, int(result[0]))
        self.assertEquals(7, int(result[1]))


    def test_range_assign_2(self):
        from helpers import capture_intermediate_exec
        src = """
        int[] foo = 10-10:4*2:100
        println {foo[3]}
        println {foo.length}
        """
        to_input = ""
        stdout, st = capture_intermediate_exec(src, to_input)
        result = stdout.split()
        self.assertEquals(24, int(result[0]))
        self.assertEquals(13, int(result[1]))


    def test_range_assign_3(self):
        from helpers import capture_intermediate_exec
        src = """
        int[] foo = -100:-100+10
        println {foo[9]}
        println {foo.length}
        """
        to_input = ""
        stdout, st = capture_intermediate_exec(src, to_input)
        result = stdout.split()
        # self.assertEquals(-91, int(result[0]))
        # self.assertEquals(10, int(result[1]))


    def test_for_ident_0(self):
        from helpers import capture_intermediate_exec
        src = """
        int[] foo = {10, 20, 30}
        for x in foo do
            println {x}
        end
        println {'K'}
        """
        to_input = ""
        stdout, st = capture_intermediate_exec(src, to_input)
        expected = '10\n20\n30\nK\n'
        self.assertEquals(expected, stdout)


    def test_for_ident_1(self):
        from helpers import capture_intermediate_exec
        src = """
        int[] foo = {10, 20, 30, 40}
        int result = 0
        for x in foo do
            result = result + x + 1
        end
        println {result}
        """
        to_input = ""
        stdout, st = capture_intermediate_exec(src, to_input)
        expected = '104\n'
        self.assertEquals(expected, stdout)


    def test_for_range_0(self):
        from helpers import capture_intermediate_exec
        src = """
        for x in 10:1:14 do
            println {x}
        end
        println {'K'}
        """
        to_input = ""
        stdout, st = capture_intermediate_exec(src, to_input)
        expected = '10\n11\n12\n13\nK\n'
        self.assertEquals(expected, stdout)


    def test_for_range_1(self):
        from helpers import capture_intermediate_exec
        src = """
        char[] howdy = {'p', 'e', 'o', 'p', 'l', 'e'}
        for x in 2:howdy.length-2 do
            print {howdy[x]}
        end
        print {'K'}
        """
        to_input = ""
        stdout, st = capture_intermediate_exec(src, to_input)
        expected = 'opK'
        self.assertEquals(expected, stdout)


    def test_for_scope_0(self):
        from helpers import capture_intermediate_exec
        src = """
        char[] x = "Scope!"
        for x in 0:10 do
            int y = x + 1
        end
        print {x}
        """
        to_input = ""
        stdout, st = capture_intermediate_exec(src, to_input)
        expected = 'Scope!'
        self.assertEquals(expected, stdout)


    def test_for_scope_1(self):
        from helpers import capture_intermediate_exec
        src = """
        char[] x = "Scope!"
        int num_chars = 0
        for x in x do
            num_chars = num_chars + 1
        end
        print {num_chars}
        """
        to_input = ""
        stdout, st = capture_intermediate_exec(src, to_input)
        expected = '6'
        self.assertEquals(expected, stdout)


    def test_for_break_1(self):
        from helpers import capture_intermediate_exec
        src = """
        for x in 0:10 do
            println {x}
            if x == 5 then
                break
            end
        end
        """
        to_input = ""
        stdout, st = capture_intermediate_exec(src, to_input)
        expected = '0\n1\n2\n3\n4\n5\n'
        self.assertEquals(expected, stdout)


    def test_print_escaped_0(self):
        from helpers import capture_intermediate_exec
        src = """
        print {"%n"}
        """
        to_input = ""
        expected = "\n"
        stdout, st = capture_intermediate_exec(src, to_input)
        self.assertEquals(expected, stdout)



    def test_print_escaped_1(self):
        from helpers import capture_intermediate_exec
        src = """
        print {"%t"}
        """
        to_input = ""
        expected = "\t"
        stdout, st = capture_intermediate_exec(src, to_input)
        self.assertEquals(expected, stdout)



    def test_print_escaped_2(self):
        from helpers import capture_intermediate_exec
        src = """
        print {"%%"}
        """
        to_input = ""
        expected = "%"
        stdout, st = capture_intermediate_exec(src, to_input)
        self.assertEquals(expected, stdout)



    def test_print_escaped_3(self):
        from helpers import capture_intermediate_exec
        src = """
        print {"%""}
        """
        to_input = ""
        expected = "\""
        stdout, st = capture_intermediate_exec(src, to_input)
        self.assertEquals(expected, stdout)



    def test_assign_escaped_0(self):
        from helpers import capture_intermediate_exec
        src = """
        char[] season = {'%t', '%'', 'a', 'u', 't', 'u', 'm', 'n', '%''}
        print {season}
        """
        to_input = ""
        expected = "\t'autumn'"
        stdout, st = capture_intermediate_exec(src, to_input)
        self.assertEquals(expected, stdout)


    def test_string_literal_0(self):
        from helpers import capture_intermediate_exec
        src = """
        "Hello world!"
        """
        to_input = ""
        expected = ""
        stdout, st = capture_intermediate_exec(src, to_input)
        self.assertEquals(expected, stdout)



    def test_string_literal_1(self):
        from helpers import capture_intermediate_exec
        src = """
        "Oh, look, %"more quotes%""
        """
        to_input = ""
        expected = ""
        stdout, st = capture_intermediate_exec(src, to_input)
        self.assertEquals(expected, stdout)



    def test_print_string_0(self):
        from helpers import capture_intermediate_exec
        src = """
        print {"Howdy!"}
        """
        to_input = ""
        expected = "Howdy!"
        stdout, st = capture_intermediate_exec(src, to_input)
        self.assertEquals(expected, stdout)



    def test_print_string_1(self):
        from helpers import capture_intermediate_exec
        src = """
        print {"%"Howdy!%""}
        """
        to_input = ""
        expected = "\"Howdy!\""
        stdout, st = capture_intermediate_exec(src, to_input)
        self.assertEquals(expected, stdout)



    def test_print_string_2(self):
        from helpers import capture_intermediate_exec
        src = """
        print {"Here is one line%nHere is another"}
        """
        to_input = ""
        expected = "Here is one line\nHere is another"
        stdout, st = capture_intermediate_exec(src, to_input)
        self.assertEquals(expected, stdout)


    def test_bubble_sort(self):
        from helpers import capture_intermediate_exec
        src = """
        int[] arr = {99, -42, 43, 12, 99, 3}
        for x in 0:arr.length do
            for y in x+1:arr.length do
                if arr[y] < arr[x] then
                    int tmp = arr[x]
                    arr[x] = arr[y]
                    arr[y] = tmp
                end
            end
        end
        for elem in arr do
            println {elem}
        end
        """
        to_input = ""
        expected = "-42\n3\n12\n43\n99\n99\n"
        stdout, st = capture_intermediate_exec(src, to_input)
        self.assertEquals(expected, stdout)



    def test_fibinocci(self):
        from helpers import capture_intermediate_exec
        src = """
        int term_0 = 1
        int term_1 = 1
        for ndx in 0:7 do
            if ndx < 2 then
                println {1}
            else
                int new_term = term_0 + term_1
                term_0 = term_1
                term_1 = new_term
                println {new_term}
            end
        end
        """
        to_input = ""
        expected = "1\n1\n2\n3\n5\n8\n13\n"
        stdout, st = capture_intermediate_exec(src, to_input)
        self.assertEquals(expected, stdout)


    def test_even_arr(self):
        from helpers import capture_intermediate_exec
        src = """
        int[10] numbers
        int next_ndx = 0
        for x in 0:numbers.length do
            int value = 10 * x + x
            if value % 2 == 0 then
                numbers[next_ndx] = value
                next_ndx = next_ndx + 1
            end
        end
        int[next_ndx] clipped
        while next_ndx - 1 >= 0 do
            next_ndx = next_ndx - 1
            clipped[next_ndx] = numbers[next_ndx]
        end
        print{clipped}
        """
        to_input = ""
        expected = "022446688"
        stdout, st = capture_intermediate_exec(src, to_input)
        self.assertEquals(expected, stdout)


    def test_reverse(self):
        from helpers import capture_intermediate_exec
        src = """
        char[] reversed = "!dlrow a tahW"
        char[reversed.length] corrected
        for ndx in 0:reversed.length do
            int fwd_ndx = reversed.length - ndx - 1
            corrected[fwd_ndx] = reversed[ndx]
        end
        print{corrected} 
        """
        to_input = ""
        expected = "What a world!"
        stdout, st = capture_intermediate_exec(src, to_input)
        self.assertEquals(expected, stdout)

    def test_custom(self):
        from helpers import capture_intermediate_exec
        src = """
        bool[] elements = {True, False}
        print {any_of elements}
        """
        to_input = ''
        stdout, st = capture_intermediate_exec(src, to_input)
        print(stdout)

    def test_custom_2(self):
        from helpers import capture_intermediate_exec
        src = """
        print {-100 + 10}
        """
        to_input = ''
        stdout, st = capture_intermediate_exec(src, to_input)
        print(stdout)

if __name__ == '__main__':
    unittest.main()
    # t = TestArrays()
    # t.test_minimum_of()
