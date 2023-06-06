from django.contrib.auth import get_user_model
UserModel = get_user_model()

def authenticate(username=None, password=None):
        """
        Overrides the authenticate method to allow users to log in using their email address.
        """
        try:
            user = UserModel.objects.using("speech-dev").get(email=username)
            if user.check_password(password):
                return user
            return None
        except:
            return None