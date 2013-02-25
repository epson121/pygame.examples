#AI implementation

class GameEntity(object):

	def __init__(self, world, name, image):
		self.world = world
		self.name = name
		self.image = image
		self.location = 