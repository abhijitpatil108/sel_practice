from pytest import mark
from test_pom_demo_sir.homepage import HomePage
from test_pom_demo_sir.loginpage import LoginPage
headers = "email, password"
data = [    ("bill.gates@company.com", "Password123"), 
            # ("hello.world@company.com", "Password123")
        ]

# C:\Users\Abhijit\PycharmProjects\selenium_practice\test_pom_demo_sir\homepage.py
@mark.parametrize(headers, data)
def test_login(_driver, email, password):

    # Click on Login Link
    hp = HomePage(_driver)
    hp.home_click_login()

    lp = LoginPage(_driver)
    # Enter Email
    lp.login_enter_email(email)
    # Enter Password
    lp.login_enter_password(password)
    # Click Login
    lp.login_click_login()

    # hp.is_user_logged_in(email)