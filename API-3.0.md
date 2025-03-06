# 数据库日志系统 API 文档

## 1. 概述
数据库日志系统用于记录和查询应用程序的日志信息，支持两种日志方式：
- `logging_logger`：基于 Python `logging` 模块的传统日志
- `sql_logger`：基于 SQLite 数据库的日志存储
- `sql_logger`记录实践日志，`logging_logger`作为补充防止日志疏漏，保障日志的完善性。

## 2. `Ealogger`的使用
-	`__inti__`:初始化`Ealogger`模块，并明确暴露两个日志记录方法，外部模块可以直接通过以下内容进行调用，而不需要知道其具体文件结构。
```bash
from package import logging_logger, sql_logger 
```

### 2.1 logging.logger模块
```bash
logging.logger(logger_name:str,level:int,log_file:str or None)
```

创建并返回一个自定义 logger。

参数:
-  `logger_name`: Logger 名称，默认值：'mylogger'
-  `level`: 日志级别，如logging. INFO, logging. DEBUG 等，默认值：logging. INFO
-  `log_file`: 日志文件路径（可选）。若不为 None，则输出到该文件，默认值：None

返回值:
-  返回配置好的 Logger 对象

#### 2.1.1 获取（或创建）`Logger` 对象
```bash
logger = logging.getLogger(logger_name=None) 
```
避免重复创建同名`Logger`
```bash
if logger.handlers:
    return logger
```
避免重复添加 Handler（如果已经配置过 Logger，就不再重复添加）

#### 2.1.2 设置 Logger 日志级别

```bash
logger.setLevel(level=int or str) 
```
-	logging.DEBUG（调试日志）
-	logging.INFO（信息日志）
-	logging.WARNING（警告日志）
-	logging.ERROR（错误日志）
-	logging.CRITICAL（严重错误）

#### 2.1.3 定义日志输出格式
```bash
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
```

占位符说明:
- **%(asctime)s**: 时间戳
- **%(name)s**: Logger名称
- **%(levelname)s**: 日志级别
- **%(message)s**: 日志内容

#### 2.1.4 创建并添加控制台 Handler
```bash
stream_handler = logging.StreamHandler(sys.stdout)
stream_handler.setFormatter(formatter)
logger.addHandler(stream_handler)
```

-	**StreamHandler(sys.stdout)**：让日志输出到控制台。
-	**setFormatter(formatter)**：设置日志格式。
-	**addHandler(stream_handler)**：将 Handler 绑定到 Logger。

#### 2.1.5 如果指定了日志文件，则创建 `FileHandler`
```bash
    if log_file:
        file_handler = logging.FileHandler(log_file, encoding='utf-8')
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
```
-	如果 log_file 提供了路径，则日志会写入文件：
-	**FileHandler(log_file, encoding='utf-8') **：创建文件日志 `Handler`，并支持 UTF-8 避免中文乱码。

### 2.2 sql.logger模块
```bash
class sql_logger:
    def __init__(self, module_name: str)
    def info(self, log_content: str) -> None
    def debug(self, log_content: str) -> None
    def warning(self, log_content: str) -> None
    def error(self, log_content: str) -> None
```
-	module_name:记录日志的模块名称，用于区分不同模块的日志记录。
-	log_content:具体的日志内容，可以是任何字符串。

#### 2.2.1 `__init__()` 初始化
```bash
    def __init__(self, module_name: str):
        self.module_name = module_name
        self.logger = log_DB()
```
参数:
-  module_name: str —— 模块名称，用于标记该日志属于哪个模块。
功能:
-  self.module_name = module_name：存储模块名称。
-  self.logger = log_DB()：实例化 log_DB 对象，以便写入日志。

#### 2.2.2 `info()` 方法
```bash
def info(self, log_content: str) -> None:
    self.logger.add_log(self.module_name, 'info', log_content)
```
参数:
- log_content: str —— 日志内容。

功能:
- 调用 log_DB.add_log() 方法，写入 info 级别的日志。

示例:
```bash
logger = sql_logger("UserModule")
logger.info("User login successful")
```
存入数据库的数据:
```pgsql
| module_name | log_level | log_content            |
|------------|----------|------------------------|
| UserModule | info     | User login successful  |
```

#### 2.2.3 `debug()` 方法
```bash
def debug(self, log_content: str) -> None:
    self.logger.add_log(self.module_name, 'debug', log_content)
```
参数：
- log_content: str —— 日志内容。

功能：
- 记录 debug 级别的日志。

示例:
```bash
logger = sql_logger("PaymentModule")
logger.debug("Payment validation passed")
```
存入数据库的数据:
``` pgsql
 
| module_name    | log_level | log_content            |
|---------------|----------|------------------------|
| PaymentModule | debug    | Payment validation passed |
```

#### 2.2.4 `warning()` 方法
```bash
def warning(self, log_content: str) -> None:
    self.logger.add_log(self.module_name, 'warning', log_content)
```
参数：
- log_content: str —— 日志内容。

功能：
- 记录 warning 级别的日志。

