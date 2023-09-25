
# PART A AND B


# annual_salary = float(input("Enter your annual salary: "))
# portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
# total_cost = float(input("Enter the cost of your dream home: "))
# semi_annual_raise = float(input("Enter the semi-annual raise, as a decimal: "))
# r = 0.04
# current_savings = 0.0
# portion_down_payment = total_cost * 0.25

# months = 0 # Months starting from 0 
# annual_raise = 0
# while current_savings < portion_down_payment: # code won't print until currrent savings is more than portiondownpayment 
#     monthly_return = (current_savings * r)/12
#     monthly_salary_saved = (annual_salary / 12)* portion_saved
#     current_savings += monthly_return + monthly_salary_saved
#     months += 1 # increment of months
    
#     if months % 6 == 0:
#         annual_salary += (1 + semi_annual_raise)
#         annual_raise += 1

# print("Number of month: " , months )


# PART C

total_cost = 1000000
portion_down_payment = 0.25
r = 0.04
months = 36  
epsilon = 100

annual_salary = float(input("Enter your starting annual salary: "))

low = 0
high = 10000
steps = 0  

while True:
    steps += 1
    portion_saved = (low + high) / 20000.0
    current_savings = 0.0
    monthly_salary = annual_salary / 12.0
    
    for month in range(1, months + 1):
        current_savings += ((current_savings * r) / 12) + (monthly_salary * portion_saved)
    
    if abs(current_savings - (total_cost * portion_down_payment)) <= epsilon:
        print("Best savings rate:", portion_saved)
        print("Steps in bisection search:", steps)
        break
    elif current_savings < total_cost * portion_down_payment:
        low = portion_saved * 10000
    else:
        high = portion_saved * 10000


if portion_saved >= 1.0:
    print("It is not possible to save for the down payment in 36 months.")























