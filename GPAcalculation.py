#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Kongphop Kayoonvichien"
__copyright__ = "Copyright 2024, Mahidol University International College"
__credits__ = ["https://newbedev.com/what-is-the-common-header-format-of-python-files", "teammate A", "add more if needed"]
__email__ = "kongphop.kay@student.mahidol.edu"


def calculate_grades(currentGPA: float, targetGPA: float, credits_earned: int, credits_total: int) -> float:
    """
    Calculate GPA needed to improve the grade
    :param currentGPA: The current cumulative GPA so far
    :param targetGPA: CGPA one wishes to achieve upon graduation
    :param credits_earned: Total number of credits earned so far (excluding non-credit and failed courses)
    :param credits_total: Total number of credits needed to graduate in your major
    :return: GPA that should be made each term until graduation
    """
    remaining_credits = credits_total - credits_earned
    required_GPA = (targetGPA * credits_total - currentGPA * credits_earned) / remaining_credits
    return round(required_GPA, 2)


# Test
assert calculate_grades(2.5, 3, 100, 164) == 3.78
assert calculate_grades(1.5, 3, 100, 164) == 5.34