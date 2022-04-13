def oneToHundered():
    """This function produces a sequence of numbers from 1 to 100\n
    Parameters -> none
    Return -> none
    """
    print("Printing numbers from 1 to 100")
    for i in range(1, 101):
        print(i, end=" ")

def tableOfTwo():
    """This function produces a table of Two\n
    Parameters -> none
    Return -> none
    """
    print("Printing table of 2")
    for i in range(1, 11):
        print(f"2 * {i} = {2 * i}")

print(tableOfTwo.__doc__)
def printEvens():
    """This function produces a sequence of even numbers from 1 to 100\n
    Parameters -> none
    Return -> none
    """
    print("Printing even numbers from 1 to 100")
    for i in range(1, 101):
        if i % 2 == 0:
            print(i)

# Docstrings - Documentation related 
print(printEvens.__doc__)