import logging, os
from logging.handlers import RotatingFileHandler

def setup_logging():
    if not os.path.exists("logs"):
        os.makedirs("logs")

    f = os.path.join("logs", "app.log")
    fmt = "%(asctime)s | %(levelname)s | %(message)s"
    
    logging.basicConfig(
        level=logging.INFO,
        format=fmt,
        handlers=[
            RotatingFileHandler(f, maxBytes=5*1024*1024, backupCount=3),
            logging.StreamHandler()
        ]
    )
    return logging.getLogger("trading_bot")
