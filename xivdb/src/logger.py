
import logger

class Logger(logger.Logger):
    def __init__(self):
        self.logFile: str = 'logs.log'
        