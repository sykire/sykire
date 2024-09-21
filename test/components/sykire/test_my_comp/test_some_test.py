from __future__ import annotations

from dataclasses import dataclass

from sykire.my_comp import core


def test_sample():
    assert core is not None


def test_my_sum_equals():
    assert core.my_sum(1, 2) == 3


def test_my_sum_not_equals():
    assert core.my_sum(1, 2) != 4


@dataclass
class Product:
    name: str | None = None


@dataclass
class Order:
    product: Product
    quantity: int


def test_do_something():
    core.do_something()
