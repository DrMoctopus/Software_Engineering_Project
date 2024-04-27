import pandas as pd
import interface
from CreditApplication.businessanalyst import BusinessAnalyst


class Administrator(BusinessAnalyst):
    def __init__(self, name, user_id, applications_df, approvals_df, credit_scores_df, thresholds_df, users_df):
        super().__init__(name, user_id, applications_df, approvals_df, credit_scores_df, thresholds_df)
        self.__users_df = users_df

    def get_users_df(self):
        return self.__users_df

    def set_thresholds_df(self, thresholds_df):
        self.__thresholds_df = thresholds_df

    def set_users_df(self, users_df):
        self.__users_df = users_df

    def main_menu(self):
        option = 0
        try:
            condition = True
            while condition is True:
                interface.sleep_and_clear_screen(1)
                print("Main Menu (Session ID " + self.get_user_id() + ")")
                print("-------------------------------------------------------------------------------------------")
                print("1. View Pending Applications")
                print("2. View Line of Credit Approvals")
                print("3. View Users")
                print("4. Modify Approval Thresholds")
                print("5. Logout")
                print("-------------------------------------------------------------------------------------------")
                option = interface.get_input_with_prompt("Select your option: ")
                condition = int(option) < 1 or int(option) > 5
        except ValueError:
            print("Input is not valid. Please try again.")
            interface.sleep_and_clear_screen(1)
            self.main_menu()

        match option:
            case "1":
                self.view_applications()
            case "2":
                self.view_approvals()
            case "3":
                self.view_users()
            case "4":
                self.modify_thresholds()
            case "5":
                self.logout()

    def view_users(self):
        option = 0
        try:
            condition = True
            while condition:
                interface.sleep_and_clear_screen(1)
                print("Users (Session ID " + self.get_user_id() + ")")
                print("-------------------------------------------------------------------------------------------")
                users_list_df = self.sort_users_df()
                if users_list_df.empty is True:
                    print("No users found. Please create an Administrator user before logging off.")
                else:
                    print(users_list_df.to_string())
                print("-------------------------------------------------------------------------------------------")
                print("1. Add User")
                print("2. Remove User")
                print("3. Back")
                print("-------------------------------------------------------------------------------------------")
                print("If you add a new user with a user ID matching an existing ID, the old user will be swapped.")
                option = interface.get_input_with_prompt("Select your option: ")
                condition = int(option) < 1 or int(option) > 3
        except ValueError:
            print("Input is not valid. Please try again.")
            interface.sleep_and_clear_screen(1)
            self.view_users()

        match option:
            case "1":
                self.add_user()
            case "2":
                self.remove_user()
            case "3":
                self.main_menu()

    def add_user(self):
        modified_df = pd.DataFrame({"User ID": [self.enter_user_id()],
                                    "Name": [self.enter_name()],
                                    "Password": [self.enter_password()]})
        if modified_df['User ID'].iloc[0] in self.get_users_df()['User ID'].values:
            old_df = self.get_users_df()
            old_df = old_df[old_df['User ID'] != modified_df['User ID'].iloc[0]]
            old_df = pd.concat([old_df, modified_df], ignore_index=True)
            modified_df = old_df
        else:
            modified_df = pd.concat([self.get_users_df(), modified_df], ignore_index=True)
        modified_df = modified_df.sort_values(by='User ID').reset_index(drop=True)
        self.set_users_df(modified_df)
        interface.sleep_and_clear_screen(1)
        print("New User (Session ID " + self.get_user_id() + ")")
        print("-------------------------------------------------------------------------------------------")
        input("New user created. Press any key to return to the users menu.")
        self.view_users()

    def enter_user_id(self):
        user_id = ""
        try:
            condition = False
            while condition is False:
                interface.sleep_and_clear_screen(1)
                print("New User (Session ID " + self.get_user_id() + ")")
                print("-------------------------------------------------------------------------------------------")
                user_id = interface.get_input_with_prompt("Enter user ID (valid character plus 4 numbers): ")
                user_id = str(user_id)
                condition = len(user_id) == 6 and interface.validate_user_id(user_id)
        except TypeError:
            print("Input is not valid. Please try again.")
            interface.sleep_and_clear_screen(1)
            self.enter_user_id()
        return user_id

    def enter_name(self):
        name = ""
        try:
            condition = False
            while condition is False:
                interface.sleep_and_clear_screen(1)
                print("New User (Session ID " + self.get_user_id() + ")")
                print("-------------------------------------------------------------------------------------------")
                name = interface.get_input_with_prompt("Enter name (one name, one last name): ")
                name = str(name)
                condition = len(name) >= 8 and interface.validate_name(name)
        except TypeError:
            print("Input is not valid. Please try again.")
            interface.sleep_and_clear_screen(1)
            self.enter_user_id()
        return name

    def enter_password(self):
        password = ""
        try:
            condition = False
            while condition is False:
                interface.sleep_and_clear_screen(1)
                print("New User (Session ID " + self.get_user_id() + ")")
                print("-------------------------------------------------------------------------------------------")
                password = interface.get_input_with_prompt("Enter password (eight characters minimum): ")
                password = str(password)
                condition = len(password) >= 8
        except TypeError:
            print("Input is not valid. Please try again.")
            interface.sleep_and_clear_screen(1)
            self.enter_password()
        return password

    def remove_user(self):
        option = 0
        sorted_users_df = self.sort_users_df()
        df_len = len(sorted_users_df)
        try:
            condition = True
            while condition:
                interface.sleep_and_clear_screen(1)
                print("Users:")
                print("-------------------------------------------------------------------------------------------")
                if sorted_users_df.empty is True:
                    print("No users in the database.")
                else:
                    print(sorted_users_df.to_string())
                    print("-------------------------------------------------------------------------------------------")
                    option = interface.get_input_with_prompt("Select the index for the user you would like to remove: ")
                    option = int(option)  # MUST ALWAYS DO, OTHERWISE DATAFRAME.DROP() DOES NOT KNOW IT IS AN INT
                    condition = option < 0 or option > (df_len - 1)
        except ValueError:
            print("Input is not valid. Please try again.")
        print("-------------------------------------------------------------------------------------------")
        input("Press any key to return to the users menu.")
        sorted_users_df = sorted_users_df.drop(sorted_users_df.index[option])
        self.set_users_df(sorted_users_df)
        self.view_users()

    def sort_users_df(self):
        sorted_users_df = self.get_users_df().sort_values(by=['User ID'])
        sorted_users_df = sorted_users_df.reset_index(drop=True)
        return sorted_users_df

    def modify_thresholds(self):
        option = 0
        try:
            condition = True
            while condition:
                interface.sleep_and_clear_screen(1)
                print("Thresholds (Session ID " + self.get_user_id() + ")")
                print("-------------------------------------------------------------------------------------------")
                print(self.get_thresholds_df().to_string())
                print("-------------------------------------------------------------------------------------------")
                print("1. Modify Credit Score Automatic Rejection Threshold (CSART)")
                print("2. Modify Debt to Income Ratio Threshold (DtIRT)")
                print("3. Modify Positive Flow Ratio Limit for Credit (PFRLfC)")
                print("4. Modify Maximum Credit Limit (MCL)")
                print("5. Back")
                print("-------------------------------------------------------------------------------------------")
                option = interface.get_input_with_prompt("Select your option: ")
                condition = int(option) < 1 or int(option) > 5
        except ValueError:
            print("Input is not valid. Please try again.")
            self.modify_thresholds()

        match option:
            case "1":
                self.modify_credit_score_automatic_rejection()
            case "2":
                self.modify_debt_to_income_ratio_rejection()
            case "3":
                self.modify_positive_flow_ratio_limit()
            case "4":
                self.modify_maximum_credit_limit()
            case "5":
                self.main_menu()

    def modify_credit_score_automatic_rejection(self):
        value = 0
        try:
            condition = False
            while condition is False:
                interface.sleep_and_clear_screen(1)
                print("Modify Credit Score Automatic Rejection (CSART) (Session ID " + self.get_user_id() + ")")
                print("-------------------------------------------------------------------------------------------")
                value = interface.get_input_with_prompt("Enter a value from 350 to 850: ")
                print("-------------------------------------------------------------------------------------------")
                value = int(value)
                condition = 350 <= value <= 850
        except TypeError:
            print("Input is not valid. Please try again.")
            interface.sleep_and_clear_screen(1)
            self.modify_credit_score_automatic_rejection()
        input("Press any key to return to the threshold menu.")
        modified_df = self.get_thresholds_df()
        modified_df['CSART'] = value
        self.set_thresholds_df(modified_df)
        self.modify_thresholds()

    def modify_debt_to_income_ratio_rejection(self):
        value = 0
        try:
            condition = False
            while condition is False:
                interface.sleep_and_clear_screen(1)
                print("Modify Debt to Income Ratio Threshold (DtIRT) (Session ID " + self.get_user_id() + ")")
                print("-------------------------------------------------------------------------------------------")
                value = interface.get_input_with_prompt("Enter a positive value up to 1.00: ")
                print("-------------------------------------------------------------------------------------------")
                value = float(value)
                condition = 0 < value <= 1.00
        except TypeError:
            print("Input is not valid. Please try again.")
            interface.sleep_and_clear_screen(1)
            self.modify_debt_to_income_ratio_rejection()
        input("Press any key to return to the threshold menu.")
        modified_df = self.get_thresholds_df()
        modified_df['DtIRT'] = value
        self.set_thresholds_df(modified_df)
        self.modify_thresholds()

    def modify_positive_flow_ratio_limit(self):
        value = 0
        try:
            condition = False
            while condition is False:
                interface.sleep_and_clear_screen(1)
                print("Modify Positive Flow Ratio Limit for Credit (PFRLfC) (Session ID " + self.get_user_id() + ")")
                print("-------------------------------------------------------------------------------------------")
                value = interface.get_input_with_prompt("Enter a positive value up to 1.00: ")
                print("-------------------------------------------------------------------------------------------")
                value = float(value)
                condition = 0 < value <= 1.00
        except TypeError:
            print("Input is not valid. Please try again.")
            interface.sleep_and_clear_screen(1)
            self.modify_positive_flow_ratio_limit()
        input("Press any key to return to the threshold menu.")
        modified_df = self.get_thresholds_df()
        modified_df['PFRLfC'] = value
        self.set_thresholds_df(modified_df)
        self.modify_thresholds()

    def modify_maximum_credit_limit(self):
        value = 0
        try:
            condition = False
            while condition is False:
                interface.sleep_and_clear_screen(1)
                print("Modify Maximum Credit Limit (MCL) (Session ID " + self.get_user_id() + ")")
                print("-------------------------------------------------------------------------------------------")
                value = interface.get_input_with_prompt("Enter a positive value: ")
                print("-------------------------------------------------------------------------------------------")
                value = int(value)
                condition = value > 0
        except TypeError:
            print("Input is not valid. Please try again.")
            interface.sleep_and_clear_screen(1)
            self.modify_maximum_credit_limit()
        input("Press any key to return to the threshold menu.")
        modified_df = self.get_thresholds_df()
        modified_df['MCL'] = value
        self.set_thresholds_df(modified_df)
        self.modify_thresholds()

    def logout(self):
        interface.sleep_and_clear_screen(1)
        self.get_applications_df().to_csv(interface.APPLICATIONS_FILEPATH, index=False)
        self.get_approvals_df().to_csv(interface.APPROVALS_FILEPATH, index=False)
        self.get_thresholds_df().to_csv(interface.THRESHOLDS_FILEPATH, index=False)
        self.get_users_df().to_csv(interface.AUTHORIZED_USERS_FILEPATH, index=False)
        print("Session finished for ID " + self.get_user_id() + ".")
