import random
import time

from twitchio.ext import commands
from twitchio.client import Client

import credentials


CHANNEL = credentials.CHANNEL
NAME = credentials.NAME
TWITCH_TOKEN = credentials.TWITCH_TOKEN
TWITCH_CLIENT_ID = credentials.TWITCH_CLIENT_ID
TWITCH_CLIENT_SECRET = credentials.TWITCH_CLIENT_SECRET

bot = commands.Bot(
    irc_token=TWITCH_TOKEN,
    client_id=TWITCH_CLIENT_ID,
    nick=NAME,
    prefix='!',
    initial_channels=CHANNEL,
)


client = Client(
    client_id=TWITCH_CLIENT_ID,
    client_secret=TWITCH_CLIENT_SECRET,
)


@bot.event
async def event_message(ctx):
    print(ctx.author)
    print(ctx.content)
    await bot.handle_commands(ctx)


@bot.command(name='joinq')
async def join_queue(ctx):
    time.sleep(.5)
    already_added = False
    for users in myQueue.queue:
        if ctx.author.name in users[0]:
            await ctx.send("You're already in the queue!")
            already_added = True
    if already_added == False:
        await ctx.send(f'Added {ctx.author.name} to queue!')
        myQueue.update()
        myQueue.insert(ctx.author.name, random.randint(0,20))

@bot.command(name='leaveq')
async def leave_queue(ctx):
    time.sleep(.5)
    try:
        for users in myQueue.queue:
            if ctx.author.name in users[0]:
                pos_in_queue = myQueue.queue.index(users)
                del myQueue.queue[pos_in_queue]
                await ctx.send(f"Removed {ctx.author.name}")
    except:
        await ctx.send("Something went wrong. Sorry, this feature is still quite new.")

@bot.command(name='listq')
async def list_queue(ctx):
    time.sleep(.5)
    if len(myQueue.queue) == 0:
        await ctx.send("No one in queue!")
    myQueue.sort()
    message = ""
    i = 1
    for x in myQueue.queue:
        if i > 3:
            break
        message += f'{i}. {x[0]}, '
        i += 1
    await ctx.send(message)

@bot.command(name='updateq1')
async def update_queue1(ctx):
	time.sleep(.5)
	if ctx.author.is_mod:
		myQueue.delete(1)
	
@bot.command(name='updateq2')
async def update_queue1(ctx):
	time.sleep(.5)
	if ctx.author.is_mod:
		myQueue.delete(2)
	
@bot.command(name='updateq3')
async def update_queue1(ctx):
	time.sleep(.5)
	if ctx.author.is_mod:
		myQueue.delete(3)

@bot.command(name='helpq')
async def help_queue(ctx):
	time.sleep(.5)
	await ctx.send("Possible commands: joinq, leaveq, listq, updateq1, updateq2, updateq3, credit")
	
@bot.command(name='credit')
async def credit(ctx):
	time.sleep(.5)
	await ctx.send(f'I was programmed by waltzingstoic.')

@bot.command(name='joincult')
async def join_cult(ctx):
    time.sleep(.5)
    await ctx.send(f'Welcome to the cult, {ctx.author.name} :)')


class WeightedRandomQueue():
    def __init__(self):
        self.queue = []

    def __str__(self):
        return ''.join([str(i) for i in self.queue])

    def isEmpty(self):
        return len(self.queue) == 0

    def insert(self, name, weight):
        self.queue.append([name, weight])

    def delete(self, n):
        if n > len(self.queue):
            print("Not that many users in queue")
            return 0
        for x in range(n):
            maxNum = 0
            currMax = self.queue[0]
            for item in self.queue:
                if item[1] > maxNum:
                    maxNum = item[1]
                    currMax = item
            self.queue.remove(currMax)

    def update(self):
        for x in range(len(self.queue)):
            val = random.randint(1, 5)
            self.queue[x][1] += val

    def sort(self):
        self.queue = sorted(self.queue, key= lambda x: int(x[1]), reverse=True)


if __name__ == '__main__':
    myQueue = WeightedRandomQueue()
    bot.run()
