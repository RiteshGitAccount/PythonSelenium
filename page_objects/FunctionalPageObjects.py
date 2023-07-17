class FunctionalPageObjects:
    clickABTesting = "xpath://a[normalize-space()='A/B Testing']"
    getTextABTesting = "xpath:/html[1]/body[1]/div[2]/div[1]/div[1]/p[1]"


    clickAddRemoveButton = "Add/Remove Elements"
    clickAddElementButton = "//button[@onclick='addElement()']"
    verifyButtonPresent = "//button[@class='added-manually']"
    clickCheckBoxLink = "//a[normalize-space()='Checkboxes']"
    verifyCheckBoxSelected1 = "(//input[@type='checkbox'])[1]"
    verifyCheckBoxSelected2 = "(//input[@type='checkbox'])[2]"
    clickContextMenuButton = "Context Menu"
    clickOnContextMenuBox = "hot-spot"
    clickDigestAuthentication = "Digest Authentication"
    clickDragAndDrop = "Drag and Drop"
    clickOnBoxA = "column-a"
    clickOnBoxB = "//div[@id='column-b']"
    clickDD = "Dropdown"
    clickRemoveButton = "//button[@onclick='swapCheckbox()']"
    clickEnableButton = "//button[@onclick='swapInput()']"
    getRemoveOrDisableText = "//p[@id='message']"
    clickDynamicControl = "Dynamic Controls"
    getCheckBoxPresent = "//div[normalize-space()='A checkbox']"
    clickDynamicLoading = "Dynamic Loading"
    clickExample1 = "Example 1: Element on page that is hidden"
    clickExample2 = "Example 2: Element rendered after the fact"
    startButton = "//button[normalize-space()='Start']"
    textHelloWorld = "//h4[normalize-space()='Hello World!']"
    subjectTitle2 = "//h4[normalize-space()='Example 2: Element rendered after the fact']"
    subjectTitle1 = "//h4[normalize-space()='Example 1: Element on page that is hidden']"
    clickEntryAd = "Entry Ad"
    clickEntryAdClickHere = "//a[@id='restart-ad']"
    getModalWindowTitle = "//h3[normalize-space()='This is a modal window']"
    clickCloseButton = "//p[normalize-space()='Close']"
    getTextOfClosedModal = "//p[contains(text(),'If closed, it will not appear on subsequent page l')]"
    # FileDownload
    clickFileDownload = "File Download"
    clickSampleDownloadFile = "samples.pdf"
    # FileUpload
    clickFileUpload = "File Upload"
    clickChooseFile = "//input[@id='file-upload']"
    clickUploadFile = "//input[@class='button']"
    getFileText = "//div[@id='uploaded-files']"
    # Floating Menu
    clickFloatingMenu = "Floating Menu"
    verifyHomeMenu = "Home"
    verifyAboutMenu = "About"
    clickPageTitle = "//h3[normalize-space()='Floating Menu']"
    # Form Authentication
    clickFormAuthentication = "Form Authentication"
    enterUserName = "//input[@id='username']"
    enterPassword = "//input[@id='password']"
    clickLoginButton = "//button[@type='submit']"
    getStatusMessage = "//div[@id='flash']"
    clickLogOutButton = "//a[@class='button secondary radius']"
    getLoginPageTitle = "//h2[normalize-space()='Login Page']"

    # Frames
    clickFrame = "Frames"
    clickNestedFrames = "Nested Frames"
    clickIFrame = "iFrame"
    getLeftFrameText = "/html[1]/body[1]"
    getBody = "body"

    # Hover
    clickHover = "Hovers"
    hoverFirstImage = "body > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div:nth-child(3) > img:nth-child(1)"
    hoverSecondImage = "//div[@class='example']//div[1]//img[2]"
    getTextUserImage1 = "//h5[normalize-space()='name: user1']"

    # Horizontal Scrollbar
    dragScrollBarH = "//input[@type = 'range']"
    scrollBarRange = "//span[@id='range']"
    clickHorizontalSlider = "Horizontal Slider"

    # Input
    input = "Inputs"
    number = "//input[@type='number']"
    input1 = "Inputs"
    number1 = "//input[@type='number']"
    numberValue = "input"

    # Drag and Drop using Javascript
    source = "#column-a"
    target = "#column-b"
    check = "//*[@id='column-a']/header"

