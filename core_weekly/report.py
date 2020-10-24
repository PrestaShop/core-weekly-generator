from .github import GitHubClient


class Report:
    def __init__(self, date_range, no_cache, debug, github_access_token):
        self.github = GitHubClient(no_cache, debug, github_access_token)
        self.date_range = date_range

    def format_release_item(self, release_data):
        """Format a GitHub release list item string

        :returns: Formatted string
        :rtype: str

        """
        template = '- [{repository_name}]({repository_url}): [{version_title}]({version_url})'
        repository = release_data['repo']
        release = release_data['release']

        return template.format(
            repository_name=repository.name,
            repository_url=repository.html_url,
            version_title=release.title,
            version_url=release.html_url
        )

    def get_last_week_releases(self):
        """Get last week GitHub releases

        :returns: List of last Week GitHub releases statements
        :rtype: list

        """
        releases_data = self.github.get_last_week_git_releases()
        return list(map(self.format_release_item, releases_data))

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
