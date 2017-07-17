from setuptools import setup, find_packages


test_dependencies = [
    'pytest==3.1.3',
]

setup(
    name='py-crawler-detect',
    version='0.1.3',
    description='Python port of https://github.com/JayBizzle/Crawler-Detect',
    packages=find_packages(),
    package_data={'crawler_detect': ['resources/*']},
    include_package_data=True,
    tests_require=test_dependencies,
    extras_require={
        'testing': test_dependencies,
    },
)
