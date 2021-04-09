
###-------------START HERE--------------------###

"""

    1. download Python : https://www.python.org/ftp/python/3.9.4/python-3.9.4-amd64.exe
    make sure when you're installing it you select 'Add to .PATH' in the installation Wizzard.

    2. Run CMD and enter these commands one after the other:
                pip install -U discord.py
                pip install requests
                pip install lxml
                pip install bs4

    3. Create a discord channel you want your bot to hangout in.

    4. Create an account at https://discord.com/developers

    5. Create a New Application (Bot)

    6. Once you've selected your Application go to: OAuth2 > Scopes **Select bot** > Bot permissions **Select Administrator**

    7. Under Scopes you should see a new link.
    Going to that link will take you to discord where you can select which channel you authorize your bot to opperate in.

    8. After these steps yor bot is ready to go. Now fill out the intializers below.

"""

#Initializers------>>

#---------------------TIME DELAY------------------------------------

#This is the time (in seconds) the script will wait before sending an HTTP request to AMD's servers.
#Less time means the bot will be faster but AMD might flag your IP.
refreshDelay = .5 

#-------------------------TOKEN-------------------------------------

#This is the Authorization Token of your DiscordBot. This is found under your Discord Developer Portal > Select your Bot > Bot > Token
TOKEN = ""

#-------------------------GUILD--------------------------------------

#This is the ID of the discord channel you want the bot to message when it finds an item in stock.
#You can find this by going into the discord channel and right clicking the channel-name in the top left of the screen.
#There will be an option to 'Copy ID'
GUILD = ""

#-------------------------FILE LOCATION------------------------------

#this is the path of your links.txt file with the AMD links.
#Leave this default if the file is in the same dir as the script.
linkFile = "links.txt"

#------------------------OPTIONAL------------------------------------

#This will run the script as normal but it will print off the stock of each item.
#run this to make sure the bot is gathering information correctly and to see custom error messages.

debug = True
