from .github import GitHub


class Report:
    def __init__(self, date_range, no_cache, debug):
        self.github = GitHub(no_cache, debug)
        self.date_range = date_range

    def get_opened_issues(self):
        """Get opened issues

        :returns: Created issues
        :rtype: dict

        """
        return self.github.get_json(
            'created:{date_range}'.format(date_range=self.date_range)
        )

    def get_closed_issues(self):
        """Get closed issues

        :returns: Closed issues
        :rtype: dict

        """
        return self.github.get_json(
            'closed:{date_range}'.format(date_range=self.date_range)
        )

    def get_fixed_issues(self):
        """Get fixed issues

        :returns: Fixed issues
        :rtype: dict

        """
        return self.github.get_json(
            'label:fixed+closed:{date_range}'.format(date_range=self.date_range)
        )

    def get_opened_pull_requests(self):
        """Get opened pull requessts

        :returns: Created pull requests
        :rtype: dict

        """
        return self.github.get_json(
            'created:{date_range}'.format(date_range=self.date_range),
            False
        )

    def get_closed_pull_requests(self):
        """Get closed pull requessts

        :returns: Closed pull requests
        :rtype: dict

        """
        return self.github.get_json(
            'closed:{date_range}'.format(date_range=self.date_range),
            False
        )

    def get_merged_pull_requests(self):
        """Get merged pull requessts

        :returns: Merged pull requests
        :rtype: dict

        """
        return self.github.get_json(
            'merged:{date_range}'.format(date_range=self.date_range),
            False
        )
