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
