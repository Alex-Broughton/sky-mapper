##################################################################
#											 					 #
#			STAR ATLAS DATABASE & GLOBAL CONFIGURATION			 #
#																 #
##################################################################

import ephem
import math
from graphics import *
from ephem import *


# PyePhem STAR LIST (94 stars)
global stardb 
stardb = [ "Sirrah", "Caph", "Algenib", "Schedar", "Mirach", "Achernar", "Almach", "Hamal", "Polaris",
		   "Menkar", "Algol", "Electra", "Taygeta", "Maia", "Merope", "Alcyone", "Atlas", "Zaurak",
		   "Aldebaran", "Rigel", "Capella", "Bellatrix", "Elnath", "Nihal", "Mintaka", "Arneb",
           "Alnilam", "Alnitak", "Saiph", "Betelgeuse", "Menkalinan", "Mirzam", "Canopus", "Alhena",
           "Sirius", "Adara", "Wezen", "Castor", "Procyon", "Pollux", "Naos", "Alphard", "Regulus",
           "Algieba", "Merak", "Dubhe", "Denebola", "Phecda", "Minkar", "Megrez", "Gienah Corvi",
           "Mimosa", "Alioth", "Vindemiatrix", "Mizar", "Spica", "Alcor", "Alcaid", "Agena", "Thuban",
           "Arcturus", "Izar", "Kochab", "Alphecca", "Unukalhai", "Antares", "Rasalgethi", "Shaula",
           "Rasalhague", "Cebalrai", "Etamin", "Kaus Australis", "Vega", "Sheliak", "Nunki",
           "Sulafat", "Arkab Prior", "Arkab Posterior", "Rukbat", "Albereo", "Tarazed", "Altair",
           "Alshain", "Sadr", "Peacock", "Deneb", "Alderamin", "Alfirk", "Enif", "Sadalmelik", "Alnair",
           "Fomalhaut", "Scheat", "Markab" ]

#PyePhem SOLAR SYSTEM NAME LIST
global solarsystemNamesdb 
solarsystemNamesdb = [ 'Sun', 'Moon', 'Mercury', 'Venus', 'Mars', 'Jupiter', 
			  	   	   'Saturn', 'Uranus', 'Neptune', 'Pluto' ]


global solarsystemColorsdb
solarsystemColorsdb = [ 'Sun', 'Moon', 'Mercury', 'Venus', 'Mars', 'Jupiter', 
			  	   	   'Saturn', 'Uranus', 'Neptune', 'Pluto' ]

#PyePhem SOLAR SYSTEM LIST
global solarsystemdb 
solarsystemdb = [ ephem.Sun(), 
				  ephem.Moon(), 
				  ephem.Mercury(), 
				  ephem.Venus(), 
				  ephem.Mars(), 
				  ephem.Jupiter(), 
				  ephem.Saturn(), 
				  ephem.Uranus(), 
				  ephem.Neptune(), 
				  ephem.Pluto() ]


# MACROS
global VERBOSE
global STATISTICS
global SAVE
global MAG_0
global MAG_1
global MAG_2
global MAG_3
global MAG_4
global MAG_FAINT
global SHOWSTARS
global SHOWSTARNAMES
global SHOWSOLARSYS
global SHOWSOLARSYSNAMES
global SHOWCONSTELLATIONS
global SHOWMESSIER
global SHOWMESSIERNAMES
global DEGREES
global RADIANS
global HALF_WINDOW_SIZE
global CANVAS_RADIUS
global LONGITUDE
global LATITUDE
global MAXMAGNITUDE
global VISIBLE
global STARCOLOR
global CANVASCOLOR
global CANVASOUTLINECOLOR
global WINDOWCOLOR
global LETTERINGCOLOR
global LABELCOLOR
global MESSIERCOLOR



