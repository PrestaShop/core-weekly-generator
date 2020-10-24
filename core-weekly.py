#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from core_weekly import CoreWeekly
import argparse
import logging


def main():
    parser = argparse.ArgumentParser(description="PrestaShop Core Weekly")
    parser.add_argument('--no-cache', action='store_const', const=True, help='Disable cache')
    parser.add_argument('--debug', action='store_const', const=True, help='Use Debug')
    parser.add_argument('--stats', action='store_const', const=True, help='Print stats report and save it in json file if you specify a week number')
    parser.add_argument('--year', type=str, help='Specify which year you want to use in Week context')
    parser.add_argument('--token', type=str, help='GitHub Access Token', required=True)

    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--date', type=str, help='Date range')
    group.add_argument('--week', type=int, help='Week number')
    group.add_argument('--compute', action='store_const', const=True, help='Compute data stored in var directory')

    args = parser.parse_args()
    logging.basicConfig()
    if args.debug:
        logging.getLogger().setLevel(logging.DEBUG)

    core_weekly = CoreWeekly(args)
    if args.stats:
        print(core_weekly.generate_stats())
    elif args.date or args.week:
        print(core_weekly.generate())
    elif args.compute:
        core_weekly.compute_files()


if __name__ == '__main__':
    main()
