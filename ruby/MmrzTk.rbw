require 'tk'

Title = "Mmrz"

tk_root_height = 250
tk_root_width = 380

tk_word_x = 10
tk_word_y = 30
tk_word_height = 50
tk_word_width  = tk_root_width - (tk_word_x * 2)

tk_pronounce_x = 10
tk_pronounce_y = 80
tk_pronounce_height = 50
tk_pronounce_width  = tk_root_width - (tk_pronounce_x * 2)

tk_show_height = 50
tk_show_width  = 100
tk_show_x = (tk_root_width - tk_show_width) / 2.0
tk_show_y = 80

tk_yes_height = 50
tk_yes_width  = 100
tk_yes_x = 60
tk_yes_y = 150

tk_no_height = 50
tk_no_width  = 100
tk_no_x = tk_root_width - tk_no_width - tk_yes_x
tk_no_y = 150

def disp str
  $tk_word.text str
end

root = TkRoot.new do
  title Title
  minsize tk_root_width, tk_root_height
  maxsize tk_root_width, tk_root_height
end

$tk_word = TkLabel.new root do
  text '敬う'
  borderwidth 0
  font TkFont.new 'consolas 20'
  foreground "black"
  relief "groove"
  place 'height' => tk_word_height, 'width' => tk_word_width, 'x' => tk_word_x, 'y' => tk_word_y
end

$tk_pronounce = TkLabel.new root do
  borderwidth 0
  font TkFont.new 'consolas 15'
  foreground "black"
  relief "groove"
  place 'height' => tk_pronounce_height, 'width' => tk_pronounce_width, 'x' => tk_pronounce_x, 'y' => tk_pronounce_y
end

$tk_yes = TkButton.new do
  text '记得住'
  background "yellow"
  foreground "blue"
  command do
    $tk_show.place 'height' => tk_show_height, 'width' => tk_show_width, 'x' => tk_show_x, 'y' => tk_show_y
    $tk_yes.unplace
    $noButton.unplace
    $tk_word.text '敬う'
    disp "OK"
    $tk_pronounce.text ""
  end
end

$noButton = TkButton.new do
  text '记不住'
  background "yellow"
  foreground "blue"
  command do
    $tk_show.place 'height' => tk_show_height, 'width' => tk_show_width, 'x' => tk_show_x, 'y' => tk_show_y
    $tk_yes.unplace
    $noButton.unplace
    # $tk_word.text '敬う'
    $tk_pronounce.text ""
  end
end

$tk_show = TkButton.new do
  text '查看'
  background "yellow"
  foreground "blue"
  place 'height' => tk_show_height, 'width' => tk_show_width, 'x' => tk_show_x, 'y' => tk_show_y
  command do
    $tk_pronounce.text 'うやまう -- 敬,尊敬,敬重'
    $tk_yes.place 'height' => tk_yes_height,'width' => tk_yes_width,'x' => tk_yes_x,'y' => tk_yes_y
    $noButton.place 'height' => tk_no_height, 'width' => tk_no_width, 'x' => tk_no_x, 'y' => tk_no_y
    unplace
  end
end

Tk.mainloop