#*******		   DEFAULT TEMPLATE	        *******
# MACROS
VERBOSE = False
STATISTICS = True
SAVE = False
MAG_0 = 0
MAG_1 = 0
MAG_2 = 0
MAG_3 = 0
MAG_4 = 0
MAG_FAINT = 0
SHOWSTARS = True
SHOWSTARNAMES = False
SHOWSOLARSYS = True
SHOWSOLARSYSNAMES = True
SHOWCONSTELLATIONS = False
SHOWMESSIER = True
SHOWMESSIERNAMES = True
DEGREES = (math.pi / 180.0)
RADIANS = (180.0 / math.pi)
HALF_WINDOW_SIZE = 300
CANVAS_RADIUS = 250
LONGITUDE = '-121.7405'
LATITUDE = '38.5449'
MAXMAGNITUDE = 4.5
VISIBLE = True
STARCOLOR = color_rgb(255, 255, 255)
CANVASCOLOR = color_rgb(22, 39, 70)
CANVASOUTLINECOLOR = color_rgb(38, 68, 121)
WINDOWCOLOR = color_rgb(19, 33, 60)
LETTERINGCOLOR = color_rgb(255, 255, 255)
LABELCOLOR = color_rgb(38, 68, 121)
MESSIERCOLOR = color_rgb(204, 204, 204)



"""
#*******		BLACK AND WHITE INVETED TEMPLATE	*******
# MACROS
VERBOSE = False
STATISTICS = True
SAVE = False
MAG_0 = 0
MAG_1 = 0
MAG_2 = 0
MAG_3 = 0
MAG_4 = 0
MAG_FAINT = 0
SHOWSTARS = True
SHOWSTARNAMES = False
SHOWSOLARSYS = True
SHOWSOLARSYSNAMES = True
SHOWCONSTELLATIONS = False
SHOWMESSIER = True
SHOWMESSIERNAMES = True
DEGREES = (math.pi / 180.0)
RADIANS = (180.0 / math.pi)
HALF_WINDOW_SIZE = 300
CANVAS_RADIUS = 250
LONGITUDE = '-121.7405'
LATITUDE = '38.5449'
MAXMAGNITUDE = 4.5
VISIBLE = True
STARCOLOR = color_rgb(0, 0, 0)
CANVASCOLOR = color_rgb(255, 255, 255)
CANVASOUTLINECOLOR = color_rgb(0, 0, 0)
WINDOWCOLOR = color_rgb(255, 255, 255)
LETTERINGCOLOR = color_rgb(0, 0, 0)
LABELCOLOR = color_rgb(104, 104, 104)
MESSIERCOLOR = color_rgb(104, 104, 104)
"""


"""
#*******		BLACK AND WHITE TEMPLATE	*******
# MACROS
VERBOSE = False
STATISTICS = True
SAVE = False
MAG_0 = 0
MAG_1 = 0
MAG_2 = 0
MAG_3 = 0
MAG_4 = 0
MAG_FAINT = 0
SHOWSTARS = True
SHOWSTARNAMES = True
SHOWSOLARSYS = True
SHOWSOLARSYSNAMES = True
SHOWCONSTELLATIONS = False
SHOWMESSIER = True
SHOWMESSIERNAMES = True
DEGREES = (math.pi / 180.0)
RADIANS = (180.0 / math.pi)
HALF_WINDOW_SIZE = 300
CANVAS_RADIUS = 250
LONGITUDE = '-121.7405'
LATITUDE = '38.5449'
MAXMAGNITUDE = 4.5
VISIBLE = True
STARCOLOR = color_rgb(255, 255, 255)
CANVASCOLOR = color_rgb(0, 0, 0)
CANVASOUTLINECOLOR = color_rgb(255, 255, 255)
WINDOWCOLOR = color_rgb(0, 0, 0)
LETTERINGCOLOR = color_rgb(255, 255, 255)
LABELCOLOR = color_rgb(104, 104, 104)
MESSIERCOLOR = color_rgb(104, 104, 104)

"""
