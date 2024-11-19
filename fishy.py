#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Kongphop Kayoonvichien"
__copyright__ = "Copyright 2024, Mahidol University International College"
__credits__ = ["https://newbedev.com/what-is-the-common-header-format-of-python-files", "teammate A", "add more if needed"]
__email__ = "kongphop.kay@student.mahidol.edu"

def calculate_price(fresh_cost: float, weight_lost: float, profit_rate: float) -> int:
    """
    Calculate the selling price of dried fish per kilogram to cover cost and target profit
    :param fresh_cost: Price of fresh fish per kilogram
    :param weight_lost: Percentage of weight lost after the drying process is complete
    :param profit_rate: Target profit percentage based on fresh fish cost
    :return: The selling price per kilogram of the dried fish, rounded to the nearest integer
    """
    effective_weight = 1 - weight_lost 
    cost_per_dried_kg = fresh_cost / effective_weight
    profit_amount = fresh_cost * profit_rate
    selling_price = cost_per_dried_kg + profit_amount
    return round(selling_price)


# Test
assert calculate_price(100, 0.5, 0.5) == 300
assert calculate_price(100, 0.7, 0.5) == 500
