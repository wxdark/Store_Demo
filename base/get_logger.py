import logging.handlers


class GetLogger:
    logger = None

    @classmethod
    def get_logger(cls):

        if cls.logger is None:
            # 获取日志器
            cls.logger = logging.getLogger("admin")
            # 设置日志器默认级别
            cls.logger.setLevel(logging.INFO)

            # 设置日志器默认格式
            fmt = "%(asctime)s %(levelname)s [%(name)s] [%(filename)s (%(funcName)s:%(lineno)d] - %(message)s"

            fm = logging.Formatter(fmt)

            # 获取日志文件处理器
            th = logging.handlers.TimedRotatingFileHandler(filename="../log/info.log", when="midnight", interval=1,

                                                           backupCount=30, encoding="utf-8")
            # 将格式器添加到处理器中
            th.setFormatter(fm)
            # 添加处理器到日志器中
            cls.logger.addHandler(th)

        # 返回日志器
        return cls.logger
