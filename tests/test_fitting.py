__author__ = "github.com/wardsimon"
__version__ = "0.0.1"

from easyTemplateLib.Objects.fitting import Parameter


def test_parameter():
    p = Parameter("a", 1)
    assert p.name == "a"
    assert p.value == 1
    assert p.fixed is False
    assert p.max is None
    assert p.min is None
