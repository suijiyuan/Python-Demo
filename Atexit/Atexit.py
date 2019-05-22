import atexit


def main():
    print('main()')


@atexit.register
def at_exit():
    print('done')


if __name__ == '__main__':
    main()
