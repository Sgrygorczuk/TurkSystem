from User import *
from Project import *
from Team import *
from Bid import *
from Issue import *
import ezcommands as ez
#import jsonIO
from datetime import *
from random import randint
import random
#available functions
#run(reset = 0):    creates classes and can reset our data
#reload(): reloads the classes from db

total_users = 70
now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
dt_now = datetime.strptime(now, "%Y-%m-%d %H:%M:%S")
dt_later = dt_now + timedelta(days=1)
later = dt_later.strftime("%Y-%m-%d %H:%M:%S")

def n_days(n = 1, time = None):
	if time:
		now = time
	else:
		now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
	if n < 1:
		dt_now = datetime.strptime(now, "%Y-%m-%d %H:%M:%S") - timedelta(days = -n)
	else:
		dt_now = datetime.strptime(now, "%Y-%m-%d %H:%M:%S") + timedelta(days = n)
	next_days = dt_now.strftime("%Y-%m-%d %H:%M:%S")
	return next_days
	
def rand_days():
	return n_days(randint(2,7))

def reload(reset = 0):
	super_user.load_db(0)
	reload_users()
	reload_teams()
	reload_projects()
	reload_bids()
	reload_issues()

def run(reset = 0):
	#if reset = 1 reload all data
	#check if data exists, if so reload instead
	if super_user.load_db(0) and not reset:
		print("Data already exists, reloading data")
		return reload()
		
	jsonIO.create_DB("user_db")
	jsonIO.create_DB("team_db")
	jsonIO.create_DB("project_db")
	jsonIO.create_DB("bid_db")
	jsonIO.create_DB("issue_db")
	
	resume = ('''Text messaging, or texting, is the act of composing and sending electronic messages, 
typically consisting of alphabetic and numeric characters, between two or more users of mobile phones,
tablets, desktops/laptops, or other devices. Text messages may be sent over a cellular network, 
or may also be sent via an Internet connection.
\n The term originally referred to messages sent using the Short
Message Service (SMS). It has grown beyond alphanumeric text to 
include multimedia messages (known as MMS) containing digital images,
videos, and sound content, as well as ideograms known as emoji
(happy faces ,sad faces ,and other icons).\ n As of 2017,
text messages are used by youth and adults for personal,
family and social purposes and in business. Governmental
and non-governmental organizations use text messaging for
communication between colleagues. As with emailing, in the 2010s,
the sending of short informal messages has become an accepted part of many cultures.
[1] This makes texting a quick and easy way to communicate with friends and colleagues,
including in contexts where a call would be impolite or inappropriate (e.g., calling very 
late at night or when one knows the other person is busy with family or work activities). 
Like e-mail and voice mail, and unlike calls (in which the caller hopes to speak directly with the recipient),
texting does not require the caller and recipient to both be free at the same moment; this permits communication
even between busy individuals. Text messages can also be used to interact with automated systems, for example, to 
order products or services from e-commerce websites, or to participate in online contests. Advertisers and service
providers use direct text marketing to send messages to mobile users about promotions, payment due dates,
and other notifications instead of using postal mail, email, or voicemail.''')


	#create new users
	super_user.new_user(name = "System Admin", username = "admin", password = "pass", user_type = "SU",  balance = 100)
	
	user1.new_user(name = "Sebastian", username = "u1", password = "u1", user_type = "dev", balance = 100, resume = resume, interests = ["data", "statistics", "AI", "computer"], status = "active")
	user2.new_user(name = "Ronny", username = "u2", password = 'u2', user_type = "dev", balance = 100,  interests = get_rand_interest(), status = "active")
	user3.new_user(name = "David", username = "u3", password = 'u3', user_type = "dev", balance = 100, interests = get_rand_interest(), status = "active")
	user4.new_user(name = "Eun Jung", username = "u4", password = 'u4', user_type = "dev", balance = 100, interests = get_rand_interest(), status = "active")
	
	#generate generic users, <<<user 28,29, and 30 are developers with no team (this is set from below)>>>
	generate_new_user(5, 49, "dev")
	
	
	#################################################################################################################
	#CREATING CLIENT
	#################################################################################################################
	#clients are from 50-70
	client0.new_user(name = "Wei", username = "Wei", password = "Wei", user_type = "client", balance = 100000000, interests = ["engineering", "projects", "AI", "optimization"], pic ="wei.jpg", status = "active")
	client1.new_user(name = "isatou", username = "isatou", password = "isatou", user_type = "client", balance = 1000000, interests = ["data", "news", "music", "AI", "stocks"], pic ="isatou.jpg", status = "active")
	generate_new_user(52, 70, "client")
	reload_users()
	#################################################################################################################
	
	#Add special conditions here
	#they are admins
	user12.set_status("bidding")#team 8
	user13.set_status("bidding")#team 9
	user22.set_status("bidding")#team 8
	user23.set_status("bidding")#team 10
	user24.set_status("bidding")#team 10
	
	
	#################################################################################################################
	#CREATING TEAM
	#################################################################################################################
	#################################################################################################################
	#turksystem
	team0.new_team(admin_ids = [1], dev_ids = [1,2,3,4], name = "REDS") #project_status = complete
	user1.set_team_id(0)
	user2.set_team_id(0)
	user3.set_team_id(0)
	user4.set_team_id(0)
	#28,29,30 could be by themselves
	team1.new_team(admin_ids = [5], dev_ids = [5,15,20], name = "WallStreet, where many things can go wrong") #complete
	user5.set_team_id(1)
	user15.set_team_id(1)
	user20.set_team_id(1)
	team2.new_team(admin_ids = [6], dev_ids = [6,16], name = "One Cow Team") #complete
	user6.set_team_id(2)
	user16.set_team_id(2)
	team3.new_team(admin_ids = [7], dev_ids = [7,17], name = "Big") #complete
	user7.set_team_id(3)
	user17.set_team_id(3)
	team4.new_team(admin_ids = [8], dev_ids = [8,18], name = "Sad life") #complete
	user4.set_team_id(4)
	user4.set_team_id(4)
	team5.new_team(admin_ids = [9], dev_ids = [9,19], name = "Rainbow Darkness") #incomplete
	user9.set_team_id(5)
	user19.set_team_id(5)
	
	team6.new_team(admin_ids = [10,14], dev_ids = [10,14], name = "This") #active
	user10.set_team_id(6)
	user14.set_team_id(6)
	team7.new_team(admin_ids = [11], dev_ids = [11,21], name = "Group") #active 
	user11.set_team_id(7)
	user21.set_team_id(7)
	team8.new_team(admin_ids = [12,22], dev_ids = [12,22], name = "Will") #bidding
	user12.set_team_id(8)
	user22.set_team_id(8)
	team9.new_team(admin_ids = [13], dev_ids = [13], name = "Get") #bidding
	user13.set_team_id(9)
	team10.new_team(admin_ids = [23,24], dev_ids = [23,24,25,26,27], name = "Hundred") #bidding
	user23.set_team_id(10)
	user24.set_team_id(10)
	user25.set_team_id(10)
	user26.set_team_id(10)
	user27.set_team_id(10)
	
	#################################################################################################################
	#################################################################################################################
	#CREATING PROJECT
	#################################################################################################################
	#################################################################################################################
	#id 50 = client 0
	project0.new_project(50, bid_id = 0, title = "Turk System", desc = "Random group of four were able to make an awesome project", bid_end_date = now,  deadline = later, status= "complete")
	project1.new_project(51, bid_id = 1, title = "Hello", desc = "I have a lot of money", bid_end_date = later, deadline = rand_days(), status= "complete")
	project2.new_project(52, bid_id = 2, title = "World", desc = "I have a lot of money, too?", bid_end_date = later, deadline = rand_days(), status= "complete")
	project3.new_project(53, bid_id = 3, title = "Goodbye", desc = "I have more money than the other guy", bid_end_date = later, deadline = rand_days(), status= "complete")
	project4.new_project(54, bid_id = 4, title = "VR", desc = "Don't listen to any of them, I have the most", bid_end_date = later, deadline = rand_days(), status= "complete")
	project5.new_project(55, bid_id = 5, title = "Cow", desc = "Moo", bid_end_date = later, deadline = rand_days(), status= "complete")
	project6.new_project(56, bid_id = 6, title = "mack", desc = "I have a lot of money", bid_end_date = later, deadline = rand_days(), status= "complete")
	project7.new_project(57, bid_id = 7, title = "EM", desc = "I have a lot of money, too?", bid_end_date = later, deadline = rand_days(), status= "bidding")
	project8.new_project(58, bid_id = 8, title = "WE", desc = "I have more money than the other guy", bid_end_date = later, deadline = rand_days(), status= "bidding")
	project9.new_project(59, bid_id = 9, title = "EWW", desc = "Don't listen to any of them, I have the most", bid_end_date = later, deadline = rand_days(), status= "bidding")
	project10.new_project(60, bid_id = 10, title = "Cow", desc = "Moo", bid_end_date = later, deadline = rand_days(), status= "bidding")
	
	project11.new_project(61, bid_id = 11, title = "NO", desc = "I have a lot of money", bid_end_date = later, deadline = rand_days(), status= "bidding")
	project12.new_project(62, bid_id = 12, title = "MORE", desc = "I have a lot of money, too?", bid_end_date = later, deadline = rand_days(), status= "bidding")
	project13.new_project(63, bid_id = 13, title = "PROJECT", desc = "I have more money than the other guy", bid_end_date = later, deadline = rand_days(), status= "bidding")
	project14.new_project(64, bid_id = 14, title = "OR", desc = "Don't listen to any of them, I have the most", bid_end_date = later, deadline = rand_days(), status= "bidding")
	project15.new_project(65, bid_id = 15, title = "CORN", desc = "Moo", bid_end_date = later, deadline = rand_days(), status= "bidding")
	project16.new_project(66, bid_id = 16, title = "Companion Without Courage", desc = "I have a lot of money", bid_end_date = later, deadline = rand_days(), status= "bidding")
	project17.new_project(67, bid_id = 17, title = "Spider Without Honor", desc = "I have a lot of money, too?",  bid_end_date = later, deadline = rand_days(), status= "bidding")
	project18.new_project(68, bid_id = 18, title = "Fish Of The Light", desc = "I have more money than the other guy",  bid_end_date = later, deadline = rand_days(), status= "bidding")
	project19.new_project(69, bid_id = 19, title = "Doctors Of Eternity", desc = "Don't listen to any of them, I have the most",  bid_end_date = later, deadline = rand_days(), status= "complete")
	project20.new_project(50, bid_id = 20, title = "Lord of the Spiders", desc = "Moo", bid_end_date = later, deadline = rand_days(), status= "complete")

	project21.new_project(50, bid_id = 21, title = "Spiders And Phantoms", desc = "I have a lot of money", bid_end_date = later, deadline = rand_days(), status= "complete")
	project22.new_project(50, bid_id = 22, title = "World Of My Imagination", desc = "I have a lot of money, too?", bid_end_date = later, deadline = rand_days(), status= "complete")
	project23.new_project(50, bid_id = 23, title = "Country With Vigor", desc = "I have more money than the other guy", bid_end_date = later, deadline = rand_days(), status= "complete")
	project24.new_project(50, bid_id = 24, title = "Answering Technology", desc = "Don't listen to any of them, I have the most", bid_end_date = later, deadline = rand_days(), status= "complete")
	project25.new_project(50, bid_id = 25, title = "Rescue In The Ashes", desc = "Moo", bid_end_date = later, deadline = rand_days(), status= "complete")
	project26.new_project(50, bid_id = 26, title = "Student In My Nightmares", desc = "I have a lot of money", bid_end_date = later, deadline = rand_days(), status= "complete")
	project27.new_project(51, bid_id = 27, title = "Owl Behind You", desc = "I have a lot of money, too?", bid_end_date = later, deadline = rand_days(), status= "complete")
	project28.new_project(51, bid_id = 28, title = "Captain Of Outer Space", desc = "I have more money than the other guy", bid_end_date = later, deadline = rand_days(), status= "complete")
	project29.new_project(51, bid_id = 29, title = "Guardian Of Time", desc = "Don't listen to any of them, I have the most", bid_end_date = later, deadline = rand_days(), status= "complete")
	
	project30.new_project(51, bid_id = 30, title = "Defenders In The Future", desc = "Moo", bid_end_date = later, deadline = rand_days(), status= "complete")
	project31.new_project(51, bid_id = 31, title = "Death Of New Worlds", desc = "I have a lot of money", bid_end_date = later, deadline = rand_days(), status= "bidding")
	project32.new_project(51, bid_id = 32, title = "Recruits And Men", desc = "I have a lot of money, too?", bid_end_date = later, deadline = rand_days(), status= "bidding")
	project33.new_project(51, bid_id = 33, title = "Corruption Of Death", desc = "I have more money than the other guy", bid_end_date = later, deadline = rand_days(), status= "complete")
	project34.new_project(52, bid_id = 34, title = "Closed For The Guests", desc = "Don't listen to any of them, I have the most", bid_end_date = later, deadline = rand_days(), status= "complete")
	project35.new_project(52, bid_id = 35, title = "Origin Of New Technology", desc = "Moo", bid_end_date = later, deadline = rand_days(), status= "complete")
	project36.new_project(52, bid_id = 36, title = "Failing Of Solar Flares", desc = "I have a lot of money", bid_end_date = later, deadline = rand_days(), status= "complete")
	project37.new_project(52, bid_id = 37, title = "Droid In The Portal", desc = "I have a lot of money, too?", bid_end_date = later, deadline = rand_days(), status= "complete")
	project38.new_project(53, bid_id = 38, title = "Fate Of The Crash", desc = "I have more money than the other guy", bid_end_date = later, deadline = rand_days(), status= "complete")
	project39.new_project(53, bid_id = 39, title = "Future Of Time", desc = "Don't listen to any of them, I have the most", bid_end_date = later, deadline = rand_days(), status= "complete")
	project40.new_project(53, bid_id = 40, title = "Abandoned By Droids", desc = "Moo", bid_end_date = later, deadline = rand_days(), status= "complete")

	project41.new_project(53, bid_id = 41, title = "Glory Of Time Travellers", desc = "I have a lot of money", bid_end_date = later, deadline = rand_days(), status= "complete")
	project42.new_project(54, bid_id = 42, title = "Cyborgs And Men", desc = "I have a lot of money, too?", bid_end_date = later, deadline = rand_days(), status= "incomplete")
	project43.new_project(54, bid_id = 43, title = "Pros", desc = "I have more money than the other guy", bid_end_date = later, deadline = rand_days(), status= "complete")
	project44.new_project(54, bid_id = 44, title = "Enemies Of The Universe", desc = "Don't listen to any of them, I have the most", bid_end_date = later, deadline = rand_days(), status= "complete")
	project45.new_project(54, bid_id = 45, title = "Man Of The New World", desc = "Moo", bid_end_date = later, deadline = rand_days(), status= "complete")
	project46.new_project(55, bid_id = 46, title = "Afraid Of The End Of The Sun", desc = "I have a lot of money", bid_end_date = later, deadline = rand_days(), status= "complete")
	project47.new_project(55, bid_id = 47, title = "Woman With Tentacles", desc = "I have a lot of money, too?", bid_end_date = later, deadline = rand_days(), status= "complete")
	project48.new_project(55, bid_id = 48, title = "Husbands And Husbands", desc = "I have more money than the other guy", bid_end_date = later, deadline = rand_days(), status= "complete")
	project49.new_project(55, bid_id = 49, title = "Promises Of The Night", desc = "Don't listen to any of them, I have the most", bid_end_date = later, deadline = rand_days(), status= "complete")
	project50.new_project(56, bid_id = 50, title = "Wizards And Boys", desc = "Moo", bid_end_date = later, deadline = rand_days(), status= "complete")
	
	project51.new_project(56, bid_id = 51, title = "Merry", desc = "I have a lot of money", bid_end_date = later, deadline = rand_days(), status= "complete")
	project52.new_project(56, bid_id = 52, title = "Christmas", desc = "I have a lot of money, too?", bid_end_date = later, deadline = rand_days(), status= "incomplete")
	project53.new_project(56, bid_id = 53, title = "Everyone", desc = "I have more money than the other guy", bid_end_date = later, deadline = rand_days(), status= "complete")
	project54.new_project(57, bid_id = 54, title = "And", desc = "Don't listen to any of them, I have the most", bid_end_date = later, deadline = rand_days(), status= "complete")
	project55.new_project(57, bid_id = 55, title = "Happy", desc = "Moo", bid_end_date = later, deadline = rand_days(), status= "complete")
	project56.new_project(70, bid_id = 56, title = "New", desc = "I have a lot of money", bid_end_date = later, deadline = rand_days(), status= "complete")
	project57.new_project(70, bid_id = 57, title = "Years", desc = "I have a lot of money, too?", bid_end_date = later, deadline = rand_days(), status= "complete")
	project58.new_project(70, bid_id = 58, title = "Hope", desc = "I have more money than the other guy", bid_end_date = later, deadline = rand_days(), status= "complete")
	project59.new_project(70, bid_id = 59, title = "You", desc = "Don't listen to any of them, I have the most", bid_end_date = later, deadline = rand_days(), status= "complete")
	project60.new_project(70, bid_id = 60, title = "Enjoy", desc = "Moo", bid_end_date = later, deadline = rand_days(), status= "complete")
	
	#################################################################################################################
	#################################################################################################################
	#ADDING CLIENT PROJECT
	#################################################################################################################
	#################################################################################################################
	client0.set_project_ids([20,21,22,23,24,25,26,0])
	client1.set_project_ids([27,28,29,30,31,32,33,1])
	client2.set_project_ids([34,35,36,37,2])#active
	client3.set_project_ids([38,39,40,41,3])#active
	client4.set_project_ids([42,43,44,45,4])#active
	client5.set_project_ids([46,47,48,49,5])#active
	client6.set_project_ids([50,51,52,53,6])#active
	client7.set_project_ids([54,55,7])#bidding
	client8.set_project_ids([8])#bidding
	client9.set_project_ids([9])#bidding
	client10.set_project_ids([10]) #high rating
	client11.set_project_ids([11]) #low rating
	client12.set_project_ids([12])#bidding
	client13.set_project_ids([13])#bidding
	client14.set_project_ids([14])#bidding
	client15.set_project_ids([15])#bidding 
	client16.set_project_ids([16])#bidding
	client17.set_project_ids([17])#bidding - no bid
	client18.set_project_ids([18])#bidding - no bid
	client19.set_project_ids([19])#inactive
	client20.set_project_ids([56,57,58,59,60])#blacklisted 
	
	#################################################################################################################
	#################################################################################################################
	#ADDING USER/TEAMS TO PROJECT
	#################################################################################################################
	#################################################################################################################
	add_project_to_team(0,[19,20,21,22,0])
	add_project_to_team(1,[1,23,24,25,26,27,28,11])
	add_project_to_team(2,[2,29,30,31,32,33,34,12])
	add_project_to_team(3,[3,35,36,37,38,39,40,13])
	add_project_to_team(4,[4,41,42,43,14])
	add_project_to_team(5,[5,44,45,46,15])
	add_project_to_team(6,[6,47,48,49,16])
	add_project_to_team(7,[50,51,52,7])
	add_project_to_team(8,[8])
	add_project_to_team(9,[9])
	add_project_to_team(10,[10])
	#lone developer
	user30.set_project_ids([53,54,55,56,57,58,59,60])
	
	#################################################################################################################
	#################################################################################################################
	#CREATING BID
	#generic method: load from user and project into bid
	generate_bids()
	
	#################################################################################################################
	#CREATING ISSUE
	#generate_issues()
	
	generate_rating_n_comments()
	#generate_warnings()
	reload_teams()
	reload_projects()
	reload_bids()
	#################################################################################################################
	#################################################################################################################
	#HELPER FUNCTIONS
	#################################################################################################################
	#################################################################################################################
	
