#!/bin/python

## Jython script
Debug.on(3) # run the script with option -c to get the log messages
import org.sikuli.ide.SikulixIDE as IDE
IDE.makeScriptjar(["plain", "/usr/local/src/AutoSell"])
