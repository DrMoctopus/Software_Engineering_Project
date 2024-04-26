import administrator
import businessanalyst
import client
import interface

if __name__ == '__main__':

    users_df = interface.open_or_create_csv(interface.AUTHORIZED_USERS_FILEPATH, interface.AUTHORIZED_USERS_COLUMNS)
    credit_scores_df = interface.open_or_create_csv(interface.CREDIT_SCORES_FILEPATH, interface.CREDIT_SCORES_COLUMNS)
    thresholds_df = interface.open_or_create_csv(interface.THRESHOLDS_FILEPATH, interface.THRESHOLDS_COLUMNS)
    applications_df = interface.open_or_create_csv(interface.APPLICATIONS_FILEPATH, interface.APPLICATIONS_COLUMNS)
    approvals_df = interface.open_or_create_csv(interface.APPROVALS_FILEPATH, interface.APPROVALS_COLUMNS)
    name, user_id = interface.login_prompt(users_df)
    session_char = user_id[0]

    match session_char:
        case 'A':
            interface.sleep_and_clear_screen(1)
            session_admin = administrator.Administrator(name,
                                                        user_id,
                                                        applications_df,
                                                        approvals_df,
                                                        credit_scores_df,
                                                        thresholds_df,
                                                        users_df)
            session_admin.main_menu()
        case 'B':
            interface.sleep_and_clear_screen(1)
            session_employee = businessanalyst.BusinessAnalyst(name,
                                                               user_id,
                                                               applications_df,
                                                               approvals_df,
                                                               credit_scores_df,
                                                               thresholds_df)
            session_employee.main_menu()
        case 'C':
            interface.sleep_and_clear_screen(1)
            session_customer = client.Client(name,
                                             user_id,
                                             applications_df,
                                             approvals_df)
            session_customer.main_menu()
