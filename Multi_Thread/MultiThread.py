import time
import _thread


def func1(lock):
    time.sleep(5)
    print('func1()')
    lock.release()


def func2(lock):
    print('func2()')
    lock.release()


if __name__ == '__main__':
    locks = []

    lock1 = _thread.allocate_lock()
    lock1.acquire()
    locks.append(lock1)

    lock2 = _thread.allocate_lock()
    lock2.acquire()
    locks.append(lock2)

    _thread.start_new_thread(func1, (lock1,))
    _thread.start_new_thread(func2, (lock2,))
    for item in locks:
        while item.locked():
            pass
    print('main finish')
