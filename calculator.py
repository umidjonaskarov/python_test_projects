import re

def calculate():
    calculation = input("enter your sequence: ")
    numbers = re.findall(r'\d+', calculation)
    if calculation.__contains__("+"):
        print(int(numbers[0]) + int(numbers[-1]))
    if calculation.__contains__("-"):
        print(int(numbers[0]) - int(numbers[-1]))  
    if calculation.__contains__("/"):
        print(int(numbers[0]) / int(numbers[-1]))   
    if calculation.__contains__("*"):
        print(int(numbers[0]) * int(numbers[-1]))

while True:
    calculate()