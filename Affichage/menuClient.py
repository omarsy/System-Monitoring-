#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
#L interface console pour permettre a l'utilisateur d enregistrer les donnees
#
#


from time import sleep
import curses, os #curses is the interface for capturing key presses on the menu, os launches the files
screen = curses.initscr() #initializes a new window for capturing key presses
curses.noecho() # Disables automatic echoing of key presses (prevents program from input each key twice)
curses.cbreak() # Disables line buffering (runs each key as it is pressed rather than waiting for the return key to pressed)
curses.start_color() # Lets you use colors when highlighting selected menu option
screen.keypad(1) # Capture input from keypad

# Change this to use different colors when highlighting
curses.init_pair(1,curses.COLOR_GREEN, curses.COLOR_WHITE) # Sets up color pair #1, it does black text with white background
h = curses.color_pair(1) #h is the coloring for a highlighted menu option
n = curses.A_NORMAL #n is the coloring for a non highlighted menu option

MENU = "menu"
COMMAND = "command"
EXITMENU = "exitmenu"

ADRESS =""
ADDRES_LIMITE_STOCKAGE="" 
#Menu Organise en titre et type d'action qu'il va realiser lorsqu"on appui dessus
#Et si le type d'actions est menu on a le sous-menu comme option
#Si l'option est une commande on doit mettre la commande qu'il va executer
menu_data = {
  'title': "Configuration Client", 'type': MENU, 'subtitle': "",
  'options':[
          { 'title': "Selection des Alertes", 'type': COMMAND, 'command': 'crisedecision.sh' },
          { 'title': "Modifier la Situation de crise", 'type': COMMAND, 'command': 'configuration_crise.sh' },

  ]
}


 	
# Cette fonction nous permet de controler les menu 
#parent est le parent du menu qu'on se trouve si le menu est  un sous menu
def runmenu(menu, parent):

  # On cherche Si il n'a pas de parent
  if parent is None:
    lastoption = "Quitter"
  else: #Si il a un parent le dernier option c'est un retourne qui le mene a son parent
    lastoption = "Return a %s Menu" % parent['title']

  optioncount = len(menu['options']) # le nombre d'element qu'on a dans le menu

  pos=0 
  oldpos=None # Variable necessaire lorsqu'on rafraichie le menu
  x = None #La touche qu'on a appuiyee
 
  # Loop until return key is pressed
  while x !=ord('\n'):
    if pos != oldpos:
      oldpos = pos
      screen.border(0)
      screen.addstr(2,2, menu['title'], curses.A_STANDOUT) # Titre du menu
      screen.addstr(4,2, menu['subtitle'], curses.A_BOLD) #Soustitre du menu

      # On affiche tous les items
      for index in range(optioncount):
        textstyle = n
        if pos==index:#si l'item a le curseur on a l'affiche d'une autre maniere
          textstyle = h
        screen.addstr(5+index,4, "%d - %s" % (index+1, menu['options'][index]['title']), textstyle)
	
     # Now display Exit/Return at bottom of menu
      textstyle = n
      if pos==optioncount:
        textstyle = h
      screen.addstr(5+optioncount,4, "%d - %s" % (optioncount+1, lastoption), textstyle)
      screen.refresh()# On rafraichie l'ecran

    x = screen.getch() 

    # Si il a appuiye sur un raccourci c'est a dire le numero de l'item
    if x >= ord('1') and x <= ord(str(optioncount+1)):
      pos = x - ord('0') - 1 #le convertir  en position
    elif x == 258: # touche down 
      if pos < optioncount:
        pos += 1
      else: pos = 0

    elif x == 259: #touche up 
      if pos > 0:
        pos += -1
      else: pos = optioncount

  # return index of the selected item
  return pos

# This function calls showmenu and then acts on the selected item
def processmenu(menu, parent=None):
  optioncount = len(menu['options'])
  exitmenu = False
  while not exitmenu: #Loop until the user exits the menu
    getin = runmenu(menu, parent)
    if getin == optioncount:
        exitmenu = True
    elif menu['options'][getin]['type'] == COMMAND:
      curses.def_prog_mode()    # save curent curses environment
      os.system('reset')
      screen.clear() #clears previous screen
      os.system(menu['options'][getin]['command']) # run the command
      screen.clear() #clears previous screen on key press and updates display based on pos
      curses.reset_prog_mode()   # reset to 'current' curses environment
      curses.curs_set(1)         # reset doesn't do this right
      curses.curs_set(0)
    elif menu['options'][getin]['type'] == MENU:
          screen.clear() #clears previous screen on key press and updates display based on pos
          processmenu(menu['options'][getin], menu) # display the submenu
          screen.clear() #clears previous screen on key press and updates display based on pos
    elif menu['options'][getin]['type'] == EXITMENU:
          exitmenu = True

# Main program
processmenu(menu_data)
curses.endwin() #VITAL! This closes out the menu system and returns you to the bash prompt.
os.system('clear')

