from datetime import timedelta, datetime

class Buffer:
	def __init__(self):
		self.buffer = dict()
		
	def clear(self, seconds):
		now = datetime.now()
		for mac in self.buffer.keys()[:]:
			if now - self.buffer[mac] > timedelta(seconds=seconds):
				self.buffer.pop(mac)
	
	def add(self, mac):
		self.buffer[mac] = datetime.now()
		
	def request(self, seconds):
		now = datetime.now()
		return [mac for mac in self.buffer if now - self.buffer[mac] <= timedelta(seconds=seconds)]
			
