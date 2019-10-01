# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Just in case it's not python 2
try:
    import urllib.request as urlrequest
except ImportError:
    import urllib as urlrequest

import ssl
import os
import json
import time

ssl._create_default_https_context = ssl._create_unverified_context


# Github api
#
class GitHub():
    def __init__(self, no_cache):
        self.sleep_time = 2
        self.url = 'https://api.github.com/search/issues?per_page=100'
        self.no_cache = no_cache

    ##
    # Build github query
    #
    # :param query String
    #
    def build_query(self, query):
        return '&q=org:PrestaShop+is:public+-repo:prestashop/prestashop.github.io+' + query

    ##
    # Generate github request and return json content
    #
    # :param str query: Represents a GitHub query
    # :param bool is_issue: Is issue or pull request
    #
    def get_json(self, query, is_issue=True):
        query_type = ('is:issue' if is_issue else 'is:pr')

        # Debug only
        # print(
        #    'Processing request for query: {query_type}+{query}'.format(
        #        query=query,
        #        query_type=query_type
        #    )
        # )

        filename = 'cache/{query}-{query_type}'.format(
            query=query,
            query_type=query_type
        )

        if os.path.exists('./' + filename) and not self.no_cache:
            with open(filename, 'r') as f:
                data = f.read()
        else:
            data = urlrequest.urlopen(
                self.url +
                self.build_query(query) +
                '+' +
                query_type
            ).read().decode('utf-8')

            with open(filename, 'w') as f:
                f.write(data)
            time.sleep(self.sleep_time)

        return json.loads(data)