def generate_new_user(initial, end, user_type):
	for count in range(initial, end+1):
		balance = randint(100,500)
		name = "u"+str(count)
		jsonIO.add_row("user_db",{"id":count, "name":name, "username":name, "password":name,
			"user_type": user_type, "balance":balance, "status":"active", "warning":0,
			"resume":"", "pic":"default_user.png", "interests":get_rand_interest(), "issue_ids":[],
			"team_id":'Nan', "project_ids":[]})
	
def add_project_to_team(team_id, project_ids):
	#generic method: set team and their user's project ids
	jsonIO.set_value("team_db", team_id, "project_ids", project_ids)
	dev_ids = jsonIO.get_value("team_db", team_id, "dev_ids")
	for id in dev_ids:
		jsonIO.set_value("user_db", id, "project_ids", project_ids)

def generate_bids():
	#generic method: load from user and project into bid
	#not SU
	for i in range(total_users, 1, -1):
		user = jsonIO.get_row("user_db", i)
		project_ids = user["project_ids"]
		client_review = ""
		if project_ids:
			if user["user_type"] == "client":
				for id in project_ids:
					project = jsonIO.get_row("project_db", id)
					bid_log = [[ez.get_now(), user["id"], 100, project["deadline"]]]
					jsonIO.add_row("bid_db", {"id":id, "chosen_index": 'Nan', "bid_log":[[]], "client_review":client_review})
			elif user["user_type"] == "dev" and (project["status"] != "no bid"):
				proceed = 1
				if user["team_id"] != 'Nan':
					if user["id"] not in jsonIO.get_value("team_db", user["team_id"] , "admin_ids"):
						proceed = 0
				if proceed:
					for id in project_ids:
						chosen_id = 1
						bid = jsonIO.get_row("bid_db", id)
						bid["bid_log"].append ([ez.get_now(), user["id"], bid["bid_log"][-1][2]- randint(1,5), n_days(randint(-5, 0), project["deadline"])])
						jsonIO.set_row("bid_db", bid)
						
