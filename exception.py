class Exception(Exception):
    def __init__(self, msg):
        super().__init__(msg)

InvalidFormatException("does not exist pin format")
