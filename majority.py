#!/usr/bin/env python

import datetime
import sys


class MajorityOfLife(object):
    def __init__(self, birthday):
        self._birthday = birthday

    def for_start_date(self, date):
        delta = date - self._birthday

        return date + delta


def parse_date(date):
    return datetime.datetime.strptime(date, "%Y-%m-%d")


def main():
    if len(sys.argv) < 3:
        print("""Usage: {:s} YOUR_BIRTHDAY START_DATE1 [START_DATE2 [...]]

Given when you were born and one or more dates, shows you you'll have spent
the majority of your life further from that date than closer to it.

Example: if you were born on April 20th, 1980 and you want to know as of what
date The Matrix will have been around for the majority of your life, you'd use:

    {:s} 1980-04-20 1999-03-31

See also: https://xkcd.com/1757/""".format(sys.argv[0], sys.argv[0]))
        sys.exit(1)

    maj = MajorityOfLife(parse_date(sys.argv[1]))

    for date in sys.argv[2:]:
        majority_date = maj.for_start_date(parse_date(date)).strftime('%Y-%m-%d')
        print("{:s} is {:s}".format(date, majority_date))


if __name__ == '__main__':
    main()
