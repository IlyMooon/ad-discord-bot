import discum
import time
import os
from pystyle import *
import json
import threading


#Open config file
def load_config():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    config_path = os.path.join(base_dir, "config.json")
    
    with open(config_path, "r", encoding="utf-8") as file:  # Spécifie l'encodage
        return json.load(file)


# Mettre un titre à la console
System.Title("Automated Advertising Bot - By IlyMoon")

#Showing initializing before starting the actual script
print("Initializing script...")
print("Starting in a second, please wait.")

# Vars needed in order to make the user experience a lot better below

command = "nothing"

username=os.getlogin()
commandline=f"{username}@windows:~$ "

def selectchoice():
    global command
    command = Write.Input(f"{commandline} ", Colors.green, interval=0.00005)

def cc():
    System.Clear()

#ASCII Art
logo="""
░█████╗░██╗░░░██╗████████╗░█████╗░███╗░░░███╗░█████╗░████████╗███████╗██████╗░
██╔══██╗██║░░░██║╚══██╔══╝██╔══██╗████╗░████║██╔══██╗╚══██╔══╝██╔════╝██╔══██╗
███████║██║░░░██║░░░██║░░░██║░░██║██╔████╔██║███████║░░░██║░░░█████╗░░██║░░██║
██╔══██║██║░░░██║░░░██║░░░██║░░██║██║╚██╔╝██║██╔══██║░░░██║░░░██╔══╝░░██║░░██║
██║░░██║╚██████╔╝░░░██║░░░╚█████╔╝██║░╚═╝░██║██║░░██║░░░██║░░░███████╗██████╔╝
╚═╝░░╚═╝░╚═════╝░░░░╚═╝░░░░╚════╝░╚═╝░░░░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░╚══════╝╚═════╝░

░█████╗░██████╗░██╗░░░██╗███████╗██████╗░████████╗██╗░██████╗██╗███╗░░██╗░██████╗░  ██████╗░░█████╗░████████╗
██╔══██╗██╔══██╗██║░░░██║██╔════╝██╔══██╗╚══██╔══╝██║██╔════╝██║████╗░██║██╔════╝░  ██╔══██╗██╔══██╗╚══██╔══╝
███████║██║░░██║╚██╗░██╔╝█████╗░░██████╔╝░░░██║░░░██║╚█████╗░██║██╔██╗██║██║░░██╗░  ██████╦╝██║░░██║░░░██║░░░
██╔══██║██║░░██║░╚████╔╝░██╔══╝░░██╔══██╗░░░██║░░░██║░╚═══██╗██║██║╚████║██║░░╚██╗  ██╔══██╗██║░░██║░░░██║░░░
██║░░██║██████╔╝░░╚██╔╝░░███████╗██║░░██║░░░██║░░░██║██████╔╝██║██║░╚███║╚██████╔╝  ██████╦╝╚█████╔╝░░░██║░░░
╚═╝░░╚═╝╚═════╝░░░░╚═╝░░░╚══════╝╚═╝░░╚═╝░░░╚═╝░░░╚═╝╚═════╝░╚═╝╚═╝░░╚══╝░╚═════╝░  ╚═════╝░░╚════╝░░░░╚═╝░░░
by IlyMoon / https://github.com/IlyMooon
"""

# Menu de démarrage
def startmenu():
    cc()
    Write.Print(f"{logo}", Colors.green, interval=0.000005)
    Write.Print("\n-=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=-", Colors.green, interval=0.00005)
    print(Colors.green + "\nuse help command to get help about")


#Start menu launch
startmenu()

#Load config in the right var
config = load_config()

while True:
    selectchoice()

# Vérifier le choix de l'utilisateur
    if command == "start":
        cc()
        Write.Print("Bot starting with actual config file...\n", Colors.green, interval=0.00005)
    
        # L'utilisateur a choisi d'exécuter le script
        token = config["token"]
        channel_ids = config["channel_ids"]
        message = config["message"]

        bot = discum.Client(token=token, log=False)

        # Fonction pour envoyer les messages
        def send_ads():
            for channel_id in channel_ids:
                try:
                    bot.sendMessage(channel_id, message)
                    Write.Print(f"Ad sent in channel : {channel_id}\n", Colors.light_green, interval=0.00005)
                except Exception as e:
                    Write.Print(f"Error while sending ad in the channel {channel_id}: {e}\n", Colors.red, interval=0.00005)
                time.sleep(3)  # Wait time before sending next ad

            Write.Print("All advertisements were sent, you can close the program.\nLaunching menu in 5 seconds.", Colors.light_green, interval=0.005)
            time.sleep(5)  # sleeping 5 secondes before returning to menu

        # Lancer le bot dans un thread
        threading.Thread(target=bot.gateway.run, kwargs={"auto_reconnect": True}).start()

        # Attendre un moment pour permettre à la connexion de s'établir
        time.sleep(3)
        System.Title("Advertising in Progress - By IlyMoon")
        send_ads()
        System.Title("Automated Advertising Bot - By IlyMoon")
        cc()
        startmenu()
        Write.Print("All ads were sent 5 seconds ago, thanks for using this script !", Colors.light_green, interval=0.00005)

    elif command == "help":
        Write.Print(f"Here are all the commands available :\nstart - Run the bot using actual configuration\neditconfig - launch notepad to edit the config file\nhelp - open the commands help\nexit - close the program\n", Colors.green, interval=0.00005)
    
    elif command == "editconfig":
        config_file_path = "config.json"
        # Open the config json
        os.system(f"notepad {config_file_path}")
        Write.Print("Press enter when you have edited the config file and saved it.\n", Colors.green, interval=0.00005)
        Write.Input("Please note that if the config file is wrongly edited, the bot won't work !\n", Colors.red, interval=0.00005)
        Write.Print("Updating config file...\n", Colors.green, interval=0.00005)
        config = load_config()
        Write.Print("Updated !\n", Colors.light_green, interval=0.00005)
        time.sleep(2)
    elif command == "exit":
        exit()

    else:
        Write.Print(f"{command} isn't recognized as an internal command, please check the spelling.\n", Colors.red, interval=0.00005)


