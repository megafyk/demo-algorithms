class Factorial(object):
    def __init__(self):
        return

    def recursive(self, num):
        """ Factorial using recursive

        Parameters
        ----------
        num : int
            Number of factorial.
        
        Returns
        int
            Result of factorial.

        """
        return 1 if (num == 0 or num == 1) else num * self.recursive(num-1)

    def split_recursive(self, num):
        """ Factorial using split recursive algorithm

        Parameters
        ----------
        num : int
            Number of factorial.
        
        Returns
        int
            Result of factorial.

        """
        return 1