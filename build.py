#!/usr/bin/env python

## Jython script

## Build jar version of this sikuli script (is multiplatform)

#Debug.on(3) # run the script with option -c to get the log messages
import org.sikuli.ide.SikulixIDE as IDE

print("Building archive...")
IDE.makeScriptjar(["plain", "/usr/local/src/auto_sell"])
