"""
Problem statement:
    Given two ranges, return if they overlap
Definitions:
    Ranges are defined as [x1, x2] - i.e. all the numbers that are x1 <= v <= x2
    Overlapping ranges are those where range1 ⊆ range2 or range1 ⊇ range2
"""


def are_ranges_overlapping(r1, r2):
    # Quick boundary check
    r1_start_le_r2 = r1[0] <= r2[0]
    r1_end_ge_r2 = r1[1] >= r2[1]
    r2_start_le_r1 = r2[0] <= r1[0]
    r2_end_ge_r1 = r2[1] >= r1[1]

    # If the boundaries of r1 are included in r2 or the reverse is true, return True
    if (r1_end_ge_r2 and r1_start_le_r2) or \
       (r2_start_le_r1 and r2_end_ge_r1):
        return True
    # Otherwise, we have non-overlapping ranges
    else:
        return False
