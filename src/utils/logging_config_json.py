"""
Configuração de logging com saída em JSON para todo o projeto.
"""
import logging
import logging.config
import json
from typing import Optional, Dict, Any


class JsonFormatter(logging.Formatter):
    """
    Formata logs como JSON.
    """
    def __init__(self, fmt: Optional[str] = None, datefmt: Optional[str] = None) -> None:
        super().__init__(fmt=fmt, datefmt=datefmt)

    def format(self, record: logging.LogRecord) -> str:
        log_record: Dict[str, Any] = {
            "timestamp": self.formatTime(record, self.datefmt),
            "level": record.levelname,
            "logger": record.name,
            "message": record.getMessage(),
            "module": record.module,
            "funcName": record.funcName,
            "lineNo": record.lineno,
        }
        if record.exc_info:
            log_record["exc_info"] = self.formatException(record.exc_info)
        return json.dumps(log_record)


def setup_json_logging(
    level: int = logging.INFO,
    datefmt: str = "%Y-%m-%dT%H:%M:%S",
    log_to_file: Optional[str] = None,
    max_bytes: int = 10 * 1024 * 1024,
    backup_count: int = 5,
) -> None:
    """
    Configura a raiz do logging para saída JSON.

    Args:
        level: nível mínimo de logging (DEBUG, INFO, ...)
        datefmt: formato de timestamp no JSON
        log_to_file: caminho do arquivo de log (rotativo se definido)
        max_bytes: tamanho máximo do arquivo antes da rotação
        backup_count: número de arquivos de backup
    """
    handlers: Dict[str, Any] = {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "json",
            "level": level,
        }
    }
    if log_to_file:
        handlers["file"] = {
            "class": "logging.handlers.RotatingFileHandler",
            "formatter": "json",
            "level": level,
            "filename": log_to_file,
            "maxBytes": max_bytes,
            "backupCount": backup_count,
        }

    config: Dict[str, Any] = {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "json": {
                "()": JsonFormatter,
                "datefmt": datefmt,
            }
        },
        "handlers": handlers,
        "root": {
            "handlers": list(handlers.keys()),
            "level": level,
        },
    }

    logging.config.dictConfig(config)
