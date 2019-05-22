import atexit


def _main():
    print('main()')


@atexit.register
def _at_exit():
    print('done')


if __name__ == '__main__':
    _main()
