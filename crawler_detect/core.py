import os
import re

from crawler_detect import RESOURCES_DIR


class CrawlerDetect(object):
    def __init__(self, empty_ua_is_crawler=True):
        self.empty_ua_is_crawler = empty_ua_is_crawler
        self.exclusion_regex_patterns = self.load_exclusion_patterns()
        self.crawler_regex_patterns = self.load_crawler_patterns()

    def load_exclusion_patterns(self):
        path = os.path.join(RESOURCES_DIR, 'exclusions_regex_list.txt')
        return self._load_regex_patterns_from_file(path)

    def load_crawler_patterns(self):
        path = os.path.join(RESOURCES_DIR, 'crawler_regex_list.txt')
        return self._load_regex_patterns_from_file(path)

    def _load_regex_patterns_from_file(self, path):
        with open(path, 'r') as f:
            return [re.compile(pattern, re.IGNORECASE) for pattern in f.read().splitlines() if len(pattern) > 0]

    def is_crawler(self, user_agent):
        user_agent_is_empty = not user_agent.strip()
        if user_agent_is_empty and self.empty_ua_is_crawler:
            return True

        cleaned_user_agent = user_agent[:]
        for pattern in self.exclusion_regex_patterns:
            cleaned_user_agent = pattern.sub("", cleaned_user_agent)

        cleaned_user_agent = cleaned_user_agent.strip()

        if len(cleaned_user_agent) == 0:
            return False

        all_matches = [regex.search(cleaned_user_agent) for regex in self.crawler_regex_patterns]
        return any(all_matches)
