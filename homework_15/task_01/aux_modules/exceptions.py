import sys


class MyBaseException(Exception):
    def __init__(self, string):
        self.str = string
        exc_type, exc_obj, exc_tb = sys.exc_info()
        self.error_line = exc_tb.tb_lineno
        """Параметр содержащий в себе имя файла из которого вызвалось исключение"""
        self.file_name = exc_tb.tb_frame.f_code.co_filename.split("\\")[-1]
        super().__init__(self.str)


class NegativeValueError(MyBaseException):
    pass


class DuplicateNameError(MyBaseException):
    pass


class NonExistentInstanceException(MyBaseException):
    pass


class NonExistentPathException(MyBaseException):
    pass


class JsonFileNotFoundError(MyBaseException):
    pass

class NotIntValueError(MyBaseException):
    pass