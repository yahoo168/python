from time import sleep

class Clock(object):
	def __init__ (self, second=0, minute=0, hour=0):
		self.second = second
		self.minute = minute
		self.hour = hour

	def run(self):
		self.second += 1
		if self.second == 60:
			self.minute += 1
			self.second = 0
			if  self.minute == 60:
				self.hour += 1
				self.minute = 0 
				if self.hour == 24:
					self.hour = 0
	def show(self):
		return ("{0:0>2}:{1:0>2}:{2:0>2}".format(self.hour, self.minute, self.second))

clock = Clock(20, 36, 11)

while True:
	print(clock.show())
	sleep(1)
	clock.run()





