import unittest

import allure
import pytest

from page_functions.FunctionalPageFunctions import FunctionalPageFunctions


@allure.epic("Epic 1")
@allure.story("Story 1")
@allure.feature("Feature 1")
@allure.title("Title 1")
@allure.id("id 1")
@allure.tag("tag 1")
@allure.description("desc 1")
@allure.label("label 1")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.usefixtures("setup")
class Test(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def classSetup(self, setup):
        self.fun = FunctionalPageFunctions(self.driver)

    # @pytest.mark.run(order=1)
    @allure.title("Check severity level - CRITICAL")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_critical(self):
        self.driver.implicitly_wait(5)
        self.fun.InputNumbers()
        # verifyText = self.fun.InputNumbers()
        # assert "5" in verifyText

    # @allure.title("Check severity level - NORMAL")
    # @allure.severity(allure.severity_level.NORMAL)
    # def test_normal(self):
    #     self.driver.implicitly_wait(5)
    #     self.fun.InputNumbers()
    #
    # @allure.title("Check severity level - BLOCKER")
    # @allure.severity(allure.severity_level.BLOCKER)
    # def test_blocker(self):
    #     self.driver.implicitly_wait(5)
    #     self.fun.InputNumbers()
    #
    # @allure.title("Check severity level - TRIVIAL")
    # @allure.severity(allure.severity_level.TRIVIAL)
    # def test_trivial(self):
    #     self.driver.implicitly_wait(5)
    #     self.fun.InputNumbers()
    #
    # @allure.title("Check severity level - MINOR")
    # @allure.severity(allure.severity_level.MINOR)
    # def test_minor(self):
    #     self.driver.implicitly_wait(5)
    #     self.fun.InputNumbers()

    # def test_Hover(self):
    #     functionalTesting = FunctionalTesting(self.driver)
    #     self.driver.implicitly_wait(5)
    #     verifyText = functionalTesting.VerifyHoverImage()
    #     assert "name: user1" in verifyText
    #
    #
    # def test_dragHorozontally(self):
    #     functionalTesting = FunctionalTesting(self.driver)
    #     self.driver.implicitly_wait(5)
    #     verifyText = functionalTesting.DragHorizontalScroll()
    #     assert "4" in verifyText

    '''def test_iFrames(self):
        functionalTesting = FunctionalTesting(self.driver)
        self.driver.implicitly_wait(5)
        verifyText = functionalTesting.VerifyIFrame()
        print(verifyText)'''

    '''def test_NestedFrames(self):
        functionalTesting = FunctionalTesting(self.driver)
        self.driver.implicitly_wait(5)
        verifyText = functionalTesting.VerifyNestedFrames()
        assert "RIGHTLEFTMIDDLEBOTTOM" in verifyText'''

    '''def test_LoginStatus(self):
        functionalTesting = FunctionalTesting(self.driver)
        self.driver.implicitly_wait(5)
        verifyText = functionalTesting.VerifySuccessLoginStatus()
        assert "You logged into a secure area!" in verifyText
        verifyText = functionalTesting.VerifyFailedLoginStatus()
        assert "Your username is invalid!" in verifyText'''

    '''def test_ScrollPageWithFloatControl(self):
        functionalTesting = FunctionalTesting(self.driver)
        self.driver.implicitly_wait(5)
        verifyText = functionalTesting.VerifyFloatingMenu()
        print(verifyText)
        assert "Home" in verifyText
        assert "About" in verifyText'''

    '''def test_UploadFiles(self):
        functionalTesting = FunctionalTesting(self.driver)
        self.driver.implicitly_wait(5)
        functionalTesting.ClickFileUpload()
        functionalTesting.ClickChooseFile()
        functionalTesting.ClickUploadFileButton()
        verifyText = functionalTesting.VerifyFileUploaded()
        assert "test.txt" in verifyText
        self.driver.get("http://the-internet.herokuapp.com/")'''

    '''def test_downloadFiles(self):
        functionalTesting = FunctionalTesting(self.driver)
        self.driver.implicitly_wait(5)
        functionalTesting.ClickFileDownload()
        fileStatus = functionalTesting.ClickSampleDowmloadFile()
        assert "File download is completed" in fileStatus
        functionalTesting.DeleteDownloadedFile()
        self.driver.get("http://the-internet.herokuapp.com/")'''

    '''def test_ModalPopUp(self):
        functionalTesting = FunctionalTesting(self.driver)
        self.driver.implicitly_wait(5)
        functionalTesting.ClickEntryAd()
        functionalTesting.ClickEntryAdClickHere()
        verifyText = functionalTesting.GetModalWindowTitle()
        assert "THIS IS A MODAL WINDOW" in verifyText
        functionalTesting.ClickCloseButton()
        verifyText = functionalTesting.GetTextOfClosedModal()
        assert "If closed, it will not appear on subsequent page loads." in verifyText
        self.driver.get("http://the-internet.herokuapp.com/")'''

    """def test_DynamicLoading(self):
        functionalTesting = FunctionalTesting(self.driver)
        self.driver.implicitly_wait(5)
        functionalTesting.ClickDynamicLoading()
        functionalTesting.ClickExample1()
        functionalTesting.ClickStartButton()
        verifyText = functionalTesting.GetTextHelloWorld()
        assert "Hello World!" in verifyText
        verifyText = functionalTesting.GetExample1Text()
        assert "Example 1: Element on page that is hidden" in verifyText
        self.driver.back()
        functionalTesting.ClickExample2()
        functionalTesting.ClickStartButton()
        verifyText = functionalTesting.GetTextHelloWorld()
        assert "Hello World!" in verifyText
        verifyText = functionalTesting.GetExample2Text()
        assert "Example 2: Element rendered after the fact" in verifyText
        self.driver.get("http://the-internet.herokuapp.com/")"""

    '''def test_DynamicControl(self):
        functionalTesting = FunctionalTesting(self.driver)
        self.driver.implicitly_wait(5)
        functionalTesting.ClickDynamicControl()
        functionalTesting.ClickRemoveButton()
        verifyText = functionalTesting.GetRemoveOrDisableText()
        assert "It's gone!" in verifyText
        functionalTesting.ClickRemoveButton()
        verifyText = functionalTesting.AddCheckBox()
        assert " A checkbox".strip() in verifyText
        functionalTesting.ClickEnableButton()
        self.driver.implicitly_wait(5)
        verifyText = functionalTesting.GetRemoveOrDisableText()
        assert "It's enabled!" in verifyText
        self.driver.get("http://the-internet.herokuapp.com/")

    def test_VerifyDropDown(self):
        functionalTesting = FunctionalTesting(self.driver)
        self.driver.implicitly_wait(5)
        functionalTesting.ClickDropDownLink()
        verifyText = functionalTesting.SelectDropDownValue('1')
        print(verifyText)
        assert "Option 1" in verifyText
        self.driver.get("http://the-internet.herokuapp.com/")'''

    '''def test_VerifyDragAndDrop(self):
        functionalTesting = FunctionalTesting(self.driver)
        self.driver.implicitly_wait(5)
        functionalTesting.ClickDragAndDropLink()
        textVerify = functionalTesting.ClickDragAndDropBoxA2BoxB()
        while textVerify != "A":
            functionalTesting.ClickDragAndDropBoxA2BoxB()
        assert "A" in textVerify'''

    '''

    def test_VerifyPageTitle(self):
        functionalTesting = FunctionalTesting(self.driver)
        self.driver.implicitly_wait(5)
        alertText = functionalTesting.GetSiteName()
        assert ("The Internet" in alertText)
        self.driver.get("http://the-internet.herokuapp.com/")


    def test_VerifyStringPresent(self):
        functionalTesting = FunctionalTesting(self.driver)
        self.driver.implicitly_wait(5)
        alertText = functionalTesting.GetSiteName()
        assert ("The Internet" in alertText)
        functionalTesting.ClickABTesting()
        self.driver.implicitly_wait(5)
        alertText2= functionalTesting.GetTextABTestControl()
        assert("Also known as split testing" in alertText2)
        self.driver.get("http://the-internet.herokuapp.com/")


    def test_VerifyAddRemoveElement(self):
        functionalTesting = FunctionalTesting(self.driver)
        self.driver.implicitly_wait(5)
        functionalTesting.ClickAddRemoveButton()
        self.driver.implicitly_wait(2)
        functionalTesting.ClickAddElement()
        self.driver.implicitly_wait(2)
        assert(functionalTesting.VerifyDeleteButton())
        self.driver.get("http://the-internet.herokuapp.com/")

    def test_VerifyCheckBoxSelected(self):
        functionalTesting = FunctionalTesting(self.driver)
        functionalTesting.ClickCheckBoxLink()
        assert not functionalTesting.VerifyCheckBox1IsSelected().is_selected()
        functionalTesting.VerifyCheckBox1IsSelected().click()
        assert functionalTesting.VerifyCheckBox1IsSelected().is_selected()
        assert functionalTesting.VerifyCheckBox2IsSelected().is_selected()
        print("I am here")
        self.driver.get("http://the-internet.herokuapp.com/")"""

    def test_VerifyJavaScriptAlert(self):
        functionalTesting = FunctionalTesting(self.driver)
        self.driver.implicitly_wait(5)
        functionalTesting.ClickContextMenuLink()
        readText = functionalTesting.RightClickOnContextMenuBox()
        assert ("You selected a context menu" in readText)
        print("I am here Right Click")
        self.driver.get("http://the-internet.herokuapp.com/")'''
