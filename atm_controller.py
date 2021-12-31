# -*- coding: utf-8 -*-
import re
import exception


class AtmController:
    def __init__(self, pin_num, account):
        # self.bank_data = {"pin_num":pin_num, "account":account}
        self.bank_data = {"pin_num":pin_num, "account":[(account), (account+1), (account+2)]}
        # self.account = [{"account":account}, {"account1":account + 1}, {"account2":account +2}]

    # 핀 넘버 형식 확인
    def check_pin_format(self):
        input_pin = input("format('XXXX'): ")
        
        if input_pin == '':
            raise Exception("it can't allow null value")

        if  len(input_pin) != 4:
            raise Exception("it has to be 4-digit number")

        pin_validation = re.compile('[a-zA-Zㄱ-힣\^\[\]\$\(\)\|\*\+\?\{\}\]\₩\~\!\@\+\#\%\&\/\'\".\,\=\-\_+]')
        if pin_validation.search(input_pin):
            raise Exception("it's incorrect pin format")

        input_pin = int(input_pin)
        if isinstance(input_pin, int) == True:
            return True    
        
    # 핀 넘버로 계좌 조회
    def check_account(self, pin_num, entered_pin, account):
        if self.bank_data['pin_num'] != entered_pin:
            raise Exception("can't find pin number")

        return self.bank_data['account'][0]

    # 핀 넘버가 존재하면, 계좌로 잔액 조회
    def check_balance(self, pin_num, account, balance):
        if pin_num != self.bank_data['pin_num']:
            raise Exception("can't find pin number")

        if account != self.bank_data['account'][0]:
            raise Exception("can't find account number")

        self.bank_data = {"pin_num":pin_num, "account":{account:balance}}
        return self.bank_data['account']

    # 예금, 출금 거래
    def make_transaction(self, pin_num, account, transaction_type, cash):
        DEPOSIT = 1
        WITHDRAW = 2
        BALANCE = 100000

        if transaction_type != 1 and transaction_type != 2:
            raise Exception(("no exist transaction_type"))

        self.bank_data = {"pin_num":pin_num, "account":[(account), (account+1), (account+2)]}
        
        if account != self.bank_data['account'][0]:
            raise Exception("does not exist account number")

        self.bank_data['account'] = {account:BALANCE}

        if transaction_type == 1:
            if cash == 0:
                raise Exception("invalid access")

            BALANCE += cash
            return BALANCE
 
        if transaction_type == 2:
            if cash == 0 or cash >= BALANCE:
                raise Exception("invalid access")

            BALANCE -= cash
            return BALANCE

    def __del__(self):
        pass

my_bank = AtmController(1234, 123412341234)
print(my_bank.check_pin_format())
print(my_bank.check_account(1234, 1234, 123412341234))
print(my_bank.check_balance(1234, 123412341234, 1000))
print(my_bank.make_transaction(1234, 123412341234, 1, 120))



# 1. 내가 직접 error를 정의할 수 있는 것?

# 1-2. try-except 를 어느경우에 쓰고 어느경우에 안써야할까

# 2. 어떤 은행이 ORM을 사용한다면 이 Controller를 적용할 수 있을까?

