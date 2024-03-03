import logging
from colorlog import ColoredFormatter

# 创建一个logger
logger = logging.getLogger('example_logger')
logger.setLevel(logging.DEBUG)

# 创建一个handler，用于输出到控制台
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

# 创建一个带颜色的formatter
formatter = ColoredFormatter(
    "%(log_color)s%(asctime)s - %(levelname)s - %(message)s%(reset)s",
    datefmt=None,
    reset=True,
    log_colors={
        'DEBUG': 'cyan',
        'INFO': 'green',
        'WARNING': 'yellow',
        'ERROR': 'red',
        'CRITICAL': 'bold_red',
    },
    secondary_log_colors={},
    style='%'
)

# 设置handler的formatter
ch.setFormatter(formatter)

# 给logger添加handler
logger.addHandler(ch)

# 使用不同的级别输出日志
logger.debug('This is a debug message')
logger.info('This is an info message')
logger.warning('This is a warning message')
logger.error('This is an error message')
logger.critical('This is a critical message')
