from Pages.LoginPage import Loginpage
from Pages.Universal import Universal

def test_valid_login():
    Universal.test_launch_application()
    Loginpage.valid_login()
    Universal.close_driver()
