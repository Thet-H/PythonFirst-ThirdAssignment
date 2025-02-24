class MiniBank:
    mainUserInfo = {}

    def firstOption(self):
        option = int(input("-Press 1 to log in:__\n-Press 2 to register:__"))
        if option == 1:
            self.login()
        elif option == 2:
            self.register()

    def login(self):
        username = input("Enter username: ")
        password = int(input("Enter password: "))
        for user_id, user in self.mainUserInfo.items():
            if user["r_username"] == username and user["r_passcode"] == password:
                print("Login successful!")
                self.menu(user_id)
                return
        print("Invalid login details.")

    def register(self):
        username = input("Enter username: ")
        amount = int(input("Enter initial deposit amount:__ "))
        passcode = int(input("Enter passcode:__ "))
        passcode2 = int(input("Pls enter again passcode to confirm:__"))

        if (passcode == passcode2):
            id: int = self.CheckinguserCount()
            userInfoForm: dict = {id: {"r_username": username, "r_passcode": passcode, "amount": amount}}
            self.mainUserInfo.update(userInfoForm)
            print("### Success registor####\n\n")
            print(self.mainUserInfo)

    def CheckinguserCount(self):
        count = len(self.mainUserInfo)
        return count + 1

    def menu(self, user_id):
        while True:
            print("1. Transfer>>\n2. Withdraw>>\n3. Update>>\n4. Log out___")
            choice = int(input("Choose an option:__ "))
            if choice == 1:
                self.transfer(user_id)
            elif choice == 2:
                self.withdraw(user_id)
            elif choice == 3:
                self.update(user_id)
            elif choice == 4:
                print("Logging out...")
                break
            else:
                print("<<Try again.>>")

    def transfer(self, user_id):
        to_username = input("Enter recipient username:__ ")
        for id, user in self.mainUserInfo.items():
            if user["r_username"] == to_username:
                amount = int(input("Enter amount to transfer:__ "))
                if self.mainUserInfo[user_id]["amount"] >= amount:
                    self.mainUserInfo[user_id]["amount"] -= amount
                    self.mainUserInfo[id]["amount"] += amount
                    print(f"Transferred {amount} to {to_username},Current yours balance:__ {self.mainUserInfo[user_id]['amount']} ")
                    return
                else:
                    print("Insufficient money.")
                    return
        print("Recipient not found.")

    def withdraw(self, user_id):
        amount = int(input("Enter amount to withdraw:__ "))
        w_pwd=int(input("PLS,Enter your password to withdraw___"))

        if self.mainUserInfo[user_id]["r_passcode"] == w_pwd:
            print("You can withdraw__")
            if self.mainUserInfo[user_id]["amount"] >= amount:
                self.mainUserInfo[user_id]["amount"] -= amount
                print(f"Withdrew {amount} fom id={user_id}. Current yours balance :__ {self.mainUserInfo[user_id]['amount']}")
            else:
                print("Insufficient money!")
        else:
            print("Invalid password.Try again")

    def update(self, user_id):
        print("1. Update Username__\n2. Update Password__\n3. Update Balance__")
        choice = int(input("Select option to update:__ "))
        if choice == 1:
            new_username = input("Enter new username:__")
            self.mainUserInfo[user_id]["r_username"] = new_username
            print("Username updated___",new_username)
        elif choice == 2:
            new_passcode = int(input("Enter new password:__ "))
            self.mainUserInfo[user_id]["r_passcode"] = new_passcode
            print("Password updated____")
        elif choice == 3:
            new_balance = int(input("Enter new balance:__ "))
            self.mainUserInfo[user_id]["amount"] += new_balance
            print(f"Balance updated. New balance: {self.mainUserInfo[user_id]['amount']}")

        else:
            print("Invalid choice.")
        print(self.mainUserInfo)

if __name__ == "__main__":
    bank = MiniBank()
    while True:
        bank.firstOption()