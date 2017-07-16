import os

import crawler_detect

RESOURCES_DIR = os.path.join(
    crawler_detect.__path__[0], 'resources',
)

from .core import CrawlerDetect
