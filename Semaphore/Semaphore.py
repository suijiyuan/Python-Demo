import threading
import time


def _work(_semaphore, _num):
    _semaphore.acquire()
    time.sleep(2)
    print('work%d' % _num)
    _semaphore.release()


def _main():
    semaphore = threading.Semaphore(2)
    for num in range(10):
        threading.Thread(target=_work, args=(semaphore, num)).start()


if __name__ == '__main__':
    _main()
