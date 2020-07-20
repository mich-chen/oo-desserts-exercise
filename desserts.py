"""Dessert classes."""


class Cupcake:
    """A cupcake."""

    # dictionary that will store all cupcake instances by name
    cache = {}

    @staticmethod
    def scale_recipe(ingredients, amount):
        """Scale list of ingredients by given amount of cupcakes.

        Ingredients are given as a list of tuples with (ingredient_name, 
        ingredient_qty) Return a list of tuples with quantity of each
        ingredient multiplied by amount.
        """
        scaled_recipe = []

        # for each ingredient in the ingredients list
        for name, qty in ingredients:
            # multiple qty by given amount and store with name as new tuple
            scaled_ingredient = (name, qty * amount)
            # append new ingredient tuple in a new list
            scaled_recipe.append(scaled_ingredient)

        return scaled_recipe

    @classmethod
    def get(cls, name):
        """Return cupcake from cache. If name not found, print a statement."""

        # check if name is in our dictionary of cupcakes
        if name not in cls.cache:
            # if not, then print statement
            print("Sorry, that cupcake doesn't exist")

        else:
            # return the __repr__ of cupcake name given (sotred as value)
            return cls.cache[name]





    def __init__(self, name, flavor, price, qty=0):
        """Instance of a cupcake."""

        self.name = name
        self.flavor = flavor
        self.price = price
        self.qty = qty
        self.cache[self.name] = self


    def __repr__(self):
        """Human-readable printout for debugging."""

        return f'<Cupcake name="{self.name}" qty={self.qty}>'

    def add_stock(self, amount):
        """Add amount to cupcake stock quantity."""

        self.qty += amount

    def sell(self, amount):
        """Sell the given amount of cupcakes and update stock quantity."""

        # if cupcakes are out of stock
        if self.qty == 0:
            print('Sorry, these cupcakes are sold out')

        else:
        # subtract amount sold from stock quantity
            self.qty -= amount
        # make sure quantity never goes below zero (no negative stock)
            if self.qty < 0:
          # if goes below zero (sold more than have) then set to 0
                self.qty = 0



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
