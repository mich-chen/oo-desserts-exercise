"""Dessert classes."""


class Cupcake:
    """A cupcake."""

    # dictionary that will store all cupcake instances by name
    cache = {}

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
