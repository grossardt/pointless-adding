"""
Adders (:mod:`pointless_adding.adders`)
===============================================

.. currentmodule:: pointless_adding.adders

The classes here are adders that can be used to add two objects.

.. autosummary::
   :toctree: ../stubs/
   :nosignatures:

    Adder
    IntAdder
    StringAdder

"""

from .adder import Adder
from .int_adder import IntAdder
from .string_adder import StringAdder

__all__ = [
    "Adder",
    "IntAdder",
    "StringAdder",
]
