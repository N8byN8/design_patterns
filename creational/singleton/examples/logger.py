from abc import ABC, ABCMeta, abstractmethod
import logging
import threading

class SingletonMeta(metaclass=ABCMeta):
    _instances = {}
    _lock = threading.Lock()

    def __call__(cls, *args, **kwargs):
        with cls._lock:
            print('<SingletonMeta> in the _call_')
            if cls not in cls._instances:
                cls._instance = super().__call__(*args, **kwargs)
        return cls._instances[cls]
    
class BaseLogger(SingletonMeta):
    @abstractmethod
    def debug(cls, message: str):
        pass
    @abstractmethod
    def info(cls, message: str):
        pass
    @abstractmethod
    def warning(cls, message: str):
        pass
    @abstractmethod
    def error(cls, message: str):
        pass
    @abstractmethod
    def critical(cls, message: str):
        pass

class MyLogger(BaseLogger):

    def __init__(self):
        print('<Logger init> init logger...')
        self._logger = logging.getLogger('my_logger')
        self._logger.setLevel(logging.DEBUG)

        file_handler = logging.FileHandler('creational/singleton/examples/my_log_file.log')
        file_handler.setLevel(logging.DEBUG)

        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)

        formatter = logging.Formatter('%(asctime)s - %(filename)s - %(name)s - %(levelname)s - %(funcName)s - %(message)s')
        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)

        self._logger.addHandler(file_handler)
        self._logger.addHandler(console_handler)

    def debug(self, message: str):
        self._logger.debug(message)

    def info(self, message: str):
        self._logger.info(message)

    def warning(self, message: str):
        self._logger.warning(message)

    def error(self, message: str):
        self._logger.error(message)

    def critical(self, message: str):
        self._logger.critical(message)

if __name__ == "__main__":
    logger = MyLogger()
    logger.debug("This is debug")