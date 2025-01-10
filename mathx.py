
PI = 3.141592653589793238


def add(x, y):
    """
    document String
    add takes two inputs x and y
    returns the sum of x and y
    """
    sum_ = x+y
    return sum_  # if there is no return, the method return None


def add_print(x, y=1, *, z=2):
    print("x =", x, "and", "y =", y)
    print("The sum is", add(x, y))


def isOld(age):
    if not age:
        return None
    if age > 90:
        return "Too old"

    if (age > 80):
        return "Can do the job!"
    else:
        return "Training is required"


def sub(x: int, y: float) -> float:    # Type annotation
    """
    This is the method for cal the diff between x an y
    """
    return x-y


if __name__ == "__main__":
    print(__name__)
    print(sub(2, 1))
    print(isOld(""))
    add_print(3, 4, z=3)  # (x,/,*,y=1,z=2)
    add_print(3)
    add_print(4)
