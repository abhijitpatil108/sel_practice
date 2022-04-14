from homepage import HomePage
from registration import RegistrationPage

from pytest import mark

headers = "gender, fname, lname, email, password"
data = [
    ("male", "steve", "jobs", "steve.jobs@company.com", "Password123"),
    ("female", "laura", "turner", "laura.turner@company.com", "Password123")
]
@mark.parametrize(headers, data)
def test_registration(_driver, gender, fname, lname, email, password):
    # Click on Register Link
    hp = HomePage(_driver)
    hp.home_click_register()

    # Select Gender
    reg = RegistrationPage(_driver)
    if gender == "male":
        reg.registration_select_male()
    else:
        reg.registration_select_female()
    # enter fname
    reg.registration_enter_first_name(fname)

    # enter lname
    reg.registration_enter_last_name(lname)

    # enter email
    reg.registration_enter_email(email)

    # enter password
    reg.registration_enter_password(password)

    # enter confirm password
    reg.registration_enter_confirm_password(password)

    # click register
    reg.registation_click_register()