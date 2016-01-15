#!/env/bin/ruby
# encoding: utf-8

require 'tk'
require "win32ole"

Encoding.default_external = Encoding::UTF_8
Encoding.default_internal = Encoding::UTF_8

WORDS = "
長野県軽井沢町で15日未明、
国道からバスが転落し14人が死亡、
27人が重軽傷を負った事故で、
負傷して病院に運ばれた乗客が取材に応じ、
当時の状況を証言した。
"

# Main window
$tk_root_height = 230
$tk_root_width = 400

$tk_root = TkRoot.new do
  title "Speak"
  minsize $tk_root_width, $tk_root_height
  maxsize $tk_root_width, $tk_root_height
end

$tk_text = TkText.new($tk_root) do
  borderwidth 1
  place 'height' => 50, 'width' => $tk_root_width
end

$tk_word = TkLabel.new $tk_root do
  borderwidth 0
  font TkFont.new 'simsun 20 bold'
  foreground "black"
  relief "groove"
  place 'height' => $tk_root_height - 50, 'width' => $tk_root_width, 'x' => 0, 'y' => 50
end

$tk_button = TkButton.new($tk_root) do
  text 'read'
  background "yellow"
  foreground "blue"
  place 'x' => 0, 'y' => 50
  command { speak_word $tk_text.get("1.0", 'end') }
end

def make_speaker
  speaker = WIN32OLE.new('Sapi.SpVoice')
  speaker.GetVoices().each do |engine|
    if engine.GetDescription().include? "Misaki"
      speaker.Voice = engine
      speaker.volume = 100 # range 0(low) - 100(loud)
      speaker.rate  = 0 # range -10(slow) - 10(fast)
    end
  end
  return speaker
end

def speak_word text
  speaker = make_speaker
  Thread.start do
    pos = 0
    len = 0
    while speaker.Status.RunningState != 1
      if pos != speaker.Status.InputWordPosition || len != speaker.Status.InputWordLength
        pos = speaker.Status.InputWordPosition
        len = speaker.Status.InputWordLength
        curWord = text[pos...(pos+len)]
        $tk_word.text curWord
      end
    end
  end
  speaker.speak text, 1
end

Tk.mainloop