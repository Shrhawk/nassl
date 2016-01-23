#!/usr/bin/python
import sys
import unittest


def main():

    suite = unittest.loader.TestLoader().discover('tests', pattern='*_Tests.py')
    result = unittest.TextTestRunner(verbosity=2).run(suite)

    exit_code = 0 if result.wasSuccessful() else 1
    sys.exit(exit_code)


if __name__ == '__main__':
    main()
