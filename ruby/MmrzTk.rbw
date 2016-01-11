require 'tk'

Title = "Mmrz"
root = TkRoot.new do
  title Title
  minsize 300, 300
  maxsize 300, 300
end

Lbl = TkLabel.new root do
  text 'oldStr'
  borderwidth 0
  font TkFont.new 'times 20 bold'
  foreground "red"
  relief "groove"
  place 'height' => 50, 'width' => 230, 'x' => 30, 'y' => 30
end

TkButton.new do
text 'Left'
 background "yellow"
 foreground "blue"
 place 'height' => 50,'width' => 100,'x' => 30,'y' => 150
end

TkButton.new do
text 'Right'
 background "yellow"
 foreground "blue"
 place 'height' => 50, 'width' => 100, 'x' => 160, 'y' => 150
end

$resultsVar = TkVariable.new
Lbl['textvariable'] = $resultsVar
$resultsVar.value = 'newStr'


Tk.mainloop