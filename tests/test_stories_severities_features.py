import unittest

import allure
import pytest

from page_functions.FunctionalPageFunctions import FunctionalPageFunctions
from utilities.BaseClass import BaseClass


@pytest.mark.usefixtures("setup")
@allure.epic("Epic 1")
@allure.feature("Feature 1")
@allure.story("Story 1")
@allure.tag("Tag_1")
@allure.description("This is demo description")
@allure.severity(allure.severity_level.NORMAL)
class Test(unittest.TestCase):
    """
    This is demo file for executing test cases based on severity, feature or story
    """

    @pytest.fixture(autouse=True)
    def classSetup(self, setup):
        self.fun = FunctionalPageFunctions(self.driver)
        self.base = BaseClass(self.driver)

    @allure.title("Check severity level - CRITICAL")
    @allure.tag("Test level tag")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.story("Story 2")
    @allure.feature("Feature 2")
    def test_critical(self):
        self.base.print_log("error log", log_type="error")
        self.base.print_log("info log", log_type="info")
        self.base.print_log("debug log", log_type="debug")
        self.fun.InputNumbers()

    @allure.title("Check severity level - NORMAL")
    @allure.story("Story 2")
    @allure.severity(allure.severity_level.NORMAL)
    def test_normal(self):
        self.fun.InputNumbers()

    @allure.title("Check severity level - BLOCKER")
    @allure.feature("Feature 2")
    @allure.severity(allure.severity_level.BLOCKER)
    def test_blocker(self):
        self.fun.InputNumbers()

    @allure.title("Check severity level - TRIVIAL")
    @allure.severity(allure.severity_level.TRIVIAL)
    def test_trivial(self):
        self.fun.InputNumbers()

    @allure.title("Check severity level - MINOR")
    @allure.severity(allure.severity_level.MINOR)
    def test_minor(self):
        self.fun.InputNumbers()
