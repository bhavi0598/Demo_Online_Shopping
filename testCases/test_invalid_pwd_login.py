from Pages.LoginPage import Loginpage
from Pages.Universal import Universal

def test_invalid_pwd_login():
    Universal.test_launch_application()
    Loginpage.invalid_password_login()
    Universal.close_driver()

