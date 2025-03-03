# 数据库日志系统 API 文档

## 1. 概述
数据库日志系统用于记录和查询应用程序的日志信息，支持两种日志方式：
- **logging_logger**：基于 Python `logging` 模块的传统日志
- **sql_logger**：基于 SQLite 数据库的日志存储

## 2. 安装与配置

### 2.1 依赖安装
确保已安装 `sqlalchemy`（如果 `sql_logger` 依赖它）：
```bash
pip install sqlalchemy
```

### 2.2 配置文件
配置文件位于 `Database_Manager/configs/` 目录下，包括：
- `database.json`: SQLite 数据库初始化相关配置。
- `logger.json`: 日志相关配置。

示例 (`logger.json`)：
```json
{
  "sqlite": {
    "ini_statement": 1
  }
}
```

## 3. 快速上手

### 3.1 使用 `logging_logger`
```python
from Database_Manager.Ealogger.logging_logger import logging_logger

logger = logging_logger("app_logger", level="INFO")
logger.info("应用启动成功")
```

### 3.2 使用 `sql_logger`
```python
from Database_Manager.Ealogger.sql_logger import sql_logger

sql_log = sql_logger("MyModule")
sql_log.info("数据库日志测试")
sql_log.error("发生错误")
```

## 4. API 说明

### 4.1 `logging_logger`
#### `logging_logger(logger_name, level, log_file=None)`
- **参数**:
  - `logger_name` (str): Logger 名称
  - `level` (str): 日志级别，如 `INFO`, `DEBUG`
  - `log_file` (str, 可选): 日志文件路径
- **返回**: `logging.Logger` 实例

示例：
```python
logger = logging_logger("my_logger", level="DEBUG", log_file="app.log")
```

### 4.2 `sql_logger`
#### `sql_logger(module_name)`
- **参数**:
  - `module_name` (str): 日志所属的模块
- **方法**:
  - `info(log_content)`: 记录 `INFO` 级别日志
  - `debug(log_content)`: 记录 `DEBUG` 级别日志
  - `warning(log_content)`: 记录 `WARNING` 级别日志
  - `error(log_content)`: 记录 `ERROR` 级别日志

示例：
```python
sql_log = sql_logger("MyModule")
sql_log.info("系统正常运行")
sql_log.error("发生错误！")
```

## 5. SQLite 数据库日志存储 (`sql_log.py`)

### 5.1 数据库表结构
- **`log_records`**: 存储日志信息
  - `record_id` (int, 主键)
  - `timestamp` (str, 日志时间)
  - `module_name` (str, 模块名)
  - `log_level` (str, 日志等级)
  - `log_content` (text, 日志内容)

### 5.2 `log_DB` 类
#### `log_DB(db_path, forced_formatting, echo)`
- **参数**:
  - `db_path` (str): 数据库文件路径
  - `forced_formatting` (bool): 是否重建数据库
  - `echo` (bool): 是否输出 SQL 语句
- **方法**:
  - `add_log(module_name, log_level, log_content)`: 添加日志记录

示例：
```python
from Database_Manager.SQLite_db.sql_log import log_DB

db = log_DB("logs.db")
db.add_log("ModuleA", "INFO", "初始化完成")
```

## 6. 工具方法 (`utils.py`)
### `finish_ini_sql_db()`
- **功能**: 初始化数据库完成后，修改 `database.json` 以防止重复创建

### `finish_ini_logger_sql_db()`
- **功能**: 初始化 `logger.json`，防止覆盖创建

## 7. 常见问题（FAQ）

### 7.1 如何切换日志存储方式？
- 使用 `logging_logger` 记录到 `stdout` 或文件。
- 使用 `sql_logger` 存储到 SQLite。

### 7.2 如何修改日志级别？
```python
logger = logging_logger("my_logger", level="DEBUG")
```

### 7.3 如何查询数据库日志？
目前 `sql_logger` 仅支持日志记录，未来可扩展查询功能。

---

## 8. 未来优化方向
- 增加 `sql_logger` 日志查询功能
- 统一 `logging_logger` 和 `sql_logger` 配置
- 提供 Web UI 供用户查看日志

---

> **作者**: 开发团队
> **最后更新**: YYYY-MM-DD



