require "win32ole"

speak = WIN32OLE.new('Sapi.SpVoice')
speak.Voice = speak.GetVoices().Item(1)
speak.speak("测试文本")