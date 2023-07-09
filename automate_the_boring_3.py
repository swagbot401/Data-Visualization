import math, sys, random, pyperclip


def div42by (divideBy):
    try:
        ans = 42 / divideBy
        print(f"I got an answer for you. It's ", end="")
        return ans
    
    except ZeroDivisionError:
        print("You can't divde by zero silly!")

    except TypeError: 
        print(f"\"{str(divideBy)}\" is a string silly")

    except:
        print("I'm not sure what went wrong")
    


def div42byB (divideBy):
    return 42 / divideBy

print(div42by("chris"))
print(div42by(3))
print(div42by("a"))

catnumb = -3
print(f"Number of cats is {int(catnumb)}")