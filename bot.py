import discord

#
# Powered by Feylinchen#1234
# inspired by https://github.com/OniSensei/Role-Message-Tracker
# who was inspired by Me ^.^
# open Source Python Variant
#
# Multiple Roles + Channels are supported!
#
# Usage:
# 1. TOKEN = Set your Bot Token
# 2. Modify rolesToWatch by your needs.
#   Either use IDs of Roles, to track invisible Roles or use Role Names.
#   If you want to use IDs, make sure "useRoleIDs" is True
#
# Example with Names:
# [{'role': 'Developer', 'channels': [ 1088231599025422356, 1088231613298647101], 'blacklistedChannels':[]}]
#
#
# Example with IDs: rolesToWatch = [{'role': 1088148992514338836, 'channels': [ 1088231599025422356,
# 1088231613298647101], 'blacklistedChannels':[]}]
#
# NEW! Use Keyword, to track messages. Add the Keyword INFRONT of your message, to make sure it gets tracked.
#
# To Modify the Style of the Message
# I recommend reading: https://python.plainenglish.io/python-discord-bots-formatting-text-efca0c5dc64a
# Chapter: Multiline Code Blocks


TOKEN = '<Your token here>'
useRoleIds = True
keyword = '!dt'
useKeyword = True

rolesToWatch = [{'role': 1088148992514338836, 'channels': [1088231599025422356, 1088231613298647101],
                 'blacklistedChannels': [662383121689477151, 362646267974647820]},
                {'role': 662383376115957770, 'channels': [1088231675605033040], 'blacklistedChannels': []}]


def search(role, message):
    if useRoleIds:
        for p in message.author.roles:
            if int(p.id) == role:
                return True
        return False
    else:
        for p in message.author.roles:
            if str(p) == role.strip():
                return True
        return False


def checkblacklist(channelid, channels):
    for channel in channels:
        if channel == int(channelid):
            print('Forbidden channel, do not track')
            return True
    return False


def notContainsKeyword(message):
    if keyword not in message.content or not message.content.startswith(keyword):
        return True
    return False


def run_discord_bot():
    intents = discord.Intents.all()

    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f'{client.user} is now running')

    @client.event
    async def on_message(message):
        print("message recieved")
        alreadyReplaced = False
        if message.author == client.user:
            return
        for item in rolesToWatch:
            # check if the Channel is Blacklisted
            if checkblacklist(int(message.channel.id), item.get('blacklistedChannels')):
                return
            # check for Role and copy message
            if search(item.get('role'), message):
                channels = item.get('channels')
                for cn in channels:
                    if useKeyword and notContainsKeyword(message):
                        return
                    elif not alreadyReplaced:
                        print("in else")
                        messageCopy = message.content.replace(keyword, "", 1)
                        alreadyReplaced = True
                    channel = client.get_channel(cn)
                    embed = discord.Embed(
                        description=messageCopy,
                        color=discord.Color.blue())
                    embed.set_author(name=str(message.author)[:-5],  # remove [:5] if you want to keep the full
                                     # Discord ID
                                     icon_url="<icon url here>")  # URL to your Icon
                    embed.set_thumbnail(url=message.author.avatar)
                    embed.add_field(name="Jump to Original Message:", value="[View](" + message.jump_url + ")",
                                    inline=False)
                    await channel.send(embed=embed)
    client.run(TOKEN)
