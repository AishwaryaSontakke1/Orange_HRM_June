import logging
import inspect
from pathlib import Path

class loggerClass:

    @staticmethod
    def getLogger():
        logger_name = inspect.stack()[1][3]
        logger = logging.getLogger(logger_name)

        # Best practice: dynamic, OS-independent log file path
        base_dir = Path(__file__).resolve().parent.parent
        log_file_path = base_dir / "Logs" / "automation.log"

        # Ensure Logs directory exists
       # log_file_path.parent.mkdir(parents=True, exist_ok=True)

        logfile = logging.FileHandler(log_file_path)
        log_format = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(funcName)s : %(lineno)s -->  %(message)s")
        logfile.setFormatter(log_format)

        logger.addHandler(logfile)
        logger.setLevel(logging.INFO)

        return logger
