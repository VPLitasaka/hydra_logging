import logging
import sub
import sys
import hydra
from omegaconf import DictConfig
from omegaconf import OmegaConf




@hydra.main(version_base=None, config_path="conf", config_name="config")
def main(args : DictConfig) -> None:
    log_config = OmegaConf.to_container(args.logger, resolve=True)
    logging.config.dictConfig(log_config)
    logger = logging.getLogger(__name__)

    # main関数内でログ出力
    logger.debug('This is a debug message from main function')
    logger.info('This is an info message from main function')
    logger.warning('This is a warning message from main function')
    logger.error('This is an error message from main function')
    logger.critical('This is a critical message from main function')

    # sub.pyの関数を呼び出してログ出力
    sub.sub_func()

if __name__ == '__main__':
    main()


