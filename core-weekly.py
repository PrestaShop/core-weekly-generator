#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import argparse
from core_weekly import CoreWeekly


def main():
    parser = argparse.ArgumentParser(description="PrestaShop Core Weekly")
    parser.add_argument('--no-cache', action='store_const', const=True, help='Disable cache')
    parser.add_argument('--debug', action='store_const', const=True, help='Use Debug')
    parser.add_argument('date_range', type=str, help='Date range')

    args = parser.parse_args()

    core_weekly = CoreWeekly(args)
    print(core_weekly.generate())


if __name__ == '__main__':
    main()
