from lines import are_ranges_overlapping as overlap
from math import inf


def test_positives():
    test_cases = [[(0, 1), (0.5, 1)],
                  [(-1, 1), (-0.5, 1)],
                  [(0, 1), (0, 0.99999999999)],
                  [(-5, 0), (-4, -1)],
                  [(-3, -1), (-4, 0)],
                  [(-9999999, -999999), (-9999998, -9999997)]
                  ]
    for test_case in test_cases:
        assert overlap(test_case[0], test_case[1])


def test_negatives():
    test_cases = [[(0, 1), (0.5, 2)],
                  [(-1, 1), (-0.5, 2)],
                  [(-1, 1), (-2, 0.99999999999)],
                  [(-5, -3), (-4, -1)],
                  [(-3, 1), (-4, 0)],
                  [(-9999999, -999999), (-9999998, 0)]
                  ]
    for test_case in test_cases:
        assert not overlap(test_case[0], test_case[1])


def test_edge_cases():
    test_cases = [[(0, 0), (0, 0)],
                  [(1, 1), (1, 1)],
                  [(-1, -1), (-1, -1)],
                  [(-inf, inf), (0, 1)]
                  ]
    for test_case in test_cases:
        assert overlap(test_case[0], test_case[1])