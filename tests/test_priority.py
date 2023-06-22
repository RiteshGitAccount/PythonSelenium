import unittest
import pytest

from page_functions.FunctionalPageFunctions import FunctionalPageFunctions


@pytest.mark.usefixtures("setup")
class Test(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def classSetup(self, setup):
        self.fun = FunctionalPageFunctions(self.driver)

    @pytest.mark.p2
    def test_critical(self):
        self.fun.InputNumbers()

    @pytest.mark.p1
    def test_normal(self):
        self.fun.InputNumbers()

    @pytest.mark.p1
    def test_blocker(self):
        self.fun.InputNumbers()
