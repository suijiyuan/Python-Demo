import time
import threading


def _func1():
    time.sleep(5)
    print('func1()')


def _func2():
    print('func2()')


if __name__ == '__main__':
    threads = []

    thread1 = threading.Thread(target=_func1, args=())
    threads.append(thread1)

    thread2 = threading.Thread(target=_func2, args=())
    threads.append(thread2)

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    print('main finish')
