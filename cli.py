#!/usr/bin/env python3
import logging
import sys

import stats


log = logging.getLogger(__name__)


def get_function_from_name(name):
    if not name:
        return stats.time_durations

    return getattr(stats, name)


if __name__ == '__main__':
    fmt = '%(name)s:%(funcName)s:%(lineno)s %(levelname)s: %(message)s'
    logging.basicConfig(format=fmt, level=logging.INFO)
    func = get_function_from_name(None if len(sys.argv) == 1 else sys.argv[1])
    log.info("%s() ...", func.__name__)
    func()
