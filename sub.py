import logging

logger = logging.getLogger(__name__)

def sub_func():
    logger.debug('sub.pyのデバッグレベル')
    logger.info('sub.pyのインフォレベル')
    logger.warning('sub.pyのワーニングレベル')
    logger.error('sub.pyのエラーレベル')
    logger.critical('sub.pyのクリティカルレベル')


