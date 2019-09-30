# Core Weekly report generator

Core weekly generator is a micro Python 3 (should be compatible with Python 2 too) CLI application that is able to generate a list of merged PR
for a selected list of branches in an interval of dates.
 
## Usage
 
```bash
 $ python ./core-weekly-generator.py 2019-08-05..2019-08-11 > my-core-weekly.md
 ```

You need to do a bit of polishing (fill in the `[XXXX]` sections, fill in the week number and the date, rework some PR titles, put a project name for some repositories) before publishing the article.
