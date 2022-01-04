# -*- coding: utf-8 -*-
import database
import exception


class AtmController:
    def __init__(self, input_pin, balance):
        self.balance = balance
 
    def check_pin(self, input_pin):
        if isinstance(input_pin, int) == True or len(str(input_pin)) == 4:
            return input_pin
        else:
            raise Exception("invalid format")

    # 1234, 12345, 12-34, 1-234, a1234 와 같은 종류의 핀번호를 어떻게 처리할 것인가?
    # 현재 코드는 오직 4자리 숫자만 처리할 수 있는 코드인데 어떻게 바꿀 수 있나 어떻게 열어둘거지?

    def check_account(self, input_pin):
        if self.input_pin != input_pin: # db의 input_pin과 param의 input_pin 값 비교
            raise Exception("can't find a pin number")
        else:
            account = self.get_account[pin_num]
            return account


    # 계정 선택과 계정 잔고 조회는 db와의 연결이 필요한 부분인데 어떻게 처리할 수 있을까
    # 어떤 db가 와도 다 통용될 수 있도록 하려면 어떻게 해야 할까?


# db = Database()
# a = AtmController(db)
# print(check_pin(input_pin))
# accounts = a.find_accounts(pin)

    def check_balance(self, account):
        if self.account != account:
            raise Exception("can't find account number")
        else:
            balance = self.get_balance[account]
            return balance

    # 예금, 출금 거래
    def deposit(self, cash):
        if cash <= 0:
            raise Exception("deposit cash must be bigger than zero")
        
        self.balance += cash
        return self.balance

    def withdraw(self, cash):
        if cash == 0 or cash >= self.balance:
            raise Exception("lack of balance")

        self.balance -= cash
        return self.balance


    # def __del__(self):
    #     pass

# my_bank = AtmController(100000)
# print(my_bank.check_pin('rrrr'))
# print(my_bank.check_account(1234, 1234, 123412341234))
# print(my_bank.check_balance(1234, 123412341234, 1000))
# print(my_bank.deposit(2000))


# 1. 내가 직접 error를 정의할 수 있는 것?

# 1-2. try-except 를 어느경우에 쓰고 어느경우에 안써야할까

# 2. 어떤 은행이 ORM을 사용한다면 이 Controller를 적용할 수 있을까?