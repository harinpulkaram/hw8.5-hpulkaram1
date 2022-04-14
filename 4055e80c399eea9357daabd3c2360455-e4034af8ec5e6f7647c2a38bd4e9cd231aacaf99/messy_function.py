def function_that_is_too_long(n: int):
    """
    Honestly, who knows why this function exists?
    """
    # let's not bother with zero or negative integers
    if n < 1:
        return 0

    # convert the input to a binary string, because
    pow = 0
    while 2 ** pow < n:  # ** means exponent, for the uninitiated
        pow += 1
    pow -= 1  # go back to the largest power that was smaller than n

    binary_string = ""
    while pow >= 0:
        if 2 ** pow <= n:
            binary_string += "1"
            n -= 2 ** pow
        else:
            binary_string += "0"
        pow -= 1

    # get every other digit of the binary string, for reasons
    every_other = ""
    for i in range(0, len(binary_string), 2):
        every_other += binary_string[i]

    # sum up the resulting string, and return that
    res = sum(
        int(digit) for digit in every_other
    )  # this is some sneaky Python called a "comprehension" - it's basically a condensed for loop
    return res
  
def mod1(s: int) -> int:
    """
    Determines if number is zero or one, if it is, does not run the remainder of the functon
    """
    if s < 1:
        return 0
    return 1
def mod2(s:int) -> int:
    """
    finding the closest power of two to the given integer, return the closest power
    """
    if mod1(s) == 0:
        pow = 0
        return pow
    else:
        pow = 0
        while 2 ** pow < s:  
            pow += 1
        pow -= 1 
        return pow

def mod3(s:int) -> str:
    """
    given an in integer, return the binary string
    """
    binary_string = ""
    if mod2(s) == 0:
        binary_string = 0
        return binary_string
    else:
        while mod2(s) >= 0:
            x = mod2(s)
            if 2 ** x <= s:
                binary_string += "1"
                s -= 2 ** x
            else:
                binary_string += "0"
            x -= 1
        return binary_string

def mod4(s:int):
    """
    given an integer, return every other value from it's binary string
    """
    if mod3(s) == 0:
        every_other = 0
        return every_other
    else:
        every_other = ""
        for i in range(0, len(mod3(s)), 2):
            every_other += mod3(s)[i]
        return every_other

def mod5(s:int):
    """
    given an integer, return the sum of values from every other value in the integer's binary string
    """
    if mod4(s) == 0:
        return 0
    else:
        res = sum(
        int(digit) for digit in mod4(s)
        )
        return res