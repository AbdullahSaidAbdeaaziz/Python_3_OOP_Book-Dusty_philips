import auth

auth.authenticator.add_user("Abdullah", "unknown123")
auth.authorizar.add_permissions("Modify this code")
auth.authorizar.add_permissions("Execute this code")
auth.authorizar.permit_user("Modify this code", "Abdullah")


class Editor:
    def __init__(self):
        self.username = None
        self.menu_map = {
            "login": self.login,
            "modify": self.modify,
            "execute": self.execute,
            "quit": self.quit,
        }

    def login(self) -> None:
        logged_in = False
        while not logged_in:
            username = input("Enter username: ")
            password = input("Enter password: ")
            try:
                auth.authenticator.login(username, password)
            except (auth.InvaildUsername, auth.InvaildPassword):
                print("Sorry, username or password does not exist!")
            else:
                self.username = username
                logged_in = True

    def is_premitted(self, permission) -> bool:
        try:
            auth.authorizar.check_permit(permission, self.username)
        except auth.NotLoggedInError as e:
            print(f"{e.username} is not logged in")
            return False
        except auth.NotPermitError as e:
            print(f"{e.username} can not {permission}")
            return False
        else:
            return True

    def modify(self):
        if self.is_premitted("Modify this code"):
            print(f"{self.username} is Modifing code now.")

    def execute(self):
        if self.is_premitted("Execute this code"):
            print(f"{self.username} is Executingg this code now.")

    def quit(self):
        raise SystemExit()

    def menu(self):
        try:
            answer = ""
            while True:
                print("""
 Please enter a command:
 \tlogin\tLogin
 \tmodify\tModify this code
 \texecute\tExecute this code
 \tquit\tQuit
 """)
                answer = input("Enter a command: ").lower()
                try:
                    func = self.menu_map[answer]
                except KeyError:
                    print("{} is not a valid option".format(answer))
                else:
                    func()
        finally:
            print("Thank you for testing the auth module")


Editor().menu()
