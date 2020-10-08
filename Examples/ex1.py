__author__ = "github.com/wardsimon"
__version__ = "0.0.1"

import numpy as np

from easyTemplateLib.interface import Interface, calculators_list
from easyTemplateLib.Objects.fitting import Model, Parameter


x = np.linspace(0, 10, 100)
y = 3.0 * x + 2.0 + np.random.normal(-1.0, 1.0, len(x))

p1 = Parameter("m", 1.5)
p2 = Parameter("c", 0.5)

f = lambda x, m, c: m * x + c  # noqa: E731
m = Model(f, [p1, p2])

interface = Interface(model=m)
interface.x = x
interface.y = y
interface.ftol = 1e-4
interface.set_calculator("scipy")
interface.fit()
interface.plot()

for calc in calculators_list:
    interface.set_calculator(calc.name)
    interface.fit()
    interface.plot()
