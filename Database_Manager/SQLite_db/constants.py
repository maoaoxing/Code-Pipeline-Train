import json

database_config = json.load(open("configs/database.json"))

INI_STATEMENT = bool(database_config["sqlite"]["ini_statement"])

main_config = json.load(open("configs/main.json"))

RUNNING_MODE = main_config["running_mode"]

logger_config = json.load(open("configs/logger.json"))

LOGGER_INI_STATEMENT = bool(logger_config["sqlite"]["ini_statement"])