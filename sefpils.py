import curses
import ascii_art
import funcs
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


"""Kode for aa haandtere ctrl+c"""
def signal_handler(signal, frame):
	curses.endwin()
	sys.exit(1)
	
		
def sjekkOgKjop(wnd, wnd2, produktlist, personlist):
	wnd2.move(0,0)
	key = wnd2.getstr()
	if key == "addperson":
		funcs.addPerson(wnd, wnd2, personlist)
	if key == "addproduct":
		funcs.addProduct(wnd, wnd2, produktlist)
		
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
	"""***************TEST*********************************"""
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
	
	#Vindu for banner overst:
	topwnd = curses.newwin(8,60,0,0) #wnd1
	topwnd.clear()
	topwnd.refresh()

	#Vindu som viser ascii_art og meny: 
	artwnd = curses.newwin(32,70,30,0) #wnd2
	artwnd.clear()
	artwnd.refresh()
	
	#Vindu som viser antall kjopte pils osv.:
	statwnd = curses.newwin(20, 70, 9, 0) #wnd3
	statwnd.clear()
	statwnd.refresh()

	#Vindu for kommandor i bunn:
	commandwnd = curses.newwin(3, 70, 63, 0) #wnd4
	commandwnd.clear()
	commandwnd.refresh()

	while True:
		topwnd.clear()
		artwnd.clear()
		commandwnd.clear()
		topwnd.addstr(0,0,ascii_art.sefpils, curses.color_pair(1))
		artwnd.addstr(0,0,ascii_art.info, curses.color_pair(2))
		artwnd.refresh()
		topwnd.refresh()
		funcs.skrivListe(statwnd, personlist)
		statwnd.refresh()
		sjekkOgKjop(artwnd, commandwnd, produktlist, personlist)

curses.wrapper(main) #tar seg av initscr og start_color osv.
	
	
	
	
	
	



