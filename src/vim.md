Exercise 1: Basic Navigation
Open a File:
Open a terminal and type vim filename.txt to create and open a file named filename.txt.
Navigation Commands:
Use h, j, k, l to move left, down, up, and right, respectively.
Use gg to go to the beginning of the file.
Use G to go to the end of the file.
Use :set number to display line numbers.
Exercise 2: Switching Modes
Insert Mode:
Press i to enter insert mode and start typing text.
Press ESC to return to normal mode.
Command Mode:
From normal mode, type : to enter command mode.
Type :w to save the file.
Type :q to quit Vim.
Type :wq to save and quit.
Exercise 3: Editing Text
Insert and Append:
Press i to insert text at the cursor position.
Press a to append text after the cursor.
Delete and Undo:
Press x to delete the character under the cursor.
Press dd to delete the current line.
Press u to undo the last change.
Press Ctrl-r to redo the undone change.
Exercise 4: Searching and Replacing
Search for a Word:
Press / and type the word you want to search for, then press Enter.
Press n to go to the next occurrence.
Press N to go to the previous occurrence.
Replace Text:
Enter command mode by typing :.
Type :%s/old/new/g to replace all occurrences of old with new in the file.
Type :s/old/new/g to replace all occurrences of old with new in the current line.
Exercise 5: Working with Multiple Files
Open Multiple Files:
Open multiple files by typing vim file1.txt file2.txt.
Navigate Between Files:
Use :n to go to the next file.
Use :prev to go to the previous file.
Use :bnext to switch to the next buffer.
Use :bprev to switch to the previous buffer.
Exercise 6: Visual Mode
Select Text:
Press v to enter visual mode and use the navigation keys to select text.
Press V to select entire lines.
Cut, Copy, and Paste:
Select text in visual mode and press d to cut.
Select text in visual mode and press y to copy.
Move the cursor to the desired location and press p to paste.
Exercise 7: Using Registers
Yank and Paste:
Yank (copy) text by pressing yy to yank the current line.
Press "ayy to yank the current line into register a.
Paste from Registers:
Press "ap to paste from register a.
Exercise 8: Using Macros
Recording Macros:
Press q followed by a letter (e.g., q) to start recording a macro into register q.
Perform the actions you want to record.
Press q again to stop recording.
Playing Macros:
Press @q to execute the macro stored in register q.
Exercise 9: Customizing Vim
Create a .vimrc File:
Open your home directory and create a file named .vimrc.
Add Basic Configurations:
Add the following lines to the .vimrc file:
vim
Copy code
set number          " Show line numbers
syntax on           " Enable syntax highlighting
set tabstop=4       " Set tab width to 4 spaces
set shiftwidth=4    " Set indent width to 4 spaces
set expandtab       " Use spaces instead of tabs
Reload Vim:
Close and reopen Vim to apply the configurations.
Exercise 10: Advanced Navigation and Editing
Navigate by Words:
Use w to move to the beginning of the next word.
Use b to move to the beginning of the previous word.
Use e to move to the end of the current word.
Delete and Change Text:
Use dw to delete a word.
Use cw to change a word.
Use d$ to delete to the end of the line.
Use c$ to change to the end of the line.
Splitting Windows:
Use :split to split the window horizontally.
Use :vsplit to split the window vertically.
Use Ctrl-w followed by navigation keys to move between splits.