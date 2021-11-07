import os
from app.connections import test_logger


def logFuntion(logtext):
    if os.environ["prodenv"]:
        test_logger.error(logtext)
    else:
        print(logtext)
