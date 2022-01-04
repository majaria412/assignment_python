class Database:
    def __init__(self):
        pass

    def get_accounts(self, pin_num):
        return {pin_num: account}
    
    def get_balance(self, account):
        return {account: balance}
    
    def __del__(self):
        pass