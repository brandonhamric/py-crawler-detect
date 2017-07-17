import os
import pkg_resources
import re

import crawler_detect


class CrawlerDetect(object):
    def __init__(self):
        self.exclusion_regex_patterns = self.load_exclusion_patterns()
        self.crawler_regex_patterns = self.load_crawler_patterns()

    def load_exclusion_patterns(self):
        return self._load_regex_patterns_from_file('exclusions_regex_list.txt')

    def load_crawler_patterns(self):
        return self._load_regex_patterns_from_file('crawler_regex_list.txt')

    def _load_regex_patterns_from_file(self, file):
        path = os.path.join('resources', file)
        content = pkg_resources.resource_string(crawler_detect.__name__, path)
        return [re.compile(pattern, re.IGNORECASE) for pattern in content.splitlines() if len(pattern) > 0]

    def is_crawler(self, user_agent):
        cleaned_user_agent = user_agent[:]
        for pattern in self.exclusion_regex_patterns:
            cleaned_user_agent = pattern.sub(b"", cleaned_user_agent)

        cleaned_user_agent = cleaned_user_agent.strip()

        if len(cleaned_user_agent) == 0:
            return False

        all_matches = [regex.search(cleaned_user_agent) for regex in self.crawler_regex_patterns]
        return any(all_matches)
