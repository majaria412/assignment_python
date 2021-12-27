# 1. 핀 번호 입력
# 2. 핀 번호 검증
# 3. 계정 선택
# 4. 계정 (입금, 출금) 잔고 조회
import database
from exception import *


class AtmController:
    def __init__(self):
        pass

    def check_pin_number(self, pin_num): # pin_num 입력 및 확인
        try:
            input_pin = int(input("XXXX format: "))

            if input_pin.isdecimal() == True and len(input_pin) == 4: # 숫자이고 4자리면 Ok
                print("valid_pin_number")
            else:
                raise DoesNotExistException("does not exist pin format")

        except PinNumberNotFoundException(f"{input_pin} is not found")

    def find_account(self, pin_num):
        db = Database()
        account = db.get_account(pin_num) # db에 있는 핀넘버에 맞는 계좌를 변수에 넣음

        if pin_num not in db.get_account(pin_num): # db에 핀넘버 없으면
            ✅ raise DoesNotExistException("does not exist pin number") #  오류 일으키기
        return account # 존재하면 -> 해당 계좌 출력

    def check_balance(self, account_number): # 계좌로 잔액만 조회
        db = Database()
        balance = db.get_balance_only(account_number)

        if  balance != None and account_number in balance:
            return balance

    def make_transaction(self, account_number, transaction_type, transaction_cash):
        # 예금 + 출금 했을 때, db 저장 후 잔금 반환
        try:
            db = Database()
            balance = db.get_balance(account_number)

            deposit = 1
            withdraw = 2

            if transaction_type == 1:
                if transaction_cash == 0:
                    raise 

                balance += transaction_cash
                db.update_balance(balance) # db 저장하고
                
                return balance

            elif transaction_type == 2:
                if transaction_cash > balance:
                    print("lack_of_balance")

                elif transaction_cash == 0:
                    print("invalid_transaction")

                balance -= transaction_cash
                db.update_balance(balance) # db 저장하고

                return balance

            else:
                raise InvalidTransactionException("invalid transaction access")

        ✅ except KeyError:
            print("invalid key error")
        
    def __del__(self):
        pass

# 1. print 문으로 invalid 오류를 나타내는 것 vs raise error 의 차이?
# 1-1. 예외처리(except - error:)와 에러일으키기(raise - exception) 차이?
# 2. table 2개 account / transaction -> history는 어떻게 보여줄수있지?
# 3. db 처리를 이렇게 하는게 맞을까?