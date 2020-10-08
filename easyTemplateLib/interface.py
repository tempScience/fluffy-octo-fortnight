__author__ = "github.com/wardsimon"
__version__ = "0.0.1"


#import matplotlib.pyplot as plt

from easyTemplateLib.Engines import calculators as calculators_list


class Interface:
    def __init__(self, model):
        self._calculator = None
        self.model = model
        self.y_opt = None
        self.ftol = 1e-8
        self._prev = None
        self._x = None
        self._y = None

    def set_calculator(self, calc):
        calc_avail = [c.name for c in calculators_list]
        if calc in calc_avail:
            self._calculator = calculators_list[calc_avail.index(calc)](
                self._for_calc()
            )

    def clear_calc(self):
        self._calculator = None

    def set_parameter(self, parm, value):
        self.model.set_parameter(parm, value)

    def fit(self):
        if self._calculator is None or self.model is None:
            raise ValueError
        self._calculator.ftol = self.ftol
        self._prev = self.model.x0
        n_new = self._calculator.calculate()
        self.model.set_parameters(*n_new)
        self.y_opt = self.model.func(self.x)

    def _for_calc(self):
        out = {"x": self.x, "y": self.y, "ftol": self.ftol, "model": self.model}
        return out

    @property
    def calculator(self):
        return self._calculator.name

    @calculator.setter
    def calculator(self, value):
        if value in [c.name for c in calculators_list]:
            self.set_calculator(value)

    @property
    def x(self):
        val = self._x
        if self._calculator is not None:
            val = self._calculator.x
        return val

    @x.setter
    def x(self, value):
        self._x = value
        if self._calculator is not None:
            # raise ValueError('Calculator has not been initialized yet')
            self._calculator.x = self._x

    @property
    def y(self):
        val = self._y
        if self._calculator is not None:
            val = self._calculator.y
        return val

    @y.setter
    def y(self, value):
        self._y = value
        if self._calculator is not None:
            # raise ValueError('Calculator has not been initialized yet')
            self._calculator.y = self._y

    def plot(self):
        plt.scatter(self.x, self.y)
        if self.y_opt is not None:
            plt.plot(self.x, self.y_opt)
        plt.show()