def get_rand_interest():
	interests = ['comedy', 'radio', 'security', 'internet', 'mobile', 'web', 'games', 'data', 'AI', 'computer', 'statistics',
	'books', 'music', 'news', 'stocks', 'money', 'robot', 'VR', 'food', 'engineering', 'projects', 'optimization']
	size = randint(1,len(interests)/2)
	indexes = random.sample(range(1,len(interests)), size)
	interest = []
	for index in indexes:
		interest.append(interests[index])
	return interest

def generate_rating_n_comments():
	projects = jsonIO.read_rows("project_db")
	for project in projects:
		if project["status"] == "incomplete":
			project["client_rating"] = 1
			project["client_review"] = "project incomplete"
		elif project["status"] == "complete":
			project["submission"] = "sample.txt"
			if project["team_rating"]:
				project["team_rating"] = randint(1,5)
			if project["team_rating"] < 3:
				project["team_review"] = "client was uncooperative"
			if not project["client_rating"]:
				project["client_rating"] = randint(1,5)
			if project["client_rating"] < 3:
				project["client_review"] = "team gave in terrible work"
		jsonIO.set_row("project_db", project)
	   
def generate_warnings():
	users = jsonIO.read_rows("user_db")
	if users:
		for user in users:
			if user["id"] > 0:
				amount = len(user["project_ids"])
				if ez.is_in_active_project(user):
					amount -= 1
				if ez.get_grade(user) < 2 and amount < 5:
					user["warning"] += 1
					jsonIO.set_row("user_db", user)

