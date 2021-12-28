# 1. 핀 번호 입력
# 2. 핀 번호 검증
# 3. 계정 선택
# 4. 계정 (입금, 출금) 잔고 조회

import database
from exception import DoesNotExistException, InvalidFormatException, InvalidTransactionException


class AtmController:
    def __init__(self):
        self.Bank = bank
        self.accounts = None

	# 핀 번호 검증
    def check_pin_number(self, pin_num): # pin_num 입력 및 확인
        try:
            input_pin = int(input("XXXX format: "))
            # 은행마다 다른 format을 "XX-XX" or "X-XXX", "X-X-X-X" 형태라면?
            # input_pin[2] == "-" and len(input_pin) == 5: 이런식으로.. 바꿀 수 있지 않을까?
            if input_pin.isdecimal() == True and len(input_pin) == 4: # 숫자이고 4자리면 Ok
                print("valid_pin_number")
            else:
                raise DoesNotExistException("does not exist pin format")

        except ValueError: # 연산이나 함수가 부적절한 값을 가진 객체에 적용 되었을 때 value error
            print(f"{input_pin} is not found")

	# 계정 선택
    def find_accounts(self, pin_num):
        db = Database()
        account = db.get_account(pin_num) # db에 있는 핀넘버에 맞는 계좌를 변수에 넣음

        if pin_num not in account: # db에 핀넘버 존재하지 않으면,
            raise DoesNotExistException("does not exist pin number") #  오류 일으키기
        return account # 존재하면 -> 해당 계좌 출력

	# 계정 잔고 조회
    def check_balance(self, account_number): # 계좌로 잔액만 조회
        db = Database()
        balance = db.get_balance(account_number)

        if  balance != None and account_number in balance:
            return balance
		
	# 입금, 출금
    def make_transaction(self, account_number, transaction_type, transaction_cash):
        # 예금 + 출금 했을 때, db 저장 후 잔금 반환
        try:
            # 정해진 값을 상수화 시켜주기
            # DEPOSIT = 1
            # WITHDRAW = 2

            if transaction_type == "deposit":
                if transaction_cash == 0:
                    raise exception

                balance += transaction_cash
                db.update_balance(balance) # db 저장하고
                
                return balance

            elif transaction_type == "withdraw":
                if transaction_cash > balance:
                    raise LackOfBalanceException("balance is insufficient")

                elif transaction_cash == 0:
                    print("invalid_transaction")
                
                balance -= transaction_cash
                db.update_balance(balance) # db 저장하고

                return balance

            else:
                raise InvalidTransactionException("invalid transaction access")

        ✅ except:
            print("")
        
    def __del__(self):
        pass

# 1. print 문으로 invalid 오류를 나타내는 것 vs raise error 의 차이?

# 1-1. 예외처리(except - error:)와 에러일으키기(raise - exception) 차이?
# raise error는 어물쩡 넘어갈 수 없도록 '무조건' error를 일으키게 하는 것.
# 내가 직접 error를 정의할 수 있는 것?

# 1-2. try-except 를 어느경우에 쓰고 어느경우에 안써야할까
# 1-3. except 에러는 정해진 것만 사용하고, raise exception은 내가 customizing할 수 있는걸까? 

# 2. table 2개 account / transaction -> history는 어떻게 보여줄수있지?

# 3. db 처리를 이렇게 하는게 맞을까? 
# 독립성 → 프레임워크와 데이터베이스로부터의 분리? 어떻게 할 수 있지?
# 4개의 메소드에 모두 디비를 끌고 들어오는데 이건 어떻게 되는걸까?

# 4. 어떤 은행이 ORM을 사용한다면 이 Controller를 적용할 수 있을까?

# 5. urls는 어떻게 처리해야할까?
