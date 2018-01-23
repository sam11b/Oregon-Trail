days = 0
date = 1
season = ""
food = 0
oxen = 0
spare_parts = 0
ammo = 0
shop_dictionary = {}
health = "Good"
miles_traveled = 0
miles_to_checkpoint = 50
miles_to_destination = 150
public_funds = 1000
Name_1 = ""
random_list = [1,2,3,4]
seasonal_list = ()
weather = ""
import random

def start():
	Oregon_Trail_Game() #starts a new game

def Oregon_Trail_Game(): #puts together all parts of game and takes in various inputs from user to control game. Allows user to input their name, pick a job/difficulty, and choose which season they start in. 
	global Name_1
	Name_1 = input("Please enter your name: ")
	print ("Welcome to the Oregon Trail " + str(Name_1) + " !\n")
	work = int(input("What career do you want your character to have? Each listed career starts with a different amount of money, listed from most to least. This will affect the difficulty of the game. Enter 1 for Banker, 2 for Merchant, 3 for Farmer: "))
	season_choice = int(input("What season do you want to leave in? Please keep in mind that it will be more difficult to leave in seasons with harsher weather. Enter 1 for winter, 2 for spring, 3 for summer, and 4 for fall: "))
	global season
	global seasonal_list
	global public_funds
	if work == 1:
		public_funds = 2000
	if work == 2:
		public_funds = 1500
	if work == 3:
		public_funds = 1000
	if season_choice == 1:
		season = "winter"
	if season_choice == 2:
		season = "spring"
	if season_choice == 3:
		season = "summer"
	if season_choice == 4:
		season = "fall"
	if season == "winter":
		seasonal_list = ("winter", "spring", "summer", "fall")
	if season == "spring":
		seasonal_list = ("spring", "summer", "fall", "winter")
	if season == "summer":
		seasonal_list = ("summer", "fall", "winter", "spring")
	if season == "fall":
		seasonal_list = ("fall", "winter", "spring", "summer")
	shop()
	user_choice()

def shop(): #allows user to buy items for game using the money they recieve when they pick a job previousely. User has option to buy oxen, food, spare parts and ammo for hunting. 
	global shop_dictionary
	global public_funds
	shop_dictionary = {'oxen' : 50, 'food' : 2, 'spare parts' : 20, 'ammo' : 5}
	print ("What do you want to buy? Please select 1 for oxen, 2 for food, 3 for spare parts, or 4 for ammo. When you are done shopping, please enter '5'.\n")
	shop_choice = int(input("Please enter a number from 1-5: "))
	if shop_choice == 1:
		print ("How many oxen do you want to buy? We recommend you buy at least 4 oxen. Each ox will cost you $50.\n")
		global oxen
		oxen = int(input("Please enter the number of oxen to buy: "))
		public_funds = public_funds - shop_dictionary['oxen'] * oxen
		if public_funds < 0:
			public_funds = public_funds + shop_dictionary['oxen'] * oxen
			print ("You don't have enough money for that! We've refunded your purchase.\n")
			shop()
		else:
			print ("You now have " + str(oxen) + " oxen and " + str(public_funds) + " dollars remaining.")
			shop()
	if shop_choice == 2:
		print ("How many pounds of food do you want to buy? We recommend you buy at least 150 pounds. Each pound will cost you $2.\n")
		global food
		food = int(input("Please enter the pounds of food to buy: "))
		public_funds = public_funds - shop_dictionary['food'] * food
		if public_funds < 0:
			public_funds = public_funds + shop_dictionary['food'] * food
			print ("You don't have enough money for that! We've refunded your purchase.\n")
			shop()
		else:
			print ("You now have " + str(food) + " pounds of food and " + str(public_funds) + " dollars remaining.\n")
			shop()
	if shop_choice == 3:
		print ("How many spare parts do you want to buy? We recommend you buy at least 3. Each part will cost you $20.\n")
		global spare_parts
		spare_parts = int(input("Please enter the number of parts to buy: "))
		public_funds = public_funds - shop_dictionary['spare parts'] * spare_parts
		if public_funds < 0:
			public_funds = public_funds + shop_dictionary['spare parts'] * spare_parts
			print ("You don't have enough money for that! We've refunded your purchase.\n")
			shop()
		else:
			print ("You now have " + str(spare_parts) + " spare parts and " + str(public_funds) + " dollars remaining.\n")
			shop()
	if shop_choice == 4:
		print ("How many bullets do you want to buy? We recommend you buy at least 20. Each bullet will cost you $5.\n")
		global ammo
		ammo = int(input("Please enter the number of bullets: "))
		public_funds = public_funds - shop_dictionary['ammo'] * ammo
		if public_funds < 0:
			public_funds = public_funds + shop_dictionary['ammo'] * ammo
			print ("You don't have enough money for that! We've refunded your purchase.\n")
			shop()
		else:
			print ("You now have " + str(ammo) + " bullets and " + str(public_funds) + " dollars remaining.\n")
			shop()
	if shop_choice == 5:
		 print ("You're ready to begin your journey. The Oregon Trail starts now.\n")
	if public_funds == 0:
		 print ("You have no more money to spend. It's time to begin your journey!\n")

