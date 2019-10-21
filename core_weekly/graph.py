from pathlib import Path
import collections
import json
import plotly.graph_objects as go
import re


class Graph:
    def __init__(self, directory):
        """Constructor
        """
        self.directory = directory

    def pull_requests_per_weeks(self, data, project='PrestaShop'):
        """Generate pull requests graph depends on weeks and years
        """

        for year, d in data.items():
            fig = go.Figure()
            fig.update_layout(title=go.layout.Title(text='Pull requests per week in ' + str(year)))
            fig.add_trace(
                go.Bar(
                    x=[week for week in d['pull_requests'].keys()],
                    y=[d['pull_requests'][week]['opened']['total_count'] for week in d['pull_requests'].keys()],
                    name='Opened',
                )

            )
            fig.add_trace(
                go.Bar(
                    x=[week for week in d['pull_requests'].keys()],
                    y=[d['pull_requests'][week]['closed']['total_count'] for week in d['pull_requests'].keys()],
                    name='Closed',
                )

            )
            fig.add_trace(
                go.Bar(
                    x=[week for week in d['pull_requests'].keys()],
                    y=[d['pull_requests'][week]['merged']['total_count'] for week in d['pull_requests'].keys()],
                    name='Merged',
                )

            )
            fig.show()

    def build(self):
        p = Path(self.directory)
        data = {}
        for directory in p.iterdir():
            if not directory.is_dir():
                continue

            year = directory.name
            data[year] = {
                'pull_requests': {},
                'issues': {},
            }

            for f in list(p.glob(year + '/*.json')):
                matches = re.search(r'^(\d+)_(\w+)\.json$', f.name)
                if not matches:
                    continue

                week = int(matches.group(1))
                typ = matches.group(2)
                if week not in data[year][typ]:
                    data[year][typ].update({week: []})

                data[year][typ][week] = json.loads(Path(f).read_text())

        data = collections.OrderedDict(data)
        self.pull_requests_per_weeks(data)
