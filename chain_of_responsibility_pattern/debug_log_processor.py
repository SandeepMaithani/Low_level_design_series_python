from chain_of_responsibility_pattern.log_processor import LogProcessor


class DebugLogProcessor(LogProcessor):
    def __init__(self, next_logger_processor) -> None:
        super().__init__(logger_processor=next_logger_processor)

    def log(self, log_level, log_message):
        if log_level == self.DEBUG:
            print(f"DEBUG: {log_message}")
        else:
            super().log(log_level=log_level, log_message=log_message)