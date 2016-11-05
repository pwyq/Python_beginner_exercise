#This version is the latest version that will be wrote in object-oriented programming style.
#Start date: Sept 04, 2016
#Staff: Yanqing(Peter) Wu
#----------------
from thespace_planet_introduction import planets_info

current_planet = None

class Scene(object):

    def enter(self):
        pass
        
class Spaceship(object):

    def __init__(self, scene_map):
        pass
        
    def start(self):
        a_begin = Earth()
        a_begin.enter()
        
class Timer(object):

    def __init__(self):
        pass
		
class IntroductionOfPlanet(object):
    
    def introduce(self):
        print '-' * 12
        print planets_info['%s'] % current_planet
        print '-' * 12
		

class Death(Scene):
    
    def enter(self):
        pass
        
class Resurgence(Scene):
  
    def enter(self):
        pass
        
class PlayerInfo(object):
    
    def enter(self):
        pass
	
class Sun(Scene):
    
    def enter(self):
        pass
        
class Moon(Scene):
  
    def enter(self):
        pass

class Mercury(Scene):

    def enter(self):
        pass
        
class Mars(Scene):

    def enter(self):
        pass
        
class Juipter(Scene):

    def enter(self):
        pass
			
class Saturn(Scene):

    def enter(self):
        pass
        
class Uranus(Scene):

    def enter(self):
        pass
        
class Nepture(Scene):

    def Pluto(self):
        pass 
        
class Earth(Scene):

    current_planet = Earth
    earth_info = IntroductionOfPlanet()
    earth_info.introduce()
	
    def enter(self):
        print """
		Saved the world. develop this paragraph later."""
		
        
class SolarSystemMap(object):

    scenes = {
        'death': 'Death()', #don't miss the colon
        'resurgence': 'Resurgence()',
        'sun': 'Sun()',
        'moon': 'Moon()',
        'earth': 'Earth()',
        'mercury': 'Mercury()',
        'venus': 'Venus()',
        'mars': 'Mars()',
        'juipter': 'Juipter()',
        'saturn': 'Saturn()',
        'uranus': 'Uranus()',
        'nepture': 'Nepture()',
        'pluto': 'Pluto()'
    }

    def __init__(self, start_scene):
        pass

#Alternative 3-line expression: 
#a_map = SolarSystemMap('earth')
#a_game = Spaceship(a_map)
#a_game.start()

Spaceship(SolarSystemMap('earth')).start()