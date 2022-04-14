from pom_demo_abhi.homepage import HomePage_
from pom_demo_abhi.register import Register_
from pytest import mark

headers = "gender, fname, lname, email, password"
data = [("male", "steve", "jobs", "steve.jobs@company.com", "Password123"),
    ("female", "laura", "turner", "laura.turner@company.com", "Password123")]

@mark.parametrize(headers,data)
def test_register(_driver, gender, fname, lname, email, password):
    hp = HomePage_(_driver)
    hp.register()

    rp = Register_(_driver)
    rp.select_gender(gender)
    rp.first_name(fname)
    rp.last_name(lname)
    rp.reg_email(email)
    rp.reg_pass(password)
    rp.reg_confirm_pass(password)
    rp.reg_register()