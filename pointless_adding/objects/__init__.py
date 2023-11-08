"""
Objects (:mod:`pointless_adding.objects`)
===============================================

.. currentmodule:: pointless_adding.objects

The classes here are objects that can be added by the adders.

.. autosummary::
   :toctree: ../stubs/
   :nosignatures:
   
   Object
   IntObject
   StringObject

"""

from .object import Object
from .int_object import IntObject
from .string_object import StringObject

__all__ = [
    "Object",
    "IntObject",
    "StringObject",
]
