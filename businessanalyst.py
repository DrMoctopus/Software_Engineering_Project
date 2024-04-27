import pandas as pd
import interface


class BusinessAnalyst:
    def __init__(self, name, user_id, applications_df, approvals_df, credit_scores_df, thresholds_df):
        self.__name = name
        self.__user_id = user_id
        self.__applications_df = applications_df
        self.__approvals_df = approvals_df
        self.__credit_scores_df = credit_scores_df
        self.__thresholds_df = thresholds_df

    def get_name(self):
        return self.__name

    def get_user_id(self):
        return self.__user_id

    def get_applications_df(self):
        return self.__applications_df

    def get_approvals_df(self):
        return self.__approvals_df

    def get_credit_scores_df(self):
        return self.__credit_scores_df

    def get_thresholds_df(self):
        return self.__thresholds_df

    def set_applications_df(self, applications_df):
        self.__applications_df = applications_df

    def set_approvals_df(self, approvals_df):
        self.__approvals_df = approvals_df

    def main_menu(self):
        print("TODO")

    def view_applications(self):
        print(self.get_user_id())

    def view_approvals(self):
        print(self.get_user_id())

    def logout(self):
        interface.sleep_and_clear_screen(1)
        '''''''''''
        self.get_applications_df().to_csv(interface.APPLICATIONS_FILEPATH, index=False)
        self.get_approvals_df().to_csv(interface.APPROVALS_FILEPATH, index=False)
        self.get_thresholds_df().to_csv(interface.THRESHOLDS_FILEPATH, index=False)
        '''''''''''
        print("Session finished for ID " + self.get_user_id() + ".")
