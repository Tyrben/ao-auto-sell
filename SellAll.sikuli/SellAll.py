app = switchApp("Albion Online Client")
if not app.isRunning():
	exit(1)

Settings.MoveMouseDelay = 0.13

with Region(app.window()):
	print "debut"
	while (exists(Pattern("SellBtn.png").similar(0.85))):
		click(getLastMatch())
		if exists(Pattern("TogglePanelBtn.png").similar(0.78).targetOffset(22,6),0.1):
			click(getLastMatch())
		if exists(Pattern("SellOrder.png").similar(0.82).targetOffset(-43,-2),0.1):
			click(getLastMatch())
		wait(Pattern("PriceLeft.png").similar(0.80).targetOffset(22,-1))
		click(getLastMatch())
		wait(Pattern("Create.png").similar(0.80))
		click(getLastMatch())
		
print "fin"
