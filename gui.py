import statsinfo as stats
import tkinter as tk
from tkinter import ttk


class PickEmKickEm(tk.Tk):
    """
    Represents the GUI for the Pick 'Em Or Kick 'Em app
    """
    def __init__(self):
        """
        Initializes the starting frame for the app with a title, an entry box for a player name, and a button to proceed
            to the next frame
        """
        tk.Tk.__init__(self)
        self.title("Pick 'Em Or Kick 'Em (NBA Player Analyzer)")

        self.player_name = ""

        # Frame for player selection
        self.player_frame = tk.Frame(self)
        self.player_frame.pack(padx=20, pady=20)

        self.title = tk.Label(self.player_frame, text="Pick 'Em Or Kick 'Em", font=('Helvetica', 20, 'bold'))
        self.title.pack(pady=10)

        self.title = tk.Label(self.player_frame, text="Enter the full name of the player you want to check:")
        self.title.pack(pady=10)

        # Entry widget for player name
        self.player_entry = tk.Entry(self.player_frame, width=30)
        self.player_entry.pack(side=tk.LEFT, padx=5)

        # Button to choose player
        self.choose_button = tk.Button(self.player_frame, text="Choose Player", command=self.choose_player)
        self.choose_button.pack(side=tk.LEFT, padx=5)

    def choose_player(self):
        """
        Hides the starting frame and packs in the "Options" frame (Last 'N' Games, H2H Games, Player vs. Player)
        """
        # store the player name and change to the player option frame
        self.player_name = self.player_entry.get()
        self.player_frame.pack_forget()

        # new frame for your 3 analysis choice
        self.option_frame = tk.Frame(self)
        self.option_frame.pack(padx=20, pady=20)

        self.option_label = tk.Label(self.option_frame, text=f"Check {self.player_name}'s:",
                                     font=('Ubuntu', 10, 'bold'))
        self.option_label.pack(pady=10)

        # Last N Games Button
        self.last_n_games_button = tk.Button(self.option_frame, text='Last N Games Stats', command=self.last_n_games)
        self.last_n_games_button.pack(padx=10, pady=10)

        # H2H Button
        self.h2h_button = tk.Button(self.option_frame, text='H2H Stats', command=self.h2h_games)
        self.h2h_button.pack(padx=10, pady=10)

        # Player v. Player Button
        self.pvp_button = tk.Button(self.option_frame, text='Player vs. Player Stats', command=self.player_vs_player)
        self.pvp_button.pack(padx=10, pady=10)

    def last_n_games(self):
        """
        Hides the "Options" frame and packs in the "Last 'N' Games" frame where user enters in relevant info used for
            calculating the hit rate of the player based on their last 'n' games
        """
        self.option_frame.pack_forget()

        # new frame for last n game analysis
        self.last_n_games_frame = tk.Frame(self)
        self.last_n_games_frame.pack(padx=20, pady=20)
        self.last_n_games_label = tk.Label(self.last_n_games_frame, text=f"Check {self.player_name}'s Last 'N' Games",
                                           font=('Ubuntu', 10, 'bold'))
        self.last_n_games_label.grid(row=0, column=0, columnspan=2, padx=5, pady=5, sticky='n')

        # num of games entry widget
        nog_label = tk.Label(self.last_n_games_frame, text='Enter the last number of games:')
        nog_label.grid(row=1, column=0, sticky='w')
        self.num_of_games_entry = tk.Entry(self.last_n_games_frame)
        self.num_of_games_entry.grid(row=1, column=1, padx=5, pady=5)

        # stat menu widget
        stat_label = tk.Label(self.last_n_games_frame, text='Choose a stat to check:')
        stat_label.grid(row=2, column=0, sticky='w')
        self.stat_options = ['PTS', 'REB', 'AST', 'PRA', '3PM', 'DREB', 'OREB', '3PA', 'FTM', 'FGA', 'BLK', 'STL']
        self.chosen_stat_menu = ttk.Combobox(self.last_n_games_frame, values=self.stat_options)
        self.chosen_stat_menu.grid(row=2, column=1, padx=5, pady=5)

        # prop line entry widget
        prop_label = tk.Label(self.last_n_games_frame, text='Enter the prop-line:')
        prop_label.grid(row=3, column=0, sticky='w')
        self.prop_line_entry = tk.Entry(self.last_n_games_frame)
        self.prop_line_entry.grid(row=3, column=1, padx=5, pady=5)

        # over or under menu widget
        ou_label = tk.Label(self.last_n_games_frame, text='Over or under?:')
        ou_label.grid(row=4, column=0, sticky='w')
        self.over_under_options = ['OVER', 'UNDER']
        self.over_under_menu = ttk.Combobox(self.last_n_games_frame, values=self.over_under_options)
        self.over_under_menu.grid(row=4, column=1, padx=5, pady=5)

        # check hit rate button for last n games
        self.hit_rate_button = tk.Button(self.last_n_games_frame, text='Check Hit Rate',
                                         command=self.check_hit_rate_lng)
        self.hit_rate_button.grid(row=5, column=1, padx=5, pady=5)

    def h2h_games(self):
        """
        Hides the "Options" frame and packs in the "H2H Games" frame where user enters in relevant info used for
            calculating the hit rate of the player based on their H2H match ups
        """
        self.option_frame.pack_forget()

        # new frame for last n game analysis
        self.h2h_games_frame = tk.Frame(self)
        self.h2h_games_frame.pack(padx=20, pady=20)
        self.h2h_games_label = tk.Label(self.h2h_games_frame, text=f"Check {self.player_name}'s Head-To-Head Games",
                                           font=('Ubuntu', 10, 'bold'))
        self.h2h_games_label.grid(row=0, column=0, columnspan=2, padx=5, pady=5, sticky='n')

        # opposing team menu widget
        self.opp_team_label = tk.Label(self.h2h_games_frame, text=f'Choose the team {self.player_name} is going against:')
        self.opp_team_label.grid(row=1, column=0, sticky='w')
        self.opp_team_options = [
            'Celtics',
            'Nets',
            'Knicks',
            '76ers',
            'Raptors',
            'Bulls',
            'Cavaliers',
            'Pistons',
            'Pacers',
            'Bucks',
            'Hawks',
            'Hornets',
            'Heat',
            'Magic',
            'Wizards',
            'Nuggets',
            'Timberwolves',
            'Thunder',
            'Trail Blazers',
            'Jazz',
            'Warriors',
            'Clippers',
            'Lakers',
            'Suns',
            'Kings',
            'Mavericks',
            'Rockets',
            'Grizzlies',
            'Pelicans',
            'Spurs'
        ]
        self.opp_team_options.sort()
        self.opp_team_menu = ttk.Combobox(self.h2h_games_frame, values=self.opp_team_options)
        self.opp_team_menu.grid(row=1, column=1, padx=5, pady=5)

        # stat menu widget
        self.stat_label = tk.Label(self.h2h_games_frame, text='Choose a stat to check:')
        self.stat_label.grid(row=2, column=0, sticky='w')
        self.stat_options = ['PTS', 'REB', 'AST']
        self.chosen_stat_menu = ttk.Combobox(self.h2h_games_frame, values=self.stat_options)
        self.chosen_stat_menu.grid(row=2, column=1, padx=5, pady=5)

        # prop line entry widget
        self.prop_label = tk.Label(self.h2h_games_frame, text='Enter the prop-line:')
        self.prop_label.grid(row=3, column=0, sticky='w')
        self.prop_line_entry = tk.Entry(self.h2h_games_frame)
        self.prop_line_entry.grid(row=3, column=1, padx=5, pady=5)

        # over or under menu widget
        self.ou_label = tk.Label(self.h2h_games_frame, text='Over or under?:')
        self.ou_label.grid(row=4, column=0, sticky='w')
        self.over_under_options = ['OVER', 'UNDER']
        self.over_under_menu = ttk.Combobox(self.h2h_games_frame, values=self.over_under_options)
        self.over_under_menu.grid(row=4, column=1, padx=5, pady=5)

        # check hit rate button for all h2h games this season
        self.hit_rate_button = tk.Button(self.h2h_games_frame, text='Check Hit Rate',
                                         command=self.check_hit_rate_h2h)
        self.hit_rate_button.grid(row=5, column=1, padx=5, pady=5)

    def player_vs_player(self):
        """
        Hides the "Options" frame and packs in the "Player Vs. Player Games" frame where user enters in relevant info
         used for calculating the hit rate of the player based on their player vs. player match up when their opponent
          is on of off the court
        """
        self.option_frame.pack_forget()

        # new frame for pvp analysis
        self.pvp_frame = tk.Frame(self)
        self.pvp_frame.pack(padx=20, pady=20)
        self.pvp_label = tk.Label(self.pvp_frame, text=f"Check {self.player_name} Vs. This Player",
                                           font=('Ubuntu', 10, 'bold'))
        self.pvp_label.grid(row=0, column=0, columnspan=2, padx=5, pady=5, sticky='n')

        # opposing player entry widget
        opp_label = tk.Label(self.pvp_frame, text='Enter the name of the player you want to compare:')
        opp_label.grid(row=1, column=0, sticky='w')
        self.opp_entry = tk.Entry(self.pvp_frame)
        self.opp_entry.grid(row=1, column=1, padx=5, pady=5)

        # opp on or off court menu widget
        on_off_label = tk.Label(self.pvp_frame, text='Compare player on or off court:')
        on_off_label.grid(row=2, column=0, sticky='w')
        self.on_off_options = ['ON', 'OFF']
        self.on_off_menu = ttk.Combobox(self.pvp_frame, values=self.on_off_options)
        self.on_off_menu.grid(row=2, column=1, padx=5, pady=5)

        # stat menu widget
        stat_label = tk.Label(self.pvp_frame, text='Choose a stat to check:')
        stat_label.grid(row=3, column=0, sticky='w')
        self.stat_options = ['PTS', 'REB', 'AST']
        self.chosen_stat_menu = ttk.Combobox(self.pvp_frame, values=self.stat_options)
        self.chosen_stat_menu.grid(row=3, column=1, padx=5, pady=5)

        # prop line entry widget
        prop_label = tk.Label(self.pvp_frame, text='Enter the prop-line:')
        prop_label.grid(row=4, column=0, sticky='w')
        self.prop_line_entry = tk.Entry(self.pvp_frame)
        self.prop_line_entry.grid(row=4, column=1, padx=5, pady=5)

        # over or under menu widget
        ou_label = tk.Label(self.pvp_frame, text='Over or under?:')
        ou_label.grid(row=5, column=0, sticky='w')
        self.over_under_options = ['OVER', 'UNDER']
        self.over_under_menu = ttk.Combobox(self.pvp_frame, values=self.over_under_options)
        self.over_under_menu.grid(row=5, column=1, padx=5, pady=5)

        # check hit rate button for last n games
        self.hit_rate_button = tk.Button(self.pvp_frame, text='Check Hit Rate',
                                         command=self.check_hit_rate_pvp)
        self.hit_rate_button.grid(row=6, column=1, padx=5, pady=5)

    def check_hit_rate_lng(self):
        """
        Calculates and displays the hit rate of a players prop-line for a specific stat based on their last 'n' games
        """
        self.last_n_games_frame.pack_forget()

        # hit rate frame
        self.hit_rate_lng_frame = tk.Frame(self)
        self.hit_rate_lng_frame.pack(padx=20, pady=20)

        # important data needed to calculate hr
        num_of_games = int(self.num_of_games_entry.get())
        chosen_stat = self.chosen_stat_menu.get()
        prop_line = float(self.prop_line_entry.get())
        over_under = self.over_under_menu.get()
        player_id = stats.get_player_id(self.player_name)

        player_last_n_games = stats.player_last_n_games(player_id, num_of_games)
        player_stat_list = stats.get_spec_stats(player_last_n_games, chosen_stat)
        hit_rate = stats.over_under_hr(player_stat_list, prop_line, over_under)

        hr_label = tk.Label(self.hit_rate_lng_frame, text=hit_rate)
        hr_label.pack()

        # button to go back to player selection
        return_button = tk.Button(self.hit_rate_lng_frame, text='Return to Player Selection', command=self.lng_to_start)
        return_button.pack(padx=10, pady=10)

    def check_hit_rate_h2h(self):
        """
        Calculates and displays the hit rate of a players prop-line for a specific stat based on their H2H games
        """
        self.h2h_games_frame.pack_forget()

        # hit rate frame
        self.hit_rate_h2h_frame = tk.Frame(self)
        self.hit_rate_h2h_frame.pack(padx=20, pady=20)

        # important data needed to calculate hr
        chosen_stat = self.chosen_stat_menu.get()
        prop_line = float(self.prop_line_entry.get())
        over_under = self.over_under_menu.get()
        chosen_team = self.opp_team_menu.get()
        player_id = stats.get_player_id(self.player_name)
        opp_team_id = stats.get_team_id(chosen_team)
        all_h2h_games = stats.h2h_games(player_id, opp_team_id)
        h2h_stat_list = stats.get_spec_stats(all_h2h_games, chosen_stat)

        hit_rate = stats.over_under_hr(h2h_stat_list, prop_line, over_under)

        hr_label = tk.Label(self.hit_rate_h2h_frame, text=hit_rate)
        hr_label.pack()

        # button to go back to player selection
        return_button = tk.Button(self.hit_rate_h2h_frame, text='Return to Player Selection', command=self.h2h_to_start)
        return_button.pack(padx=10, pady=10)

    def check_hit_rate_pvp(self):
        """
        Calculates and displays the hit rate of a players prop-line for a specific stat based on their player vs. player
         match ups
        """
        self.pvp_frame.pack_forget()

        # hit rate frame
        self.hit_rate_pvp_frame = tk.Frame(self)
        self.hit_rate_pvp_frame.pack(padx=20, pady=20)

        # important data needed to calculate hr
        chosen_stat = self.chosen_stat_menu.get()
        prop_line = float(self.prop_line_entry.get())
        over_under = self.over_under_menu.get()
        on_off = self.on_off_menu.get()
        opp_name = self.opp_entry.get()
        player_team = stats.get_team_nickname_from_player(self.player_name)
        opp_team = stats.get_team_nickname_from_player(opp_name)
        player_vs_player_stats = stats.player_vs_player(self.player_name, opp_name, player_team,
                                                        opp_team, on_off)

        if player_vs_player_stats is not None:
            pvp_stat_list = stats.get_spec_stats(player_vs_player_stats, chosen_stat)
            hit_rate = stats.over_under_hr(pvp_stat_list, prop_line, over_under)
            hr_label = tk.Label(self.hit_rate_pvp_frame, text=hit_rate)
            hr_label.pack()
        else:
            hr_label = tk.Label(self.hit_rate_pvp_frame,
                                text='There are no stats for this match up against this player')
            hr_label.pack()

        # button to go back to player selection
        return_button = tk.Button(self.hit_rate_pvp_frame, text='Return to Player Selection', command=self.pvp_to_start)
        return_button.pack(padx=10, pady=10)

    def lng_to_start(self):
        """
        Redirects user from the "Last 'N' Games" Hit Rate frame to the starting frame
        """
        self.hit_rate_lng_frame.pack_forget()
        self.player_frame.pack(padx=20, pady=20)

    def h2h_to_start(self):
        """
        Redirects user from the "H2H" Hit Rate frame to the starting frame
        """
        self.hit_rate_h2h_frame.pack_forget()
        self.player_frame.pack(padx=20, pady=20)

    def pvp_to_start(self):
        """
        Redirects user from the "Player Vs. Player" Hit Rate frame to the starting frame
        """
        self.hit_rate_pvp_frame.pack_forget()
        self.player_frame.pack(padx=20, pady=20)
