# imported packages
from nba_api.stats.static import players
from nba_api.stats.endpoints import playergamelog
from nba_api.stats.static import teams
from nba_api.stats.endpoints import boxscoretraditionalv2
from nba_api.stats.endpoints import teamgamelog
from nba_api.stats.endpoints import playergamelogs
from nba_api.stats.endpoints import teamgamelogs
from nba_api.stats.endpoints import commonplayerinfo
import pandas as pd


def get_team_nickname_from_player(player):
    """
    Get the team nickname (Suns, Lakers, Nuggets etc.) of a player

    :param player: The full name of an active NBA player
    :type player: str
    :return: The team nickname of a player
    :rtype: str
    """
    team_info = commonplayerinfo.CommonPlayerInfo(player_id=get_player_id(player)).common_player_info.get_data_frame()
    team_id = team_info['TEAM_ID'].iloc[0]  # Get the first team ID, assuming it's the current team
    nba_teams = teams.get_teams()
    for team in nba_teams:
        if team['id'] == team_id:
            return team['nickname']


def player_last_n_games(player_id, num_of_games):
    """
    Get the last "n" game logs of a player

    :param player_id: The player id of an active NBA player
    :type player_id: str
    :param num_of_games: The chosen number of games
    :type num_of_games: int
    :return: The last "n" game logs of a player
    :rtype: pandas.DataFrame
    """
    player_games = playergamelog.PlayerGameLog(player_id=player_id, season_type_all_star='Regular Season',
                                               league_id_nullable='00')
    games_df = player_games.get_data_frames()[0]
    return games_df.head(n=num_of_games)


def get_game_ids_from_player(player_games_df):
    """
    Retrieve the game ID(s) from the game log of a player

    :param player_games_df: The game logs of an active NBA player
    :type player_games_df: pandas.DataFrame
    :return: A list of the game ID(s) of the games that the player played in
    :rtype: list
    """
    return player_games_df['Game_ID'].tolist()


def get_spec_stats(player_games_df, stat):
    """
    Get the specific stats from a players game log (PTS, REB, AST, etc.)

    :param player_games_df: The game log of an active NBA player
    :type player_games_df: pandas.DataFrame
    :param stat: The specific stat to be chosen from the players game log
    :type stat: str
    :return: A list of the chosen stat column from a players game log
    :rtype: list
    """
    stat_dict = {
        'PTS': player_games_df['PTS'].tolist(),
        'REB': player_games_df['REB'].tolist(),
        'AST': player_games_df['AST'].tolist(),
        'PRA': (player_games_df['PTS'] + player_games_df['REB'] + player_games_df['AST']).tolist(),
        '3PM': player_games_df['FG3M'].tolist(),
        'DREB': player_games_df['DREB'].tolist(),
        'OREB': player_games_df['OREB'].tolist(),
        '3PA': player_games_df['FG3A'].tolist(),
        'FTM': player_games_df['FTM'].tolist(),
        'FGA': player_games_df['FGA'].tolist(),
        'BLK': player_games_df['BLK'].tolist(),
        'STL': player_games_df['STL'].tolist()
    }
    return stat_dict[stat]


def over_under_hr(stat_list, prop_line, o_or_u):
    """
    Find the hit-rate of a prop line of a players "n" games (Over 18.5 pts, Under 3.5 reb, etc.)

    :param stat_list: The list of a players specific stat though out "n" games
    :type stat_list: list
    :param prop_line: The prop line for a stat
    :type prop_line: float
    :param o_or_u: Over or under a prop-line
    :type o_or_u: str
    :return: The hit-rate percentage of the prop line for the chosen stat
    :rtype: float
    """
    total_hits = 0
    if o_or_u == 'OVER':
        for stat in stat_list:
            if stat > prop_line:
                total_hits += 1
    elif o_or_u == 'UNDER':
        for stat in stat_list:
            if stat < prop_line:
                total_hits += 1

    if len(stat_list) == 0:
        return 'There are no available stats for this prop'
    else:
        hit_rate = total_hits/len(stat_list)
        return f'This line has hit {total_hits} of the last {len(stat_list)} games, with a hit rate of {hit_rate*100}%'


def get_player_id(player_name):
    """
    Get a players ID

    :param player_name: The full name of an NBA player
    :type player_name: str
    :return: The player ID of the player
    :rtype: str
    """
    active_players = players.get_active_players()
    for person in active_players:
        if person['full_name'] == player_name:
            nba_player_id = person['id']
            return nba_player_id


def get_team_id(team_name):
    """
    Get a teams ID

    :param team_name: The nickname of a team (Pistons, Pacers, Timberwolves, etc.)
    :type team_name: str
    :return: The team ID of the team
    :rtype: str
    """
    nba_teams = teams.get_teams()
    for team in nba_teams:
        if team['nickname'] == team_name:
            team_id = team['id']
            return team_id


def get_team_starters(team_id):
    """
    Retrieves all the names of a teams starting 5

    :param team_id: The team ID of a team
    :type team_id: str
    :return: A list of the names of a teams starting 5
    :rtype: list
    """
    game_id = get_game_id_from_teams(team_id)
    game_box_score = boxscoretraditionalv2.BoxScoreTraditionalV2(game_id=game_id)
    player_stats_data = game_box_score.player_stats.get_data_frame()
    team_starters = player_stats_data[
        (player_stats_data['TEAM_ID'] == team_id) & (player_stats_data['START_POSITION'] != '')]
    return team_starters['PLAYER_ID'].tolist()


def get_game_id_from_teams(team_id):
    """
    Get all the game IDs from the games the team played in

    :param team_id: The team ID of the team
    :type team_id: str
    :return: The list of all the game IDs that the team played in
    :rtype: list
    """
    game_log = teamgamelog.TeamGameLog(season='2024-25', season_type_all_star='Regular Season', team_id=team_id)
    game_log_df = game_log.team_game_log.get_data_frame()
    game_id = game_log_df['Game_ID'].tolist()
    return game_id


