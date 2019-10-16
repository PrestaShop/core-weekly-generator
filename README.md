# Core Weekly report generator

Core weekly generator is a micro Python 3.4+ CLI application that is able to generate a list of merged PR
for a selected list of branches in an interval of dates.

## Installation

```bash
$ pip install -r requirements.txt
```

## Usage

Display help

```bash
$ ./core-weekly.py --help
usage: core-weekly.py [-h] [--no-cache] date_range

PrestaShop Core Weekly

positional arguments:
  date_range  Date range

optional arguments:
  -h, --help  show this help message and exit
  --no-cache  Disable cache
```

Generate Core Weekly

```bash
 $ python ./core-weekly.py 2019-08-05..2019-08-11 > my-core-weekly.md
 ```

You need to do a bit of polishing (fill in the `[XXXX]` sections, reorder categories, repositories, put the full category names instead of TE or CO) before publishing the article.
