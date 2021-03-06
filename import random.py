import random
import time

allcarrying = allway = moneyairplanes = moneyauto = moneytrains = moneysmall = moneymed = moneybig = colvotime1 = all_money = days = time_ = 0

weather_forecast = []
colvotime = []

class WeatherAuto():
	def __init__(self, sunny, storm, shower, extreme, wind):
		self.sunny = sunny
		self.storm = storm
		self.shower = shower
		self.extreme = extreme
		self.wind = wind

	def Sunny(self):
		x_speed = 5
		x_crash = -0.04

		y_speed = 25
		y_crash = -0.09

		z_speed = 100
		z_crash = -0.009

		

		return [x_speed, x_crash, y_speed, y_crash, z_speed, z_crash]

	def Storm(self):
		x_speed = -10
		x_crash = 1

		y_speed = -50
		y_crash = 0.2

		z_speed = -100
		z_crash = 0.29

	

		return [x_speed, x_crash, y_speed, y_crash, z_speed, z_crash]

	def Shower(self):
		x_speed = 0
		x_crash = 0

		y_speed = 0
		y_crash = 0

		z_speed = 0
		z_crash = 0.04

		

		return [x_speed, x_crash, y_speed, y_crash, z_speed, z_crash]

	def Extreme(self):
		x_speed = -15
		x_crash = 3

		y_speed = -100
		y_crash = 0.9

		z_speed = 100
		z_crash = 9.99

		

		return [x_speed, x_crash, y_speed, y_crash, z_speed, z_crash]

	def Wind(self):
		x_speed = 15
		x_crash = 0.5

		y_speed = 50
		y_crash = 0.4

		z_speed = 200
		z_crash = 0

		return [x_speed, x_crash, y_speed, y_crash, z_speed, z_crash]

class Delivery():

	def __init__(self, Sunny, Storm, Shower, Extreme, Wind, weather, weather_forecast):

		self.Sunny = Sunny()
		self.Storm = Storm()
		self.Shower = Shower()
		self.Extreme = Extreme()
		self.Wind = Wind()
		self.weather = weather
		self.weather_forecast = weather_forecast


	def delevery(self, client, start, time_, importance):

		need_hours = way = money = 0

		if client <= 3 or client == 9:
			print('Выбор клиента это грузовики')
			money_give1 = 10
			money_give2 = 25
			money_need = 15
			carrying_give1 = 1000
			carrying_give2 = 2750
			carrying = 2500
			weather_now = 0
			crash = 5


		if client == 4 or client == 5 or client == 6 or client == 8:
			print('Выбор клиента это поезд')
			money_give1 = 30
			money_give2 = 80
			money_need = 45
			carrying_give1 = 10000
			carrying_give2 = 55000
			carrying = 50000
			weather_now = 2
			crash = 0.1

		if client == 7:
			print('Выбор клиента это самолёт')
			money_give1 = 75
			money_give2 = 200
			money_need = 120
			carrying_give1 = 3000
			carrying_give2 = 16000
			carrying = 15000
			weather_now = 4
			crash = 0.01


		
		for i in range(start):
			money += random.randint(money_give1, money_give2)

		need_carrying = random.randint(carrying_give1, carrying_give2)
		print('Клиент предлагает', money, 'рублей, а себестоимость приблезительно', start * money_need, 'рублей')

		if float(money) * 0.9 >= start * money_need and carrying >= need_carrying:
			print('Ваша компания решила принять заказ, выручка', money - start * money_need, 'рублей')

			chel = days = 0

			while way <= start:

				

				need_hours += 1

				if time_ + need_hours > 22 or time_ + need_hours < 4:
					while time_ + need_hours < 4 or time_ + need_hours > 22:
						need_hours += 1
						if time_ + need_hours >= 24:
							chel += 1
							days += 1
							need_hours = (time_ + need_hours) - 24
							time_ = 0

				if crash + weather_forecast[chel][weather_now + 1] * 10 > 15 and importance != 5 or crash + weather_forecast[chel][weather_now + 1] * 10 > 30:
					pass

				else:

					way += random.randint(60, 110)
					way += weather_forecast[chel][weather_now]	#WEATHER VERY HARD!

					accident = random.randint(0, 2000)
					if accident <= crash + weather_forecast[chel][weather_now + 1] * 10:
					
						money = start * money_need * (-2)
						print('Пройзошла авария, ваша компания теряет 2х стоимость заказа')
						return [money, need_hours, need_carrying]


				if chel == 7:
					print('Пасхалочка (Это не должно выводиться)')
					break

			return [money - start * money_need, need_hours, need_carrying]

		else:
			print('Ваша компания решила отказаться ')
			return [0, 0, 0]


