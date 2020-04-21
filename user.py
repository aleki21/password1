class User:
    '''
    This class shall be used for the user's login information, 
    the username and their password. Credentials shall also be saved under a user's information
    '''
    user_list = [] #list to store our users
    def __init__(self,user_name,login_password):
        self.user_name = user_name
        self.login_password = login_password

    def save_user(self):
        User.user_list.append(self)

    def delete_user(self):
        User.user_list.remove()
    

    