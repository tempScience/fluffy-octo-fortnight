__author__ = "github.com/wardsimon"
__version__ = "0.0.1"

from easyTemplateLib.Engines.calculatorTemplate import CalculatorTemplate


class Calculator2(CalculatorTemplate):
    name = "not_implemented"

    def __init__(self, obj):
        super().__init__(obj)

    def calculate(self):
        m = self._store.get("model")
        m.std = [0] * len(m.x0)
        return [0] * len(m.x0)
