from User import *
from Project import *
from Team import *
from Bid import *
from Issue import *
import ezcommands as ez
#import jsonIO
from datetime import *
from random import randint

#available functions
#run(reset = 0):    creates classes and can reset our data
#reload(): reloads the classes from db

now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
dt_now = datetime.strptime(now, "%Y-%m-%d %H:%M:%S")
dt_later = dt_now + timedelta(days=1)
later = dt_later.strftime("%Y-%m-%d %H:%M:%S")
def n_days(n = 1):
	now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
	dt_now = datetime.strptime(now, "%Y-%m-%d %H:%M:%S")
	return dt_now + timedelta(days = n)

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

bid0 = Bid()
bid1 = Bid()
bid2 = Bid()
bid3 = Bid()
bid4 = Bid()

issue0 = Issue()
issue1 = Issue()
issue2 = Issue()
issue3 = Issue()

def reload(reset = 0):
	super_user.load_db(0)
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

	client0.load_db(20)
	client1.load_db(21)
	client2.load_db(22)
	client3.load_db(23)
	client4.load_db(24)
	client5.load_db(25)
	client6.load_db(26)
	client7.load_db(27)
	client8.load_db(28)
	client9.load_db(29)
	client10.load_db(30)
	client11.load_db(31)
	client12.load_db(32)
	client13.load_db(33)
	client14.load_db(34)

	project0.load_db(0)
	project1.load_db(1)
	project2.load_db(2)
	project3.load_db(3)
	project4.load_db(4)
	project5.load_db(5)
	project1.load_db(6)
	project2.load_db(7)
	project3.load_db(8)
	project4.load_db(9)
	project5.load_db(10)
	project1.load_db(11)
	project2.load_db(12)
	project3.load_db(13)
	project4.load_db(14)
	project5.load_db(15)

	bid0.load_db(0)
	bid1.load_db(1)
	bid2.load_db(2)
	bid3.load_db(3)
	bid4.load_db(4)
	
	issue0.load_db(0)
	issue1.load_db(1)
	issue2.load_db(2)
	issue3.load_db(3)

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

	super_user.new_user(name = "System Admin", username = "admin", password = "pass", user_type = "SU",  balance = 100)
	
	user1.new_user(name = "Sebastian", username = "u1", password = "u1", user_type = "dev", balance = 100, resume = resume, interests = ["data", "statistics", "AI", "computer"], status = "active")
	user2.new_user(name = "Ronny", username = "u2", password = 'u2', user_type = "dev", balance = 100,  interests = ["AI", "data", "statistics"], status = "active")
	user3.new_user(name = "David", username = "u3", password = 'u3', user_type = "dev", balance = 100, interests = ["books", "music", "games"], status = "active")
	user4.new_user(name = "Eun Jung", username = "u4", password = 'u4', user_type = "dev", balance = 100, interests = ["news", "stocks", "money"], status = "active")
	user5.new_user(name = "Bonder", username = "bonder", password = 'bonder', user_type = "dev", balance = 50, interests = ["robot", "AI", "computer"], status = "active")
	
	user6.new_user(name = "u6", username = "u6", password = 'u6', user_type = "dev", balance = 60, interests = ["VR", "books", "computer", "internet"], status = "active", warning = 1)
	user7.new_user(name = "u7", username = "u7", password = 'u7', user_type = "dev", balance = 70, interests = ["games", "web", "mobile", "internet"], status = "active")
	user8.new_user(name = "u8", username = "u8", password = 'u8', user_type = "dev", balance = 80, interests = ["radio", "web", "statistics", "internet"], status = "active", warning = 1)
	user9.new_user(name = "u9", username = "u9", password = 'u9', user_type = "dev", balance = 90, interests = ["mobile", "web", "mobile", "internet"], status = "bidding")
	user10.new_user(name = "u10", username = "u10", password = 'u10', user_type = "dev", balance = 100, interests = ["AI", "food", "money", "stocks"], status = "bidding")
	
	user11.new_user(name = "blah1", username = "blah1", password = '1', user_type = "dev", balance = 110, interests = ["games", "web", "radio", "web"], status = "temp")
	user12.new_user(name = "blah2", username = "blah2", password = '2', user_type = "dev", balance = 120, interests = ["security", "web", "mobile", "internet"], status = "temp")
	user13.new_user(name = "blah3", username = "blah3", password = '3', user_type = "dev", balance = 130, interests = ["comedy", "radio", "security", "internet"], status = "temp")
	user14.new_user(name = "blah4", username = "blah4", password = '4', user_type = "dev", balance = 140, interests = ["interent", "web", "mobile", "games"], status = "temp")
	user15.new_user(name = "blah5", username = "blah5", password = '5', user_type = "dev", balance = 150, interests = ["data", "web", "games", "internet"], status = "temp")
	
	user11.new_user(name = "blah6", username = "blah6", password = '6', user_type = "dev", balance = 110, interests = ["games", "web", "radio", "web"], status = "rejected")
	user12.new_user(name = "blah7", username = "blah7", password = '7', user_type = "dev", balance = 120, interests = ["security", "web", "mobile", "internet"], status = "rejected")
	user13.new_user(name = "blah8", username = "blah8", password = '8', user_type = "dev", balance = 130, interests = ["comedy", "radio", "security", "internet"], status = "rejected")
	user14.new_user(name = "blah9", username = "blah9", password = '9', user_type = "dev", balance = 140, interests = ["interent", "web", "mobile", "games"], status = "rejected")
	user15.new_user(name = "blah10", username = "blah10", password = '10', user_type = "dev", balance = 150, interests = ["data", "web", "games", "internet"], status = "rejected")
	
	user11.new_user(name = "blah11", username = "blah11", password = '11', user_type = "dev", balance = 110, interests = ["games", "web", "radio", "web"], status = "blacklisted", warning = 2)
	user12.new_user(name = "blah12", username = "blah12", password = '12', user_type = "dev", balance = 120, interests = ["security", "web", "mobile", "internet"], status = "blacklisted", warning = 2)
	user13.new_user(name = "blah13", username = "blah13", password = '13', user_type = "dev", balance = 130, interests = ["comedy", "radio", "security", "internet"], status = "blacklisted", warning = 2)
	user14.new_user(name = "blah14", username = "blah14", password = '14', user_type = "dev", balance = 140, interests = ["interent", "web", "mobile", "games"], status = "blacklisted", warning = 2)
	user15.new_user(name = "blah15", username = "blah15", password = '15', user_type = "dev", balance = 150, interests = ["data", "web", "games", "internet"], status = "blacklisted", warning = 2)
	
	user16.new_user(name = "blah16", username = "blah16", password = '16', user_type = "dev", balance = 110, interests = ["games", "web", "radio", "web"], status = "inactive", warning = 1)
	user17.new_user(name = "blah17", username = "blah17", password = '17', user_type = "dev", balance = 120, interests = ["security", "web", "mobile", "internet"], status = "inactive")
	user18.new_user(name = "blah18", username = "blah18", password = '18', user_type = "dev", balance = 130, interests = ["comedy", "radio", "security", "internet"], status = "inactive", warning = 1)
	user19.new_user(name = "blah19", username = "blah19", password = '19', user_type = "dev", balance = 140, interests = ["interent", "web", "mobile", "games"], status = "inactive")
	
	#turksystem
	team0.new_team(admin_ids = [1], dev_ids = [1,2,3,4], name = "REDS") 
	
	team1.new_team(admin_ids = [user1.get_id()], dev_ids = [user1.get_id(), user2.get_id()], name = "WallStreet, where many things can go wrong")
	team2.new_team(admin_ids = [user2.get_id()], dev_ids = [user2.get_id()], name = "One Cow Team")
	team3.new_team(admin_ids = [user4.get_id()], dev_ids = [user4.get_id()], name = "Big")
	team4.new_team(admin_ids = [user4.get_id()], dev_ids = [user4.get_id()], name = "Sad life")
	team5.new_team(admin_ids = [user4.get_id()], dev_ids = [user4.get_id()], name = "Rainbow Darkness")
	
	team6.new_team(admin_ids = [user4.get_id()], dev_ids = [user4.get_id()], name = "This")
	team7.new_team(admin_ids = [user4.get_id()], dev_ids = [user4.get_id()], name = "Group")
	team8.new_team(admin_ids = [user4.get_id()], dev_ids = [user4.get_id()], name = "Will")
	team9.new_team(admin_ids = [user4.get_id()], dev_ids = [user4.get_id()], name = "Get")
	team10.new_team(admin_ids = [user4.get_id()], dev_ids = [user4.get_id()], name = "Hundred")

	client0.new_user(name = "Wei", username = "Wei", password = "Wei", user_type = "client", balance = 100000000, interests = ["engineering", "projects", "AI", "optimization"], pic ="wei.jpg", status = "active")
	client1.new_user(name = "isatou", username = "isatou", password = "isatou", user_type = "client", balance = 1000000, interests = ["data", "news", "music", "AI", "stocks"], pic ="isatou.jpg", status = "active")
	
	client2.new_user(name = "c2", username = "c2", password = 'c2', user_type = "client", balance = 20, interests = ["games", "computer", "mobile", "statistics", "stocks"], status = "active")
	client3.new_user(name = "c3", username = "c3", password = 'c3', user_type = "client", balance = 30, interests = ["data", "web", "books", "AI", "music"], status = "active")
	client4.new_user(name = "c4", username = "c4", password = 'c4', user_type = "client", balance = 40, interests = ["games", "money", "mobile", "AI", "robot"], status = "active")
	client5.new_user(name = "c5", username = "c5", password = 'c5', user_type = "client", balance = 50, interests = ["radio", "web", "music", "internet"], status = "active")
	
	client6.new_user(name = "c6", username = "c6", password = "c6", user_type = "client", balance = 60, interests = ["data", "news", "music", "AI", "stocks"], status = "active")
	client7.new_user(name = "c7", username = "c7", password = 'c7', user_type = "client", balance = 70, interests = ["games", "computer", "food", "statistics", "stocks"], status = "active")
	client8.new_user(name = "c8", username = "c8", password = 'c8', user_type = "client", balance = 80, interests = ["data", "music", "books", "AI", "music"], status = "active")
	client9.new_user(name = "c9", username = "c9", password = 'c9', user_type = "client", balance = 90, interests = ["games", "money", "mobile", "AI", "robot"], status = "active", warning = 1)
	client10.new_user(name = "c10", username = "c10", password = 'c10', user_type = "client", balance = 100, interests = ["games", "money", "mobile", "AI", "robot"], status = "active")
	
	client11.new_user(name = "c11", username = "c11", password = "c11", user_type = "client", balance = 110, interests = ["data", "news", "music", "AI", "stocks"], status = "active")
	client12.new_user(name = "c12", username = "c12", password = 'c12', user_type = "client", balance = 5, interests = ["games", "computer", "mobile", "statistics", "stocks"], status = "temp")
	client13.new_user(name = "c13", username = "c13", password = 'c13', user_type = "client", balance = 120, interests = ["data", "web", "books", "AI", "music"], status = "inactive")
	client14.new_user(name = "c14", username = "c14", password = 'c14', user_type = "client", balance = 130, interests = ["games", "money", "mobile", "AI", "robot"], status = "rejected")
	client15.new_user(name = "c15", username = "c15", password = 'c15', user_type = "client", balance = 140, interests = ["games", "money", "mobile", "AI", "robot"], status = "blacklisted", warning = 2)

	project0.new_project(client_id = client0.get_id(), title = "Turk System", desc = "Random group of four were able to make an awesome project",  deadline = later)
	project1.new_project(client_id = client1.get_id(), client_rating = 3, team_rating = 4, title = "Hello", desc = "I have a lot of money", deadline = later, bid_end_date = later)
	project2.new_project(client_id = client2.get_id(), client_rating = 2, team_rating = 3, title = "World", desc = "I have a lot of money, too?", deadline = later, bid_end_date = later)
	project3.new_project(client_id = client3.get_id(), client_rating = 4, team_rating = 2, title = "Goodbye", desc = "I have more money than the other guy", deadline = later, bid_end_date = later)
	project4.new_project(client_id = client4.get_id(), client_rating = 3, team_rating = 4, title = "VR", desc = "Don't listen to any of them, I have the most", deadline = later, bid_end_date = later)
	project5.new_project(client_id = client5.get_id(), status = "active", title = "Cow", desc = "Moo", deadline = later, bid_end_date = later)

	project6.new_project(client_id = client1.get_id(), client_rating = 3, team_rating = 4, title = "mack", desc = "I have a lot of money", deadline = later, bid_end_date = later)
	project7.new_project(client_id = client2.get_id(), client_rating = 2, team_rating = 3, title = "EM", desc = "I have a lot of money, too?", deadline = later, bid_end_date = later)
	project8.new_project(client_id = client3.get_id(), client_rating = 4, team_rating = 2, title = "WE", desc = "I have more money than the other guy", deadline = later, bid_end_date = later)
	project9.new_project(client_id = client4.get_id(), client_rating = 3, team_rating = 4, title = "EWW", desc = "Don't listen to any of them, I have the most", deadline = later, bid_end_date = later)
	project10.new_project(client_id = client5.get_id(), status = "active", title = "BAH", desc = "HAB", deadline = later, bid_end_date = later)
	
	project11.new_project(client_id = client6.get_id(), client_rating = 3, team_rating = 4, title = "NO", desc = "I have a lot of money", deadline = later, bid_end_date = later)
	project12.new_project(client_id = client7.get_id(), client_rating = 2, team_rating = 3, title = "MORE", desc = "I have a lot of money, too?", deadline = later, bid_end_date = later)
	project13.new_project(client_id = client8.get_id(), client_rating = 4, team_rating = 2, title = "PROJECT", desc = "I have more money than the other guy", deadline = later, bid_end_date = later)
	project14.new_project(client_id = client9.get_id(), client_rating = 3, team_rating = 4, title = "OR", desc = "Don't listen to any of them, I have the most", deadline = later, bid_end_date = later)
	project15.new_project(client_id = client10.get_id(), status = "active", title = "NOT", desc = "Moo", deadline = later, bid_end_date = later)
	
	user1.add_project_ids(project1.get_id())
	user2.add_project_ids(project1.get_id())
	user3.add_project_ids(project1.get_id())
	user4.add_project_ids(project1.get_id())
	user5.add_project_ids(project2.get_id())
	user6.add_project_ids(project2.get_id())
	user7.add_project_ids(project2.get_id())
	user8.add_project_ids(project2.get_id())
	user9.add_project_ids(project2.get_id())
	user10.add_project_ids(project2.get_id())
	user11.add_project_ids(project2.get_id())
	user12.add_project_ids(project2.get_id())
	
	bid0.new_bid(project_id = project0.get_id(), bid_log = [[now, client0.get_id(), 1000, later]])
	bid1.new_bid(project_id = project1.get_id(), bid_log = [[now, client0.get_id(), 1000, later]])
	bid2.new_bid(project_id = project2.get_id(), bid_log = [[now, client0.get_id(), 1000, later]])
	bid3.new_bid(project_id = project3.get_id(), bid_log = [[now, client0.get_id(), 1000, later]])
	bid4.new_bid(project_id = project4.get_id(), bid_log = [[now, client0.get_id(), 1000, later]])
	
	issue0.new_issue(referred_id = 1, issue_desc ="new user")
	issue1.new_issue(referred_id = 2, issue_desc ="new user", admin_review = "user denied", date_resolved = now)
	issue2.new_issue(referred_id = 2, issue_desc ="new user")
	issue3.new_issue(referred_id = 5, issue_desc ="quit request")