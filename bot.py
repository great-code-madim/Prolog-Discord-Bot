import discord, pyswip, traceback, os

def write_kb(kbContent, kbName):
    print(kbName)
    try:
        with open(kbName + '.pl', "w") as kbFile:
            kbFile.write(kbContent + "\n")
        return "KB saved."
    except Exception as e:
        return e

def deleteKb(kbName):
    import os
    try:
        if os.path.exists(kbName + ".pl"):
            os.remove(kbName + ".pl")
            return "Knowledge base " + kbName + " deleted."
        else:
            return("The file does not exist")

    except Exception as e:
        return e

def prolog_query(query, kbName):
    prolog = pyswip.Prolog()
    prolog.consult(kbName + ".pl")
    try:
        return list(prolog.query(query))
    except Exception as e:
        traceback.print_exc()
        return e

def prolog_assert(assertion, kbName):
    prolog = pyswip.Prolog()
    prolog.consult(kbName + ".pl")
    try: 
        result = list(prolog.query(assertion))

        if result == []:
            return "No"
        elif result == [{}]:
            return "Yes"

    except Exception as e:
        traceback.print_exc()
        return e


client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    target = "".join((message.content.split(' ', 1)[1]).split(" ")[:-1])
    kbName = message.content.split(' ', 1)[1].split(" ")[-1]
    if message.content.__contains__('bot'):
        await message.channel.send('what')

    if message.content.startswith('!consult'):
        print(target)
        await message.channel.send(write_kb(target, kbName))

    if message.content.startswith('!query'):
        await message.channel.send(prolog_query(target, kbName))

    if message.content.startswith('!delete'):
        await message.channel.send(deleteKb(kbName))

    if message.content.startswith('!assert'):
        await message.channel.send(prolog_assert(target, kbName))


client.run('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')


