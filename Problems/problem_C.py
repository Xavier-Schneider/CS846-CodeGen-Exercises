# ============================================================
# Problem C: INI Config Validator + Normalizer
# ============================================================
#
# You are given a string containing an INI-like configuration.
# Your task is to:
#
#   1) Validate the configuration text using the rules below
#   2) Parse it into an internal mapping
#   3) Return a canonical, normalized INI string
#
# ------------------------------------------------------------
# Input
# ------------------------------------------------------------
# A single string `text` containing zero or more lines.
#
# The configuration format is a restricted INI subset:
#
# 1) Blank lines are allowed anywhere.
#
# 2) Comments:
#    - A comment begins with ';' or '#'
#    - Comments can appear on their own line OR after content.
#    - Everything from the first ';' or '#' onward is ignored.
#    - This simplified format does NOT support quoted values:
#      ';' and '#' ALWAYS start a comment if they appear.
#
# 3) Section headers:
#    - Format: [section_name]
#    - section_name must match:
#        ^[A-Za-z_][A-Za-z0-9_]*$
#    - Example: [db], [App_Config], [_x1]
#
# 4) Key-value lines:
#    - Format: key=value
#    - Spaces around '=' are allowed:
#        key = value
#        key=value
#    - key must match (lowercase only):
#        ^[a-z_][a-z0-9_]*$
#    - value is the remainder after '=', trimmed of whitespace.
#    - Empty value is allowed: key=
#
# 5) Keys must appear inside a section:
#    - A key-value line before the first section is invalid.
#
# ------------------------------------------------------------
# Validation constraints (must raise error if violated)
# ------------------------------------------------------------
# - Duplicate section names are invalid.
# - Duplicate keys within the same section are invalid.
# - Any non-empty, non-comment line must be either:
#     a) a valid section header, or
#     b) a valid key=value line
#
# ------------------------------------------------------------
# Normalization rules (canonical output)
# ------------------------------------------------------------
# Return a normalized INI string that:
#
# - Sorts sections lexicographically by section name
# - Sorts keys lexicographically within each section
# - Uses exact formatting:
#
#     [section]
#     key=value
#     key2=value2
#
# - Inserts exactly ONE blank line between sections
# - Has NO trailing spaces on any line
# - Ends with a trailing newline '\n'
#
# ------------------------------------------------------------
# Error handling requirements
# ------------------------------------------------------------
# If invalid data is encountered, raise ValueError with a clear,
# descriptive message. The tests check that the message contains:
#
# - An error code substring (one of the codes below)
# - The 1-based line number substring like "line 3"
#
# Use these error codes (exact substring match required):
#
#   - KEY_OUTSIDE_SECTION
#   - INVALID_SECTION
#   - DUPLICATE_SECTION
#   - INVALID_KEY
#   - DUPLICATE_KEY
#   - INVALID_LINE
#
# ------------------------------------------------------------
# Example
# ------------------------------------------------------------
# Input:
#
#   # comment
#   [db]
#   port = 5432
#   host=localhost  ; trailing
#
#   [app]
#   debug = true
#
# Normalized output:
#
#   [app]
#   debug=true
#
#   [db]
#   host=localhost
#   port=5432
#
# (plus a final trailing newline)
#
# ============================================================

def problem_C(text: str) -> str:
    """
    Validate, parse, and normalize a restricted INI configuration.

    Args:
        text: raw INI-like configuration string

    Returns:
        Canonical normalized INI string.

    Raises:
        ValueError: if the input is invalid (see spec for required
                    error code substrings and line numbers).
    """
    # TODO: implement
    raise NotImplementedError
