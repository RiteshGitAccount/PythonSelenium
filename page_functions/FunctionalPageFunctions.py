from utilities.BaseClass import BaseClass
from page_objects.FunctionalPageObjects import FunctionalPageObjects


class FunctionalPageFunctions(BaseClass):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.fun_obj = FunctionalPageObjects()

    def InputNumbers(self):
        self.print_log("demo log",log_type="error")
        self.print_log("demo log",log_type="info")
        self.print_log("demo log",log_type="debug")
        self.wait_for_element_visibility("Inputs", locator_type="link", timeout=5, poll_frequency=1)
        self.click_element("Inputs", locator_type="link")
        # self.wait_for_element_invisibility("Inputs", locator_type="link")
        # self.send_text("5", "//input[@type='number']")

    # def DragHorizontalScroll(self):
    #     self.driver.find_element(*FunctionalTesting.clickHorizontalSlider).click()
    #     action = ActionChains(self.driver)
    #     slider = self.driver.find_element(*FunctionalTesting.dragScrollBarH)
    #     action.click_and_hold(slider).move_by_offset(40, 0).release().perform()
    #     self.driver.implicitly_wait(5)
    #     getText = self.driver.find_element(*FunctionalTesting.scrollBarRange).text
    #     return getText
    #
    # def VerifyHoverImage(self):
    #     self.driver.find_element(*FunctionalTesting.clickHover).click()
    #     self.driver.implicitly_wait(5)
    #     action = ActionChains(self.driver)
    #     hover = self.driver.find_element(*FunctionalTesting.hoverFirstImage)
    #     action.move_to_element(hover).click().perform()
    #     self.driver.implicitly_wait(5)
    #     verifyText = self.driver.find_element(*FunctionalTesting.getTextUserImage1).text
    #     return verifyText
    #
    # def VerifyIFrame(self):
    #     self.driver.implicitly_wait(5)
    #     self.driver.find_element(*FunctionalTesting.clickFrame).click()
    #     self.driver.find_element(*FunctionalTesting.clickIFrame).click()
    #     self.driver.implicitly_wait(5)
    #     self.driver.switch_to.frame("mce_0_ifr")
    #     frame = self.driver.find_element(*FunctionalTesting.getBody)
    #     frameRightText = frame.text
    #     print(frameRightText)
    #     # self.driver.switch_to.frame("frame-right")
    #
    # def VerifyNestedFrames(self):
    #
    #     self.driver.implicitly_wait(5)
    #     self.driver.find_element(*FunctionalTesting.clickFrame).click()
    #     self.driver.find_element(*FunctionalTesting.clickNestedFrames).click()
    #     self.driver.implicitly_wait(5)
    #     self.driver.switch_to.frame("frame-top")
    #     self.driver.switch_to.frame("frame-right")
    #     frame = self.driver.find_element(*FunctionalTesting.getBody)
    #     frameRightText = frame.text
    #     print(frameRightText)
    #     self.driver.get("http://the-internet.herokuapp.com/")
    #     self.driver.find_element(*FunctionalTesting.clickFrame).click()
    #     self.driver.find_element(*FunctionalTesting.clickNestedFrames).click()
    #     self.driver.switch_to.frame("frame-top")
    #     self.driver.switch_to.frame("frame-left")
    #     frame = self.driver.find_element(*FunctionalTesting.getBody)
    #     frameLeftText = frame.text
    #     print(frameLeftText)
    #     self.driver.get("http://the-internet.herokuapp.com/")
    #     self.driver.find_element(*FunctionalTesting.clickFrame).click()
    #     self.driver.find_element(*FunctionalTesting.clickNestedFrames).click()
    #     self.driver.switch_to.frame("frame-top")
    #     self.driver.switch_to.frame("frame-middle")
    #     frame = self.driver.find_element(*FunctionalTesting.getBody)
    #     frameMiddleText = frame.text
    #     print(frameMiddleText)
    #     self.driver.get("http://the-internet.herokuapp.com/")
    #     self.driver.find_element(*FunctionalTesting.clickFrame).click()
    #     self.driver.find_element(*FunctionalTesting.clickNestedFrames).click()
    #     # self.driver.switch_to.frame("frame-top")
    #     self.driver.switch_to.frame("frame-bottom")
    #     frame = self.driver.find_element(*FunctionalTesting.getBody)
    #     frameBottomText = frame.text
    #     print(frameBottomText)
    #     return frameRightText + frameLeftText + frameMiddleText + frameBottomText
    #
    # def VerifySuccessLoginStatus(self):
    #     self.driver.find_element(*FunctionalTesting.clickFormAuthentication).click()
    #     self.driver.implicitly_wait(5)
    #     self.driver.find_element(*FunctionalTesting.enterUserName).send_keys("tomsmith")
    #     self.driver.find_element(*FunctionalTesting.enterPassword).send_keys("SuperSecretPassword!")
    #     self.driver.find_element(*FunctionalTesting.clickLoginButton).click()
    #     verifyText = self.driver.find_element(*FunctionalTesting.getStatusMessage).text
    #     self.driver.find_element(*FunctionalTesting.clickLogOutButton).click()
    #     return verifyText
    #
    # def VerifyFailedLoginStatus(self):
    #     self.driver.implicitly_wait(5)
    #     self.driver.find_element(*FunctionalTesting.enterUserName).send_keys("wrongUN")
    #     self.driver.find_element(*FunctionalTesting.enterPassword).send_keys("wrongPwd!")
    #     self.driver.find_element(*FunctionalTesting.clickLoginButton).click()
    #     verifyText = self.driver.find_element(*FunctionalTesting.getStatusMessage).text
    #     return verifyText
    #
    # def VerifyFloatingMenu(self):
    #
    #     self.driver.find_element(*FunctionalTesting.clickFloatingMenu).click()
    #     # self.driver.find_element(*FunctionalTesting.clickPageTitle).click()
    #     self.driver.implicitly_wait(5)
    #     self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    #     verifyText1 = self.driver.find_element(*FunctionalTesting.verifyHomeMenu).text
    #     verifyText2 = self.driver.find_element(*FunctionalTesting.verifyAboutMenu).text
    #     return verifyText1 + verifyText2
    #
    # def ClickFileUpload(self):
    #     return self.driver.find_element(*FunctionalTesting.clickFileUpload).click()
    #
    # def ClickChooseFile(self):
    #     return self.driver.find_element(*FunctionalTesting.clickChooseFile).send_keys(
    #         "C://Users//Ritesh.Kumar//Documents//test.txt")
    #
    # def ClickUploadFileButton(self):
    #     return self.driver.find_element(*FunctionalTesting.clickUploadFile).click()
    #
    # def VerifyFileUploaded(self):
    #     return self.driver.find_element(*FunctionalTesting.getFileText).text
    #
    # def ClickFileDownload(self):
    #     return self.driver.find_element(*FunctionalTesting.clickFileDownload).click()
    #
    # def ClickSampleDowmloadFile(self):
    #     fileStatus = " "
    #     self.driver.find_element(*FunctionalTesting.clickSampleDownloadFile).click()
    #
    #     while not os.path.exists("C://Users//Ritesh.Kumar//Downloads//samples.pdf"):
    #         self.driver.implicitly_wait(5)
    #         if os.path.isfile("C://Users//Ritesh.Kumar//Downloads//samples.pdf"):
    #             fileStatus = "File download is completed"
    #             print(fileStatus)
    #         '''else:
    #             print("File download is not completed")'''
    #
    #     return fileStatus
    #
    # def DeleteDownloadedFile(self):
    #     os.remove("C://Users//Ritesh.Kumar//Downloads//samples.pdf")
    #
    # def GetTextOfClosedModal(self):
    #     return self.driver.find_element(*FunctionalTesting.getTextOfClosedModal).text
    #
    # def ClickCloseButton(self):
    #     return self.driver.find_element(*FunctionalTesting.clickCloseButton).click()
    #
    # def GetModalWindowTitle(self):
    #     self.driver.find_element(*FunctionalTesting.getModalWindowTitle).click()
    #     test = self.driver.find_element(*FunctionalTesting.getModalWindowTitle).text
    #     print(test)
    #     return self.driver.find_element(*FunctionalTesting.getModalWindowTitle).text
    #
    # def ClickEntryAdClickHere(self):
    #     return self.driver.find_element(*FunctionalTesting.clickEntryAdClickHere).click()
    #
    # def ClickEntryAd(self):
    #     return self.driver.find_element(*FunctionalTesting.clickEntryAd).click()
    #
    # def GetExample2Text(self):
    #     return self.driver.find_element(*FunctionalTesting.subjectTitle2).text
    #
    # def GetExample1Text(self):
    #     return self.driver.find_element(*FunctionalTesting.subjectTitle1).text
    #
    # def GetTextHelloWorld(self):
    #     self.driver.find_element(*FunctionalTesting.textHelloWorld).click()
    #     test = self.driver.find_element(*FunctionalTesting.textHelloWorld).text
    #     print(test)
    #     return test
    #
    # def ClickStartButton(self):
    #     return self.driver.find_element(*FunctionalTesting.startButton).click()
    #
    # def ClickExample1(self):
    #
    #     return self.driver.find_element(*FunctionalTesting.clickExample1).click()
    #
    # def ClickExample2(self):
    #     return self.driver.find_element(*FunctionalTesting.clickExample2).click()
    #
    # def ClickDynamicLoading(self):
    #     return self.driver.find_element(*FunctionalTesting.clickDynamicLoading).click()
    #
    # def AddCheckBox(self):
    #     return self.driver.find_element(*FunctionalTesting.getCheckBoxPresent).text
    #
    # def ClickDynamicControl(self):
    #     return self.driver.find_element(*FunctionalTesting.clickDynamicControl).click()
    #
    # def ClickRemoveButton(self):
    #     return self.driver.find_element(*FunctionalTesting.clickRemoveButton).click()
    #
    # def ClickEnableButton(self):
    #     return self.driver.find_element(*FunctionalTesting.clickEnableButton).click()
    #
    # def GetRemoveOrDisableText(self):
    #     return self.driver.find_element(*FunctionalTesting.getRemoveOrDisableText).text
    #
    # def SelectDropDownValue(self, inputValue):
    #     select = Select(self.driver.find_element(By.ID, "dropdown"))
    #     select.select_by_value(inputValue)
    #     self.driver.implicitly_wait(2)
    #     selectedValue = select.first_selected_option.text
    #     print(selectedValue)
    #     return selectedValue
    #
    # def ClickDropDownLink(self):
    #     return self.driver.find_element(*FunctionalTesting.clickDD).click()
    #
    # def ClickDragAndDropLink(self):
    #     return self.driver.find_element(*FunctionalTesting.clickDragAndDrop).click()
    #
    # def ClickDragAndDropBoxA2BoxB(self):
    #     source = self.driver.find_element(*FunctionalTesting.clickOnBoxA)
    #     print(source.location)
    #     target = self.driver.find_element(*FunctionalTesting.clickOnBoxB)
    #     print(target.location)
    #     action = ActionChains(self.driver)
    #     action.drag_and_drop(source, target).pause(1).perform()
    #     self.driver.implicitly_wait(2)
    #     # action.drag_and_drop(source, target).perform()
    #     # self.driver.implicitly_wait(5)
    #     verifyText = self.driver.find_element(*FunctionalTesting.clickOnBoxB).text
    #     return verifyText
    #
    # def RightClickOnContextMenuBox(self):
    #     rightClick = self.driver.find_element(*FunctionalTesting.clickOnContextMenuBox)
    #     # action chain object creation
    #     action = ActionChains(self.driver)
    #     # right click operation and then perform
    #     action.context_click(rightClick).perform()
    #     # to close the browser
    #     readText = self.driver.switch_to.alert
    #     self.driver.switch_to.default_content()
    #     self.driver.find_element(*FunctionalTesting.clickOnContextMenuBox).click()
    #     return readText
    #
    # def ClickContextMenuLink(self):
    #     return self.driver.find_element(*FunctionalTesting.clickContextMenuButton).click()
    #
    # def VerifyCheckBox1IsSelected(self):
    #     return self.driver.find_element(*FunctionalTesting.verifyCheckBoxSelected1)
    #
    # def VerifyCheckBox2IsSelected(self):
    #     return self.driver.find_element(*FunctionalTesting.verifyCheckBoxSelected2)
    #
    # def ClickCheckBoxLink(self):
    #     return self.driver.find_element(*FunctionalTesting.clickCheckBoxLink).click()
    #
    # def VerifyDeleteButton(self):
    #     return self.driver.find_element(*FunctionalTesting.verifyButtonPresent).is_displayed()
    #
    # def ClickAddElement(self):
    #     return self.driver.find_element(*FunctionalTesting.clickAddElementButton).click()
    #
    # def ClickABTesting(self):
    #     return self.driver.find_element(*FunctionalTesting.clickABTesting).click()
    #
    # def GetSiteName(self):
    #     print(self.driver.title)
    #     return self.driver.title
    #
    # def GetTextABTestControl(self):
    #     return self.driver.find_element(*FunctionalTesting.getTextABTesting).text
    #
    # def ClickAddRemoveButton(self):
    #     return self.driver.find_element(*FunctionalTesting.clickAddRemoveButton).click()
    #
    # def drag_and_drop_js(self):
    #     file = cwd.split("tests")
    #     fname = file[0] + "resources\\drag_and_drop_helper.js"
    #     print(fname)
    #     with open(fname, 'r') as js_file:
    #         line = js_file.readline()
    #         script = ''
    #         while line:
    #             script += line
    #             line = js_file.readline()
    #
    #     driver.execute_script(script + "$('" + source + "').simulateDragDrop({ dropTarget: '" + target + "'});")
    #     time.sleep(2)
    #
    #     assert driver.find_element(*FunctionalTesting.check).text == "B"
    #
    #     return success
    #
    # def drag_and_drop(self):
    #     action = ActionChains(self.driver)
    #
    #     action.drag_and_drop(src, trgt).perform()
    #
    #     return success
    #
    # def drag_and_drop_by_offset(self, x_offset, y_offset):
    #     action = ActionChains(self.driver)
    #
    #     action.drag_and_drop_by_offset(src, x_offset, y_offset).perform()
    #
    #     return success
