from tokenize import String

import pytest
import os.path
from selenium.webdriver import Keys, ActionChains

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.select import Select


class FunctionalTesting:

    def __init__(self, driver):
        self.driver = driver

    clickABTesting = (By.XPATH, "//a[normalize-space()='A/B Testing']")
    getTextABTesting = (By.XPATH, "/html[1]/body[1]/div[2]/div[1]/div[1]/p[1]")
    clickAddRemoveButton = (By.LINK_TEXT, "Add/Remove Elements")
    clickAddElementButton = (By.XPATH, "//button[@onclick='addElement()']")
    verifyButtonPresent = (By.XPATH, "//button[@class='added-manually']")
    clickCheckBoxLink = (By.XPATH, "//a[normalize-space()='Checkboxes']")
    verifyCheckBoxSelected1 = (By.XPATH, "(//input[@type='checkbox'])[1]")
    verifyCheckBoxSelected2 = (By.XPATH, "(//input[@type='checkbox'])[2]")
    clickContextMenuButton = (By.LINK_TEXT, "Context Menu")
    clickOnContextMenuBox = (By.ID, "hot-spot")
    clickDigestAuthentication = (By.LINK_TEXT, "Digest Authentication")
    clickDragAndDrop = (By.LINK_TEXT, "Drag and Drop")
    clickOnBoxA = (By.ID, "column-a")
    clickOnBoxB = (By.XPATH, "//div[@id='column-b']")
    clickDD = (By.LINK_TEXT, "Dropdown")
    clickRemoveButton = (By.XPATH, "//button[@onclick='swapCheckbox()']")
    clickEnableButton = (By.XPATH, "//button[@onclick='swapInput()']")
    getRemoveOrDisableText = (By.XPATH, "//p[@id='message']")
    clickDynamicControl = (By.LINK_TEXT, "Dynamic Controls")
    getCheckBoxPresent = (By.XPATH, "//div[normalize-space()='A checkbox']")
    clickDynamicLoading = (By.LINK_TEXT, "Dynamic Loading")
    clickExample1 = (By.LINK_TEXT, "Example 1: Element on page that is hidden")
    clickExample2 = (By.LINK_TEXT, "Example 2: Element rendered after the fact")
    startButton = (By.XPATH, "//button[normalize-space()='Start']")
    textHelloWorld = (By.XPATH, "//h4[normalize-space()='Hello World!']")
    subjectTitle2 = (By.XPATH, "//h4[normalize-space()='Example 2: Element rendered after the fact']")
    subjectTitle1 = (By.XPATH, "//h4[normalize-space()='Example 1: Element on page that is hidden']")
    clickEntryAd = (By.LINK_TEXT, "Entry Ad")
    clickEntryAdClickHere = (By.XPATH, "//a[@id='restart-ad']")
    getModalWindowTitle = (By.XPATH, "//h3[normalize-space()='This is a modal window']")
    clickCloseButton = (By.XPATH, "//p[normalize-space()='Close']")
    getTextOfClosedModal = (By.XPATH, "//p[contains(text(),'If closed, it will not appear on subsequent page l')]")
    # FileDownload
    clickFileDownload = (By.LINK_TEXT, "File Download")
    clickSampleDownloadFile = (By.LINK_TEXT, "samples.pdf")
    # FileUpload
    clickFileUpload = (By.LINK_TEXT, "File Upload")
    clickChooseFile = (By.XPATH, "//input[@id='file-upload']")
    clickUploadFile = (By.XPATH, "//input[@class='button']")
    getFileText = (By.XPATH, "//div[@id='uploaded-files']")
    # Floating Menu
    clickFloatingMenu = (By.LINK_TEXT, "Floating Menu")
    verifyHomeMenu = (By.LINK_TEXT, "Home")
    verifyAboutMenu = (By.LINK_TEXT, "About")
    clickPageTitle = (By.XPATH, "//h3[normalize-space()='Floating Menu']")
    # Form Authentication
    clickFormAuthentication = (By.LINK_TEXT, "Form Authentication")
    enterUserName = (By.XPATH, "//input[@id='username']")
    enterPassword = (By.XPATH, "//input[@id='password']")
    clickLoginButton = (By.XPATH, "//button[@type='submit']")
    getStatusMessage = (By.XPATH, "//div[@id='flash']")
    clickLogOutButton = (By.XPATH, "//a[@class='button secondary radius']")
    getLoginPageTitle = (By.XPATH, "//h2[normalize-space()='Login Page']")

    # Frames
    clickFrame = (By.LINK_TEXT, "Frames")
    clickNestedFrames = (By.LINK_TEXT, "Nested Frames")
    clickIFrame = (By.LINK_TEXT, "iFrame")
    getLeftFrameText = (By.XPATH, "/html[1]/body[1]")
    getBody = (By.TAG_NAME, "body")

    # Hover
    clickHover = (By.LINK_TEXT, "Hovers")
    hoverFirstImage = (By.CSS_SELECTOR, "body > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div:nth-child(3) > img:nth-child(1)")
    hoverSecondImage = (By.XPATH, "(//div[@class='example']//div[1]//img[2]")
    getTextUserImage1 = (By.XPATH, "//h5[normalize-space()='name: user1']")

    # Horizontal Scrollbar
    dragScrollBarH = (By.XPATH, "//input[@type = 'range']")
    scrollBarRange = (By.XPATH, "//span[@id='range']")
    clickHorizontalSlider = (By.LINK_TEXT, "Horizontal Slider")

    #Input
    input = (By.LINK_TEXT, "Inputs")
    number = (By.XPATH, "//input[@type='number']")
    numberValue = (By.TAG_NAME, "input")


    def InputNumbers(self):
        self.driver.find_element(*FunctionalTesting.input).click()
        self.driver.implicitly_wait(5)
        self.driver.find_element(*FunctionalTesting.number).send_keys("5")
        verifyText = self.driver.find_element(*FunctionalTesting.numberValue).get_attribute('value')
        return verifyText


    def DragHorizontalScroll(self):
        self.driver.find_element(*FunctionalTesting.clickHorizontalSlider).click()
        action = ActionChains(self.driver)
        slider = self.driver.find_element(*FunctionalTesting.dragScrollBarH)
        action.click_and_hold(slider).move_by_offset(40, 0).release().perform()
        self.driver.implicitly_wait(5)
        getText = self.driver.find_element(*FunctionalTesting.scrollBarRange).text
        return getText

    def VerifyHoverImage(self):
        self.driver.find_element(*FunctionalTesting.clickHover).click()
        self.driver.implicitly_wait(5)
        action = ActionChains(self.driver)
        hover = self.driver.find_element(*FunctionalTesting.hoverFirstImage)
        action.move_to_element(hover).click().perform()
        self.driver.implicitly_wait(5)
        verifyText = self.driver.find_element(*FunctionalTesting.getTextUserImage1).text
        return verifyText


    def VerifyIFrame(self):
        self.driver.implicitly_wait(5)
        self.driver.find_element(*FunctionalTesting.clickFrame).click()
        self.driver.find_element(*FunctionalTesting.clickIFrame).click()
        self.driver.implicitly_wait(5)
        self.driver.switch_to.frame("mce_0_ifr")
        frame = self.driver.find_element(*FunctionalTesting.getBody)
        frameRightText = frame.text
        print(frameRightText)
        # self.driver.switch_to.frame("frame-right")

    def VerifyNestedFrames(self):

        self.driver.implicitly_wait(5)
        self.driver.find_element(*FunctionalTesting.clickFrame).click()
        self.driver.find_element(*FunctionalTesting.clickNestedFrames).click()
        self.driver.implicitly_wait(5)
        self.driver.switch_to.frame("frame-top")
        self.driver.switch_to.frame("frame-right")
        frame = self.driver.find_element(*FunctionalTesting.getBody)
        frameRightText = frame.text
        print(frameRightText)
        self.driver.get("http://the-internet.herokuapp.com/")
        self.driver.find_element(*FunctionalTesting.clickFrame).click()
        self.driver.find_element(*FunctionalTesting.clickNestedFrames).click()
        self.driver.switch_to.frame("frame-top")
        self.driver.switch_to.frame("frame-left")
        frame = self.driver.find_element(*FunctionalTesting.getBody)
        frameLeftText = frame.text
        print(frameLeftText)
        self.driver.get("http://the-internet.herokuapp.com/")
        self.driver.find_element(*FunctionalTesting.clickFrame).click()
        self.driver.find_element(*FunctionalTesting.clickNestedFrames).click()
        self.driver.switch_to.frame("frame-top")
        self.driver.switch_to.frame("frame-middle")
        frame = self.driver.find_element(*FunctionalTesting.getBody)
        frameMiddleText = frame.text
        print(frameMiddleText)
        self.driver.get("http://the-internet.herokuapp.com/")
        self.driver.find_element(*FunctionalTesting.clickFrame).click()
        self.driver.find_element(*FunctionalTesting.clickNestedFrames).click()
        # self.driver.switch_to.frame("frame-top")
        self.driver.switch_to.frame("frame-bottom")
        frame = self.driver.find_element(*FunctionalTesting.getBody)
        frameBottomText = frame.text
        print(frameBottomText)
        return frameRightText + frameLeftText + frameMiddleText + frameBottomText

    def VerifySuccessLoginStatus(self):
        self.driver.find_element(*FunctionalTesting.clickFormAuthentication).click()
        self.driver.implicitly_wait(5)
        self.driver.find_element(*FunctionalTesting.enterUserName).send_keys("tomsmith")
        self.driver.find_element(*FunctionalTesting.enterPassword).send_keys("SuperSecretPassword!")
        self.driver.find_element(*FunctionalTesting.clickLoginButton).click()
        verifyText = self.driver.find_element(*FunctionalTesting.getStatusMessage).text
        self.driver.find_element(*FunctionalTesting.clickLogOutButton).click()
        return verifyText

    def VerifyFailedLoginStatus(self):
        self.driver.implicitly_wait(5)
        self.driver.find_element(*FunctionalTesting.enterUserName).send_keys("wrongUN")
        self.driver.find_element(*FunctionalTesting.enterPassword).send_keys("wrongPwd!")
        self.driver.find_element(*FunctionalTesting.clickLoginButton).click()
        verifyText = self.driver.find_element(*FunctionalTesting.getStatusMessage).text
        return verifyText

    def VerifyFloatingMenu(self):

        self.driver.find_element(*FunctionalTesting.clickFloatingMenu).click()
        # self.driver.find_element(*FunctionalTesting.clickPageTitle).click()
        self.driver.implicitly_wait(5)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        verifyText1 = self.driver.find_element(*FunctionalTesting.verifyHomeMenu).text
        verifyText2 = self.driver.find_element(*FunctionalTesting.verifyAboutMenu).text
        return verifyText1 + verifyText2

    def ClickFileUpload(self):
        return self.driver.find_element(*FunctionalTesting.clickFileUpload).click()

    def ClickChooseFile(self):
        return self.driver.find_element(*FunctionalTesting.clickChooseFile).send_keys(
            "C://Users//Ritesh.Kumar//Documents//test.txt")

    def ClickUploadFileButton(self):
        return self.driver.find_element(*FunctionalTesting.clickUploadFile).click()

    def VerifyFileUploaded(self):
        return self.driver.find_element(*FunctionalTesting.getFileText).text

    def ClickFileDownload(self):
        return self.driver.find_element(*FunctionalTesting.clickFileDownload).click()

    def ClickSampleDowmloadFile(self):
        fileStatus = " "
        self.driver.find_element(*FunctionalTesting.clickSampleDownloadFile).click()

        while not os.path.exists("C://Users//Ritesh.Kumar//Downloads//samples.pdf"):
            self.driver.implicitly_wait(5)
            if os.path.isfile("C://Users//Ritesh.Kumar//Downloads//samples.pdf"):
                fileStatus = "File download is completed"
                print(fileStatus)
            '''else:
                print("File download is not completed")'''

        return fileStatus

    def DeleteDownloadedFile(self):
        os.remove("C://Users//Ritesh.Kumar//Downloads//samples.pdf")

    def GetTextOfClosedModal(self):
        return self.driver.find_element(*FunctionalTesting.getTextOfClosedModal).text

    def ClickCloseButton(self):
        return self.driver.find_element(*FunctionalTesting.clickCloseButton).click()

    def GetModalWindowTitle(self):
        self.driver.find_element(*FunctionalTesting.getModalWindowTitle).click()
        test = self.driver.find_element(*FunctionalTesting.getModalWindowTitle).text
        print(test)
        return self.driver.find_element(*FunctionalTesting.getModalWindowTitle).text

    def ClickEntryAdClickHere(self):
        return self.driver.find_element(*FunctionalTesting.clickEntryAdClickHere).click()

    def ClickEntryAd(self):
        return self.driver.find_element(*FunctionalTesting.clickEntryAd).click()

    def GetExample2Text(self):
        return self.driver.find_element(*FunctionalTesting.subjectTitle2).text

    def GetExample1Text(self):
        return self.driver.find_element(*FunctionalTesting.subjectTitle1).text

    def GetTextHelloWorld(self):
        self.driver.find_element(*FunctionalTesting.textHelloWorld).click()
        test = self.driver.find_element(*FunctionalTesting.textHelloWorld).text
        print(test)
        return test

    def ClickStartButton(self):
        return self.driver.find_element(*FunctionalTesting.startButton).click()

    def ClickExample1(self):
        return self.driver.find_element(*FunctionalTesting.clickExample1).click()

    def ClickExample2(self):
        return self.driver.find_element(*FunctionalTesting.clickExample2).click()

    def ClickDynamicLoading(self):
        return self.driver.find_element(*FunctionalTesting.clickDynamicLoading).click()

    def AddCheckBox(self):
        return self.driver.find_element(*FunctionalTesting.getCheckBoxPresent).text

    def ClickDynamicControl(self):
        return self.driver.find_element(*FunctionalTesting.clickDynamicControl).click()

    def ClickRemoveButton(self):
        return self.driver.find_element(*FunctionalTesting.clickRemoveButton).click()

    def ClickEnableButton(self):
        return self.driver.find_element(*FunctionalTesting.clickEnableButton).click()

    def GetRemoveOrDisableText(self):
        return self.driver.find_element(*FunctionalTesting.getRemoveOrDisableText).text

    def SelectDropDownValue(self, inputValue):
        select = Select(self.driver.find_element(By.ID, "dropdown"))
        select.select_by_value(inputValue)
        self.driver.implicitly_wait(2)
        selectedValue = select.first_selected_option.text
        print(selectedValue)
        return selectedValue

    def ClickDropDownLink(self):
        return self.driver.find_element(*FunctionalTesting.clickDD).click()

    def ClickDragAndDropLink(self):
        return self.driver.find_element(*FunctionalTesting.clickDragAndDrop).click()

    def ClickDragAndDropBoxA2BoxB(self):
        source = self.driver.find_element(*FunctionalTesting.clickOnBoxA)
        print(source.location)
        target = self.driver.find_element(*FunctionalTesting.clickOnBoxB)
        print(target.location)
        action = ActionChains(self.driver)
        action.drag_and_drop(source, target).pause(1).perform()
        self.driver.implicitly_wait(2)
        # action.drag_and_drop(source, target).perform()
        # self.driver.implicitly_wait(5)
        verifyText = self.driver.find_element(*FunctionalTesting.clickOnBoxB).text
        return verifyText

    def RightClickOnContextMenuBox(self):
        rightClick = self.driver.find_element(*FunctionalTesting.clickOnContextMenuBox)
        # action chain object creation
        action = ActionChains(self.driver)
        # right click operation and then perform
        action.context_click(rightClick).perform()
        # to close the browser
        readText = self.driver.switch_to.alert
        self.driver.switch_to.default_content()
        self.driver.find_element(*FunctionalTesting.clickOnContextMenuBox).click()
        return readText

    def ClickContextMenuLink(self):
        return self.driver.find_element(*FunctionalTesting.clickContextMenuButton).click()

    def VerifyCheckBox1IsSelected(self):
        return self.driver.find_element(*FunctionalTesting.verifyCheckBoxSelected1)

    def VerifyCheckBox2IsSelected(self):
        return self.driver.find_element(*FunctionalTesting.verifyCheckBoxSelected2)

    def ClickCheckBoxLink(self):
        return self.driver.find_element(*FunctionalTesting.clickCheckBoxLink).click()

    def VerifyDeleteButton(self):
        return self.driver.find_element(*FunctionalTesting.verifyButtonPresent).is_displayed()

    def ClickAddElement(self):
        return self.driver.find_element(*FunctionalTesting.clickAddElementButton).click()

    def ClickABTesting(self):
        return self.driver.find_element(*FunctionalTesting.clickABTesting).click()

    def GetSiteName(self):
        print(self.driver.title)
        return self.driver.title

    def GetTextABTestControl(self):
        return self.driver.find_element(*FunctionalTesting.getTextABTesting).text

    def ClickAddRemoveButton(self):
        return self.driver.find_element(*FunctionalTesting.clickAddRemoveButton).click()
