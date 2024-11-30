import multiprocessing

name = 'sdow'
bind = '0.0.0.0:5000'
errorlog = 'errors.log'
accesslog = 'access.log'
capture_output = True
workers = multiprocessing.cpu_count() * 2 + 1
