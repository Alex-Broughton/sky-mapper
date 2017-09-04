####################################################################
#							    	  	 					       #
#							    	  	 					       #
#						STAR ATLAS v.0.0						   #
#			   Python 3.6.2 (v3.6.2:5) GCC v4.2.1    	  	 	   #
#							    	  	 					       #
#					     Alex Broughton							   #
#						   08.30.2017  	 					       #
#							    	  	 					       #
#							    	  	 					       #
####################################################################

import os
import sys
import math
import graphics
import ephem
import config

from PIL import Image as NewImage
from graphics import *
from ephem import *


def main():
	observer = SetObserver()
	window = SetEnvironment()

	Process(window, observer)

	if(config.STATISTICS): 
		Analyze()

	bugfix = Rectangle(Point(0,0), Point(config.HALF_WINDOW_SIZE / 3.,config.HALF_WINDOW_SIZE / 3.))
	bugfix.setFill(config.WINDOWCOLOR)
	bugfix.setOutline(config.WINDOWCOLOR)
	bugfix.draw(window)

	print("Done.")
	print("")

	save(window)

	return

def save(window):
	print("Saving...")
	# saves the current TKinter object in postscript format
	window.postscript(file="starmap.eps", colormode='color')

	# Convert from eps format to gif format using PIL
	img = NewImage.open("starmap.eps")

	print("Saved.")
	print("")

	return

def importMessierDatabase(fileName, window, observer):
	
	with open(fileName) as db:
		for line in db:
			messierObj = ephem.readdb(line)
			messierObj.compute(observer)

			if messierObj.name not in config.stardb:
				if(messierObj.neverup):	# Makes it run faster
					continue

			obj_rad = (messierObj.size * (1./3600.) * (500./180)) / 2. # Arcseconds->pixels 

			[x,y] = ProjectCoordinates(messierObj.alt, messierObj.az)

			if(config.VISIBLE):
					messier = Circle(Point(x,y), obj_rad*5)
					messier.setOutline(config.MESSIERCOLOR)
					messier.draw(window)

					if(config.SHOWMESSIERNAMES):
						starName = Text(Point(x,y - obj_rad*5 - 5), messierObj.name.upper())
						starName.setOutline(config.MESSIERCOLOR)
						starName.setSize(7)
						starName.draw(window)

					if(config.VERBOSE):
						print(obj.name)
						print("Mag: " + str(obj.mag))
						print("alt: " + str(obj.alt))
						print("az:  " + str(obj.az))
						print("")

			config.VISIBLE = True
	return


# Project / Plot stars
def PlotStars(window, observer):
	for astroObj in config.stardb:
		star_db_element = ephem.star(astroObj)
		star_db_element.compute(observer)

		if(star_db_element.neverup):	# Makes it run faster
			continue

		[x,y] = ProjectCoordinates(star_db_element.alt, star_db_element.az) # degrees (alt/az)
			
		if(config.VISIBLE and star_db_element.mag < config.MAXMAGNITUDE):
			star = Circle(Point(x,y), magnitudeScale(star_db_element))
			star.setFill(config.STARCOLOR)
			star.setOutline(config.STARCOLOR)
			star.draw(window)

			if(config.SHOWSTARNAMES):
				starName = Text(Point(x,y - 10), astroObj.upper())
				starName.setOutline(config.LABELCOLOR)
				starName.setSize(7)
				starName.draw(window)

			if(config.VERBOSE):
				print(astroObj)
				print("Mag: " + str(star_db_element.mag))
				print("alt: " + str(star_db_element.alt))
				print("az:  " + str(star_db_element.az))
				print("")

		config.VISIBLE = True

	return


