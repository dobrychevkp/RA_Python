import argparse
import re

from typing import Iterable

from Collectors import *


class WordParser(object):
    def __init__(self, source: Iterable[str], collector: AbstractCollector):
        self.__source = source
        self.__collector = collector

    def start(self):
        for line in self.__source:
            # NOTE: Выкусываем отдельные слова из строки по регулярному выражению.
            for word in re.findall(r'(\w+)', line):
                self.__collector.push(word)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='A trivial utility for word counting.'
    )

    parser.add_argument(
        '--ignore-case',
        action='store_true',
        help='Ignore case',
    )

    parser.add_argument(
        '-i', '--input',
        nargs='?',
        default=None,
        help='Input file',
    )

    parser.add_argument(
        '-o', '--output',
        nargs='?',
        default=None,
        help='Output file',
    )

    options = vars(parser.parse_args())

    _collector = WordCountCollector()
    _collector.configure(options)

    with open(options['input'], 'r') as f:
        parser = WordParser(f.readlines(), _collector)
        parser.start()

    _collector.save()