# def generate_issues():
	# projects = jsonIO.read_rows("project_db")
	# users = jsonIO.read_rows("user_db")
	# for project in projects:
		# if project["status"] == "bidding":
			# referred_id = project["client_id"]
			# issue = Issue(referred_id = referred_id, issue_desc = "payment")
	# for user in users:
		# if user['status'] == "temp":
			# referred_id = user["id"]
			# desc = "new user"
			# admin_review = ""
			# date_resolved = now
			# resolved = False
		# elif user["status"] == "reject":
			# referred_id = user["id"]
			# desc = "new user"
			# admin_review = "User has too little funds or already blacklisted"
			# date_resolved = now
			# resolved = True
		# elif user["status"] == "blacklisted":
			# referred_id = user["id"]
			# desc = "blacklisted"
			# admin_review = "Has reached maximum warnings"
			# date_resolved = now
			# resolved = True
		# jsonIO.add_row("issue_db",{"id":id, "referred_id":referred_id, "issue_desc":desc,
		# "admin_review":admin_review, "date_resolved":date_resolved, "resolved":resolved})
			
super_user = User()
user1 = User()
user2 = User()
user3 = User()
user4 = User()
user5 = User()
user6 = User()
user7 = User()
user8 = User()
user9 = User()
user10 = User()
user11 = User()
user12 = User()
user13 = User()
user14 = User()
user15 = User()
user16 = User()
user17 = User()
user18 = User()
user19 = User()
user20 = User()
user21 = User()
user22 = User()
user23 = User()
user24 = User()
user25 = User()
user26 = User()
user27 = User()
user28 = User()
user29 = User()
user30 = User()
user31 = User()
user32 = User()
user33 = User()
user34 = User()
user35 = User()
user36 = User()
user37 = User()
user38 = User()
user39 = User()
user40 = User()
user41 = User()
user42 = User()
user43 = User()
user44 = User()
user45 = User()
user46 = User()
user47 = User()
user48 = User()
user49 = User()

