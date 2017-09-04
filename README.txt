*******************************************************************
*			 					  *
*			 STAR ATLAS v.1.0.0   			  *
*	        Python 3.6.2 (v3.6.2:5) GCC v4.2.1	          *
*		 					          *
*	        	   Alex Broughton	                  *
*			     08.30.2017 		          *
*							          *
*******************************************************************


StarAtlas is a python-3.6 based customizable generator for localized 
star maps intended for the amateur astronomer and for web-development. 
The application currently has a database with over 3,500 stars, planets
and objects from the built-in EPHEM database, the Yale Bright Star 
(YBS)database, and a catalogue of Messier objects.The user may configure
the map to their specifications by simply changing the global parameters 
in the config.py module. The Star Atlas application takes care of scaling 
and non-user defined functionality for an easy-to-use interface.


Dependencies: graphics.py v.5.0.1, ephem.py v.3.7.6.0


Currently, databases for stars and messier objects are in the database
directory, but extra object databases in XEPHEM format can be found at:

https://git.nexlab.net/astronomy/skylived/tree/bd59190026d9d95b39983f8a0106a7e17023aee8/DecraDB/xephemdb


		GLOBAL VARIABLE REFERENCE
***********************************************************
VERBOSE = False						# Show detailed mag/alt/az data during runtime
STATISTICS = True					# Show breakdown of tabulated stars
MAG_0 = 0						# System variable; always keep these as zero at launch time
MAG_1 = 0						#			|
MAG_2 = 0                                               #			|
MAG_3 = 0                                               #		        |
MAG_4 = 0                                               #			|
MAG_FAINT = 0                                           #              	      __|__
SHOWSTARS = True					# Display stars
SHOWSTARNAMES = False					# Display stars' names
SHOWSOLARSYS = True					# Display solar system objects (includes Sun and Pluto)
SHOWSOLARSYSNAMES = True				# Display solar system objects' names
SHOWCONSTELLATIONS = True				# Show Constellation (under construction, only Big Dipper avail.)
SHOWMESSIER = True 					# Show Messier objects
SHOWMESSIERNAMES = True					# Show Messier objects' names							
DEGREES = (math.pi / 180.0)				# Const.
RADIANS = (180.0 / math.pi)				# Const.
HALF_WINDOW_SIZE = 300					# 1/2 the graphical window size in px
CANVAS_RADIUS = 250					# Radius of the canvas in px
LONGITUDE = '-121.7405'					# Longitude (˚W) (measured in degrees counter-clockwise from prime meridian)
LATITUDE = '38.5449'					# Latitude  (˚N) (measured in degrees north from the equator)
MAXMAGNITUDE = 4.5					# Maximum allowed magnitude of displayed stars
VISIBLE = True						# System variable; always keep at 'True' at launch time
STARCOLOR = color_rgb(255, 255, 255)			# Graphics parameter: star color in RGB color code
CANVASCOLOR = color_rgb(0, 0, 0)			# Graphics parameter: canvas color in RGB color code
CANVASOUTLINECOLOR = color_rgb(255, 255, 255)		# Graphics parameter: canvas outline color in RGB color code
WINDOWCOLOR = color_rgb(0, 0, 0)			# Graphics parameter: window color in RGB color code
LETTERINGCOLOR = color_rgb(255, 255, 255)		# Graphics parameter: canvas label color in RGB color code
LABELCOLOR = color_rgb(104, 104, 104)			# Graphics parameter: object label color in RGB color code



		 RGB COLOR CODE REFERENCE
***********************************************************
(1) Cal Blue 				rgb(0, 85, 129)
(2) Darker Cal Blue			rgb(0, 54, 82)
(3) Lighter Cal Blue			rgb(0, 119, 180)
(3) Google Blue 			rgb(72, 133, 237)
(4) White				rgb(255, 255, 255)
(5) Gray				rgb(104, 104, 104)
(6) Black				rgb(0, 0, 0)
(7) Default Window Color 		rgb(19, 33, 60)	
(8) Default Canvas Color 		rgb(22, 39, 70)
(9) Default Outline Color 		rgb(38, 68, 121)
***********************************************************