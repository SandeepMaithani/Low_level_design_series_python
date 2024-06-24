
from chain_of_responsibility_pattern.debug_log_processor import DebugLogProcessor
from chain_of_responsibility_pattern.error_log_processor import ErrorLogProcessor
from chain_of_responsibility_pattern.info_log_processor import InfoLogProcessor
from chain_of_responsibility_pattern.log_processor import LogProcessor


if __name__ == "__main__":

    logger_instance = InfoLogProcessor(
        next_logger_processor=DebugLogProcessor(
            next_logger_processor=ErrorLogProcessor(
                next_logger_processor=None
            )
        )
    )

    logger_instance.log(log_level=LogProcessor.ERROR, log_message="Exception occured while performing operation.")
    logger_instance.log(log_level=LogProcessor.DEBUG, log_message="Adding extra checks for debugging.")
    logger_instance.log(log_level=LogProcessor.INFO, log_message="Logging info for future reference.")
    
    # case which cannot be handle by any handler
    logger_instance.log(log_level=5, log_message="Unknown log level and message.")