def setPlanetColor(objectName):
	if(objectName == 'Sun'): return color_rgb(240,243,193) 
	if(objectName == 'Mercury'): return color_rgb(220,187,160)
	if(objectName == 'Venus'): return color_rgb(236,181,59)
	if(objectName == 'Moon'): return color_rgb(204,204,204)
	if(objectName == 'Mars'): return color_rgb(254,118,89)
	if(objectName == 'Jupiter'): return color_rgb(241,215,179)
	if(objectName == 'Saturn'):return color_rgb(134,119,95)
	if(objectName == 'Uranus'):return color_rgb(172,212,218)
	if(objectName == 'Neptune'):return color_rgb(66,108,255)
	if(objectName == 'Pluto'): return color_rgb(82,45,24)

	return color_rgb(255, 255, 255)


def PlotSolarSystem(window, observer):
	i=0
	for data in config.solarsystemdb:
		data.compute(observer)

		if(data.neverup):	# Makes it run faster
			continue
	
		[x,y] = ProjectCoordinates(data.alt, data.az) # degrees (alt/az)

		if(config.VISIBLE):
			obj = Circle(Point(x,y), 7 if (config.solarsystemNamesdb[i] == 'Sun' or config.solarsystemNamesdb[i] == 'Moon') else 3)
			obj.setFill(setPlanetColor(config.solarsystemNamesdb[i]))
			obj.setOutline(setPlanetColor(config.solarsystemNamesdb[i]))
			obj.draw(window)

			if(config.SHOWSOLARSYSNAMES):
				objName = Text(Point(x,y - 10), config.solarsystemNamesdb[i].upper())
				objName.setOutline(config.LABELCOLOR)
				objName.setSize(7)
				objName.draw(window)

			if(config.VERBOSE):
				print(config.solarsystemNamesdb[i])
				print("Mag: " + str(data.mag))
				print("alt: " + str(data.alt))
				print("az:  " + str(data.az))
				print("")

		i = i + 1
		config.VISIBLE = True

	return



# Converts from declination/right ascention data to alt/az data
def Degrees(alt, az):
	
	alt = str(alt)
	az = str(az)

	altitudeData = alt.split(":")
	azimuthData = az.split(":")

	alt = float(altitudeData[0]) + ((float(altitudeData[1]) + (float(altitudeData[2]) / 60.0)) / 60.0)
	az = float(azimuthData[0]) + ((float(azimuthData[1]) + (float(azimuthData[2]) / 60.0)) / 60.0)


	return [alt,az]


# Returns stereographic projection point from altitude/azimuth data
def ProjectCoordinates(alt, az):
	# Equations derived from http://www2.arnes.si/~gljsentvid10/horizon.html
	[alt, az] = Degrees(alt, az)

	if(alt < 0.0 or alt > 180.0):
		VISIBLE = False
		return [-1, -1]

	x_normalized = -1 * (math.sin(az * config.DEGREES) * math.tan(((90 - alt) / 2.0) * config.DEGREES))
	y_normalized = -1 * (math.cos(az * config.DEGREES) * math.tan(((90 - alt) / 2.0) * config.DEGREES))
				#  /\   
				#   |   
				#   |___ Coefficient to flip coordinates, so 
				#		 they align with geological directions
	
	x = config.HALF_WINDOW_SIZE + (config.CANVAS_RADIUS * x_normalized)
	y = config.HALF_WINDOW_SIZE + (config.CANVAS_RADIUS * y_normalized)

	return [x,y]


# Locate the PYEPHEM Observer
def SetObserver():
	observer = ephem.Observer()
	observer.lon = config.LONGITUDE
	observer.lat = config.LATITUDE
	observer.elevation = 52
	observer.date = ephem.now()
	observer.pressure = 0.0 #IGNORE ATMOSPHERIC REFRFRACTION, defaults to 1010mBar otherwise
	observer.temp = 25.0 # DEFAULTS TO 25.C

	return observer


