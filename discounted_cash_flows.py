"""
Discounted Cash Flow (DCF) Explained With Formula and Examples
What Is Discounted Cash Flow (DCF)?
Discounted cash flow (DCF) refers to a valuation method that estimates the value of an investment using its expected future cash flows.
DCF analysis attempts to determine the value of an investment today, based on projections of how much money that investment will generate in the future.
It can help those considering whether to acquire a company or buy securities. Discounted cash flow analysis can also assist business owners and managers 
in making capital budgeting or operating expenditures decisions.
"""
# Import necessary libraries
import numpy as np

def discounted_cash_flow(cash_flows: list[float], discount_rate: float) -> float:
    """
    Calculate the present value of a series of cash flows given a discount rate.

    :param cash_flows: List of cash flows (float or int)
    :param discount_rate: Discount rate (float)
    :return: Present value (float)
    """
    cash_flows = np.array(cash_flows)
    periods = np.arange(1, len(cash_flows) + 1)
    present_value = np.sum(cash_flows / (1 + discount_rate) ** periods)
    return present_value

def project_future_cash_flows(initial_cash_flows: list[float], growth_rate: float, periods: int) -> list[float]:
    """
    Project future cash flows based on initial cash flows and growth rate.

    :param initial_cash_flows: List of initial cash flows (float or int)
    :param growth_rate: Annual growth rate (float)
    :param periods: Number of periods to project (int)
    :return: List of projected cash flows (float)
    """
    projected_cash_flows = initial_cash_flows[:]
    last_cash_flow = initial_cash_flows[-1]
    for _ in range(periods):
        next_cash_flow = last_cash_flow * (1 + growth_rate)
        projected_cash_flows.append(next_cash_flow)
        last_cash_flow = next_cash_flow
    return projected_cash_flows

def get_user_inputs() -> tuple[dict[str, tuple[list[float], float, int]], float]:
    """
    Get investment portfolio and discount rate from user input.

    :return: Tuple containing the portfolio dictionary and discount rate
    """
    portfolio = {}
    while True:
        try:
            investments = int(input("Enter the number of investments in your portfolio: "))
            if investments <= 0:
                raise ValueError
            break
        except ValueError:
            print("Please enter a valid number of investments.")

    for i in range(investments):
        investment_name = input(f"\nEnter the name of investment {i + 1}: ")
        
        while True:
            try:
                cash_flows = input(f"Enter the initial cash flows for {investment_name} separated by commas: ")
                cash_flows = list(map(float, cash_flows.split(',')))
                break
            except ValueError:
                print("Please enter valid cash flows separated by commas.")

        while True:
            try:
                growth_rate = float(input(f"Enter the annual growth rate for {investment_name} (as a decimal): "))
                break
            except ValueError:
                print("Please enter a valid growth rate.")

        while True:
            try:
                periods = int(input(f"Enter the number of periods to project for {investment_name}: "))
                if periods < 0:
                    raise ValueError
                break
            except ValueError:
                print("Please enter a valid number of periods.")

        portfolio[investment_name] = (cash_flows, growth_rate, periods)

    while True:
        try:
            discount_rate = float(input("\nEnter the discount rate (as a decimal): "))
            break
        except ValueError:
            print("Please enter a valid discount rate.")

    return portfolio, discount_rate

def main():
    # Get inputs from the user
    portfolio, discount_rate = get_user_inputs()

    # Calculate the present value for each investment in the portfolio
    portfolio_values = {}
    total_value = 0

    for investment, (cash_flows, growth_rate, periods) in portfolio.items():
        projected_cash_flows = project_future_cash_flows(cash_flows, growth_rate, periods)
        pv = discounted_cash_flow(projected_cash_flows, discount_rate)
        portfolio_values[investment] = pv
        total_value += pv

    # Output the results
    print("\nPresent Value of Investments:")
    for investment, pv in portfolio_values.items():
        print(f"{investment}: ${pv:.2f}")

    print(f"\nTotal Portfolio Value: ${total_value:.2f}")

if __name__ == "__main__":
    main()
