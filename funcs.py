def addPerson(wnd, wnd2, personlist):
	wnd.clear()
	helpstr = "Enter: cardnumber"
	wnd.addstr(0,0, helpstr, curses.color_pair(3))
	wnd.move(1,0)
	wnd.refresh()
	cardnumber = wnd.getstr()
	helpstr = "Enter: name"
	wnd.addstr(2,0, helpstr, curses.color_pair(3))
	wnd.move(3,0)
	wnd.refresh()
	name = wnd.getstr()
	newPerson = Person(name, cardnumber, [], 0, 0)
	personlist.append(newPerson)

def addProduct(wnd, wnd2, produktlist):
	wnd.clear()
	helpstr = "Enter: barcode"
	wnd.addstr(0,0, helpstr, curses.color_pair(3))
	y, x = wnd.getyx()
	wnd.move(y+1, 0)
	wnd.refresh()
	barcode = wnd.getstr()
	helpstr = "Enter: productname,price,quantity"
	wnd.addstr(y+2,0, helpstr, curses.color_pair(3))
	wnd.move(y+3, 0)
	wnd.refresh()
	key = wnd.getstr()
	prodstr = key.split(",")
	newProduct = Produkt(prodstr[0], barcode, int(prodstr[1]), int(prodstr[2]))
	wnd.addstr(y+4,0, str(newProduct), curses.color_pair(3))
	wnd.addstr(y+5,0, "Correct??? Confirm with: yes", curses.color_pair(3))
	wnd.move(y+6,0)
	wnd.refresh()
	key = wnd.getstr()
	if key == "yes": produktlist.append(newProduct)


def skrivListe(wnd, personlist):
	personlist.sort(key= lambda p: -1*p.antallpils)
	linje = 8
	for i in personlist:
		wnd.addstr(linje, 0, str(i))
		linje += 1
