# nba_stats

This project uses NBA's api to retrieve data about various statistics for NBA players and teams.

It is written in Python3 (should work for Python2 as well). 

Table of contents:

* [Installation](#installation)

* [Usage Instructions](#usage-instructions)

### Installation 

For installation of this package, all you have to do is clone repo
and invoke pip:

`git clone git@github.com:danchyy/nba_stats.git`

`cd nba_stats`

`pip install .`

### Usage Instructions

Here is a simple python code to retrieve data for Russell Westbrook using retriever factories:

```python
from nba_stats.retriever_factories.api_retriever_factory import ApiRetrieverFactory
name = "Russell Westbrook"
retriever = ApiRetrieverFactory.create_players_retriever_for_season()
player_id = retriever.get_player_id()
retriever = ApiRetrieverFactory.create_regular_shotchart_retriever_for_player(player_id=player_id,
                                                                              season="2017-18")
data = retriever.get_shotchart()
```