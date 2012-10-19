###
# Copyright (c) 2012, Steven
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
#   * Redistributions of source code must retain the above copyright notice,
#     this list of conditions, and the following disclaimer.
#   * Redistributions in binary form must reproduce the above copyright notice,
#     this list of conditions, and the following disclaimer in the
#     documentation and/or other materials provided with the distribution.
#   * Neither the name of the author of this software nor the name of
#     contributors to this software may be used to endorse or promote products
#     derived from this software without specific prior written consent.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED.  IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.

###

import random

import supybot.utils as utils
from supybot.commands import *
import supybot.plugins as plugins
import supybot.ircutils as ircutils
import supybot.callbacks as callbacks
import supybot.ircmsgs as ircmsgs

class Slap(callbacks.Plugin):

    def __init__(self, irc):
        self.__parent = super(Slap, self)
        self.__parent.__init__(irc)
        
        self.irc = irc
        # TODO get channelname from somewhere, not hardcode it
        self.channel = ""
        
        self.rng = random.Random()   # create our rng
        self.rng.seed()   # automatically seeds with current time
        
        self.slaps = [
            "slaps %s",
        ]
        
        self.entry_actions = [
            "kicks open the door to %(target)s's office, ",
            "walks in %(target)s's office, ",
            "waits for %(target)s at the toilets, ",
        ]
        self.weapon_actions = [
            "kicks %(target)s to the floor while swinging a %(weapon)s.",
            "swings her %(weapon)s, puts it on the ground and bodychecks %(target)s into the wall.",
            "shouts 'YIPIKAYE MOTHERFUCKER' and charges with a %(weapon)s towards %(target)s.",
            "says 'say hello to my little %(weapon)s' while bombarding %(target)s with all sorts of filthy words.",
        ]
        self.after_actions = [
            "%(target)s never knew what hit him.",
            "%(target)s was unable to dodge the blow.",
            "%(target)s collapsed to the ground.",
            "%(target)s dodged the attack with a smooth movement.",
            "The memorial for %(target)s is next wednesday at 2pm.",
            "%(target)s leaves behind two kids, a wive, an old dog, and an asian robot.",
        ]
        self.weapon = [
            "trout",
            "laptop",
            "bowling ball",
            "stick",
            "coffee table",
            "giant sword",
            "broken M16",
        ]
        
    def me(self, msg):
        self.irc.queueMsg(ircmsgs.action(self.channel, msg))
        self.irc.noReply()
    
    def message(self, msg):
        self.irc.queueMsg(ircmsgs.privmsg(self.channel, msg))
        self.irc.noReply()

    def hit(self, irc, msg, args, name):
        
        text = ( self.entry_actions[ self.rng.randint(0, len(self.entry_actions)-1) ]
                + self.weapon_actions[ self.rng.randint(0, len(self.weapon_actions)-1) ] + " "
                + self.after_actions[ self.rng.randint(0, len(self.after_actions)-1) ] ) \
                % {"target" : name.title(), "weapon" : self.weapon[ self.rng.randint(0, len(self.weapon)-1) ] }
        
        self.me(irc, text)
        
    hit = wrap(hit, ['anything'])
    
    def slap(self, irc, msg, args, name):
        
        text = self.slaps[ self.rng.randint(0, len(self.slaps)-1) ] % name
        
        self.me(irc, text)
        
    slap = wrap(slap, ['anything'])
    

Class = Slap
