from setuptools import setup, find_packages
setup(
    name="nba_stats",
    version="0.1.1",
    packages=find_packages(exclude=['tests']),

    install_requires=['docutils>=0.3', 'pandas>=0.20.3', 'requests'],

    include_package_data=True,

    # metadata for upload to PyPI
    author="Daniel Bratulic",
    author_email="danielbratulic@gmail.com",
    description="Package which is used for retrieving stats by NBA players.",
    license="MIT",
    keywords="nba stats analytics sports",
    url="https://github.com/danchyy/nba_stats",  # project home page, if any
    project_urls={
        "Source Code": "https://github.com/danchyy/nba_stats"
    },
    zip_safe=False
)
