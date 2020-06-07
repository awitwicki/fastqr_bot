def init_logger():
    import logging

    logger = logging.getLogger("bot_logger")
    logger.setLevel(logging.DEBUG)
    file_handler = logging.FileHandler('log.txt', 'a', 'utf-8')
    file_handler.setLevel(logging.DEBUG)

    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)

    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')
    console_formatter = logging.Formatter('%(message)s')
    error_file_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(module)s - %(funcName)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(console_formatter)

    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    return logger

logger = init_logger()
