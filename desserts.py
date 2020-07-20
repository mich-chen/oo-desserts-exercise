"""Dessert classes."""


class Cupcake:
    """A cupcake."""

    # dictionary that will store all cupcake instances by name
    cache = {}
    class_name = 'Cupcake'

    @staticmethod
    def scale_recipe(ingredients, amount):
        """Scale list of ingredients by given amount of cupcakes.

        Ingredients are given as a list of tuples with (ingredient_name, 
        ingredient_qty) Return a list of tuples with quantity of each
        ingredient multiplied by amount.
        """

        # multiple qty by amount and store new tuple in a list
        # scaled_recipe = [(name, qty * amount) for name, qty in ingredients]

        return [(name, qty * amount) for name, qty in ingredients]



    @classmethod
    def get(cls, name):
        """Return cupcake from cache. If name not found, print a statement."""

        # check if name is in our dictionary of cupcakes
        if name not in cls.cache:
            # if not, then print statement
            print(f"Sorry, that {cls.class_name} doesn't exist")

        else:
            # return the __repr__ of cupcake name given (sotred as value)
            return cls.cache[name]


    def __init__(self, name, flavor, price):
        """Instance of a cupcake."""

        self.name = name
        self.flavor = flavor
        self.price = price
        self.qty = 0
        self.cache[self.name] = self


    def __repr__(self):
        """Human-readable printout for debugging."""

        return f'<{self.class_name} name="{self.name}" qty={self.qty}>'

    def add_stock(self, amount):
        """Add amount to cupcake stock quantity."""

        self.qty += amount

    def sell(self, amount):
        """Sell the given amount of cupcakes and update stock quantity."""

        # if cupcakes are out of stock
        if self.qty == 0:
            print(f'Sorry, these cupcake are sold out')

        else:
        # subtract amount sold from stock quantity
            self.qty -= amount
        # make sure quantity never goes below zero (no negative stock)
            if self.qty < 0:
          # if goes below zero (sold more than have) then set to 0
                self.qty = 0


class Brownie(Cupcake):
    """A brownie."""
    class_name = 'Brownie'

    def __init__(self, name, price):
        """ Initializing a brownie."""

        super().__init__(name, 'chocolate', price)

    def __repr__(self):
        """Human-readable printout for debugging."""

        return f'<Brownie name="{self.name}" qty={self.qty}>'

#     def sell(self, amount):
#         """Sell the given amount of cupcakes and update stock quantity."""

#         super().sell(amount)
#         # if cupcakes are out of stock
#         if self.qty == 0:
#             print('Sorry, these brownies are sold out')

#         else:
#         # subtract amount sold from stock quantity
#             self.qty -= amount
#         # make sure quantity never goes below zero (no negative stock)
#             if self.qty < 0:
#           # if goes below zero (sold more than have) then set to 0
#                 self.qty = 0


if __name__ == '__main__':
    import doctest

    result = doctest.testfile('doctests.py',
                              report=False,
                              optionflags=(
                                  doctest.REPORT_ONLY_FIRST_FAILURE
                              ))
    doctest.master.summarize(1)
    if result.failed == 0:
        print('ALL TESTS PASSED')