示例：
```bash
logger = sql_logger("NetworkModule")
logger.warning("Network connection is slow")
```

存入数据库的数据：
```pgsql
| module_name    | log_level | log_content                  |
|---------------|----------|------------------------------|
| NetworkModule | warning  | Network connection is slow   |
```
#### 2.2.5 `error()` 方法
```bash
def error(self, log_content: str) -> None:
    self.logger.add_log(self.module_name, 'error', log_content)
```
参数：
- log_content: str —— 日志内容。

功能：
- 记录 error 级别的日志。

示例：
```bash
logger = sql_logger("DatabaseModule")
logger.error("Database connection failed")
```

存入数据库的数据：
```pgsql
| module_name    | log_level | log_content                  |
|---------------|----------|------------------------------|
| DatabaseModule | error    | Database connection failed  |
```
### 完整示例
```bash
# 创建 SQL 日志记录器（模块名：UserModule）
user_logger = sql_logger("UserModule")

# 记录不同级别的日志
user_logger.info("User logged in")
user_logger.debug("Fetching user data from cache")
user_logger.warning("User session is about to expire")
user_logger.error("User authentication failed")
```
### 数据库日志示例
```pgsql
| module_name  | log_level | log_content                     |
|-------------|----------|---------------------------------|
| UserModule  | info     | User logged in                 |
| UserModule  | debug    | Fetching user data from cache  |
| UserModule  | warning  | User session is about to expire |
| UserModule  | error    | User authentication failed     |
```


## 3. `SQLite_db`的使用
- `__init__`:用于模块初始化，它导入并暴露了 `log_DB` 类，
使得外部代码可以通过以下内容直接使用该类，而无需访问 sql_log.py 具体文件。 
```bash
from SQLite_db import log_DB 
```
### 3.1 `sql.log`模块的使用
数据库字段：
- id:	Integer  primary_key=True, autoincrement=True	自增主键
- timestamp:	String(19)	记录日志时间，精确到秒（格式：YYYY-MM-DD HH:MM:SS）
- module_name:	String(255)	记录日志来源的模块或函数信息如 'my_module.some_func'
- log_level: String(10)	日志等级（info, debug, warning 等）
- log_content:	Text	具体的日志内容（可存储大量文本数据，最大可达 4GB）

#### 3.1.1 `log_DB`类
```bash
class log_DB:
    def __init__(self, db_path: str = 'logs/app_log.db', forced_formatting: bool = False, echo: bool = False)
    def add_log(self, module_name: str, log_level: str, log_content: str) -> None
```
功能：
- 管理日志数据库（自动初始化）
- 存储日志（add_log()）
- 支持强制删除数据库（forced_formatting=True）
- 可调试 SQL 语句（echo=True）

#### 3.1.2 `__init__()`
```bash
def __init__(self, db_path: str = 'logs/app_log.db', forced_formatting: bool = False, echo: bool = False):
```
- 参数
	初始化数据库连接。如果 forced_formatting 为 True，或 INI_STATEMENT 为 False，则会先删除旧的数据库文件，再重新创建新表。
- db_path: SQLite 数据库文件路径（默认：logs/app_log.db）
- forced_formatting:是否强制删除并重建数据库（默认 False）
- echo:是否打印 SQL 语句（调试用）（默认 False）

#### 3.1.2 `_create_and_bind_engine()`
```bash
def _create_and_bind_engine(self, echo: bool):
```
参数：
- echo: 是否打印 SQL 语句（True 进行调试）。

功能：
- 创建数据库连接：sqlite:///{self.db_path} 

创建表结构：
- 创建 session 用于数据库操作

#### 3.1.2 `add_log()`
```bash
def add_log(self, module_name: str, log_level: str, log_content: str) -> None:
```
参数：
- module_name:记录日志的模块名称
- log_level:日志级别（info, debug, warning, error）
- log_content:具体日志内容

功能：
- 创建一条新的日志记录，并插入到 `log_records` 表中
- 提交事务

示例：
```bash
db = log_DB()
db.add_log("UserModule", "info", "User logged in successfully")
```

### 完整示例
```bash
# 初始化日志数据库
db = log_DB(db_path="logs/app_log.db", forced_formatting=False, echo=True)

# 记录不同级别的日志
db.add_log("AuthModule", "info", "User login successful")
db.add_log("PaymentModule", "debug", "Payment processed")
db.add_log("NetworkModule", "warning", "Slow network detected")
db.add_log("DatabaseModule", "error", "Failed to connect to database")
```

### 数据库日志示例
```pgsql
| record_id | timestamp           | module_name    | log_level | log_content                  |
|-----------|---------------------|---------------|----------|------------------------------|
| 1         | 2025-03-03 12:00:00 | AuthModule    | info     | User login successful        |
| 2         | 2025-03-03 12:05:10 | PaymentModule | debug    | Payment processed            |
| 3         | 2025-03-03 12:10:30 | NetworkModule | warning  | Slow network detected        |
| 4         | 2025-03-03 12:15:45 | DatabaseModule| error    | Failed to connect to database |
```




