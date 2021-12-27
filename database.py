import sqlite3

class Database:
    def __init__(self):
        self.conn = sqlite3.connect("database.db")

    def get_account(self, pin_num):
        cur = self.conn.cursor()
        cur.execute(
                    """
                    select account_number from account where pin_num = ?
                    """, (pin_num,)
            )
        rows = cur.fetchall() # ex.pin_num=1234 에 대한 다수의 계좌가 있다고 가정 -> fetchall
        return rows
        
    def get_balance(self, account_number): # 고유 account_number 받음
        cur = self.conn.cursor()
        cur.execute(
                    """
                    SELECT * FROM account WHERE account_number = ?
                    """, (account_number)
            ) # 계좌 number 넣었을 때 해당 계좌에 대한 정보 보여줌
        balance = cur.fetchone()
        return balance

    def update_balance(self, account_number, new_amount):
        cur = self.conn.cursor()
        cur.execute(
                """
                UPDATE account 
                SET balance = ?
                """, (new_amount)
            )
        self.conn.commit()
        
    def transaction_history(self, cash):
        cur = self.conn.cursor()
        cur.execute(
                """
                SELECT history from account
                """, (cash)
            )
        history = cur.fetchone()
        return history

    def __del__(self):
        self.conn.close()

    