bigtowns = []
medtowns = []
smalltowns = []

for i in range(random.randint(20, 50)):
	smalltowns += [random.randint(250, 800)]

for i in range(random.randint(10, 25)):
	medtowns += [random.randint(700, 2500)]

for i in range(random.randint(3, 10)):
	bigtowns += [random.randint(2000, 4000)]


Weather = WeatherAuto(WeatherAuto.Sunny, WeatherAuto.Storm, WeatherAuto.Shower, WeatherAuto.Extreme, WeatherAuto.Wind)


weather = [Weather.Sunny(), Weather.Sunny(), Weather.Sunny(), Weather.Sunny(), Weather.Sunny(), Weather.Sunny(), Weather.Shower(),
Weather.Shower(), Weather.Shower(), Weather.Shower(), Weather.Storm(), Weather.Storm(), Weather.Extreme(), Weather.Wind(), Weather.Wind()]


Del = Delivery(Weather.Sunny, Weather.Storm, Weather.Shower, Weather.Extreme, Weather.Wind, weather, weather_forecast)

for i in range(7):

	weather_forecast += [random.choice(weather)]

kikc = int(input('Введите количество дней иммитации '))

while kikc >= days:
	
	chance = random.randint(0, 100)

	if chance > 95:
		choicer = random.randint(1, 10)

		if choicer <= 4:
			start = int(random.choice(smalltowns))
			print('Выбор, малый город')
			client = random.randint(1, 4)
			importance = random.randint(1, 5)


		elif choicer == 5 or choicer == 6 or choicer == 7:
			start = int(random.choice(medtowns))
			print('Выбор, средний город')
			client = random.randint(2, 6)
			importance = random.randint(2, 5)

		else:
			start = int(random.choice(bigtowns))
			print('Выбор, большой город')
			client = random.randint(7, 9)
			importance = random.randint(3, 5)

		nosok = Del.delevery(client, start, time_, importance)

		print(nosok)

		money = int(nosok[0])

		if int(nosok[1]) == 0:
			pass

		else:
			colvotime += [int(nosok[1])]
			colvotime1 += int(nosok[1])


		if choicer <= 4:
			moneysmall += money
		elif choicer == 5 or choicer == 6 or choicer == 7:
			moneymed += money
		else:
			moneybig += money


		if client <= 3 or client == 9:
			moneyauto += money
		elif client == 4 or client == 5 or client == 6 or client == 8:
			moneytrains += money
		else:
			moneyairplanes += money


		allcarrying += int(nosok[2])
		allway += start

		try:
			print('Пока что среднее время доставки ', colvotime1 / len(colvotime))
		except:
			pass

		all_money += money
		
		print('Ваш общий заработок ', all_money, ' рублей\nЗаработок от маленьких городов ', moneysmall, ' рублей\nС средних ', moneymed, ' рублей, а с больших', moneybig)
		print('Заработок с грузовиков ', moneyauto, ' рублей, с поездов ', moneytrains, ' рублей, а с самолётов ', moneyairplanes, ' рублей')
		print('Всего доставлено ', allcarrying, ' кг разных грузов, всего проехано ', allway, 'км\nдоход тонно-километр ', allcarrying / allway, ' кг/км')

	time.sleep(0.1)
	time_ += 1

	if time_ == 25:
		time_ = 1
		days += 1
		weather_forecast.pop(0)
		weather_forecast += [random.choice(weather)]
		print('\nПрошёл ', days, ' день\n')

		# Юбилей!

	if time_ <= 12:
		print('Сейчас ', time_, ' AM')
	else:
		print('Сейчас ', time_ - 12, ' PM')