# Generate/initialize the graphics system
def SetEnvironment():
	# Set window
	name = "Star Atlas (v.1.0.0)  " + str(config.LATITUDE) + "˚N, " + str(config.LONGITUDE) + "˚W"
	window = GraphWin(name, 2*config.HALF_WINDOW_SIZE, 2*config.HALF_WINDOW_SIZE)
	window.setBackground(config.WINDOWCOLOR)

	background = Rectangle(Point(0,0), Point(2*config.HALF_WINDOW_SIZE, 2*config.HALF_WINDOW_SIZE))
	background.setFill(config.WINDOWCOLOR)
	background.setOutline(config.WINDOWCOLOR)
	background.draw(window)
	
	# Set canvas
	canvasSetting = Circle(Point(config.HALF_WINDOW_SIZE, config.HALF_WINDOW_SIZE), config.CANVAS_RADIUS + 6)
	canvasSetting.setFill(config.WINDOWCOLOR)
	canvasSetting.setOutline(config.CANVASOUTLINECOLOR)
	canvasSetting.draw(window)
	border = Circle(Point(config.HALF_WINDOW_SIZE, config.HALF_WINDOW_SIZE), config.CANVAS_RADIUS)
	border.setFill(config.CANVASCOLOR)
	border.setOutline(config.CANVASOUTLINECOLOR)
	border.setWidth(3)

	# Set labels
	N = Text(Point(300,30), "N")
	S = Text(Point(300,570), "S")
	E = Text(Point(570,300), "E")
	W = Text(Point(30,300), "W")
	N.setOutline(config.LETTERINGCOLOR)
	S.setOutline(config.LETTERINGCOLOR)
	E.setOutline(config.LETTERINGCOLOR)
	W.setOutline(config.LETTERINGCOLOR)
	N.draw(window)
	S.draw(window)
	E.draw(window)
	W.draw(window)
	border.draw(window)

	return window


def importStarDatabase(fileName, window, observer):
	with open(fileName) as db:
		for line in db:
			obj = ephem.readdb(line)
			obj.compute(observer)

			if obj.name not in config.stardb:
				if(obj.neverup):	# Makes it run faster
					continue

				[x,y] = ProjectCoordinates(obj.alt, obj.az) # degrees (alt/az)
					
				if(config.VISIBLE and obj.mag < config.MAXMAGNITUDE):
					star = Circle(Point(x,y), magnitudeScale(obj))
					star.setFill(config.STARCOLOR)
					star.setOutline(config.STARCOLOR)
					star.draw(window)

					if(config.SHOWSTARNAMES):
						starName = Text(Point(x,y - 10), obj.name.upper())
						starName.setOutline(config.LABELCOLOR)
						starName.setSize(7)
						starName.draw(window)

					if(config.VERBOSE):
						print(obj.name)
						print("Mag: " + str(obj.mag))
						print("alt: " + str(obj.alt))
						print("az:  " + str(obj.az))
						print("")

				config.VISIBLE = True

		
	return

def magnitudeScale(obj):
	if(obj.mag <= 1.0): 
		if(config.STATISTICS): 
			config.MAG_0 = config.MAG_0 + 1
		return 3
	if(obj.mag <= 2.0): 
		if(config.STATISTICS): 
			config.MAG_1 = config.MAG_1 + 1
		return 2.5
	if(obj.mag <= 3.0): 
		if(config.STATISTICS): 
			config.MAG_2 = config.MAG_2 + 1
		return 2
	if(obj.mag <= 4.0): 
		if(config.STATISTICS):
			config.MAG_3 = config.MAG_3 + 1 
		return .5
	if(obj.mag <= 5.0): 
		if(config.STATISTICS): 
			config.MAG_4 = config.MAG_4 + 1
		return .1

	if(config.STATISTICS): 
			config.MAG_FAINT = config.MAG_FAINT + 1

	return 0.1

