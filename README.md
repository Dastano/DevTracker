# DevTracker - Discord Bot

### Features

- Tracks Messages of a specific Role Name or ID
- Post Messages of tracked roles in channel(s) you like!
- Blacklist Channels you do not want to be tracked

### Example

![Example](https://i.imgur.com/f4KELUP_d.webp?maxwidth=760&fidelity=grand "Example Image of the Discord Bot")



### Setup / Requirements
https://pypi.org/project/discord.py/

### Usage
    1. Replace <Token here> with your Discord Bot Token without <> in bot.py
    2. Modify rolesToWatch to your needs
    3. Set useRoleIds to either True or False, depending on your rolesToWatch Setup.
    4. Change the Icon URL on Line 74
    5. Modify the Channel Blocklist, to stop tracking Private channels.
    For more Details, check examples.

### Examples

          
        
````python
TOKEN = '12512515.5125125' # example
useRoleIds = True
rolesToWatch = [{'role': 1088148992514338836, 'channels': [ 1088231599025422356, 1088231613298647101], 'blacklistedChannels':[]}]


TOKEN = '12512515.5125125' # example
useRoleIds = False
rolesToWatch =[{'role': 'Developer', 'channels': [ 1088231599025422356, 1088231613298647101]},{'role': 'TestRole', 'channels': [ 1088231599025422356], 'blacklistedChannels':[]}]
````

### Others
If you want to modify the Message of the Bot, I recommend reading:
https://python.plainenglish.io/python-discord-bots-formatting-text-efca0c5dc64a


### Credits
inspired by https://github.com/OniSensei/Role-Message-Tracker
Who got inspired by me ^.^

Wanted to give it a shot myself, to get an Open Source Version up and running in Python.
