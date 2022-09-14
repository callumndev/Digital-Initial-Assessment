methods = [
    # Addition
    {
        "symbol": "+",
        "fn":     lambda a, b: a + b
    },
    # Subtraction
    {
        "symbol": "-",
        "fn":     lambda a, b: a - b
    },
    # Multiplication
    {
        "symbol": "*",
        "fn":     lambda a, b: a * b
    },
    # Division
    {
        "symbol": "/",
        "fn":     lambda a, b: a / b
    },
    # Modulus
    {
        "symbol": "%",
        "fn":     lambda a, b: a % b
    },
    # Exponentiation
    {
        "symbol": "**",
        "fn":     lambda a, b: a ** b
    },
    # Floor division
    {
        "symbol": "//",
        "fn":     lambda a, b: a // b
    },
]

def allSymbols():
    return list(map(lambda method: method["symbol"], methods))

def isValidSymbol(symbol):
    for method in methods:
        if method["symbol"] == symbol:
            return True

    return False

def inputInt(prompt):
    try:
        return int(input(prompt));
    except:
        return None



firstNum  = inputInt("Enter first number: ")
if firstNum is None:
    print("Invalid first number")
    exit(1)

secondNum = inputInt("Enter second number: ")
if secondNum is None:
    print("Invalid second number")
    exit(1)


try:
    methodInput = input("Enter method ({}) ".format(", ".join(allSymbols())))
    if isValidSymbol(methodInput) == False:
        print("Invalid method")
        exit(1)

    print()
    
    fn = list(filter(lambda method: method["symbol"] == methodInput, methods))[0]["fn"]
    print("Result: {}".format(fn(firstNum, secondNum)))

except Exception as err:
    print("Error calculating: {}".format(err))