def PlotConstellations(window, observer):
	Benetnasch = ephem.readdb("Benetnasch,f|V|B3,13:47:32.4,49:18:48,1.86,2000")
	Benetnasch.compute(observer)
	Mizar = ephem.star("Mizar")
	Mizar.compute(observer)
	Alioth = ephem.star("Alioth")
	Alioth.compute(observer)
	Megrez = ephem.star("Megrez")
	Megrez.compute(observer)
	Phecda = ephem.star("Phecda")
	Phecda.compute(observer)
	Dubhe = ephem.star("Dubhe")
	Dubhe.compute(observer)
	Merak = ephem.star("Merak")
	Merak.compute(observer)

	[Benetnaschx,Benetnaschy] = ProjectCoordinates(Benetnasch.alt, Benetnasch.az)
	[Mizarx,Mizary] = ProjectCoordinates(Mizar.alt, Mizar.az)
	[Aliothx,Aliothy] = ProjectCoordinates(Alioth.alt, Alioth.az)
	[Megrezx,Megrezy] = ProjectCoordinates(Megrez.alt, Megrez.az)
	[Dubhex,Dubhey] = ProjectCoordinates(Dubhe.alt, Dubhe.az)
	[Merakx,Meraky] = ProjectCoordinates(Merak.alt, Merak.az)
	[Phecdax,Phecday] = ProjectCoordinates(Phecda.alt, Phecda.az)
	
	# Benetnasch -> Mizar
	L1 = Line(Point(Benetnaschx,Benetnaschy), Point(Mizarx,Mizary))
	# Mizar -> Alioth
	L2 = Line(Point(Mizarx,Mizary), Point(Aliothx,Aliothy))
	# Alioth -> Megrez
	L3 = Line(Point(Aliothx,Aliothy), Point(Megrezx,Megrezy))
	# Megrez -> Phecda
	L4 = Line(Point(Megrezx,Megrezy), Point(Phecdax,Phecday))
	# Megrez -> Dubhe
	L5 = Line(Point(Megrezx,Megrezy), Point(Dubhex,Dubhey))
	# Dubhe -> Merak
	L6 = Line(Point(Dubhex,Dubhey), Point(Merakx,Meraky))
	# Phecda -> Merak
	L7 = Line(Point(Phecdax,Phecday), Point(Merakx,Meraky))

	L1.setOutline(color_rgb(255, 255, 255))
	L2.setOutline(color_rgb(255, 255, 255))
	L3.setOutline(color_rgb(255, 255, 255))
	L4.setOutline(color_rgb(255, 255, 255))
	L5.setOutline(color_rgb(255, 255, 255))
	L6.setOutline(color_rgb(255, 255, 255))
	L7.setOutline(color_rgb(255, 255, 255))

	L1.setWidth(0.5) 
	L2.setWidth(0.5) 
	L3.setWidth(0.5) 
	L4.setWidth(0.5) 
	L5.setWidth(0.5) 
	L6.setWidth(0.5) 
	L7.setWidth(0.5) 

	L1.draw(window)
	L2.draw(window)
	L3.draw(window)
	L4.draw(window)
	L5.draw(window)
	L6.draw(window)
	L7.draw(window)


def Process(window, observer):
	if(config.SHOWSTARS):
		if(config.VERBOSE):
			print("STARS")
			print("*****************************")
		PlotStars(window, observer)
		importStarDatabase("./database/YBS.txt", window, observer)
		
	if(config.SHOWSOLARSYS):
		if(config.VERBOSE):
			print("SOLAR SYSTEM OBJECTS")
			print("*****************************")
		PlotSolarSystem(window, observer)

	if(config.SHOWMESSIER):
		if(config.VERBOSE):
			print("MESSIER OBJECTS")
			print("*****************************")
		importMessierDatabase("./database/Messier.txt", window, observer)

	if(config.SHOWCONSTELLATIONS):	
		PlotConstellations(window, observer)

	return

def Analyze():
	total_stars = config.MAG_0 + config.MAG_1 + config.MAG_2 + config.MAG_3 + config.MAG_4 + config.MAG_FAINT

	print("")
	print("      ATLAS STATISTICS")
	print("*****************************")
	print("  Stars (MAG < 1.0): " + str(config.MAG_0))
	print("  Stars (MAG < 2.0): " + str(config.MAG_1))
	print("  Stars (MAG < 3.0): " + str(config.MAG_2))
	print("  Stars (MAG < 4.0): " + str(config.MAG_3))
	print("  Stars (MAG < 5.0): " + str(config.MAG_4))
	print("  Stars (MAG > 5.0): " + str(config.MAG_FAINT))
	print("TOTAL STARS PLOTTED: " + str(total_stars))
	print("")







# EOF