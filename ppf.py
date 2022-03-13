year_opening_balance = 15020
interest_rate = float(7.1/100)
monthly_rate = float(interest_rate/12)
enter_years = int(input("years:"))
interest = 0
monthly_transfer = int(input("transfer each month:"))
monthly_balance = year_opening_balance
interest_list = []
for month in range(enter_years*12+1):
    if month%12==0:
        if month>=12:
            monthly_balance = monthly_balance + monthly_transfer
            interest = monthly_balance*monthly_rate
            interest_list.append(interest)
        year_opening_balance = monthly_balance+sum(interest_list)
        interest = 0
        monthly_balance = year_opening_balance
    else:
        monthly_balance = monthly_balance + monthly_transfer
        interest = monthly_balance*monthly_rate
        interest_list.append(interest)
equity_gold_interest = float(16.41/100)
equity_start_fund = 0
all_weather_interest = float(12.27/100)
all_weather_start_fund = 0

for i in range(0, enter_years):
    invested_amt_equity = 2500*12
    invested_amt_all_weather = 5000*12
    equity_start_fund = invested_amt_equity + equity_start_fund
    all_weather_start_fund = invested_amt_all_weather + all_weather_start_fund
    equity_start_fund = equity_start_fund + equity_start_fund*equity_gold_interest
    all_weather_start_fund = all_weather_start_fund + all_weather_start_fund*all_weather_interest

print("Equity return=",equity_start_fund, ";earned interest on equity=", equity_start_fund-invested_amt_equity*enter_years, "|| All weather return=", all_weather_start_fund, 
";earned interest on all_weather=", all_weather_start_fund-invested_amt_all_weather*enter_years)
print(year_opening_balance, "||", equity_start_fund+all_weather_start_fund, " || Total val:", equity_start_fund+all_weather_start_fund+year_opening_balance)