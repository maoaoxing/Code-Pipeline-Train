# mylogger/logger_config.py
import logging
import sys


def logging_logger(
        logger_name='mylogger',
        level=logging.INFO,
        log_file=None
):
    """
    创建并返回一个自定义 logger。

    :param logger_name: Logger 名称
    :param level: 日志级别，如 logging.INFO, logging.DEBUG 等
    :param log_file: 日志文件路径（可选）。若不为 None，则输出到该文件
    :return: 返回配置好的 Logger 对象
    """
    # 1. 获取（或创建）Logger 对象
    logger = logging.getLogger(logger_name)
    # 避免重复添加 Handler（如果已经配置过 Logger，就不再重复添加）
    if logger.handlers:
        return logger

    # 2. 设置 Logger 日志级别
    logger.setLevel(level)

    # 3. 定义日志输出格式
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )

    # 4. 创建并添加控制台 Handler
    stream_handler = logging.StreamHandler(sys.stdout)
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)

    # 5. 如果指定了日志文件，则创建 FileHandler
    if log_file:
        file_handler = logging.FileHandler(log_file, encoding='utf-8')
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    return logger
