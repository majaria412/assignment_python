# exception 만 모아서 에러처리
class InvalidValueException(Exception):
    def __init__(self):
        super().__init__()

class LackOfBalanceException(Exception):
    def __init__(self, msg):
        super().__init__(msg)

class InvalidTransactionException(Exception):
    def __init__(self, msg):
        super().__init__(msg)