team0 = Team()
team1 = Team()
team2 = Team()
team3 = Team()
team4 = Team()
team5 = Team()
team6 = Team()
team7 = Team()
team8 = Team()
team9 = Team()
team10 = Team()

client0 = User()
client1 = User()
client2 = User()
client3 = User()
client4 = User()
client5 = User()
client6 = User()
client7 = User()
client8 = User()
client9 = User()
client10 = User()
client11 = User()
client12 = User()
client13 = User()
client14 = User()
client15 = User()
client16 = User()
client17 = User()
client18 = User()
client19 = User()
client20 = User()

project0 = Project()
project1 = Project()
project2 = Project()
project3 = Project()
project4 = Project()
project5 = Project()
project6 = Project()
project7 = Project()
project8 = Project()
project9 = Project()
project10 = Project()
project11 = Project()
project12 = Project()
project13 = Project()
project14 = Project()
project15 = Project()
project16 = Project()
project17 = Project()
project18 = Project()
project19 = Project()
project20 = Project()
project21 = Project()
project22 = Project()
project23 = Project()
project24 = Project()
project25 = Project()
project26 = Project()
project27 = Project()
project28 = Project()
project29 = Project()
project29 = Project()
project30 = Project()
project31 = Project()
project32 = Project()
project33 = Project()
project34 = Project()
project35 = Project()
project36 = Project()
project37 = Project()
project38 = Project()
project39 = Project()
project40 = Project()
project41 = Project()
project42 = Project()
project43 = Project()
project44 = Project()
project45 = Project()
project46 = Project()
project47 = Project()
project48 = Project()
project49 = Project()
project50 = Project()
project51 = Project()
project52 = Project()
project53 = Project()
project54 = Project()
project55 = Project()
project56 = Project()
project57 = Project()
project58 = Project()
project59 = Project()
project60 = Project()

