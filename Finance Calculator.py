'''This Finance calculator program calculates the simple and compound interest using python'''

def simple_interest(original, rate, time):
    interest = (original * rate * time) / 100
    return interest

def compound_interest(original, rate, time):
    amount = original * (1 + (rate / 100)) ** time
    interest = amount - original
    return interest

# Taking input from user
original = float(input("Enter the original amount: £"))
rate = float(input("Enter the rate of interest: "))
time = float(input("Enter the time period in years: "))

# Calling functions and printing results
print("The Simple interest is = ", simple_interest(original, rate, time))
print("The Compound interest is = ", compound_interest(original, rate, time))
