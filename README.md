supybot-plugins
===============

Some little plugins for IRC bot Supybot
http://sourceforge.net/projects/supybot/

Eightball: 

command: eightball <question>
- output: an official eightball answer

Slap: 

command: slap <target>
- output: /me slaps <target>

command: hit <target>
- output: random hit message including targets name and a random weapon

installation:
in plugin.py fill in your channel name on this line: 'self.channel = ""'
