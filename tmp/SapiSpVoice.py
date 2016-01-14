#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Refer to: http://www.thinksaas.cn/group/topic/318160/
import win32com.client

voices = {
'Sam' : 'Microsoft Sam',
'Mary' : 'Microsoft Mary',
'Mike' : 'Microsoft Mike'
}

# choose voice from the voices dictionary
voice = 'Sam'
# range 0(low) - 100(loud)
volume = 100
# range -10(slow) - 10(fast)
rate = -1

# some text to speak
text ="""
It is said, that if you line up all the cars in the world end to end, 
someone would be stupid enough and try to pass them.
"""

# initialize COM components of MS Speech API
# COM is Microsoft's Component Object Model
# (COM is also used by Peter Parente's pyTTS)
speak = win32com.client.Dispatch('Sapi.SpVoice')
# assign a voice
speak.Voice = speak.GetVoices().Item(1)
speak.speak(u"测试文本")
# speak.Voice = speak.GetVoices('Name='+voices[voice]).Item(0)
# speak.Rate = rate
# speak.Volume = volume
# # now speak out the text
# speak.Speak(text)
