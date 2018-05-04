import uuid
from src.common.database import Database
import src.models.users.errors as UserErrors
from src.common.utils import Utils


class User(object):
    def __init__(self, email, password, _id=None):
        self.email = email
        self.password = password
        self._id = uuid.uuid4().hex if _id is None else _id

    def __repr__(self):
        return "<User {}>".format(self.email)

    # Check if user/password is valid
    @staticmethod
    def is_login_vlaid(email, password):
        """
        This method verifies than an email/password combo (as sent by the site forms) is valid or not.
        Checks that the email exists, and that password associates to that email is correct.
        :param email: The user's email
        :param password: A sha512 hashed password
        :return: True if valid, False otherwise
        """

        user_data = Database.find_one("users", {"email": email}) # password in pbkdf2_sha512
        if user_data is None:
            # tell the user their email doesnt exists
            raise UserErrors.UserNotExistsError("Your user does not exist.")

        if not Utils.check_hashed_password(password, user_data['password']):
            # Tell the user the password doesnt match
            raise UserErrors.IncorrectPasswordError("Your password was wrong.")

        return True