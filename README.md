## MRU Open Files

This plugin for Sublime Text 3 is intended to reorder tabs/openFiles in the MRU ctrl+tab order. This way, when you are pressing ctrl+tab, you know where you are going. It's intended to emulate the ctrl+tab popup that other editors have.

However. As of now, there is no way to know the order of ctrl+tab MRU stack! And there is no way to differenciate between the editor showing the tabs while ctrl is pressed and while ctrl is released, since the Sublime API won't let you check which modifier keys are pressed.

I will try to do something with AHK to send a command when ctrl is down and another command when ctrl is up. But I want to make an alternative for Linux and OSX too, since I work on Windows and Linux.

Also, my Python knowledge is close to 0. I put this togeather by looking at other plugins. So don't expect much.

## How is it working now

Since we can't really make it behave like we would wish. The behaviour that is doing right now is: after you focus a new tab, after X seconds (3 by default), the tab is moved to first place. It works, pretty well.

Anyway, here are some things that don't work:

- In the open files list, after calling `window.set_view_index` the file won't get highlighted. But I think this is a ST3 bug.

## Sublime Text 2

Never tried it in ST2. Doubt it will work. And I don't really know the differences between the APIs.