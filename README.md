

## 🛠️ DEPLOYMENT ON LOCAL HOST / VPS

Initiate deployment with these sophisticated steps:

```bash
sudo apt-get update && sudo apt-get upgrade -y           # 1. Upgrade and Update System

sudo apt-get install python3-pip -y          # 2. Install Required Packages

sudo pip3 install -U pip          # 3. Upgrade Pip

git clone https://github.com/Infamous-Hydra/YaeMiko && cd YaeMiko           # 4. Clone the Repository

pip3 install -U -r requirements.txt          # 5. Install Required Packages

vi variables.py           # 6. Modify Variables
# Press `I` to begin editing. Press `Ctrl+C` to save, then `:wq` or `:qa` to exit.

sudo apt install tmux && tmux           # 7. Install Tmux (Optional)

python3 -m Mikobot         # 8. Run the Bot
# Press `Ctrl+b` and then `d` to exit Tmux Session
```
━━━━━━━━━━━━━━━━━━━━

<h1 align="center">Deploy on Heroku</h1>

<p align="center">Click the button below to deploy YAE ダ MIKO on Heroku and enjoy its enhanced features and user-friendly interface!</p>

<p align="center">
    <a href="https://heroku.com/deploy?template=https://github.com/Infamous-Hydra/YaeMiko">
        <img src="https://www.herokucdn.com/deploy/button.svg" alt="Deploy">
    </a>
</p>

<h1 align="center"><img src="./.github/yae-miko.gif" /></h1>

## CREDITS
The foundation of the application is rooted in the initial efforts undertaken by [PaulSonOfLars](https://github.com/PaulSonOfLars)
+ [lostb053](https://github.com/lostb053) > Anime
+ [TheHamkerCat](https://github.com/TheHamkerCat) > Python-Arq
+ [ProjectCodeX](https://github.com/Team-ProjectCodeX) > Modules

Others in the commit history and files. If anything is missing, feel free to  [![gmail](https://img.shields.io/badge/mail-Here-red?style=for-the-badge&logo=gmail)](mailto:makandu2054@gmail.com)  or submit a pull request.

> Try this bot [@MIKO_V2BOT](https://t.me/MIKO_V2BOT); it's made with this repository for demonstration purposes.
