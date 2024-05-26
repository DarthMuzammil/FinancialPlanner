# Initial Salary Calculation
initial_salary = 110000
yearly_increment = 1.1 #Salary hike every year 10%
additional_increment = 2.2 #Job switch every 3 years 22%
fixed_expenses = 30000
savings_rate = 0.65

# Growth rates
equity_growth = 0.12
debt_growth = 0.07

# Investment allocation
emergency_fund_percentage = 0.18  # First year only
debt_percentage = 0.30
equity_percentage = 0.70

# Lists to store values for each year
salaries = []
investments = []

# Calculate investments over the years
salary = initial_salary
for year in range(10):
    if year % 3 == 0 and year != 0:
        salary *= additional_increment
    salary *= yearly_increment
    
    disposable_income = salary - fixed_expenses
    savings = disposable_income * savings_rate

    if year == 0:
        emergency_fund = savings * emergency_fund_percentage
        remaining_savings = savings - emergency_fund
    else:
        emergency_fund = 0
        remaining_savings = savings
    
    debt_investment = remaining_savings * debt_percentage
    equity_investment = remaining_savings * equity_percentage
    
    investments.append((emergency_fund, debt_investment, equity_investment))
    salaries.append(salary)

# Initialize investment totals
total_debt = 0
total_equity = 0
total_gold = 0
total_other = 0

# Apply growth rates to each year's investments
for i, inv in enumerate(investments):
    emergency_fund, debt_investment, equity_investment = inv
    
    total_debt = (total_debt + debt_investment) * (1 + debt_growth)
    total_equity = (total_equity + equity_investment) * (1 + equity_growth)

total_net_worth = total_debt + total_equity 
print(total_net_worth)
