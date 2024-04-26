import pandas as pd
from datetime import datetime
from time import sleep
import sys
import subprocess
import re

AUTHORIZED_USERS_FILEPATH = "authorized_users.csv"
CREDIT_SCORES_FILEPATH = "credit_scores.csv"
THRESHOLDS_FILEPATH = "thresholds.csv"
APPLICATIONS_FILEPATH = "applications.csv"
APPROVALS_FILEPATH = "approvals.csv"

AUTHORIZED_USERS_COLUMNS = ["User ID",
                            "Name",
                            "Password"]
CREDIT_SCORES_COLUMNS = ["SSN",
                         "Credit Score"]
THRESHOLDS_COLUMNS = ["CSART",
                      "DtIRT",
                      "PFRLfC",
                      "MCL"]
APPLICATIONS_COLUMNS = ["Timestamp",
                        "Name",
                        "User ID",
                        "SSN",
                        "Monthly Income",
                        "Monthly Debts",
                        "Credit Score",
                        "Approval Status",
                        "Approved by ID"]
APPROVALS_COLUMNS = ["Timestamp",
                     "User ID",
                     "Credit Line Limit"]


def get_input_with_prompt(prompt):
    print(prompt, end="")
    return input()


def sleep_and_clear_screen(secs=1):
    sleep(secs)
    operating_system = sys.platform
    if operating_system == 'win32':
        subprocess.run('cls', shell=True)
    elif operating_system == 'linux' or operating_system == 'darwin':
        subprocess.run('clear', shell=True)


def get_pandas_timestamp():
    current_datetime = datetime.now()
    current_datetime = current_datetime.strftime('%Y-%m-%d %H:%M:%S')
    timestamp = pd.Timestamp(current_datetime)
    return timestamp


def open_or_create_csv(filepath, column_names):
    try:
        df = pd.read_csv(filepath)
    except FileNotFoundError:
        df = pd.DataFrame(columns=column_names)
        df.to_csv(filepath, index=False)
    return df


def validate_login(df, user_id, password):
    try:
        filtered_df = df[df['User ID'] == user_id]
        if len(filtered_df) == 1 and filtered_df['Password'].values[0] == password:
            return True
        else:
            print("\nIncorrect login information!")
            return False
    except KeyError:
        print("Error: Username or password column not found in DataFrame.")
        return False


def login_prompt(users_list_df):
    sleep_and_clear_screen(1)
    print("Welcome to the system! Please insert your credentials below.\n")
    user_id = get_input_with_prompt("Enter your user ID: ")
    password = get_input_with_prompt("Enter your password: ")

    while validate_login(users_list_df, user_id, password) is False:
        print("Login failed.")
        sleep_and_clear_screen(1)
        print("Welcome to the system! Please insert your credentials below.\n")
        user_id = get_input_with_prompt("Enter your user ID: ")
        password = get_input_with_prompt("Enter your password: ")

    filtered_df = users_list_df[users_list_df['User ID'] == user_id]
    name = filtered_df['Name'].values[0]
    filtered_df = users_list_df[users_list_df['User ID'] == user_id]
    print(f"\nLogin successful! Welcome, {name}!")
    return name, user_id


def validate_ssn(ssn):
    pattern = r'^\d{3}-\d{2}-\d{4}$'
    if re.match(pattern, ssn):
        return True
    else:
        return False


def validate_user_id(user_id):
    pattern = r'^[A-C][0-9]{5}$'
    if re.match(pattern, user_id):
        return True
    else:
        return False


def validate_name(name):
    pattern = r'^[A-Z][a-z]+ [A-Z][a-z]+$'
    if re.match(pattern, name):
        return True
    else:
        return False
