import curses
import ascii_art
import sys
import signal


class Person:
	def __init__(self, navn, kortnr, pilslist, antallpils, totalsum):
		self.navn = navn
		self.kortnr = kortnr
		self.pilslist = pilslist
		self.totalsum = totalsum
		self.antallpils = antallpils
		
	def __str__ (self):
		return "%s: %s har kjopt: %d til en totalpris: %d" % (self.kortnr, self.navn, self.antallpils, self.totalsum)
	
	
	
class Produkt:
	def __init__(self, prodnavn, kode, pris, antallKjol):
		self.prodnavn = prodnavn
		self.kode = kode
		self.pris = pris
		self.antallKjol = antallKjol
	def __str__ (self):
		return "Produkt: %s, pris: %d, Antall igjen: %d" % (self.prodnavn, self.pris, self.antallKjol) 



#def leggTilPerson
"""Kode for aa haandtere ctrl+c"""
def signal_handler(signal, frame):
	wnd2.addstr(0,0, "ctrl+c", curses.color_pair(3))
	curses.endwin()
	sys.exit(1)
	
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
		
def sjekkOgKjop(wnd, wnd2, produktlist, personlist):
	wnd2.move(0,0)
	key = wnd2.getstr()
	if key == "addperson":
		addPerson(wnd, wnd2, personlist)
	if key == "addproduct":
		addProduct(wnd, wnd2, produktlist)
		
	elif key == "help":
		wnd.clear()
		helpstr = """<<<<<<Help>>>>>>
			options (enter options) then do:
			addperson (add new person)
			addproduct (add new person)
			remperson (remove existing person)
			remproduct (remove existing product)
			updateq (update quantity of product)
			addq (add quantity of product)
			clear (clear person)"""
		wnd.addstr(0,0, helpstr, curses.color_pair(3))
		wnd.refresh()
		wnd2.clear()
		wnd2.move(0,0)
		key = wnd2.getstr()
	else:
		for i in produktlist:
			if i.kode == key:
				wnd.clear()
				wnd.addstr(0,0, ascii_art.ok, curses.color_pair(3))
				wnd.refresh()
				key2 = wnd2.getstr()
				for j in personlist:
					if j.kortnr == key2:
						j.antallpils += 1
						j.pilslist.append(i.prodnavn)
						j.totalsum += i.pris
						i.antallKjol -= 1
						return True
				return False
	return False
		





def main(wnd):
	p1 = Person("Anders", "UO00267920", [], 0, 0)
	p2 = Person("Snorre", "UO00259236", [], 0, 0)
	p3 = Person("Jon Magnus", "UO00224628", [], 0, 0)
	personlist = [p1, p2, p3]

	prod = Produkt("Tuborg", "7044610029351", 15, 12)
	produktlist = [prod]

	"""*******************************************************"""
	signal.signal(signal.SIGINT, signal_handler)
	curses.echo()
	wnd.clear()
	curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
	curses.init_pair(3, curses.COLOR_RED, curses.COLOR_BLACK)
	curses.init_pair(1, curses.COLOR_RED, curses.COLOR_GREEN)
	wnd.refresh()

	wnd1 = curses.newwin(8,60,0,0)
	wnd1.clear()
	wnd1.refresh()

	wnd2 = curses.newwin(32,70,30,0)
	wnd2.clear()
	wnd2.refresh()

	wnd3 = curses.newwin(20, 70, 9, 0)
	wnd3.clear()
	wnd3.refresh()

	wnd4 = curses.newwin(3, 70, 63, 0)
	wnd4.clear()
	wnd4.refresh()

	while True:
		wnd1.clear()
		wnd2.clear()
		wnd4.clear()
		wnd1.addstr(0,0,ascii_art.sefpils, curses.color_pair(1))
		wnd2.addstr(0,0,ascii_art.info, curses.color_pair(2))
		wnd2.refresh()
		wnd1.refresh()
		skrivListe(wnd3, personlist)
		wnd3.refresh()
		sjekkOgKjop(wnd2, wnd4, produktlist, personlist)

curses.wrapper(main) #tar seg av initscr og start_color osv.
	
	
	
	
	
	



