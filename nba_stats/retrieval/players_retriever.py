from nba_stats.retriever_factories.api_retriever import ApiRetriever
from nba_stats.utils import constants


class PlayersRetriever(ApiRetriever):

    def __init__(self, league_id="00", season=constants.CURRENT_SEASON, is_only_current_season=1):
        """
        Constructor for retrieval of players.

        :param league_ID: ID of the league, either 00, 20 or 10 (00 is normal NBA).
        :param season: Format of yyyy-yy.
        :param is_only_current_season: 1 marks that only current season is watched, 0 otherwise.
        """
        super().__init__(constants.PLAYERS_PARAM)
        self.league_id = league_id
        self.season = season
        self.is_only_current_season = is_only_current_season
        self.build_param_value_dict()

    def build_param_value_dict(self):
        """
        Builds parameter dictionary for retrieval of shotchart data.
        """
        self.param_dict["LeagueID="] = self.league_id
        self.param_dict["Season="] = self.season
        self.param_dict["Isonlycurrentseason="] = self.is_only_current_season

    def get_players(self):
        """
        Returns DataFrame with all players based on parameters set for API call.

        :return: DataFrame which contains data about every player in given season/league.
        """
        return self.load_nba_dataset(index=0)

    def get_player(self, player_name):
        """
        Returns one row from DataFrame based on the name of player.

        :param player_name: Name of the player whose data wants to be retrieved.
        :return: Row from DataFrame if that player exists, otherwise empty row.
        """
        pandas_data = self.get_players()
        return pandas_data.loc[pandas_data.DISPLAY_FIRST_LAST.str.lower() == player_name.lower()]

    def get_player_id(self, player_name):
        """
        Returns player id based on player's name.

        :param player_name: Name of the player whose ID wants to be retrieved.
        :return: player's id, used for further fetching of data.
        """
        player_data = self.get_player(player_name)
        return player_data.iloc[0].PERSON_ID
