import pytest
from arbetare import Arbetare


def test_arbetare_creation():
    arbetare = Arbetare("Anna")
    assert arbetare.name == "Anna"
    assert not arbetare.sick


def test_invalid_arbetare_name():
    with pytest.raises(ValueError):
        Arbetare("")


def test_make_sick_and_healthy():
    arbetare = Arbetare("Anna")
    arbetare.make_sick()
    assert arbetare.sick
    arbetare.make_healthy()
    assert not arbetare.sick
