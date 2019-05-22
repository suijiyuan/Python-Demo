import threading
import time


def work(_semaphore, _num):
    _semaphore.acquire()
    time.sleep(2)
    print('work%d' % _num)
    _semaphore.release()


def main():
    semaphore = threading.Semaphore(2)
    for num in range(10):
        threading.Thread(target=work, args=(semaphore, num)).start()


if __name__ == '__main__':
    main()
