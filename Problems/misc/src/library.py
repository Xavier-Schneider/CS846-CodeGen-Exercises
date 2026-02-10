# examstats.py
# Import this file with: from Problems.misc.src import library as examlib
# You must use this exact path

from __future__ import annotations

from typing import Any, Dict, Iterable, List, Mapping, Optional


class InvalidRecordError(ValueError):
    """Raised when an input record is missing fields or has invalid values."""


def _to_record_list(records: Iterable[Mapping[str, Any]]) -> List[Dict[str, Any]]:
    # Ensure we can iterate multiple times and give nicer errors for non-iterables.
    if records is None:
        raise InvalidRecordError("records cannot be None")
    try:
        return [dict(r) for r in records]
    except TypeError as e:
        raise InvalidRecordError("records must be an iterable of dict-like objects") from e


def validate_records(records: Iterable[Mapping[str, Any]]) -> List[Dict[str, Any]]:
    recs = _to_record_list(records)
    if len(recs) == 0:
        raise InvalidRecordError("record list cannot be empty")

    for i, r in enumerate(recs):
        # Required keys
        for k in ("name", "score", "weight"):
            if k not in r:
                raise InvalidRecordError(f"record {i} missing required field: {k}")

        # Name
        if not isinstance(r["name"], str) or not r["name"].strip():
            raise InvalidRecordError(f"record {i} name must be a non-empty string")

        # Score
        score = r["score"]
        if not isinstance(score, (int, float)):
            raise InvalidRecordError(f"record {i} score must be a number")
        if score != score:  # NaN check
            raise InvalidRecordError(f"record {i} score cannot be NaN")
        if score < 0 or score > 100:
            raise InvalidRecordError(f"record {i} score must be between 0 and 100")

        # Weight
        weight = r["weight"]
        if not isinstance(weight, (int, float)):
            raise InvalidRecordError(f"record {i} weight must be a number")
        if weight != weight:  # NaN check
            raise InvalidRecordError(f"record {i} weight cannot be NaN")
        if weight <= 0:
            raise InvalidRecordError(f"record {i} weight must be > 0")

    return recs


def weighted_average(records: Iterable[Mapping[str, Any]]) -> float:
    recs = validate_records(records)
    total_weight = sum(r["weight"] for r in recs)
    weighted_sum = sum(r["score"] * r["weight"] for r in recs)
    return round(weighted_sum / total_weight, 2)


def top_student(records: Iterable[Mapping[str, Any]]) -> str:
    recs = validate_records(records)
    top = max(recs, key=lambda r: r["score"])
    return top["name"]


def pass_rate(records: Iterable[Mapping[str, Any]], pass_mark: float = 50) -> float:
    if not isinstance(pass_mark, (int, float)) or pass_mark != pass_mark:
        raise InvalidRecordError("pass_mark must be a valid number")
    recs = validate_records(records)
    passed = sum(1 for r in recs if r["score"] >= pass_mark)
    return round((passed / len(recs)) * 100, 2)


def grade_distribution(
    records: Iterable[Mapping[str, Any]],
    *,
    boundaries: Optional[Mapping[str, float]] = None,
) -> Dict[str, int]:
    """
    Returns counts per grade.

    Default boundaries:
      A >= 70, B >= 60, C >= 50, F < 50

    You can override by passing boundaries like:
      {"A": 80, "B": 70, "C": 60}  # F is implicit
    """
    recs = validate_records(records)

    if boundaries is None:
        boundaries = {"A": 70, "B": 60, "C": 50}

    # Validate boundaries: must contain A,B,C at least, be numeric, and descending.
    needed = ("A", "B", "C")
    for g in needed:
        if g not in boundaries:
            raise InvalidRecordError(f"boundaries must include {g}")

    for g, v in boundaries.items():
        if not isinstance(v, (int, float)) or v != v:
            raise InvalidRecordError(f"boundary for {g} must be a valid number")

    a, b, c = float(boundaries["A"]), float(boundaries["B"]), float(boundaries["C"])
    if not (a > b > c):
        raise InvalidRecordError("boundaries must be strictly descending: A > B > C")

    dist = {"A": 0, "B": 0, "C": 0, "F": 0}
    for r in recs:
        s = r["score"]
        if s >= a:
            dist["A"] += 1
        elif s >= b:
            dist["B"] += 1
        elif s >= c:
            dist["C"] += 1
        else:
            dist["F"] += 1
    return dist
