import unittest
import pytest

from page_functions.FunctionalPageFunctions import FunctionalPageFunctions


@pytest.mark.usefixtures("setup")
class Test(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def classSetup(self, setup):
        self.fun = FunctionalPageFunctions(self.driver)

    def test_critical(self):
        self.fun.InputNumbers()
        assert 2 == 3

    @pytest.mark.depends(on=['test_critical'])
    def test_normal(self):
        self.fun.InputNumbers()

    @pytest.mark.depends(on=['test_normal'])
    def test_blocker(self):
        self.fun.InputNumbers()
