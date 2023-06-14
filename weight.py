weight = float(input("Enter your weight: "))
unit = input("Is it in KG or LB? Enter K for KG or L for LB: ")

def check_weight():
    if unit == "K":
        converted = weight * 2.20462
        print("Your weight is " + str(converted) + " lbs")
    elif unit == "L":
        converted = weight / 2.20462
        print("Your weight is " + str(converted) + " kg")
    else:
        print("Invalid unit. Please enter K for KG or L for LB.")

if check_weight == True:
    check_weight()
else
    check_weight()


check_weight()