def daily_health(random_list): #reveals the daily health of user. If user has dysentary, they lose more food per day making game harder. 
	global health
	global food
	random_list = random.choice(random_list)
	if random_list == 1:
		health = "has dysentary"
		food -= 2
		print(health)
	else:
		health = "Good"
		print(health)

def seasonal_health(weather): #makes it so user is more likely to get sick depending on the season. Colder seasons make it more likely for user to get dysentary. 
	global health
	if weather == "winter" or "fall":
		random_list = [1,2,3,4,5]
		daily_health(random_list)
	else:
		random_list = [1,2,3,4,5,6,7]
		daily_health(random_list)
	
def hunting(random_list): #allows user to hunt if they have sufficient ammo. User can catch 0 lbs, 50 lbs or 100 lbs of food. Most likely, the user will catch 50 lbs of food. 
	global food
	global ammo
	random_list = random.choice(random_list)
	if ammo < 5:
		print("You cannot hunt at this time. You don't have enough bullets.\n")
		user_choice()
	else:
		if random_list == 1 or random_list == 2:
			ammo -= 5
			food += 50
			print("You have caught 50 lbs of food.\n")
		if random_list == 3:
			ammo -= 5
			food += 0
			print("You have caught 0 lbs of food.\n")
		if random_list == 4:
			ammo -= 5
			food += 100
			print("You have caught 100 lbs of food.\n")
# winter= 1, spring= 2, summer= 3, fall= 4#
def current_weather(): #reveals the weather to the user depending on the season. 
	temp = random.choice(random_list)
	global weather
	global season
	if season == "summer":
		if temp == 1 or 2 or 3:
			weather = "hot"
		if temp == 4:
			weather = "unsatisfactory"
	if season == "winter":
		if temp == 1 or 2 or 3:
			weather = "frigid"
		if temp == 4:
			weather = "unsatisfactory"
	if season == "fall":
		if temp == 1 or 2:
			weather = "frigid"
		if temp == 3:
			weather = "pleasant" 
		if temp == 4:
			weather = "unsatisfactory"
	if season == "spring":
		if temp == 1 or 2:
			weather = "hot"
		if temp == 3:
			weather = "pleasant"
		if temp == 4:
			weather = "unsatisfactory"
      
def oxen_dying(): #oxen have a 1/15 chance of dying throughout the game. If an oxen dies the user loses one of the oxen. If the user has no oxen to pull the wagon, the game ends.
	global oxen
	probability = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
	number = random.choice(probability)
	if oxen > 0:
		if number == 6:
			oxen -= 1
			print("Oh no! One of your oxen has died!\n")

def wagon_breaking(): #the wagon has a 1/15 chance of breaking down. If the user has no spare parts left and their wagon breaks down, they lose the game. 
	global spare_parts
	probability = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
	number = random.choice(probability)
	if spare_parts > -1:
		if number == 13:
			spare_parts -= 1
			print("Oh no! Your wagon broke! You used one of your spare parts to fix it! Good job!\n")
	
