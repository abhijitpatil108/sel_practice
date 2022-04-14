from pytest import mark
from loginpage import LoginPage
from homepage import HomePage

headers = "email, password"
data = [    ("bill.gates@company.com", "Password123"), 
            ("hello.world@company.com", "Password123")
        ]

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