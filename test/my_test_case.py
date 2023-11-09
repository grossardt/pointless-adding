"""My Test Case"""

from abc import ABC
import unittest
import time

class MyTestCase(unittest.TestCase, ABC):
    """My Test Case"""

    def setUp(self) -> None:
        self._started_at = time.time()
        self._class_location = __file__

    def tearDown(self) -> None:
        elapsed = time.time() - self._started_at
        if elapsed > 5.0:
            print(f"({round(elapsed, 2):.2f}s)", flush=True)
