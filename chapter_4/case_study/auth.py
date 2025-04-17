from hashlib import sha256


class User:
    def __init__(self, name: str, password: str):
        self.name = name
        self.password = self.encrypt_password(password)
        self.__is_login = False

    @property
    def is_login(self) -> bool:
        return self.__is_login

    @is_login.setter
    def is_login(self, value: bool) -> None:
        self.__is_login = value

    def encrypt_password(self, password: str) -> str:
        hash_str = self.name + password
        hash_str = hash_str.encode("utf8")
        return sha256(hash_str).hexdigest()

    def check_password(self, _ps: str) -> bool:
        encrypted = self.encrypt_password(_ps)
        return self.password == encrypted


# define exceptions that will be happened


class AuthException(Exception):
    def __init__(self, username: str, user: User = None):
        super().__init__(self, username, user)
        self.username = username
        self.user = user


class UserAlreadyExist(AuthException):
    pass


class PasswordTooShort(AuthException):
    pass


class InvaildUsername(AuthException):
    pass


class InvaildPassword(AuthException):
    pass


class NotLoggedInError(AuthException):
    pass


class NotPermitError(AuthException):
    pass


class Authenticator:
    def __init__(self):
        self.users = {}

    def add_user(self, username: str, password: str) -> None:
        if username in self.users:
            raise UserAlreadyExist(username)
        if len(password) < 6:
            raise PasswordTooShort(username)

        self.users[username] = User(username, password)

    def login(self, username: str, password: str) -> bool:
        try:
            user: User = self.users[username]
        except KeyError:
            raise InvaildUsername(username)

        if not user.check_password(password):
            raise InvaildPassword(username, user)

        user.is_login = True
        return True

    def is_logged_in(self, username: str) -> bool:
        if username in self.users:
            return self.users[username].is_login
        return False


authenticator = Authenticator()

# ------------------------------ Authorizar ------------------------------


class PermissionError(Exception):
    pass


class Authorizar:
    def __init__(self, authenticator: Authenticator):
        self.authenticator = authenticator
        self.permissions = {}

    def add_permissions(self, prem_name: str) -> None:
        try:
            perm_set = self.permissions[prem_name]
        except KeyError:
            self.permissions[prem_name] = set()
        else:
            raise PermissionError(f"Permission Exist! {perm_set}")

    def permit_user(self, perm_name: str, username: str) -> None:
        try:
            perm_set = self.permissions[perm_name]
        except KeyError:
            raise PermissionError("Permission does not exist.")
        else:
            if username not in authenticator.users:
                raise InvaildUsername(username)
            perm_set.add(username)

    def check_permit(self, perm_name: str, username: str) -> bool:
        if not self.authenticator.is_logged_in(username):
            raise NotLoggedInError(username)

        try:
            perm_set = self.permissions[perm_name]
        except KeyError:
            raise PermissionError("Permission does nott exist.")
        else:
            if username not in perm_set:
                raise NotPermitError(username)
            else:
                return True


authorizar = Authorizar(authenticator)
