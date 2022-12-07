# Core Weekly report generator

_This repository is archived as this tool has been replaced by a [PHP Core Monthly generator](https://github.com/PrestaShop/presthubot/blob/master/src/App/Command/GitHubMonthlyReportCommand.php)._

![Core Weekly Integration tests](https://github.com/prestashop/core-weekly-generator/workflows/Core%20Weekly%20Integration%20tests/badge.svg)

Core weekly generator is a micro Python 3.6+ CLI application that is able to generate a list of merged PR
for a selected list of branches in an interval of dates.

## Installation

```bash
$ pip install -r requirements.txt
```

## Usage

Display help

```bash
$ ./core-weekly.py --help
usage: core-weekly.py [-h] [--no-cache] [--debug] [--stats] [--year YEAR]
                      (--date DATE | --week WEEK | --compute)

PrestaShop Core Weekly

optional arguments:
  -h, --help   show this help message and exit
  --no-cache   Disable cache
  --debug      Use Debug
  --stats      Print stats report and save it in json file if you specify a
               week number
  --year YEAR  Specify which year you want to use in Week context
  --date DATE  Date range
  --week WEEK  Week number
  --compute    Compute data stored in var directory
```

### Core Weekly

Generate Core Weekly with a date range

```bash
 $ python core-weekly.py --date 2019-08-05..2019-08-11 > my-core-weekly.md
 ```

Or easier by specifing a week number

```bash
 $ python core-weekly.py --week 11 > my-core-weekly.md
 ```

 And if you want the same week but in 2018

```bash
 $ python core-weekly.py --year 2018 --week 11 > my-core-weekly.md
 ```

The output template is almost ready to be published. What you might add manually is:
- weekly releases of prestashop projects
- a message targeting developers

### Stats

Stats are generated and saved under `var` directory.

```bash
 $ python core-weekly.py --year 2018 --week 11 --stats
 ```

When stats are downloaded, you can compute them.

```bash
 $ python core-weekly.py --compute
 ```

## Troubleshooting

Be aware that data fetched from GitHub is stored into a local sqlite cache file! This might create issues when submitting code changes to the tool logic.

## Code quality

Install dependencies:

```bash
$ ./setup.py install
```

### Static analysis

```bash
$ ./setup.py flake8
```

### Running tests

To run unit tests:

```bash
$ ./setup.py nosetests
$ # or
$ nosetests
```
