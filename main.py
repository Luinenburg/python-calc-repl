import sys
from enum import Enum

class Error(Enum):
    DIV_ZERO = "DIV_ZERO"
    UNS_OP = "UNS_OP"
    BAD_EQ = "BAD_EQ"
    UNS_VAL = "UNS_VAL"

def process_operation(num1, operation, num2):
    try:
        num1 = float(num1)
        num2 = float(num2)
    except ValueError:
        return Error.UNS_VAL
    match operation:
        case "+":
            return num1 + num2
        
        case "*":
            return num1 * num2

        case "/":
            if num2 == 0:
                return Error.DIV_ZERO
            return num1 / num2

        case "-":
            return num1 - num2
        case _:
            return Error.UNS_OP

def unmix(mixed_symbols):
    numbers = []
    operations = []
    number = ""
    for symbol in mixed_symbols:
        if "+*/-".find(symbol) > -1:
            if number == "":
                return Error.BAD_EQ
            operations.append(symbol)
            numbers.append(float(number))
            number = ""
        elif "0123456789".find(symbol) > -1:
            number += symbol
        else:
            return Error.UNS_VAL
    try:
        numbers.append(float(number))
    except ValueError:
        return Error.BAD_EQ
    if len(numbers) != len(operations)+1:
        return Error.BAD_EQ
    return [numbers, operations]

def operate(sorted_symbols):
    try:
        if sorted_symbols in Error: return sorted_symbols
    except TypeError:
        pass
    numbers = sorted_symbols[0]
    operations = sorted_symbols[1]
   
    index = 0
    while operations.count("*") > 0 or operations.count("/") > 0:
        operation = operations[index]
        if "*/".find(operation) > -1:
            result = process_operation(numbers[index], operation, numbers[index+1])
            if result in Error:
                return result
            numbers[index] = result
            numbers.pop(index+1)
            operations.pop(index)
            index = 0
        index += 1

    index = 0
    while operations.count("+") > 0 or operations.count("-") > 0:
        print(numbers)
        print(operations)
        if (index >= len(operations)): index = 0
        operation = operations[index]
        if "+-".find(operation) > -1:
            result = process_operation(numbers[index], operation, numbers[index+1])
            if result in Error:
                return result
            numbers[index] = result
            numbers.pop(index+1)
            operations.pop(index)
            index = 0
        index += 1
 
    return numbers[0]


def rep():
    return    

def main():
    if (len(sys.argv) > 2):
        print("Error: Too many arguments. Ensure equation is surrounded in quotes")
        return
    if (len(sys.argv) < 2):
        print("Error: Too few arguments. Did you provide an equation?")
        return
    print(operate(unmix(sys.argv[1])))

if __name__=="__main__":
    main()
