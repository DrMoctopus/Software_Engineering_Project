"""
Program: Credit Card Fraud Detection System
Group Members:
  - William Mock
  - Christian Tuarez
  - Valary Musibega
  - Thimothy Moorthy

Description:
  This program is a group project developed by the above-listed group members as part of a collaborative effort.
  The project aims to implement a credit card fraud detection system with real-time monitoring capabilities.
  The system is designed to analyze transactional data, identify fraudulent activities, and provide alerts for further investigation.

  Throughout the development process, the group members collaborated on various tasks, including data preprocessing, system design, implementation, and user interface development.

  This prologue serves as documentation for the project, providing an overview of the purpose, objectives, and contributors involved in its development.
"""

# User Class
class User:
    def __init__(self, user_id, username, password):
        self.user_id = user_id
        self.username = username
        self.password = password

    def get_user_id(self):
        return self.user_id

    def get_username(self):
        return self.username

    def get_password(self):
        return self.password

# Cardholder Class
class Cardholder:
    def __init__(self, cardholder_id, name):
        self.cardholder_id = cardholder_id
        self.name = name
        self.balance = 0.0

    def get_cardholder_id(self):
        return self.cardholder_id

    def get_name(self):
        return self.name

    def get_balance(self):
        return self.balance

# UserInterface Class
class UserInterface:
    def request_view_blocklist(self):
        blocklist = BlocklistClass.fetch_blocklist()
        self.display_blocklist(blocklist)

    def display_blocklist(self, blocklist):
        for entry in blocklist:
            print(f"Entry: {entry}")

    def submit_addition(self, entry_data):
        confirmation = BlocklistClass.add_entry(entry_data)
        self.display_confirmation(confirmation)

    def display_confirmation(self, confirmation):
        print(confirmation)

    def request_removal(self, entry_id):
        confirmation = BlocklistClass.remove_entry(entry_id)
        self.display_confirmation(confirmation)

    def request_transactional_data(self, transaction_id):
        data = TransactionClass.fetch_transactional_data(transaction_id)
        self.display_data(data)

    def display_data(self, data):
        print(data)

    def request_page_refresh(self):
        updated_data = TransactionClass.fetch_updated_transactional_data()
        self.display_updated_data(updated_data)

    def display_updated_data(self, updated_data):
        print(updated_data)

    def initiate_training(self):
        training_status = FraudDetectionClass.train_model()
        self.display_training_status(training_status)

    def display_training_status(self, training_status):
        print(training_status)

# BlocklistClass
class BlocklistClass:
    blocklist = []

    @classmethod
    def fetch_blocklist(cls):
        return cls.blocklist

    @classmethod
    def add_entry(cls, entry_data):
        cls.blocklist.append(entry_data)
        return "Entry added successfully."

    @classmethod
    def remove_entry(cls, entry_id):
        for entry in cls.blocklist:
            if entry.id == entry_id:
                cls.blocklist.remove(entry)
                return "Entry removed successfully."
        return "Entry not found."

# TransactionClass
class TransactionClass:
    transactions = []

    @classmethod
    def fetch_transactional_data(cls, transaction_id):
        for transaction in cls.transactions:
            if transaction.transaction_id == transaction_id:
                return transaction
        return "Transaction not found."

    @classmethod
    def fetch_updated_transactional_data(cls):
        # Fetch and return the updated transactional data
        # Implementation missing
        return "Updated transactional data not available."

# FraudDetectionClass
class FraudDetectionClass:
    model = None

    @classmethod
    def train_model(cls):
        # Train the fraud detection model
        # Implementation missing
        cls.model = FraudPredictionModel()
        return "Model training completed."

# FraudPredictionModel
class FraudPredictionModel:
    def __init__(self, model_id, model_name):
        self.model_id = model_id
        self.model_name = model_name

    def get_model_id(self):
        return self.model_id

    def get_model_name(self):
        return self.model_name

    def predict_fraud(self, transaction):
        # Fraud prediction implementation missing
        return False

# Main program
if __name__ == "__main__":
    user_interface = UserInterface()
    # Call the desired methods from the UserInterface class
    # For example:
    user_interface.request_view_blocklist()
    user_interface.submit_addition("Entry data")
    user_interface.request_removal("Entry ID")
    user_interface.request_transactional_data("Transaction ID")
    user_interface.request_page_refresh()
    user_interface.initiate_training()