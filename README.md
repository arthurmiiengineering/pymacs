# pymacs: pythonic tool system

## An extension driven tool development system, written in pure python.

This is a simple tool system for the terminal. Powered by a simple extension system, it is meant to be simple, reliable, and extensible. This is achieved with a simple prompt as a base and a data driven config system which can load any modules from the extensions folder via the config settings. Its main extension as of now is a line editor like ED, the standard text editor for linux.

#### Features(Current):
- basic line editing via the texteditor extension
- basic loading and saving functionality via the same extension (only 1 buffer supported currently)
- global data via the 'app_data' variable in the app file
- json configuration using the config.json file. the top level represents the folder within extensions and the names within that block are the modules you expect to be loaded
- hooking functions into the main loop via the app scheduler and the event broker

#### TODO:
- multiple buffers
- more ergonomic commands
- syntax highlighting
- more built in functionality extensions

## Structure
- README.md *<- you are here!*
- src/
	- core/
		- broker.py
		- extensions.py
		- schedule.py
		- test_broker.py
		- test_schedule.py
	- extensions/
		- ledit/
			- editor.py
- docs
	- getting_started.md
