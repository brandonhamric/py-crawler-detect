import os

from crawler_detect import RESOURCES_DIR, CrawlerDetect


def get_known_useragents():
    known_crawler_useragents_path = os.path.join(RESOURCES_DIR, 'known_crawler_useragents.txt')
    with open(known_crawler_useragents_path, 'r') as f:
        return f.read().splitlines()


def test_CrawlerDetect_is_crawler_on_known_bots():
    detect = CrawlerDetect()

    for user_agent in get_known_useragents():
        assert detect.is_crawler(user_agent)
