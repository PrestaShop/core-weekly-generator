from .github import GitHub


class Report:
    def __init__(self, date_range, no_cache, debug):
        self.github = GitHub(no_cache, debug)
        self.date_range = date_range

    ##
    # Get opened issues
    #
    def get_opened_issues(self):
        return self.github.get_json(
            'created:{date_range}'.format(date_range=self.date_range)
        )

    ##
    # Get closed issues
    #
    def get_closed_issues(self):
        return self.github.get_json(
            'closed:{date_range}'.format(date_range=self.date_range)
        )

    ##
    # Get fixed issues
    #
    def get_fixed_issues(self):
        return self.github.get_json(
            'label:fixed+closed:{date_range}'.format(date_range=self.date_range)
        )

    ##
    # Get opened pull requests
    #
    def get_opened_pull_requests(self):
        return self.github.get_json(
            'created:{date_range}'.format(date_range=self.date_range),
            False
        )

    ##
    # Get closed pull requests
    #
    def get_closed_pull_requests(self):
        return self.github.get_json(
            'closed:{date_range}'.format(date_range=self.date_range),
            False
        )

    ##
    # Get merged pull request
    #
    def get_merged_pull_requests(self):
        return self.github.get_json(
            'merged:{date_range}'.format(date_range=self.date_range),
            False
        )
