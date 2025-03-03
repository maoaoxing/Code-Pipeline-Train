import json
from .constants import INI_STATEMENT, LOGGER_INI_STATEMENT

def finish_ini_sql_db():
    """初始化完成数据库后在配置文件中进行注册，防止覆盖创建"""
    with open('configs/database.json', 'r') as f:
        config = json.load(f)
        config['sqlite']['ini_statement'] = 1
    with open('configs/database.json', 'w') as f:
        json.dump(config, f, indent=4, ensure_ascii=False)





def finish_ini_logger_sql_db():
    """初始化完成数据库后在配置文件中进行注册，防止覆盖创建"""
    with open('configs/logger.json', 'r') as f:
        config = json.load(f)
        config['sqlite']['ini_statement'] = 1
    with open('configs/logger.json', 'w') as f:
        json.dump(config, f, indent=4, ensure_ascii=False)
    LOGGER_INI_STATEMENT = True
