from abc import ABC

class LogProcessor(ABC):

    INFO = 1
    DEBUG = 2
    ERROR = 3

    next_logger_processor = None

    def __init__(self, logger_processor) -> None:
        self.next_logger_processor = logger_processor


    def log(self, log_level, log_message):
        if self.next_logger_processor != None:
            self.next_logger_processor.log(log_level=log_level, log_message=log_message)
        else:
            print(f"Log level: {log_level} not defined.")
        