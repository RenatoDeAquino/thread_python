import logging
import threading
import time

def thread_function(name):
    logging.info("thread %s: starting", name)
    time.sleep(2)
    logging.info("thread %s: finishig", name)

if __name__ == "__main__":
    format = "%(asctime)s %(message)s"
    logging.basicConfig(filename="teste-log",format=format, level=logging.INFO, datefmt = "%d/%m/%y %H:%M:%S")


logging.info("main: before creating the thread")

x = threading.Thread(target=thread_function, args=(1,))

logging.info("main: before running thread")

x.start()

logging.info("main: wait for the thread to finish")

x.join()

logging.info("main: all done")
