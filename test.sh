FILE_BASE=(`basename $0 .sh`)
log_file="${FILE_BASE}.log"

python main.py logger.handlers.file_handler.filename=${log_file}
