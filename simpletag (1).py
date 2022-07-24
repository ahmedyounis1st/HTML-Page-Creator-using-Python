import pandas as pd
import numpy as np

from dataclasses import dataclass

@dataclass
class SelectOption:
    value: 'typing.Any'
    disabled: bool = False
    selected: bool = False

    def __iter__(self):
        return iter((self.value, self.disabled, self.selected))

    def __repr__(self):
        return (f'[{self.value}, {self.disabled}, {self.selected}]')


class HtmlInput:
    serialcnt = 0

    def __init__(self, .... ):
        #
        # fill in whatever is needed for your implementation.
        #

    def _evaluate(self):
        #
        # fill in whatever is needed for your implementation.
        #


class Number (HtmlInput):
    def __repr__(self):     # check out the meaning of __repr__ yourself
        return ('<input type="number" ' + self._evaluate() + '/>')

class Date (HtmlInput):
    def __repr__(self):
        return ('<input type="date" ' + self._evaluate() + '/>')

class Button (HtmlInput):
    #
    # complete this and other APIs
    #

class STag (HtmlInput):
    #
    # complete the rest
    #


class DOM:
    class HtmlTable:
        def __enter__(self):    # check out the meaning of __enter__ and __exit__ yourself
            #
            # complete the rest
            #

        def __exit__(self, exception_type, exception_value, traceback):
            #
            # complete the rest
            #

    def table(self, dim, colwidths, **auxpr): 
        return (self.HtmlTable(self, dim, colwidths, **auxpr))

    #
    # complete other APIs yourself
    #

