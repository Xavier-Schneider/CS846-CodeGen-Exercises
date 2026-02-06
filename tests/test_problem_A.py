import unittest

from Problems.problem_A import problem_A


class TestProblemAValid(unittest.TestCase):
    def assert_summary_shape(self, out):
        self.assertIsInstance(out, dict)
        expected_keys = {"count", "weighted_average", "top_student", "pass_rate", "grade_distribution"}
        self.assertEqual(set(out.keys()), expected_keys)

        self.assertIsInstance(out["count"], int)
        self.assertIsInstance(out["weighted_average"], (int, float))
        self.assertIsInstance(out["top_student"], str)
        self.assertIsInstance(out["pass_rate"], (int, float))

        grade_distribution = out["grade_distribution"]
        self.assertIsInstance(grade_distribution, dict)
        self.assertEqual(set(grade_distribution.keys()), {"A", "B", "C", "F"})
        for grade, count in grade_distribution.items():
            self.assertIsInstance(count, int)
            self.assertGreaterEqual(count, 0)

    def test_happy_path(self):
        records = [
            {"name": "Alice", "score": 78, "weight": 1.0},
            {"name": "Bob", "score": 45, "weight": 0.5},
            {"name": "Charlie", "score": 88, "weight": 1.5},
            {"name": "Diana", "score": 60, "weight": 1.0},
            {"name": "Eve", "score": 52, "weight": 1.0},
        ]

        out = problem_A(records)
        self.assert_summary_shape(out)

        total_weight = 1.0 + 0.5 + 1.5 + 1.0 + 1.0
        weighted_sum = 78 * 1.0 + 45 * 0.5 + 88 * 1.5 + 60 * 1.0 + 52 * 1.0
        expected_avg = round(weighted_sum / total_weight, 2)

        passed = sum(1 for r in records if r["score"] >= 50)
        expected_pass_rate = round((passed / len(records)) * 100, 2)

        self.assertEqual(out.get("count"), 5)
        self.assertEqual(out.get("top_student"), "Charlie")
        self.assertEqual(out.get("weighted_average"), expected_avg)
        self.assertEqual(out.get("pass_rate"), expected_pass_rate)
        self.assertEqual(out.get("grade_distribution"), {"A": 2, "B": 1, "C": 1, "F": 1})

    def test_rounding(self):
        records = [
            {"name": "A", "score": 0, "weight": 1},
            {"name": "B", "score": 100, "weight": 2},
        ]

        out = problem_A(records)
        self.assert_summary_shape(out)
        self.assertEqual(out.get("weighted_average"), 66.67)
        self.assertEqual(out.get("pass_rate"), 50.0)

    def test_grade_boundaries(self):
        records = [
            {"name": "A", "score": 70, "weight": 1},
            {"name": "B", "score": 60, "weight": 1},
            {"name": "C", "score": 50, "weight": 1},
            {"name": "F", "score": 49.999, "weight": 1},
        ]

        out = problem_A(records)
        self.assert_summary_shape(out)
        self.assertEqual(out.get("grade_distribution"), {"A": 1, "B": 1, "C": 1, "F": 1})

    def test_iterable_support(self):
        records = (
            {"name": "Alice", "score": 80, "weight": 1},
            {"name": "Bob", "score": 20, "weight": 1},
        )

        out = problem_A(records)
        self.assert_summary_shape(out)
        self.assertEqual(out.get("count"), 2)
        self.assertEqual(out.get("top_student"), "Alice")

    def test_top_student_tie(self):
        records = [
            {"name": "A", "score": 90, "weight": 1},
            {"name": "B", "score": 90, "weight": 1},
            {"name": "C", "score": 10, "weight": 1},
        ]

        out = problem_A(records)
        self.assert_summary_shape(out)
        self.assertIn(out.get("top_student"), {"A", "B"})


class TestProblemAInvalid(unittest.TestCase):
    def test_validation_errors(self):
        cases = [
            ("records=None", lambda: problem_A(None)),
            ("empty list records", lambda: problem_A([])),
            ("empty tuple records", lambda: problem_A(())),
            ("empty generator records", lambda: problem_A(iter([]))),
            ("non-iterable records", lambda: problem_A(123)),
            ("record not dict-like", lambda: problem_A(["not a dict"])),
            ("missing field (weight)", lambda: problem_A([{"name": "Alice", "score": 80}])),
            ("invalid name (empty)", lambda: problem_A([{"name": "", "score": 80, "weight": 1}])),
            ("score out of range high", lambda: problem_A([{"name": "Alice", "score": 101, "weight": 1}])),
            ("score out of range low", lambda: problem_A([{"name": "Alice", "score": -1, "weight": 1}])),
            ("score is NaN", lambda: problem_A([{"name": "Alice", "score": float("nan"), "weight": 1}])),
            ("weight not positive", lambda: problem_A([{"name": "Alice", "score": 80, "weight": 0}])),
            ("weight is NaN", lambda: problem_A([{"name": "Alice", "score": 80, "weight": float("nan")}])),
            ("records is a string", lambda: problem_A("abc")),
        ]

        for label, fn in cases:
            with self.subTest(label=label):
                with self.assertRaises(Exception):
                    fn()


if __name__ == "__main__":
    unittest.main()
