import threading
import time


# more information about Semaphore and BoundedSemaphore:
# https://stackoverflow.com/questions/48971121/what-is-the-difference-between-semaphore-and-boundedsemaphore

def _work(_semaphore, _num):
    _semaphore.acquire()
    time.sleep(2)
    print('work%d' % _num)
    _semaphore.release()


def _main():
    semaphore = threading.BoundedSemaphore(2)
    for num in range(10):
        threading.Thread(target=_work, args=(semaphore, num)).start()


if __name__ == '__main__':
    _main()
