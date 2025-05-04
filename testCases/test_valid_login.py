from pageObjects.LoginPage import Loginpage
from pageObjects.Universal import Universal

def test_valid_login():
    Universal.test_launch_application()
    Loginpage.valid_login()
    Universal.close_driver()
