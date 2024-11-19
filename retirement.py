#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Kongphop Kayoonvichien"
__copyright__ = "Copyright 2024, Mahidol University International College"
__credits__ = ["https://newbedev.com/what-is-the-common-header-format-of-python-files", "teammate A", "add more if needed"]
__email__ = "kongphop.kay@student.mahidol.edu"


def retirement_saving():
    """
    Calculate retirement savings needs based on user inputs.
    Takes into account inflation, current savings, and future value calculations.
    Provides step-by-step calculations for retirement planning.
    """
    desired_income = float(input("Enter your desired first-year retirement income in today's currency value: "))
    pension = float(input("Enter the total annual estimated defined benefit pension income plus Social Security in today's currency value: "))
    income_gap = desired_income - pension
    print(f"==> Your retirement income gap before inflation: {income_gap:.0f}")

    inflation_factor = float(input("Enter the inflation factor: "))
    inflated_gap = income_gap * inflation_factor
    print(f"==> Your retirement income gap after inflation: {inflated_gap:.0f}")

    payment_factor = float(input("Enter the payment factor: "))
    funds_needed = inflated_gap * payment_factor
    print(f"==> Funds needed at retirement to close the income gap: {funds_needed:.0f}")

    current_savings = float(input("Enter the savings available now: "))
    compound_factor = float(input("Enter the compounding factor: "))
    future_savings = current_savings * compound_factor
    print(f"==> Future value of available savings: {future_savings:.0f}")

    additional_savings = funds_needed - future_savings
    print(f"==> Additional savings needed at retirement: {additional_savings:.0f}")
    
    savings_factor = float(input("Enter the savings factor: "))
    annual_savings_needed = additional_savings * savings_factor
    print(f"==> Annual savings needed now to reach future retirement income goal: {annual_savings_needed:.0f}")

    current_annual_savings = float(input("Enter the current savings: "))
    additional_annual_savings = annual_savings_needed - current_annual_savings
    print(f"==> Annual additional savings needed now: {additional_annual_savings:.0f}")


if __name__ == "__main__":
    retirement_saving()