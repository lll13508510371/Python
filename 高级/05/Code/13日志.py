import logging

# # 1.1 设置日志的等级
# logging.basicConfig(level=logging.ERROR)

logging.basicConfig(
    filename='app1.log',
    filemode='w',
    format='%(name)s - %(levelname)s - %(message)s',
    level=logging.DEBUG)

logging.debug('这里是调试信息')
logging.info('这里是详情信息')
logging.warning('这里是警告信息')
logging.error('这里是错误信息')
logging.critical('这里是危机信息')