bid0 = Bid()
bid1 = Bid()
bid2 = Bid()
bid3 = Bid()
bid4 = Bid()
bid5 = Bid()
bid6 = Bid()
bid7 = Bid()
bid8 = Bid()
bid9 = Bid()
bid10 = Bid()
bid11 = Bid()
bid12 = Bid()
bid13 = Bid()
bid14 = Bid()
bid15 = Bid()
bid16 = Bid()
bid17 = Bid()
bid18 = Bid()
bid19 = Bid()
bid20 = Bid()
bid21 = Bid()
bid22 = Bid()
bid23 = Bid()
bid24 = Bid()
bid25 = Bid()
bid26 = Bid()
bid27 = Bid()
bid28 = Bid()
bid29 = Bid()
bid30 = Bid()
bid31 = Bid()
bid32 = Bid()
bid33 = Bid()
bid34 = Bid()
bid35 = Bid()
bid36 = Bid()
bid37 = Bid()
bid38 = Bid()
bid39 = Bid()
bid40 = Bid()
bid41 = Bid()
bid42 = Bid()
bid43 = Bid()
bid44 = Bid()
bid45 = Bid()
bid46 = Bid()
bid47 = Bid()
bid48 = Bid()
bid49 = Bid()
bid50 = Bid()
bid51 = Bid()
bid52 = Bid()
bid53 = Bid()
bid54 = Bid()
bid55 = Bid()
bid56 = Bid()
bid57 = Bid()
bid58 = Bid()
bid59 = Bid()
bid60 = Bid()

