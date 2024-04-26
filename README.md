

# Pick 'Em Or Kick 'Em

https://github.com/khoamelo/pickemkickem/assets/123230736/b60bafbd-ab61-4d92-a123-f56e9de590fb

An app designed to help sports bettors choose NBA props with the best chances of hitting by calculating the "hit rate" of a prop that the user wants to check. The app can check
the hit rate of a prop for:
(1) The last "n" games that a player played in
(2) The "head-to-head" games that a player played in
(3) The games where a player faced off against a specific player when they're on or off the court  

FYI: This app uses data from 2023-24 regular season of the NBA, so it's excluding the playoffs.

## Installation

### Using PyCharm (because that's what I used)

1. Clone the repository in PyCharm:
   - Go to `Git` > `Clone`.
   - Enter the repository URL: `https://github.com/khoamelo/pickemkickem.git`.
   - Choose the directory where you want to save the project and click `Clone`.

2. Set up the Python interpreter:
   - Open the project in PyCharm.
   - Go to `File` > `Settings` > `Project: parlaypredictor` > `Python Interpreter`.
   - Click on the gear icon and select `Add`.
   - Choose `Existing environment` and select `Python 3.12`.
   - Click `OK` to confirm.

3. Install the required dependencies:
   - Click on the `Python Packages` icon and install the following packages:
     - nba_api v1.4.1
     - pandas v2.2.2
    
4. Run the app:
   - Open `main.py` in PyCharm.
   - Right-click on the file and select `Run 'main'`.

## Usage

Once you have installed, you can either right-click on the file and select `Run 'main'`, or execute the following command in the terminal: python main.py

A GUI will be launched which will prompt you to enter in the name of an NBA player you wish to analyze:
![projectss1](https://github.com/khoamelo/pickemkickem/assets/123230736/5a3638fa-412c-4179-9e40-2e8dc0483562)

Once you enter in the FULL name of the NBA player (De'Aaron Fox, LeBron James, etc.) and press the choose player button, it will then prompt you to calculate the hit rate of a specific prop of a player based on:
(1) The last "n" games that they played in
(2) The "head-to-head" games that they played in
(3) The games where they faced off against a specific player when they're on or off the court

![projectss2](https://github.com/khoamelo/pickemkickem/assets/123230736/37935d14-75da-4a8f-be02-6fb0aaa5b528)


Choose one of the three options and you will be asked to fill in and choose specific details that will help calculate the hit rate of a players prop:


![image](https://github.com/khoamelo/pickemkickem/assets/123230736/bd48a3fa-4657-4099-b16e-da0435eb1759)
![image](https://github.com/khoamelo/pickemkickem/assets/123230736/388d1a8d-4655-42b8-a849-dd2ccd859c55)
![image](https://github.com/khoamelo/pickemkickem/assets/123230736/636b5331-b2ad-494a-b21d-50f2a779a91f)


After you enter fill out all the required details, it will calculate how often the prop for that player hits based on the factor you chose and the hit rate percentage, and you can press the 'Return to Player Section' button to check more players:

![image](https://github.com/khoamelo/pickemkickem/assets/123230736/3e22bbd4-3cb2-43ea-a53a-bbcdbfac77f1)
![image](https://github.com/khoamelo/pickemkickem/assets/123230736/a250b682-9c56-423a-a3c5-b2c90e51a588)
![image](https://github.com/khoamelo/pickemkickem/assets/123230736/95ef7f05-4024-414d-995e-e5199726699a)


