import os
import pkg_resources

import crawler_detect
from crawler_detect import CrawlerDetect


def get_known_useragents():
    path = os.path.join('resources', 'known_crawler_useragents.txt')
    content = pkg_resources.resource_string(crawler_detect.__name__, path)
    return content.splitlines()


def test_CrawlerDetect_is_crawler_on_known_bots():
    detect = CrawlerDetect()

    for user_agent in get_known_useragents():
        assert detect.is_crawler(user_agent)