issue0 = Issue()
issue1 = Issue()
issue2 = Issue()
issue3 = Issue()
issue4 = Issue()
issue5 = Issue()
issue6 = Issue()
issue7 = Issue()
issue8 = Issue()
issue9 = Issue()
issue10 = Issue()
# issue11 = Issue()
# issue12 = Issue()
# issue13 = Issue()
# issue14 = Issue()
# issue15 = Issue()
# issue16 = Issue()
# issue17 = Issue()
# issue18 = Issue()
# issue19 = Issue()
# issue20 = Issue()
# issue21 = Issue()
# issue22 = Issue()
# issue23 = Issue()
# issue24 = Issue()
# issue25 = Issue()
# issue26 = Issue()
# issue27 = Issue()
# issue28 = Issue()
# issue29 = Issue()
# issue30 = Issue()




def reload_users():
	user1.load_db(1)
	user2.load_db(2)
	user3.load_db(3)
	user4.load_db(4)
	user5.load_db(5)
	user6.load_db(6)
	user7.load_db(7)
	user8.load_db(8)
	user9.load_db(9)
	user10.load_db(10)
	user11.load_db(11)
	user12.load_db(12)
	user13.load_db(13)
	user14.load_db(14)
	user15.load_db(15)
	user16.load_db(16)
	user17.load_db(17)
	user18.load_db(18)
	user19.load_db(19)
	user20.load_db(20)
	user21.load_db(21)
	user22.load_db(22)
	user23.load_db(23)
	user24.load_db(24)
	user25.load_db(25)
	user26.load_db(26)
	user27.load_db(27)
	user28.load_db(28)
	user29.load_db(29)
	user30.load_db(30)
	user31.load_db(31)
	user32.load_db(32)
	user33.load_db(33)
	user34.load_db(34)
	user35.load_db(35)
	user36.load_db(36)
	user37.load_db(37)
	user38.load_db(38)
	user39.load_db(39)
	user40.load_db(40)
	user41.load_db(41)
	user42.load_db(42)
	user43.load_db(43)
	user44.load_db(44)
	user45.load_db(45)
	user46.load_db(46)
	user47.load_db(47)
	user48.load_db(48)
	user49.load_db(49)
	
	client0.load_db(50)
	client1.load_db(51)
	client2.load_db(52)
	client3.load_db(53)
	client4.load_db(54)
	client5.load_db(55)
	client6.load_db(56)
	client7.load_db(57)
	client8.load_db(58)
	client9.load_db(59)
	client10.load_db(60)
	client11.load_db(61)
	client12.load_db(62)
	client13.load_db(63)
	client14.load_db(64)
	client15.load_db(65)
	client16.load_db(66)
	client17.load_db(67)
	client18.load_db(68)
	client19.load_db(69)
	client20.load_db(70)
	
def reload_teams():
	team0.load_db(0)
	team1.load_db(1)
	team2.load_db(2)
	team3.load_db(3)
	team4.load_db(4)
	team5.load_db(5)
	team6.load_db(6)
	team7.load_db(7)
	team8.load_db(8)
	team9.load_db(9)
	team10.load_db(10)

