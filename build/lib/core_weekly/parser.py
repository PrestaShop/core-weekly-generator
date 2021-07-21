from coreteam import PROJECTS
import re


class Parser:
    def get_body_detail(self, body, key, regex='.+'):
        """Parse body to retrieve a specific detail

        :param body: Body content
        :type body: str
        :param key: The key we want to retrieve
        :type key: str
        :param regex: Optional regex
        :type regex: str
        :returns: Match object
        :rtype: re.Match

        """
        return re.search(
            r'^(?:\|\s+{}\?[ ]*\|[ ]*)({})?[ ]*$'.format(
                key,
                regex
            ),
            body,
            re.MULTILINE
        )

    def extract_core_category(self, body):
        """Extract core category information

        :param body: Body content
        :type body: str
        :returns: Returns category if possible, otherwise None
        :rtype: None|str

        """
        if body is None:
            return

        matches = self.get_body_detail(body, 'Category')
        if matches:
            if matches.group(1):
                return matches.group(1).strip()

            return 'Misc'

    def extract_branch(self, body):
        """Extract core branch information

        :param body: Body content
        :type body: str
        :returns: Returns branch if possible, otherwise None
        :rtype: None|str

        """
        if body is None:
            return

        matches = self.get_body_detail(body, 'Branch')
        if matches:
            if matches.group(1):
                return matches.group(1).strip()

            return 'unknown branch'

    def extract_repository(self, url, raw=False):
        """Extract repository from GitHub URL

        :param body: Body content
        :type body: str
        :param raw: Translate if raw is False, otherwise returns the urlvalue
        :type raw: bool
        :returns: Returns repository if possible, otherwise the url
        :rtype: str

        """
        matches = re.search('github.com/PrestaShop/(.+?)/', url)
        if matches:
            if not raw and matches.group(1) in PROJECTS.keys():
                # map repository with a project name
                return PROJECTS[matches.group(1)]

            return matches.group(1)

        return url