def h2h_games(player_id, opp_team_id):
    """
    Get all the games that player and a chosen opponent faced off against ("Head 2 Head" games)

    :param player_id: The player ID of the player
    :type player_id: str
    :param opp_team_id: The player ID of the opposing player
    :type opp_team_id: str
    :return: The head-to-head game logs between the two chosen players
    :rtype: pandas.DataFrame
    """
    player_h2h_games = playergamelogs.PlayerGameLogs(player_id_nullable=player_id,
                                                     opp_team_id_nullable=opp_team_id,
                                                     season_type_nullable='Regular Season',
                                                     season_nullable='2024-25')
    player_h2h_games_df = player_h2h_games.player_game_logs.get_data_frame()
    return player_h2h_games_df


def get_all_h2h_games(team1_name, team2_name):
    """
    Get all the game IDs of the games that a team and a chosen opposing team faced off against ("Head 2 Head" games)

    :param team1_name: The nickname of the team (Heat, Rockets, Warriors, etc.)
    :type team1_name: str
    :param team2_name: The nickname of the opposing team (76ers, Nets, Spurs, etc.)
    :type team2_name: str
    :return: A list of the head-to-head game IDs between the two chosen teams
    :rtype: list
    """
    t1games = teamgamelogs.TeamGameLogs(team_id_nullable=get_team_id(team1_name),
                                        season_nullable='2024-25').team_game_logs.get_data_frame()

    t2games = teamgamelogs.TeamGameLogs(team_id_nullable=get_team_id(team2_name),
                                        season_nullable='2024-25').team_game_logs.get_data_frame()

    t1game_set = set(t1games['GAME_ID'].tolist())
    t2game_set = set(t2games['GAME_ID'].tolist())

    intersection = list(t1game_set.intersection(t2game_set))
    return intersection


def find_games_player_not_play(player_name, team1_name, team2_name):
    """
    Find the game IDs of the head-to-head games that a player missed (off court)

    :param player_name: The full name of an NBA player
    :type player_name: str
    :param team1_name: The nickname of the team (Heat, Rockets, Warriors, etc.)
    :type team1_name: str
    :param team2_name: The nickname of the opposing team (76ers, Nets, Spurs, etc.)
    :type team2_name: str
    :return: The list of game IDs of the players missed head-to-head games
    :rtype: list
    """
    players_game_log = playergamelog.PlayerGameLog(get_player_id(player_name)).player_game_log.get_data_frame()
    all_h2h_game = set(get_all_h2h_games(team1_name, team2_name))
    game_id_log = set(players_game_log['Game_ID'].tolist())
    intersection = all_h2h_game.intersection(game_id_log)
    all_h2h_game -= intersection
    missed_games = list(all_h2h_game)
    return missed_games


def player_vs_player(player_name, opp_name, team1_name, team2_name, on_off_court):
    """
    Find the game logs of a player vs. another player when they're on or off the court

    :param player_name: The name of an NBA player
    :type player_name: str
    :param opp_name: The name of an opposing NBA player
    :type opp_name: str
    :param team1_name: The nickname of the opposing team (76ers, Nets, Spurs, etc.)
    :type team1_name: str
    :param team2_name: The nickname of the team (Heat, Rockets, Warriors, etc.)
    :type team2_name: str
    :param on_off_court: Whether player is on or off the court
    :type on_off_court: str
    :return: The head-to-head game logs of when the opposing player is on or off the court
    :rtype: pandas.DataFrame
    """
    player_id = get_player_id(player_name)

    if on_off_court == 'ON':
        h2h_games_list = get_all_h2h_games(team1_name, team2_name)
        opp_missed_games = set(find_games_player_not_play(opp_name, team1_name, team2_name))
        h2h_games_list = list(set(h2h_games_list) - opp_missed_games)  # Convert both to sets for set difference
        game_df = []
        for game_id in h2h_games_list:
            game_df.append(get_player_box_score(game_id, player_id))
        if len(game_df) > 0:
            return pd.concat(game_df, ignore_index=True)
        else:
            print("No games found.")
            return None
    elif on_off_court == 'OFF':
        h2h_games_list = get_all_h2h_games(team1_name, team2_name)
        opp_missed_games = set(find_games_player_not_play(opp_name, team1_name, team2_name))
        h2h_games_list = list(set(h2h_games_list) - opp_missed_games)  # Convert both to sets for set difference
        game_df = []
        if len(opp_missed_games) == 0:
            print('No missed games!')
            for game_id in h2h_games_list:
                game_df.append(get_player_box_score(game_id, player_id))
            if len(game_df) > 0:
                return pd.concat(game_df, ignore_index=True)
            else:
                print("No games found.")
                return None
        else:
            for game_id in opp_missed_games:
                game_df.append(get_player_box_score(game_id, player_id))
            if len(game_df) > 0:
                return pd.concat(game_df, ignore_index=True)
            else:
                print("No games found.")
                return None


def get_player_box_score(game_id, player_id):
    """
    Find a players box score of a specific game

    :param game_id: The game ID of the game
    :type game_id: str
    :param player_id: The player ID of the player
    :type player_id: str
    :return: The box score of the player for that specific game
    :rtype: pandas.DataFrame
    """
    # Get the box score for the specific game
    box_score = boxscoretraditionalv2.BoxScoreTraditionalV2(game_id=game_id)
    box_score_df = box_score.player_stats.get_data_frame()

    # Filter the box score for the player's statistics
    player_box_score = box_score_df[box_score_df['PLAYER_ID'] == player_id]
    return player_box_score
