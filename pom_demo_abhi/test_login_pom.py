
from pom_demo_abhi.homepage import HomePage_
from pom_demo_abhi.login import Login_
from pytest import  mark

headers = "email, password"
data = [("bill.gates@company.com", "Password123"),
            ("hello.world@company.com", "Password123")]

@mark.parametrize(headers,data)
def test_login(_driver, email, password):

    hp = HomePage_(_driver)
    hp.login_()

    lp = Login_(_driver)
    lp.log_email(email)
    lp.log_password(password)
    lp.log_login()

