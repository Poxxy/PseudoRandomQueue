# PseudoRandomQueue
A Twitch Bot which allows users to join a queue which is somewhat randomized but favors those who have been waiting longer. Feel free to use this program for yourself and modify it to your liking!

# Install/Setup

1. Make sure you have python 3+ installed.
2. Download the files in this repo and put them in a folder together.
3. In a terminal type ``pip install -r requirements.txt`` while in the folder directory.
4. Set up your user credentials in credentials.py. **NOTE: Do Not Share These Credentials With Anyone!**
5. In the terminal type `python weightedRandomQueue.py`
6. You're done!

# Commands
1. ``!helpq`` lists all the commands out
2. ``!joinq`` adds yourself to the queue
3. ``!leaveq`` removes yourself from queue
4. ``!listq`` lists the top 5 people in the queue
5. ``!updateq1`` removes the top person
6. ``!updateq2`` removes the top 2 people
7. ``!updateq3`` removes the top 3 people

# Planned Updates
~~1. Code refinement, particularly eliminating repeat code.~~ Done

~~2. Automatically detect approved mod based on user info rather than hardcode.~~ Added

~~3. Add ability to remove yourself from queue.~~ Added
