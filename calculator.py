def fraction_to_decimal(numerator: int, denominator: int) -> str:
    """
    Converts a fraction to its decimal representation as a string.

    This function handles negative fractions, detects repeating decimal sequences, 
    and correctly formats them with parentheses.

    Parameters
    ----------
    numerator : int
        The numerator of the fraction.
    denominator : int
        The denominator of the fraction (non-zero).

    Returns
    -------
    str
        The decimal representation of the fraction. If the decimal part repeats, 
        the repeating sequence is enclosed in parentheses.

    Notes
    -----
    - If the fraction is negative, a "-" sign is placed at the beginning.
    - If the fraction is an integer, the function returns it as a string.
    - If the decimal has a repeating sequence, it is enclosed in parentheses.
    - A dictionary (`lookup`) is used to detect repeating decimals by storing 
      the positions of remainders.

    Examples
    --------
    >>> fraction_to_decimal(1, 2)
    '0.5'

    >>> fraction_to_decimal(2, 3)
    '0.(6)'

    >>> fraction_to_decimal(4, 333)
    '0.(012)'

    >>> fraction_to_decimal(-50, 8)
    '-6.25'

    >>> fraction_to_decimal(7, -12)
    '-0.58(3)'

    >>> fraction_to_decimal(1, 5)
    '0.2'
    """
    if numerator == 0:
        return "0"
    result = []
    if (numerator < 0 < denominator) or (denominator < 0 < numerator):
        result.append("-")

    # we might forget about handling with sign and operate on asb values:
    numerator = abs(numerator)
    denominator = abs(denominator)
    integer_part = numerator // denominator
    result.append(str(integer_part))
    reminder = numerator % denominator

    # it may happen that reminder is sero then we have integer number
    if reminder == 0:
        return "".join(result)

    # otherwise there will be for sure decimal part that must be separated by character '.'
    result.append('.')
    # dictionary to store place in decimal key: reminder, value: len of fraction, so position of reminder
    lookup = {}
    while reminder != 0:
        if reminder in lookup:
            result.insert(lookup[reminder], "(")
            result.append(')')
            break
        lookup[reminder] = len(result)
        reminder *= 10
        result.append(str(reminder // denominator))
        reminder %= denominator
    return "".join(result)


class Calculator:
    """
    A simple calculator class that provides basic arithmetic operations.

    Attributes:
        __result (float): Stores the current result of calculations.
    """

    def __init__(self, result=0):
        """
        Initializes the calculator with an optional starting result.

        Parameters
        ----------
        result : float, optional
            Initial value of the calculator, by default 0.
        """
        self.__result = result

    def add(self, a):
        """
        Adds a number to the current result.

        Parameters
        ----------
        a : float
            The number to be added.
        """
        self.__result += a

    def subtract(self, a):
        """
        Subtracts a number from the current result.

        Parameters
        ----------
        a : float
            The number to be subtracted.
        """
        self.__result -= a

    def multiply(self, a):
        """
        Multiplies the current result by a given number.

        Parameters
        ----------
        a : float
            The number to multiply by.
        """
        self.__result = self.__result * a

    def divide(self, a):
        """
        Divides the current result by a given number.

        Parameters
        ----------
        a : float
            The number to divide by.

        Raises
        ------
        ValueError
            If attempting to divide by zero.
        """
        if a == 0:
            raise ValueError("cannot divide by zero")
        else:
            self.__result = self.__result / a

    def modulo(self, a):
        """
        Computes the remainder of the division of the current result by a given number.

        Parameters
        ----------
        a : float
            The divisor.

        Raises
        ------
        ValueError
            If attempting to compute modulo by zero.
        """
        if a == 0:
            raise ValueError("cannot divide by zero")
        else:
            self.__result = self.__result % a

    def power(self, a):
        """
        Raises the current result to the power of a given number.

        Parameters
        ----------
        a : float
            The exponent.
        """
        self.__result = self.__result ** a

    def square_root(self):
        """
        Computes the square root of the current result.

        Notes
        -----
        The result is computed as `result ** 0.5`.
        """
        self.__result = self.__result ** 0.5

    def clear(self):
        """
        Resets the current result to zero.
        """
        self.__result = 0

    def get_result(self):
        """
        Returns the current result of the calculator.

        Returns
        -------
        float
            The current result.
        """
        return self.__result
