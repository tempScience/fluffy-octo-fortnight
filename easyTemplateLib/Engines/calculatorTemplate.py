__author__ = "github.com/wardsimon"
__version__ = "0.0.1"

from abc import ABCMeta, abstractmethod

import numpy as np


class CalculatorTemplate(metaclass=ABCMeta):
    calculators = []

    def __init_subclass__(cls, is_abstract=False, **kwargs):
        super().__init_subclass__(**kwargs)
        if not is_abstract:
            cls.calculators.append(cls)

    def __init__(self, obj):
        self._store = obj
        self._cov = None

    @property
    def x(self) -> np.ndarray:
        return self._store.get("x")

    @x.setter
    def x(self, value: np.ndarray):
        self._store["x"] = value

    @property
    def y(self) -> np.ndarray:
        return self._store.get("y")

    @y.setter
    def y(self, value: np.ndarray):
        self._store["y"] = value

    @property
    def ftol(self) -> float:
        return self._store.get("ftol", None)

    @ftol.setter
    def ftol(self, value: float):
        self._store["ftol"] = value

    @abstractmethod
    def calculate(self):
        pass
