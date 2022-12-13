"""
This is Sanya Assistant API
"""

from .geo import Geo
from .assistant import Assistant


def geo() -> Geo | None:
        
        """:class:`.Geo` Returns the user location info."""
        
        return Geo()

location = geo