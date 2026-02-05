# test/test_problem_C.py
import unittest

from Problems.problem_C import problem_C


class TestProblemCValid(unittest.TestCase):
    def test_basic_normalization_single_section(self):
        text = """
        [db]
        host = localhost
        port=5432
        """
        out = problem_C(text)
        self.assertEqual(out, "[db]\nhost=localhost\nport=5432\n")

    def test_comments_and_blank_lines(self):
        text = """
        ; full line comment
        [db]

        host = localhost   # trailing comment
        port=5432 ; trailing comment
        """
        out = problem_C(text)
        self.assertEqual(out, "[db]\nhost=localhost\nport=5432\n")

    def test_sort_sections_and_keys(self):
        text = """
        [z]
        b=2
        a=1
        [a]
        k=v
        """
        out = problem_C(text)
        expected = (
            "[a]\n"
            "k=v\n"
            "\n"
            "[z]\n"
            "a=1\n"
            "b=2\n"
        )
        self.assertEqual(out, expected)

    def test_empty_value_allowed(self):
        text = """
        [s]
        key=
        """
        out = problem_C(text)
        self.assertEqual(out, "[s]\nkey=\n")

    def test_end_to_end_example(self):
        text = """
        # comment
        [db]
        port = 5432
        host=localhost  ; trailing

        [app]
        debug = true
        """
        out = problem_C(text)
        expected = (
            "[app]\n"
            "debug=true\n"
            "\n"
            "[db]\n"
            "host=localhost\n"
            "port=5432\n"
        )
        self.assertEqual(out, expected)


class TestProblemCInvalid(unittest.TestCase):
    def assertError(self, text: str, code: str, line: int):
        with self.assertRaises(ValueError) as cm:
            problem_C(text)
        msg = str(cm.exception)
        self.assertIn(code, msg)
        self.assertIn(f"line {line}", msg)

    def test_key_outside_section(self):
        self.assertError("x=1\n[a]\ny=2\n", "KEY_OUTSIDE_SECTION", 1)

    def test_invalid_section_name(self):
        self.assertError("[bad-name]\nx=1\n", "INVALID_SECTION", 1)

    def test_duplicate_section(self):
        self.assertError("[a]\nx=1\n[a]\ny=2\n", "DUPLICATE_SECTION", 3)

    def test_invalid_key_name_uppercase(self):
        self.assertError("[a]\nHost=localhost\n", "INVALID_KEY", 2)

    def test_duplicate_key_same_section(self):
        self.assertError("[a]\nx=1\nx=2\n", "DUPLICATE_KEY", 3)

    def test_invalid_line_gibberish(self):
        self.assertError("[a]\nthis is not valid\n", "INVALID_LINE", 2)

    def test_missing_equals(self):
        self.assertError("[a]\nkey\n", "INVALID_LINE", 2)


if __name__ == "__main__":
    unittest.main()
