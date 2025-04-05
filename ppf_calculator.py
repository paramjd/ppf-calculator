def calculate_ppf_maturity(principal, initial_contribution, rate, growth_rate, years):
    rate_decimal = rate / 100
    growth_decimal = growth_rate / 100
    
    # Future value of upfront principal
    future_principal = principal * (1 + rate_decimal) ** years
    
    # Future value of growing annual contributions
    future_contributions = 0
    for year in range(1, years + 1):
        contribution = initial_contribution * (1 + growth_decimal) ** (year - 1)
        contribution_fv = contribution * (1 + rate_decimal) ** (years - year + 1)
        future_contributions += contribution_fv
    
    total_maturity = future_principal + future_contributions
    return round(total_maturity, 2)

def input_data_calculate_and_ppf_maturirity():
    principal = float(input("Enter the existing PPF balance: ₹"))
    initial_contribution = float(input("Enter the Year 1 contribution: ₹"))
    ppf_rate = float(input("Enter the PPF interest rate (%): "))
    growth_rate = float(input("Enter the annual contribution growth rate (%): "))
    years = int(input("Enter the investment period (in years): "))
    maturity = calculate_ppf_maturity(principal, initial_contribution, ppf_rate, growth_rate, years)
    print(f"Maturity after {years} years: ₹{maturity:,}")

if __name__ == '__main__':
    # unittest.main()
    input_data_calculate_and_ppf_maturirity()
    


# Example
# principal = 5280838        # Existing balance
# initial_contribution = 420000  # Year 1 contribution
# ppf_rate = 12           # PPF interest rate (%)
# growth_rate = 10         # Annual contribution growth rate (%)
# years = 15               # Investment period

# maturity = calculate_ppf_maturity(principal, initial_contribution, ppf_rate, growth_rate, years)
# print(f"Maturity after {years} years: ₹{maturity:,}")

