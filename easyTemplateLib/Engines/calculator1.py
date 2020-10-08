__author__ = "github.com/wardsimon"
__version__ = "0.0.1"

import numpy as np
import scipy.optimize as sio

from easyTemplateLib.Engines.calculatorTemplate import CalculatorTemplate


class Calculator1(CalculatorTemplate):
    name = "scipy"

    def __init__(self, obj):
        super().__init__(obj)

    def calculate(self):
        m = self._store.get("model")
        fit, cov = sio.curve_fit(m.fit_func, self.x, self.y, p0=m.x0, ftol=self.ftol)
        m.std = np.sqrt(np.diag(cov))
        return fit
