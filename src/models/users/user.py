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


    @staticmethod
    def register_user(email, password):
        """
        This method registers user using email and password
        The password already commes hashed as sha-512
        :param email: user's email (might be invalid)
        :param password: sha512-hashed password
        :return: True if registered successfully, or False otherwise (exceptions can also be raised)
        """
        user_data = Database.find_one("users", {"email": email})

        if user_data is not None:
            # tell the user they are already registered
            raise UserErrors.UserAlreadyRegisteredError("The e-mail you used to register already exists.")
        if not Utils.email_is_valid(email):
            #Tell the user their email is not constructed properly
            raise UserErrors.InvalidEmailError("The e-mail does not have the right form.")

        User(email, Utils.hash_password(password)).save_to_db()

        return True

    def save_to_db(self):
        Database.insert("users", self.json())

    def json(self):
        return {
            "_id": self._id,
            "email": self.email,
            "password": self.password
        }