import unittest
import pytest

from page_functions.FunctionalPageFunctions import FunctionalPageFunctions


@pytest.mark.usefixtures("setup")
class Test(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def classSetup(self, setup):
        self.fun = FunctionalPageFunctions(self.driver)

    def test_blocker(self):
        self.fun.input_numbers()

    @pytest.mark.run(order=2)
    def test_critical(self):
        self.fun.input_numbers()

    @pytest.mark.run(order=1)
    def test_normal(self):
        self.fun.input_numbers()
