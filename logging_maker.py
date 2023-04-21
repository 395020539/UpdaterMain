#!/usr/bin/python
# -*- coding: utf-8 -*-

import logging
import os
from logging.handlers import RotatingFileHandler
from configuration_reader import MyPath


mypath = MyPath()

# 配置 logging 模块
log_file = os.path.join(mypath.log_dir, 'log.log')

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# 创建 RotatingFileHandler，设置文件名、文件大小、保留文件数量和编码方式
handler = RotatingFileHandler(log_file, maxBytes=10 * 1024 * 1024, backupCount=5,
                              encoding='utf-8')

# 设置日志输出格式
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
handler.setFormatter(formatter)

# 添加处理器到 logger
logger.addHandler(handler)

# 输出日志信息
# logger.debug('debug message')
# logger.info('info message')
# logger.warning('warning message')
# logger.error('error message')
# logger.critical('critical message')

logger.info('初始化日志...')
