import os
from typing import Optional
from sqlalchemy import create_engine, Column, Integer, String, Text
from sqlalchemy.orm import sessionmaker, declarative_base
import datetime

from .sql_base import delete_db
from .utils import finish_ini_logger_sql_db

# 声明一个全局的 SQLAlchemy 基类，用于映射数据库表
Base = declarative_base()


class Log(Base):
    """
    日志记录表，用于存储模块日志信息。

    字段:
    - id: 自增主键
    - timestamp: 日志时间，精确到秒 (YYYY-MM-DD HH:MM:SS)
    - module_name: 模块或函数信息，如 'my_module.some_func'
    - log_level: 日志等级 (info, debug, warning 等)
    - log_content: 日志内容，可非常长，最大可达 4GB
    """
    __tablename__ = 'log_records'

    record_id = Column(Integer, primary_key=True, autoincrement=True, comment="自增主键")
    # 这里使用 String(19) 来存储 'YYYY-MM-DD HH:MM:SS' 格式的时间字符串
    timestamp = Column(String(19), nullable=False,
                       default=lambda: datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                       comment="日志时间，格式: YYYY-MM-DD HH:MM:SS")
    module_name = Column(String(255), nullable=False, comment="来源模块或函数名")
    log_level = Column(String(10), nullable=False, comment="日志等级: info, debug, warning")
    # 对于可容纳 4GB 的文本，MySQL 等数据库可映射为 LONGTEXT；在 SQLAlchemy 中用 Text 即可
    log_content = Column(Text, nullable=True, comment="日志内容，可非常长")

    def __repr__(self):
        return f"<LogRecord(id={self.id}, timestamp='{self.timestamp}', module='{self.module_name}', level='{self.log_level}')>"


class log_DB:
    def __init__(self, db_path: str = 'logs/app_log.db', forced_formatting: bool = False, echo: bool = False):
        """
        初始化数据库连接。如果 forced_formatting 为 True，或 INI_STATEMENT 为 False，
        则会先删除旧的数据库文件，再重新创建新表。

        :param db_path: SQLite 数据库文件路径
        :param forced_formatting: 是否强制删除已有数据库并重建
        :param echo: 是否打印 SQL 语句到控制台（调试用）
        """
        self.db_path = db_path
        self.forced_formatting = forced_formatting
        self.engine = None
        self.session = None
        # 如果未完成初始化 (INI_STATEMENT=False) 或强制重建，则删除旧库并创建新表
        from .constants import LOGGER_INI_STATEMENT
        if not LOGGER_INI_STATEMENT or forced_formatting:
            delete_db(db_path)
            self._create_and_bind_engine(echo)
            finish_ini_logger_sql_db()
        else:
            # 如果不需要初始化，检查是否已存在数据库文件，如果存在则绑定；否则给出警告
            if os.path.exists(db_path):
                self._create_and_bind_engine(echo)
            else:
                delete_db(db_path)
                self._create_and_bind_engine(echo)
                finish_ini_logger_sql_db()

    def _create_and_bind_engine(self, echo: bool):
        """
        内部方法：创建引擎、绑定元数据、创建表并初始化 session
        """
        self.engine = create_engine(f'sqlite:///{self.db_path}', echo=echo)
        Base.metadata.create_all(self.engine)

        Session = sessionmaker(bind=self.engine)
        self.session = Session()

    def add_log(self, module_name: str, log_level: str, log_content: str) -> None:
        """
        添加一条日志记录。
        """
        new_record = Log(module_name=module_name, log_level=log_level, log_content=log_content)
        self.session.add(new_record)
        self.session.commit()
