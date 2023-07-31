class HomePageObjects:
    search_input = "xpath://input[@name='q']"
    username_input = "xpath://span[text()='Enter Email/Mobile number']/parent::label/preceding-sibling::input"
    close_login_window_btn = "xpath://button[text()='✕']"

    product_link = "xpath://div[contains(text(),'{0}')]"
    add_to_cart = "xpath://button[text()='Add to cart']"
    buy_now = "xpath://button[text()='Buy Now']"

rmdir /s /q .\allure_report\
rmdir /s /q .\screenshots\
del .\automation.log

@REM python -m venv c:\path\to\myenv
@REM venv/Script/activate
@REM pip install -r requirements.txt

pytest -v -s .\tests\test_stories_severities_features.py --alluredir="allure_report" -n 5
@REM pytest -v -s .\tests\ --alluredir="allure_report"
 pytest -v -s --ignore=.\tests\test_stories_severities_features --alluredir="allure_report"
@REM  pytest -v -s --ignore=.\tests\amazon\ --ignore=.\tests\flipkart\ --alluredir="allure_report"

@REM pytest -v -s --browser_name edge .\tests\test_dependency.py --alluredir="allure_report"
@REM pytest -v -s --browser_name firefox .\tests\flipkart\ --alluredir="allure_report"
@REM pytest -v -s --browser_name chrome .\tests\amazon\ --alluredir="allure_report"

@REM pytest -v -s --allure-stories "Story 2" .\tests\ --alluredir="allure_report"
@REM pytest -v -s --allure-severities normal,critical .\tests\ --alluredir="allure_report"
@REM pytest -v -s --allure-features "feature 2" .\tests\ --alluredir="allure_report"
@REM pytest -v -s --allure-features "feature 1" --allure-stories story2 .\tests\ --alluredir="allure_report"

@REM pytest -v -s -m "p1" .\tests\ --alluredir="allure_report"
@REM pytest -v -s -m "p1 or p2" .\tests\ --alluredir="allure_report"

@REM pytest -v -s .\tests\test_order.py --alluredir="allure_report"
@REM pytest -v -s .\tests\test_dependency.py --alluredir="allure_report"


xcopy /e /i /y .\reports\history .\allure_report\history

rmdir /s /q reports

allure generate .\allure_report\ --clean -o reports

@REM --lf #for failed test cases
@REM --ff #Failed first
