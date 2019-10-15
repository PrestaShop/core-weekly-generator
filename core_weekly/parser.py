from coreteam import PROJECTS
import re


class Parser:
    ##
    # Get body detail
    #
    # :param str body: Body string
    # :param str search_type: Type we want to retrieve in the body
    # :param str regex: Selector
    #
    def get_body_detail(self, body, search_type, regex='.+'):
        return re.search(
            r'(?:\|\s+{}\?\s+\|\s+)({})\s+'.format(
                search_type,
                regex
            ),
            body
        )

    ##
    # Extract core category
    #
    # :param str body: Body string
    #
    def extract_core_category(self, body):
        matches = self.get_body_detail(body, 'Category')
        if matches:
            if matches.group(1):
                return matches.group(1).strip()

            return 'Misc'

    ##
    # Extract branch
    #
    # :param str body: Body string
    #
    def extract_branch(self, body):
        matches = self.get_body_detail(body, 'Branch')
        if matches:
            if matches.group(1):
                return matches.group(1).strip()

            return 'unknown branch'

    ##
    # Extract repository
    #
    # :param str url: URL string
    #
    def extract_repository(self, url):
        matches = re.search('github.com/PrestaShop/(.+?)/', url)
        if matches:
            if matches.group(1) in PROJECTS.keys():
                # map repository with a project name
                return PROJECTS[matches.group(1)]

            return matches.group(1)

        return url
