# Discord-Drop-Auto-Buyer
Used during 2020 to purchase a PlayStation 5 from Discord drops. This script utilizes Selenium, Beautiful Soup 4, LXML, and Webdriver Manager to quickly click on new links in a certain discord drop page and automatically try to purchase them. If purchase is not made within 20 attempts, reroute back to discord page to continue trying.

to install reqruired dependencies run
"""
pip install -r requirements.txt 
"""

Make sure you open "creds.txt" and input your Discord email and password in the text fields. This will be used to automatically log-in and start the purchasing loop.

Open "discord_listen.py" and change the value of "url2" to whichever discord room you want the bot to target.
Included are some standard ones for RTX 30 series, PS5, and Xbox Series S room links.

Once that is completed, run
"""
python discord_listen.py
"""

Enjoy and good luck!