def reload_projects():
	project0.load_db(0)
	project1.load_db(1)
	project2.load_db(2)
	project3.load_db(3)
	project4.load_db(4)
	project5.load_db(5)
	project6.load_db(6)
	project7.load_db(7)
	project8.load_db(8)
	project9.load_db(9)
	project10.load_db(10)
	project11.load_db(11)
	project12.load_db(12)
	project13.load_db(13)
	project14.load_db(14)
	project15.load_db(15)
	project16.load_db(16)
	project17.load_db(17)
	project18.load_db(18)
	project19.load_db(19)
	project20.load_db(20)
	project21.load_db(21)
	project22.load_db(22)
	project23.load_db(23)
	project24.load_db(24)
	project25.load_db(25)
	project26.load_db(26)
	project27.load_db(27)
	project28.load_db(28)
	project29.load_db(29)
	project30.load_db(30)
	project31.load_db(31)
	project32.load_db(32)
	project33.load_db(33)
	project34.load_db(34)
	project35.load_db(35)
	project36.load_db(36)
	project37.load_db(37)
	project38.load_db(38)
	project39.load_db(39)
	project40.load_db(40)
	project41.load_db(41)
	project42.load_db(42)
	project43.load_db(43)
	project44.load_db(44)
	project45.load_db(45)
	project46.load_db(46)
	project47.load_db(47)
	project48.load_db(48)
	project49.load_db(49)
	project50.load_db(50)
	project51.load_db(51)
	project52.load_db(52)
	project53.load_db(53)
	project54.load_db(54)
	project55.load_db(55)
	project56.load_db(56)
	project57.load_db(57)
	project58.load_db(58)
	project59.load_db(59)
	project60.load_db(60)
def reload_bids():
	bid0.load_db(0)
	bid1.load_db(1)
	bid2.load_db(2)
	bid3.load_db(3)
	bid4.load_db(4)
	bid5.load_db(5)
	bid6.load_db(6)
	bid7.load_db(7)
	bid8.load_db(8)
	bid9.load_db(9)
	bid10.load_db(10)
	bid11.load_db(11)
	bid12.load_db(12)
	bid13.load_db(13)
	bid14.load_db(14)
	bid15.load_db(15)
	bid16.load_db(16)
	bid17.load_db(17)
	bid18.load_db(18)
	bid19.load_db(19)
	bid20.load_db(20)
	bid21.load_db(21)
	bid22.load_db(22)
	bid23.load_db(23)
	bid24.load_db(24)
	bid25.load_db(25)
	bid26.load_db(26)
	bid27.load_db(27)
	bid28.load_db(28)
	bid29.load_db(29)
	bid30.load_db(30)
	bid31.load_db(31)
	bid32.load_db(32)
	bid33.load_db(33)
	bid34.load_db(34)
	bid35.load_db(35)
	bid36.load_db(36)
	bid37.load_db(37)
	bid38.load_db(38)
	bid39.load_db(39)
	bid40.load_db(40)
	bid41.load_db(41)
	bid42.load_db(42)
	bid43.load_db(43)
	bid44.load_db(44)
	bid45.load_db(45)
	bid46.load_db(46)
	bid47.load_db(47)
	bid48.load_db(48)
	bid49.load_db(49)
	bid50.load_db(50)
	bid51.load_db(51)
	bid52.load_db(52)
	bid53.load_db(53)
	bid54.load_db(54)
	bid55.load_db(55)
	bid56.load_db(56)
	bid57.load_db(57)
	bid58.load_db(58)
	bid59.load_db(59)
	bid60.load_db(60)
def reload_issues():
	issue0.load_db(0)
	issue1.load_db(1)
	issue2.load_db(2)
	issue3.load_db(3)
	issue4.load_db(4)
	issue5.load_db(5)
	issue6.load_db(6)
	issue7.load_db(7)
	issue8.load_db(8)
	issue9.load_db(9)
	issue10.load_db(10)
	# issue11.load_db(11)
	# issue12.load_db(12)
	# issue13.load_db(13)
	# issue14.load_db(14)
	# issue15.load_db(15)
	# issue16.load_db(16)
	# issue17.load_db(17)
	# issue18.load_db(18)
	# issue19.load_db(19)
	# issue20.load_db(20)
	# issue21.load_db(21)
	# issue22.load_db(22)
	# issue23.load_db(23)
	# issue24.load_db(24)
	# issue25.load_db(25)
	# issue26.load_db(26)
	# issue27.load_db(27)
	# issue28.load_db(28)
	# issue29.load_db(29)
	# issue30.load_db(30)