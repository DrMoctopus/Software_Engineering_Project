import pandas as pd
import interface


class Client:
    def __init__(self, name, user_id, applications_df, approvals_df):
        self.__name = name
        self.__user_id = user_id
        self.__applications_df = applications_df
        self.__approvals_df = approvals_df

    def get_name(self):
        return self.__name

    def get_user_id(self):
        return self.__user_id

    def get_applications_df(self):
        return self.__applications_df

    def get_approvals_df(self):
        return self.__approvals_df

    def set_applications_df(self, applications_df):
        self.__applications_df = applications_df

    def main_menu(self):
        option = 0
        try:
            condition = True
            while condition is True:
                interface.sleep_and_clear_screen(1)
                print("Welcome, " + self.get_name() + "!")
                print("-------------------------------------------------------------------------------------------")
                print("1. Open an Application")
                print("2. View Previous Applications")
                print("3. View Approved Lines of Credit")
                print("4. Logout")
                print("-------------------------------------------------------------------------------------------")
                option = interface.get_input_with_prompt("Select your option: ")
                condition = int(option) < 1 or int(option) > 4
        except ValueError:
            print("Input is not valid. Please try again.")
            interface.sleep_and_clear_screen(1)
            self.main_menu()

        match option:
            case "1":
                self.new_application()
            case "2":
                self.previous_applications()
            case "3":
                self.approved_lines_of_credit()
            case "4":
                self.logout()

    def new_application(self):
        modified_df = pd.DataFrame({"Timestamp": [interface.get_pandas_timestamp()],
                                    "Name": [self.get_name()],
                                    "User ID": [self.get_user_id()],
                                    "SSN": [self.enter_ssn()],
                                    "Monthly Income": [self.enter_monthly_income()],
                                    "Monthly Debts": [self.enter_monthly_debts()],
                                    "Credit Score": -1,
                                    "Approval Status": "Pending",
                                    "Approved by ID": "System"})
        modified_df = pd.concat([self.get_applications_df(), modified_df], ignore_index=True)
        modified_df = modified_df.sort_values(by='Timestamp', ascending=False)
        modified_df = modified_df.reset_index(drop=True)
        self.set_applications_df(modified_df)
        interface.sleep_and_clear_screen(1)
        print("New Application for " + self.get_name())
        print("-------------------------------------------------------------------------------------------")
        input("Application finished. Press any key to return to the main menu.")
        self.main_menu()

    def enter_ssn(self):
        ssn = 0
        try:
            condition = False
            while condition is False:
                interface.sleep_and_clear_screen(1)
                print("New Application for " + self.get_name())
                print("-------------------------------------------------------------------------------------------")
                ssn = interface.get_input_with_prompt("Enter SSN (include hyphens): ")
                ssn = int(ssn)
                condition = interface.validate_ssn(ssn)
        except TypeError:
            print("Input is not valid. Please try again.")
            interface.sleep_and_clear_screen(1)
            self.enter_ssn()
        return ssn

    def enter_monthly_income(self):
        monthly_income = 0
        try:
            condition = False
            while condition is False:
                interface.sleep_and_clear_screen(1)
                print("New Application for " + self.get_name())
                print("-------------------------------------------------------------------------------------------")
                monthly_income = interface.get_input_with_prompt("Enter monthly income (no negative numbers): ")
                monthly_income = int(monthly_income)
                condition = monthly_income > 0
        except TypeError:
            print("Input is not valid. Please try again.")
            interface.sleep_and_clear_screen(1)
            self.enter_monthly_income()
        return monthly_income

    def enter_monthly_debts(self):
        monthly_debts = 0
        try:
            condition = False
            while condition is False:
                interface.sleep_and_clear_screen(1)
                print("New Application for " + self.get_name())
                print("-------------------------------------------------------------------------------------------")
                monthly_debts = interface.get_input_with_prompt("Enter monthly debts (no negative numbers): ")
                monthly_debts = int(monthly_debts)
                condition = monthly_debts > 0
        except TypeError:
            print("Input is not valid. Please try again.")
            interface.sleep_and_clear_screen(1)
            self.enter_monthly_debts()
        return monthly_debts

    def previous_applications(self):
        interface.sleep_and_clear_screen(1)
        print("Previously Completed Applications for " + self.get_name())
        print("-------------------------------------------------------------------------------------------")
        previous_applications = self.user_previous_applications()
        if previous_applications.empty is True:
            print("No previous applications have been completed.")
        else:
            print(previous_applications.to_string())
        print("-------------------------------------------------------------------------------------------")
        input("Press any key to return to the main menu.")
        self.main_menu()

    def user_previous_applications(self):
        filtered_df = self.get_applications_df()[self.get_applications_df()['User ID'] == self.get_user_id()]
        filtered_df = filtered_df.sort_values(by=['Timestamp'], ascending=False)
        filtered_df = filtered_df.reset_index(drop=True)
        return filtered_df

    def approved_lines_of_credit(self):
        interface.sleep_and_clear_screen(1)
        print("Approved Lines of Credit for " + self.get_name())
        print("-------------------------------------------------------------------------------------------")
        previous_lines_of_credit = self.user_approved_lines_of_credit()
        if previous_lines_of_credit.empty is True:
            print("No lines of credit have been approved.")
        else:
            print(previous_lines_of_credit.to_string())
        print("-------------------------------------------------------------------------------------------")
        input("Press any key to return to the main menu.")
        self.main_menu()

    def user_approved_lines_of_credit(self):
        filtered_df = self.get_approvals_df()[self.get_approvals_df()['User ID'] == self.get_user_id()]
        filtered_df = filtered_df.sort_values(by=['Timestamp'], ascending=False)
        filtered_df = filtered_df.reset_index(drop=True)
        return filtered_df

    def logout(self):
        interface.sleep_and_clear_screen(1)
        sorted_applications_df = self.get_applications_df().sort_values(by=['Timestamp'], ascending=False)
        sorted_applications_df = sorted_applications_df.reset_index(drop=True)
        sorted_applications_df.to_csv(interface.APPLICATIONS_FILEPATH, index=False)
        sorted_approvals_df = self.get_approvals_df().sort_values(by=['Timestamp'], ascending=False)
        sorted_approvals_df = sorted_approvals_df.reset_index(drop=True)
        sorted_approvals_df.to_csv(interface.APPROVALS_FILEPATH, index=False)
        print("Thank you for choosing us as your credit provider, " + self.get_name() + ". Have a great day!")