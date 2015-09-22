from types import *
from string import *

def revealtype( inputString ):
    "Input a variable and it will output its type regardless of its casting."

    print "InputString=%s" % inputString
    if not inputString:
        return None

    if inputString.isdigit() == True:
        return int

    if inputString.isalpha() == True:
        return str

    strlen=len(inputString)
    hasdec=inputString.find(".",0,strlen) #size?
    if hasdec is not None:
        inputString1=inputString[:hasdec]
        if inputString1.isdigit() == True:
            inputString1=inputString[hasdec+1:]
            if inputString1.isdigit() == True:
                return float #also should look for "10."

    hascom=inputString.find(",",0,strlen)
    if hascom is not None:
        inputString1=inputString[:hascom]
        if inputString1.isalpha() == True:
            inputString1=inputString[hascom+1:]
            if inputString1.isalpha() == True:
                return "hascomma"

    neg=inputString.find("-",0)
    if neg is not None:
        inputString1=inputString[neg+1:]
        if inputString1.isdigit() == True:
            return int

    if (inputString == "True") or (inputString == "False"):
        return bool

    #support for complex type, dict type, etc...

    if inputString.isalnum() == True:
        return "alphanumeric"

    if inputString.isspace() == True:
        return "space"

    return "ERROR_Type"