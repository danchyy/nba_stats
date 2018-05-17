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
shotchart_retriever = ApiRetrieverFactory.create_regular_shotchart_retriever_for_player(player_id=player_id,
                                                                              season="2017-18")
data = shotchart_retriever.get_shotchart()
league_average_data = shotchart_retriever.get_league_averages()  # gets the league average data for each position

# You can filter the shotchart data based on zones, areas and ranges
areas = [u'Right Side(R)', u'Right Side Center(RC)']
zones = [u'Above the Break 3', u'Right Corner 3']
ranges = [u'24+ ft.']

filter_area = shotchart_retriever.get_shotchart_for_areas(areas)  # getting shotchart data only for given areas
filter_zones = shotchart_retriever.get_shotchart_for_zones(zones)  # getting shotchart data only for given zones
filter_ranges = shotchart_retriever.get_shotchart_for_ranges(ranges)  # getting shotchart data only for given ranges
filter_all = shotchart_retriever.get_shotchart_for_zones_areas_ranges(zones=zones, areas=areas, ranges=ranges)

# You can view the available areas, ranges and zones in documentation of specific methods.

```

The reason why factories are first mentioned is because there is a lot of parameters that have to be given 
to each retriever so that call can be made and some of those parameters are often not needed for simple retrieval of
stats. This way, Factories take care of giving users what they need without needing to care about other parameters.


However, you can directly use players retriever:

```python
from nba_stats.retrieval.players_retriever import PlayersRetriever
retriever = PlayersRetriever()
player_data = retriever.get_player(player_name="LeBron James")
``` 

Or you can use shot chart retriever to get data for shots:

```python
from nba_stats.retrieval.shotchart_retriever import ShotchartRetriever
westbrook_id = "201566"
retriever = ShotchartRetriever(player_id=westbrook_id)
shotchart_data = retriever.get_shotchart()
```