def user_choice(): #allows user to make choice about day to day life on the Oregon Trail. If the user hits a checkpoint, they have the added option to shop or talk to the local civilians. Every day, the user gets the option to continue the journey, check their supplies, or hunt. The code also takes into account the factors that end or win the game and displays accordingly. Depending on the user's choice the variables will change. 
	global days
	global date
	global season
	global oxen
	global ammo
	global food
	global spare_parts
	global miles_traveled
	global seasonal_list
	global weather
	game_over()
	game_win()
	if miles_traveled == 50:
		print ("Welcome to your first checkpoint! You find a small town with several locals and small vendors selling supplies and oxen. Up ahead you see the mountainous, harsh terrain of the Oregon Trail. What would you like to do?\n")
		check1_choice = int(input("Please enter '1' to shop, '2' to talk to locals, or '3' to continue alog the trail: "))
		if check1_choice == 1:
			shop()
		if check1_choice == 2:
			print ("An elderly local man approaches you with sage words of advice. He says, 'According to all known laws of aviation, there is no way a bee should be able to fly. Its wings are too small to get its fat little body off the ground. The bee, of course, flies anyway; because bees don't care what humans think is impossible.' He then walks away with a tip of his hat. You continue on your journey a little bit wiser.\n")
			user_choice()
		if check1_choice == 3:
			days += 1
			date += 1
			miles_traveled += 5
			food -= 5
			user_choice()
	if miles_traveled == 100:
		print ("Welcome to your second checkpoint! You've happened upon a large mountain village with bustling shops and many locals dressed in heavy gear. There appears to be quite a few travelers just like you. What do you do next?\n")
		check2_choice = int(input("Please enter '1' to shop, '2' to talk to locals, or '3' to continue alog the trail: "))
		if check2_choice == 1:
			shop()
		if check2_choice == 2:
			print ("An old bear rocks back and forth on a chair, sipping black coffee and staring into the horizon.'Oski? Haven't heard that name in years...Lemme tell ya kid...Once I put on the suit they didn't care who I was underneath. So it never came off.' You walk away, shaken to your core. What an odd experience.\n")
			user_choice()
		if check2_choice == 3:
			days += 1
			date += 1
			miles_traveled += 5
			food -= 5
			user_choice()
	print("Choose 1 to continue the journey, 2 to see your items, and 3 to hunt. You will encounter checkpoints every 50 miles and the final destination after 150 miles.\n")
	x = int(input("Please enter a number: "))
	if x == 1:
		days += 1
		date += 1
		miles_traveled += 5
		food -= 5
		oxen_dying()
		wagon_breaking()
		current_weather()
		print("current state of health is")
		seasonal_health(season)
		if days > 50 and days < 100:
			season = seasonal_list[1]
			print("Days passed: {}, date: {}, season: {}, weather: {}, miles traveled {}".format(days, date, season, weather, miles_traveled))
			user_choice()
		if days > 100 and days < 150:
			season = seasonal_list[2]
			print("Days passed: {}, date: {}, season: {}, weather: {}, miles traveled {}".format(days, date, season, weather, miles_traveled))
			user_choice()
		if days > 150 and days < 200:
			season = seasonal_list[3]
			print("Days passed: {}, date: {}, season: {}, weather: {}, miles traveled {}".format(days, date, season, weather, miles_traveled))
			user_choice()
		if days < 50:
			season = seasonal_list[0]
			print("Days passed: {}, date: {}, season: {}, weather: {}, miles traveled {}".format(days, date, season, weather, miles_traveled))
			user_choice()
	if x == 2:
		print("Oxen: {}, Food: {}, Spare Parts {}, and Ammo {}".format(oxen, food, spare_parts, ammo))
		user_choice()
	if x == 3:
		hunting(random_list)
		user_choice()
	
def game_over(): #this ends the game. The user will lose the game if they run out of oxen, their wagon breaks and they have no spare parts, or they starve to death. Users can last 3 days without food before starving to death. 
	global oxen
	global spare_parts
	global food
	if oxen <= 0:
		print("Congratulations! You have no oxen left to pull your wagon. You lose.\n")
		quit()
	if spare_parts <= -1:
		print("Congratulations! Your wagon is broken and you can't fix it. You lose.\n")
		quit()
	if food <= -15:
		print("Congratulations! You've starved to death! You lose.\n")
		quit()

def game_win(): #this ends the game. The user will win the game if they make it all the way to the end of the trail without losing through the game over code. The game over code also tells the user their ending amounts of supplies and public funds. 
	global miles_traveled
	if miles_traveled == 150:
		print ("Congratulations! You reached the end of the trail. You beat the game with " + str(oxen) + " oxen, " + str(food) + " pounds of food and " + str(public_funds) + " dollars. Try playing again with different starting settings and see if you can still win!\n")
		quit()
