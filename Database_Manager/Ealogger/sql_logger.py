from .sql_log import log_DB


class sql_logger:
    """一个sql日志对象"""
    def __init__(self, module_name: str):
        self.module_name = module_name
        self.logger = log_DB()

    def info(self, log_content: str = "未成功记录") -> None:
        self.logger.add_log(self.module_name, 'info', log_content)

    def debug(self, log_content: str) -> None:
        self.logger.add_log(self.module_name, 'debug', log_content)

    def warning(self, log_content: str) -> None:
        self.logger.add_log(self.module_name, 'warning', log_content)

    def error(self, log_content: str) -> None:
        self.logger.add_log(self.module_name, 'error', log_content)