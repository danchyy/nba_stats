# nba_stats

This project uses NBA's api to retrieve data about various statistics for NBA players and teams.

It is written in Python3. 

Table of contents:

* [Installation](#installation)

* [Usage Instructions](#usage-instructions)

### Installation 

You can install this package through pip system:

`pip3 install nba_stats`

### Usage Instructions

Here is a simple python code to retrieve data for Russell Westbrook using retriever factories:

```python
from nba_stats.retriever_factories.api_retriever_factory import ApiRetrieverFactory
name = "Russell Westbrook"
retriever = ApiRetrieverFactory.create_players_retriever_for_season()
player_id = retriever.get_player_id(name)
retriever = ApiRetrieverFactory.create_regular_shotchart_retriever_for_player(player_id=player_id,
                                                                              season="2017-18")
data = retriever.get_shotchart()
```

Following snippet retrieves league average data. This data comes with each and every retrieval of player's stats.
So we will just continue the previous example:

```python
...  # continued from prior example
league_average_data = retriever.get_league_averages()
```