import os
from app.connections import test_logger


def logFunction(type, logtext, extralog = {}):
    if os.environ["PRODENV"].lower() == "true":
        getattr(test_logger, type)(logtext, extra=extralog)
    else:
        print("{0} : {1} {2}".format(type, logtext, extralog))
