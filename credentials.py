import unittest #unittest module
from user import User #importing the user class
from credentials import Credentials #importing the credentials class

class TestPasswordLockerUser(unittest.TestCase):
    def setUp(self):
        self.newUser = User("Alex Kimutai","Kimuati101")
    def test_init(self):
        self.assertEqual(self.newUser.user_name,"Alex Kimutai")
        self.assertEqual(self.newUser.login_password,"Kimutai101")

    def test_save_user(self):
        self.newUser.save_user()
        self.assertEqual(len(User.user_list),1)

    def tearDown(self):
        User.user_list = []

    def test_save_multiple_users(self):
        self.newUser.save_user()
        test_user = User("Alex A.K","12kimutai")
        test_user.save_user()
        self.assertEqual(len(User.user_list),2)

class TestPasswordLockerCredentials(unittest.TestCase):
    def setUp(self):
        self.newCredentials = Credentials("Instagram","alex kimutai","password12345")

    def test_init(self):
        self.assertEqual(self.newCredentials.application_name,"Instagram")
        self.assertEqual(self.newCredentials.username,"alexkimutai")
        self.assertEqual(self.newCredentials.password,"password12345")

    def test_save_credentials(self):
        self.newCredentials.save_credentials()
        self.assertEqual(len(Credentials.credentials_list),2)

    def tearDown(self):
        User.user_list = []

    def test_save_multiple_credentials(self):
        self.newCredentials.save_credentials()
        test_credentials = Credentials("Twitter","@alexkimutai","12345karanu")
        test_credentials.save_credentials()
        self.assertEqual(len(Credentials.credentials_list),4)

    def test_display_credentials(self):
        self.assertEqual(Credentials.display_credentials(),Credentials.credentials_list)
    
    def test_delete_credentials(self):
        self.newCredentials.save_credentials()
        test_credentials = Credentials("Twitter","@alexkimutai","12345karanu")
        test_credentials.save_credentials()
        self.newCredentials.delete_credentials()
        self.assertEqual(len(Credentials.credentials_list),1)

if __name__ == '__main__':
    unittest.main()
