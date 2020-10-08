__author__ = "github.com/wardsimon"
__version__ = "0.0.1"

from typing import Callable


class Parameter:
    def __init__(self, name=None, value=1.0, min=None, max=None, fixed=False):

        if not name:
            ValueError("Name can not be none")

        self.name = name

        self.value = value
        self.fixed = fixed

        if min is not None and max is not None and min > max:
            if not self.fixed:
                raise ValueError(
                    "The value of `min` should be less than or"
                    " equal to the value of `max`."
                )
        else:
            self.min = min
            self.max = max


class Model:
    def __init__(self, model, parameters, constraints=None):
        self._fun = model
        self._constraints = constraints
        self._parameters = {}
        self.std = None
        for parameter in parameters:
            self._parameters[parameter.name] = parameter
            setattr(
                self.__class__,
                parameter.name,
                property(self.__gitem(parameter.name), self.__sitem(parameter.name)),
            )

    def __repr__(self):
        info = ""
        items = [self._parameters[key] for key in self._parameters.keys()]
        for num, item in enumerate(items):
            info += f"{item.name}:{item.value}"
            if not item.fixed:
                info += "("
                if self.std is not None:
                    info += f"{self.std[num]}"
                info += ")"
            info += ", "
        if len(items) > 0:
            info = info[:-2]
        return f"Function f: {info}"

    @property
    def func(self):
        def inner(x):
            return self._fun(
                x, *[self._parameters[key].value for key in self._parameters.keys()]
            )

        return inner

    @property
    def fit_func(self):
        def inner(x, *args):
            return self._fun(x, *args)

        return inner

    @property
    def x0(self):
        return [
            self._parameters[key].value
            for key in self._parameters.keys()
            if not self._parameters[key].fixed
        ]

    def set_parameters(self, *args):
        items = [
            self._parameters[key]
            for key in self._parameters.keys()
            if not self._parameters[key].fixed
        ]
        if len(args) == 1 and isinstance(args[0], list):
            args = args[0]
        if len(items) != len(args):
            raise ValueError(
                f"Incorrect number of parameters. Expected {len(items)}, got {len(args)}."
            )
        for enum, value in enumerate(args):
            items[enum].value = value

    def set_parameter(self, param, value):
        item = self._parameters.get(param, None)
        if item:
            item.value = value

    # def __apply_constraints(self, parameter):
    #     if self._constraints is not None:
    #         for constraint in self._constraints:
    #             self._parameters[parameter.name] = constraint(parameter)

    @staticmethod
    def __gitem(key: str) -> Callable:
        def inner(obj):
            try:
                data = obj._parameters[key]
                return data.value
            except KeyError:
                raise AttributeError

        return lambda obj: inner(obj)

    @staticmethod
    def __sitem(key):
        return lambda obj, value: obj._parameters.__getitem__(key).__setitem__(
            "value", value
        )
