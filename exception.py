# exception 만 모아서 에러처리
class InvalidFormatException(Exception):
    def __init__(self, msg):
        self.msg = message

class DoesNotExistException(Exception):
    def __init__(self, msg):
        self.msg = message

class InvalidTransactionException(Exception):
    def __init__(self, msg):
        self.msg = message
