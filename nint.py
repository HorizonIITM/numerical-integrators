# just a sample code, dont take it serious
from typing import Callable, Iterable


class Integrators:
    def __init__(self, scheme: str = "euler"):
        self.scheme = scheme

    def integrate(
        self, func: Callable, step: float, init_vals: Iterable[float], end: float
    ):
        # some content
        self.result = integ_gen_obj  # integ_gen_object is the generator object

    def scheme1(self, *args):
        pass

    def scheme2(self, *args):
        pass
