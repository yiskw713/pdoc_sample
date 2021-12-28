"""This documentation was updated by github actions.
Please see my blog for the detail: https://yiskw713.hatenablog.com/pdoc-github-actions
"""


class SampleClass(object):
    """This is a smaple class."""

    def __init__(self, a: int, b: float, c: str) -> None:
        """Sample constructor.
        Args:
            a: integer
            b: flaot
            c: string
        """
        self.a = a
        self.b = b
        self.c = c

    def sample(self, x: int) -> int:
        """Sample method.
        Args:
            x: integer
        Return:
            integer
        """
        return self.a + x

    def call(self, input_str: str) -> str:
        """Sample call method.
        Args:
            x: str
        Return:
            str
        """
        return self.c + input_str
