"""
日志工具模块。
"""
import logging
import sys
from typing import Optional


def get_logger(name: str, level: Optional[int] = None) -> logging.Logger:
    """
    获取配置好的日志器。
    
    Args:
        name: 日志器名称
        level: 日志级别，默认为INFO
        
    Returns:
        logging.Logger: 配置好的日志器
    """
    if level is None:
        level = logging.INFO
    
    logger = logging.getLogger(name)
    logger.setLevel(level)
    
    # 检查是否已经有处理器，避免重复添加
    if not logger.handlers:
        handler = logging.StreamHandler(sys.stdout)
        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)
    
    return logger 