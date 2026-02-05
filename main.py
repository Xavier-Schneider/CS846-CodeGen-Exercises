# test_problem_A_no_pytest.py

from problems.problem_A import problem_A
from typing import Any, Callable, Optional

def run_problem_A_tests() -> bool:
    failures = 0

    def section(title: str) -> None:
        print(f"\n[Problem_A] {title}")

    def ok(msg: str) -> None:
        print(f"  ✅ {msg}")

    def fail(msg: str) -> None:
        nonlocal failures
        failures += 1
        print(f"  ❌ {msg}")

    def assert_true(cond: bool, msg: str) -> None:
        if cond:
            ok(msg)
        else:
            fail(msg)

    def assert_equal(actual: Any, expected: Any, msg: str) -> None:
        if actual == expected:
            ok(msg)
        else:
            fail(f"{msg} | expected={expected!r}, got={actual!r}")

    def assert_in(sub: str, s: str, msg: str) -> None:
        if sub in s:
            ok(msg)
        else:
            fail(f"{msg} | expected substring {sub!r} in {s!r}")

    def safe_call(label: str, fn: Callable[[], Any]) -> Optional[Any]:
        """
        For calls that are expected to succeed.
        If an exception occurs, record a failure and return None.
        """
        try:
            return fn()
        except Exception as e:
            fail(f"{label} raised unexpectedly: {type(e).__name__}: {e}")
            return None

    def expect_raises_contains(label: str, fn: Callable[[], Any], expected_substring: str) -> None:
        """
        For calls that are expected to raise.
        If no exception is raised, record a failure.
        If raised, check that message contains expected_substring.
        """
        try:
            fn()
            fail(f"{label} | expected exception but none was raised")
        except Exception as e:
            assert_in(expected_substring, str(e), f"{label} error message check")

    def assert_summary_shape(out: Any, label: str) -> None:
        if out is None:
            fail(f"{label}: no output (call failed)")
            return

        assert_true(isinstance(out, dict), f"{label}: output is a dict")
        if not isinstance(out, dict):
            return

        expected_keys = {"count", "weighted_average", "top_student", "pass_rate", "grade_distribution"}
        assert_equal(set(out.keys()), expected_keys, f"{label}: top-level keys match")

        # Type checks (guarded)
        if "count" in out:
            assert_true(isinstance(out["count"], int), f'{label}: "count" is int')
        if "weighted_average" in out:
            assert_true(isinstance(out["weighted_average"], (int, float)), f'{label}: "weighted_average" is numeric')
        if "top_student" in out:
            assert_true(isinstance(out["top_student"], str), f'{label}: "top_student" is str')
        if "pass_rate" in out:
            assert_true(isinstance(out["pass_rate"], (int, float)), f'{label}: "pass_rate" is numeric')

        gd = out.get("grade_distribution")
        if gd is not None:
            assert_true(isinstance(gd, dict), f'{label}: "grade_distribution" is dict')
            if isinstance(gd, dict):
                assert_equal(set(gd.keys()), {"A", "B", "C", "F"}, f"{label}: grade_distribution keys match")
                for g in ("A", "B", "C", "F"):
                    if g in gd:
                        assert_true(
                            isinstance(gd[g], int) and gd[g] >= 0,
                            f'{label}: grade_distribution["{g}"] is non-negative int',
                        )

    # ============================================================
    # 1) Happy path
    # ============================================================
    section("Happy path")

    records = [
        {"name": "Alice", "score": 78, "weight": 1.0},
        {"name": "Bob", "score": 45, "weight": 0.5},
        {"name": "Charlie", "score": 88, "weight": 1.5},
        {"name": "Diana", "score": 60, "weight": 1.0},
        {"name": "Eve", "score": 52, "weight": 1.0},
    ]

    out = safe_call("Happy path call", lambda: problem_A(records))
    assert_summary_shape(out, "Happy path")

    if isinstance(out, dict):
        # Expected values
        total_weight = 1.0 + 0.5 + 1.5 + 1.0 + 1.0
        weighted_sum = 78 * 1.0 + 45 * 0.5 + 88 * 1.5 + 60 * 1.0 + 52 * 1.0
        expected_avg = round(weighted_sum / total_weight, 2)

        passed = sum(1 for r in records if r["score"] >= 50)
        expected_pass_rate = round((passed / len(records)) * 100, 2)

        assert_equal(out.get("count"), 5, "Happy path: count == 5")
        assert_equal(out.get("top_student"), "Charlie", "Happy path: top_student == Charlie")
        assert_equal(out.get("weighted_average"), expected_avg, "Happy path: weighted_average correct")
        assert_equal(out.get("pass_rate"), expected_pass_rate, "Happy path: pass_rate correct")
        assert_equal(
            out.get("grade_distribution"),
            {"A": 2, "B": 1, "C": 1, "F": 1},
            "Happy path: grade_distribution correct",
        )

    # ============================================================
    # 2) Rounding
    # ============================================================
    section("Rounding behavior")

    records = [
        {"name": "A", "score": 0, "weight": 1},
        {"name": "B", "score": 100, "weight": 2},
    ]

    out = safe_call("Rounding call", lambda: problem_A(records))
    assert_summary_shape(out, "Rounding")

    if isinstance(out, dict):
        assert_equal(out.get("weighted_average"), 66.67, "Rounding: weighted_average rounds to 2 decimals")
        assert_equal(out.get("pass_rate"), 50.0, "Rounding: pass_rate rounds to 2 decimals")

    # ============================================================
    # 3) Grade boundaries
    # ============================================================
    section("Grade boundaries")

    records = [
        {"name": "A", "score": 70, "weight": 1},
        {"name": "B", "score": 60, "weight": 1},
        {"name": "C", "score": 50, "weight": 1},
        {"name": "F", "score": 49.999, "weight": 1},
    ]

    out = safe_call("Boundaries call", lambda: problem_A(records))
    assert_summary_shape(out, "Boundaries")

    if isinstance(out, dict):
        assert_equal(
            out.get("grade_distribution"),
            {"A": 1, "B": 1, "C": 1, "F": 1},
            "Boundaries: exact cutoffs behave correctly",
        )

    # ============================================================
    # 4) Iterable support
    # ============================================================
    section("Iterable support")

    records = (
        {"name": "Alice", "score": 80, "weight": 1},
        {"name": "Bob", "score": 20, "weight": 1},
    )

    out = safe_call("Iterable call", lambda: problem_A(records))
    assert_summary_shape(out, "Iterable")

    if isinstance(out, dict):
        assert_equal(out.get("count"), 2, "Iterable: count == 2")
        assert_equal(out.get("top_student"), "Alice", "Iterable: top_student == Alice")

    # ============================================================
    # 5) Validation errors
    # ============================================================
    section("Validation errors (expected exceptions)")

    expect_raises_contains("records=None", lambda: problem_A(None), "records cannot be None")
    expect_raises_contains("empty records", lambda: problem_A([]), "record list cannot be empty")
    expect_raises_contains("non-iterable records", lambda: problem_A(123), "records must be an iterable")
    expect_raises_contains(
        "missing field (weight)",
        lambda: problem_A([{"name": "Alice", "score": 80}]),
        "missing required field",
    )
    expect_raises_contains(
        "invalid name",
        lambda: problem_A([{"name": "", "score": 80, "weight": 1}]),
        "name must be a non-empty string",
    )
    expect_raises_contains(
        "score out of range",
        lambda: problem_A([{"name": "Alice", "score": 101, "weight": 1}]),
        "score must be between 0 and 100",
    )
    expect_raises_contains(
        "weight not positive",
        lambda: problem_A([{"name": "Alice", "score": 80, "weight": 0}]),
        "weight must be > 0",
    )

    # ============================================================
    # Summary
    # ============================================================
    section("Summary")
    if failures == 0:
        print("✅ All Problem_A tests passed.")
        return True
    else:
        print(f"❌ {failures} Problem_A test(s) failed.")
        return False


if __name__ == "__main__":
    run_problem_A_tests()
