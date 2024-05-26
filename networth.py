# Initial Parameters
initial_salary = 110000
fixed_expenses = 30000
savings_rate = 0.65
investment_increase_rate = 0.05  # 5% annual increase in investment amount
yearly_increment = 1.10 # Yearly salary hike 10%
additional_increment = 2.20 # Job switch or promotion every 3 year 20%
inflation_rate = 0.04  # 4% annual inflation rate
investment_horizon = 10

# Growth rates for investments
equity_growth = 0.12

# Investment allocation
emergency_fund_percentage = 0.18  # Only for the first year
equity_percentage = 0.50

# Lists to store values for each year
salaries = []
real_salaries = []
investments = []
investment_multiplier = 1.0

# Calculate investments over the years
salary = initial_salary
for year in range(investment_horizon):
    if year % 3 == 0 and year != 0:
        salary *= additional_increment
    salary *= yearly_increment
    
    # Adjust salary for inflation to get real salary
    real_salary = salary / ((1 + inflation_rate) ** year)
    
    disposable_income = salary - fixed_expenses
    real_disposable_income = real_salary - fixed_expenses  # Adjust for inflation
    
    savings = disposable_income * savings_rate * investment_multiplier

    if year == 0:
        emergency_fund = savings * emergency_fund_percentage
        remaining_savings = savings - emergency_fund
    else:
        emergency_fund = 0
        remaining_savings = savings

    equity_investment = remaining_savings * equity_percentage
    
    investments.append((emergency_fund, equity_investment))
    salaries.append(salary)
    real_salaries.append(real_salary)
    
    investment_multiplier *= (1 + investment_increase_rate)

# Initialize investment totals
total_equity = 0

# Apply growth rates to each year's investments
for i, inv in enumerate(investments):
    emergency_fund, equity_investment = inv
    total_equity = (total_equity + equity_investment) * (1 + equity_growth)

# Calculate total net worth in current money terms
total_net_worth =  total_equity 

# Calculate total net worth in inflation-adjusted terms
total_net_worth_real = total_net_worth / ((1 + inflation_rate) ** 10)

print(total_net_worth, total_net_worth_real)
