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
	next_days = dt_now.strftime("%Y-%m-%d %H:%M:%S")
	return next_days

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

	bid0.load_db(0)
	bid1.load_db(1)
	bid2.load_db(2)
	bid3.load_db(3)
	bid4.load_db(4)
	bid5.load_db(55)
	bid6.load_db(56)
	bid7.load_db(57)
	bid8.load_db(58)
	bid9.load_db(59)
	bid10.load_db(60)
	bid11.load_db(61)
	bid12.load_db(62)
	bid13.load_db(63)
	bid14.load_db(64)
	bid15.load_db(65)
	
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
	user9.new_user(name = "u9", username = "u9", password = 'u9', user_type = "dev", balance = 90, interests = ["mobile", "web", "mobile", "internet"], status = "active")
	user10.new_user(name = "u10", username = "u10", password = 'u10', user_type = "dev", balance = 100, interests = ["AI", "food", "money", "stocks"], status = "active")
	user11.new_user(name = "u11", username = "u11", password = 'u11', user_type = "dev", balance = 110, interests = ["games", "web", "radio", "web"], status = "active")
	user12.new_user(name = "u12", username = "u12", password = 'u12', user_type = "dev", balance = 120, interests = ["security", "web", "mobile", "internet"], status = "active")
	user13.new_user(name = "u13", username = "u13", password = 'u13', user_type = "dev", balance = 130, interests = ["comedy", "radio", "security", "internet"], status = "active")
	user14.new_user(name = "u14", username = "u14", password = 'u14', user_type = "dev", balance = 140, interests = ["interent", "web", "mobile", "games"], status = "active")
	user15.new_user(name = "u15", username = "u15", password = 'u15', user_type = "dev", balance = 150, interests = ["data", "web", "games", "internet"], status = "active")
	user16.new_user(name = "u16", username = "u16", password = 'u16', user_type = "dev", balance = 110, interests = ["games", "web", "radio", "web"], status = "active")
	user17.new_user(name = "u17", username = "u17", password = 'u17', user_type = "dev", balance = 120, interests = ["security", "web", "mobile", "internet"], status = "active")
	user18.new_user(name = "u18", username = "u18", password = 'u18', user_type = "dev", balance = 130, interests = ["comedy", "radio", "security", "internet"], status = "active")
	user19.new_user(name = "u19", username = "u19", password = 'u19', user_type = "dev", balance = 140, interests = ["interent", "web", "mobile", "games"], status = "active")
	user20.new_user(name = "u20", username = "u20", password = 'u20', user_type = "dev", balance = 150, interests = ["data", "web", "games", "internet"], status = "active")
	user21.new_user(name = "u21", username = "u21", password = 'u21', user_type = "dev", balance = 110, interests = ["games", "web", "radio", "web"], status = "active")
	user22.new_user(name = "u22", username = "u22", password = 'u22', user_type = "dev", balance = 120, interests = ["security", "web", "mobile", "internet"], status = "active")
	user23.new_user(name = "u23", username = "u23", password = 'u23', user_type = "dev", balance = 130, interests = ["comedy", "radio", "security", "internet"], status = "active")
	user24.new_user(name = "u24", username = "u24", password = 'u24', user_type = "dev", balance = 140, interests = ["interent", "web", "mobile", "games"], status = "active")
	user25.new_user(name = "u25", username = "u25", password = 'u25', user_type = "dev", balance = 150, interests = ["data", "web", "games", "internet"], status = "active", warning = 2)
	
	user26.new_user(name = "u26", username = "u26", password = 'u26', user_type = "dev", balance = 110, interests = ["games", "web", "radio", "web"], status = "bidding")
	user27.new_user(name = "u27", username = "u27", password = 'u27', user_type = "dev", balance = 120, interests = ["security", "web", "mobile", "internet"], status = "bidding")
	user28.new_user(name = "u28", username = "u28", password = 'u28', user_type = "dev", balance = 130, interests = ["comedy", "radio", "security", "internet"], status = "bidding")
	user29.new_user(name = "u29", username = "u29", password = 'u29', user_type = "dev", balance = 140, interests = ["interent", "web", "mobile", "games"], status = "bidding")
	user30.new_user(name = "u30", username = "u30", password = 'u30', user_type = "dev", balance = 150, interests = ["data", "web", "games", "internet"], status = "bidding")
	
	user31.new_user(name = "u31", username = "u31", password = 'u31', user_type = "dev", balance = 110, interests = ["games", "web", "radio", "web"], status = "temp")
	user32.new_user(name = "u32", username = "u32", password = 'u32', user_type = "dev", balance = 120, interests = ["security", "web", "mobile", "internet"], status = "temp")
	user33.new_user(name = "u33", username = "u33", password = 'u33', user_type = "dev", balance = 130, interests = ["comedy", "radio", "security", "internet"], status = "temp")
	user34.new_user(name = "u34", username = "u34", password = 'u34', user_type = "dev", balance = 140, interests = ["interent", "web", "mobile", "games"], status = "temp")
	user35.new_user(name = "u35", username = "u35", password = 'u35', user_type = "dev", balance = 150, interests = ["data", "web", "games", "internet"], status = "temp")
	
	user36.new_user(name = "blah6", username = "admin", password = '6', user_type = "dev", balance = 110, interests = ["games", "web", "radio", "web"], status = "rejected")
	user37.new_user(name = "blah7", username = "blah8", password = '8', user_type = "dev", balance = 5, interests = ["security", "web", "mobile", "internet"], status = "rejected")
	user38.new_user(name = "blah8", username = "blah8", password = '8', user_type = "dev", balance = 5, interests = ["comedy", "radio", "security", "internet"], status = "rejected")
	user39.new_user(name = "blah9", username = "blah11", password = '10', user_type = "dev", balance = 140, interests = ["interent", "web", "mobile", "games"], status = "rejected")
	user40.new_user(name = "blah10", username = "blah10", password = '10', user_type = "dev", balance = 5, interests = ["data", "web", "games", "internet"], status = "rejected")
	
	user41.new_user(name = "blah11", username = "blah11", password = '11', user_type = "dev", balance = 110, interests = ["games", "web", "radio", "web"], status = "blacklisted", warning = 2)
	user42.new_user(name = "blah12", username = "blah12", password = '12', user_type = "dev", balance = 120, interests = ["security", "web", "mobile", "internet"], status = "blacklisted", warning = 2)
	user43.new_user(name = "blah13", username = "blah13", password = '13', user_type = "dev", balance = 130, interests = ["comedy", "radio", "security", "internet"], status = "blacklisted", warning = 2)
	user44.new_user(name = "blah14", username = "blah14", password = '14', user_type = "dev", balance = 140, interests = ["interent", "web", "mobile", "games"], status = "blacklisted", warning = 2)
	user45.new_user(name = "blah15", username = "blah15", password = '15', user_type = "dev", balance = 150, interests = ["data", "web", "games", "internet"], status = "blacklisted", warning = 2)
	
	user46.new_user(name = "blah16", username = "blah16", password = '16', user_type = "dev", balance = 110, interests = ["games", "web", "radio", "web"], status = "inactive", warning = 1)
	user47.new_user(name = "blah17", username = "blah17", password = '17', user_type = "dev", balance = 120, interests = ["security", "web", "mobile", "internet"], status = "inactive")
	user48.new_user(name = "blah18", username = "blah18", password = '18', user_type = "dev", balance = 130, interests = ["comedy", "radio", "security", "internet"], status = "inactive", warning = 1)
	user49.new_user(name = "blah19", username = "blah19", password = '19', user_type = "dev", balance = 140, interests = ["interent", "web", "mobile", "games"], status = "inactive")
	
	#################################################################################################################
	#################################################################################################################
	#CREATING TEAM
	#################################################################################################################
	#################################################################################################################
	#turksystem
	team0.new_team(admin_ids = [1], dev_ids = [1,2,3,4], name = "REDS") 
	#14,24,25 could be by themselves
	team1.new_team(admin_ids = [5], dev_ids = [5,15,20], name = "WallStreet, where many things can go wrong")
	team2.new_team(admin_ids = [6], dev_ids = [6,16], name = "One Cow Team")
	team3.new_team(admin_ids = [7], dev_ids = [7,17], name = "Big")
	team4.new_team(admin_ids = [8], dev_ids = [8,18], name = "Sad life")
	team5.new_team(admin_ids = [9], dev_ids = [9,19], name = "Rainbow Darkness")
	
	team6.new_team(admin_ids = [10,21], dev_ids = [10,21], name = "This")
	team7.new_team(admin_ids = [11], dev_ids = [11,22], name = "Group")
	team8.new_team(admin_ids = [12,23], dev_ids = [12,23], name = "Will")
	team9.new_team(admin_ids = [13], dev_ids = [13], name = "Get")
	team10.new_team(admin_ids = [26,27], dev_ids = [26,27,28,29,30], name = "Hundred")
	
	#################################################################################################################
	#################################################################################################################
	#CREATING CLIENT
	#################################################################################################################
	#################################################################################################################
	
	client0.new_user(name = "Wei", username = "Wei", password = "Wei", user_type = "client", balance = 100000000, interests = ["engineering", "projects", "AI", "optimization"], pic ="wei.jpg", status = "active")
	client1.new_user(name = "isatou", username = "isatou", password = "isatou", user_type = "client", balance = 1000000, interests = ["data", "news", "music", "AI", "stocks"], pic ="isatou.jpg", status = "active")
	
	client2.new_user(name = "c2", username = "c2", password = 'c2', user_type = "client", balance = 20, interests = ["games", "computer", "mobile", "statistics", "stocks"], status = "active")
	client3.new_user(name = "c3", username = "c3", password = 'c3', user_type = "client", balance = 30, interests = ["data", "web", "books", "AI", "music"], status = "active")
	client4.new_user(name = "c4", username = "c4", password = 'c4', user_type = "client", balance = 40, interests = ["games", "money", "mobile", "AI", "robot"], status = "active", warning = 1)
	client5.new_user(name = "c5", username = "c5", password = 'c5', user_type = "client", balance = 50, interests = ["radio", "web", "music", "internet"], status = "active")
	
	client6.new_user(name = "c6", username = "c6", password = "c6", user_type = "client", balance = 60, interests = ["data", "news", "music", "AI", "stocks"], status = "active")
	client7.new_user(name = "c7", username = "c7", password = 'c7', user_type = "client", balance = 70, interests = ["games", "computer", "food", "statistics", "stocks"], status = "active")
	client8.new_user(name = "c8", username = "c8", password = 'c8', user_type = "client", balance = 80, interests = ["data", "music", "books", "AI", "music"], status = "active")
	client9.new_user(name = "c9", username = "c9", password = 'c9', user_type = "client", balance = 90, interests = ["games", "money", "mobile", "AI", "robot"], status = "active", warning = 1)
	client10.new_user(name = "c10", username = "c10", password = 'c10', user_type = "client", balance = 100, interests = ["games", "money", "mobile", "AI", "robot"], status = "active")
	
	client11.new_user(name = "c11", username = "c11", password = "c11", user_type = "client", balance = 110, interests = ["data", "news", "music", "AI", "stocks"], status = "active", warning = 2)
	client12.new_user(name = "c12", username = "c12", password = 'c12', user_type = "client", balance = 120, interests = ["games", "computer", "mobile", "statistics", "stocks"], status = "temp")
	client13.new_user(name = "c13", username = "c13", password = 'c13', user_type = "client", balance = 130, interests = ["data", "web", "books", "AI", "music"], status = "inactive")
	client14.new_user(name = "c14", username = "c14", password = 'c14', user_type = "client", balance = 140, interests = ["games", "money", "mobile", "AI", "robot"], status = "blacklisted", warning = 2)
	client15.new_user(name = "c15", username = "c15", password = 'c15', user_type = "client", balance = 5, interests = ["games", "money", "mobile", "AI", "robot"], status = "rejected")

	#################################################################################################################
	#################################################################################################################
	#CREATING PROJECT
	#################################################################################################################
	#################################################################################################################
	
	project0.new_project(client_id = client0.get_id(), bid_id = 0, title = "Turk System", desc = "Random group of four were able to make an awesome project", bid_end_date = now,  deadline = later, status= "active")
	project1.new_project(client_id = client1.get_id(), bid_id = 1, title = "Hello", desc = "I have a lot of money", bid_end_date = later, deadline = n_days(2), status= "active")
	project2.new_project(client_id = client2.get_id(), bid_id = 2, title = "World", desc = "I have a lot of money, too?", bid_end_date = later, deadline = n_days(2), status= "active")
	project3.new_project(client_id = client3.get_id(), bid_id = 3, title = "Goodbye", desc = "I have more money than the other guy", bid_end_date = later, deadline = n_days(2), status= "active")
	project4.new_project(client_id = client4.get_id(), bid_id = 4, title = "VR", desc = "Don't listen to any of them, I have the most", bid_end_date = later, deadline = n_days(2), status= "active")
	project5.new_project(client_id = client5.get_id(), bid_id = 5, title = "Cow", desc = "Moo", bid_end_date = later, deadline = n_days(2), status= "active")

	project6.new_project(client_id = client6.get_id(), bid_id = 6, title = "mack", desc = "I have a lot of money", bid_end_date = later, deadline = n_days(2), status= "active")
	project7.new_project(client_id = client7.get_id(), bid_id = 7, title = "EM", desc = "I have a lot of money, too?", bid_end_date = later, deadline = n_days(2), status= "active")
	project8.new_project(client_id = client8.get_id(), bid_id = 8, title = "WE", desc = "I have more money than the other guy", bid_end_date = later, deadline = n_days(2), status= "active")
	project9.new_project(client_id = client9.get_id(), bid_id = 9, title = "EWW", desc = "Don't listen to any of them, I have the most", bid_end_date = later, deadline = n_days(2), status= "active")
	project10.new_project(client_id = client10.get_id(), bid_id = 10, title = "Cow", desc = "Moo", bid_end_date = later, deadline = n_days(2), status= "active")
	
	project11.new_project(client_id = client11.get_id(), bid_id = 11, title = "NO", desc = "I have a lot of money", bid_end_date = later, deadline = n_days(2), status= "active")
	project12.new_project(client_id = client12.get_id(), bid_id = 12, title = "MORE", desc = "I have a lot of money, too?", bid_end_date = later, deadline = n_days(2), status= "active")
	project13.new_project(client_id = client13.get_id(), bid_id = 13, title = "PROJECT", desc = "I have more money than the other guy", bid_end_date = later, deadline = n_days(2), status= "active")
	project14.new_project(client_id = client14.get_id(), bid_id = 14, title = "OR", desc = "Don't listen to any of them, I have the most", bid_end_date = later, deadline = n_days(2), status= "active")
	project15.new_project(client_id = client15.get_id(), bid_id = 15, title = "Cow", desc = "Moo", bid_end_date = later, deadline = n_days(2), status= "active")
	
	project16.new_project(client_id = client11.get_id(), bid_id = 16, title = "NO", desc = "I have a lot of money", bid_end_date = later, deadline = n_days(2), status= "active")
	project17.new_project(client_id = client11.get_id(), bid_id = 17, title = "MORE", desc = "I have a lot of money, too?",  bid_end_date = later, deadline = n_days(2), status= "active")
	project18.new_project(client_id = client12.get_id(), bid_id = 18, title = "PROJECT", desc = "I have more money than the other guy",  bid_end_date = later, deadline = n_days(2), status= "active")
	project19.new_project(client_id = client13.get_id(), bid_id = 19, title = "OR", desc = "Don't listen to any of them, I have the most",  bid_end_date = later, deadline = n_days(2), status= "active")
	project20.new_project(client_id = client14.get_id(), bid_id = 20, title = "NOT", desc = "Moo", bid_end_date = later, deadline = n_days(2), status= "active")

	project21.new_project(client_id = client6.get_id(), bid_id = 21, title = "NO", desc = "I have a lot of money", bid_end_date = later, deadline = n_days(2), status= "active")
	project22.new_project(client_id = client7.get_id(), bid_id = 22, title = "MORE", desc = "I have a lot of money, too?", bid_end_date = later, deadline = n_days(2), status= "active")
	project23.new_project(client_id = client8.get_id(), bid_id = 23, title = "PROJECT", desc = "I have more money than the other guy", bid_end_date = later, deadline = n_days(2), status= "active")
	project24.new_project(client_id = client9.get_id(), bid_id = 24, title = "OR", desc = "Don't listen to any of them, I have the most", bid_end_date = later, deadline = n_days(2), status= "active")
	project25.new_project(client_id = client10.get_id(), bid_id = 25, title = "NOT", desc = "Moo", bid_end_date = later, deadline = n_days(2), status= "active")
	
	project26.new_project(client_id = client6.get_id(), bid_id = 26, title = "NO", desc = "I have a lot of money", bid_end_date = later, deadline = n_days(2), status= "active")
	project27.new_project(client_id = client7.get_id(), bid_id = 27, title = "MORE", desc = "I have a lot of money, too?", bid_end_date = later, deadline = n_days(2), status= "active")
	project28.new_project(client_id = client8.get_id(), bid_id = 28, title = "PROJECT", desc = "I have more money than the other guy", bid_end_date = later, deadline = n_days(2), status= "active")
	project29.new_project(client_id = client9.get_id(), bid_id = 29, title = "OR", desc = "Don't listen to any of them, I have the most", bid_end_date = later, deadline = n_days(2), status= "active")
	project30.new_project(client_id = client10.get_id(), bid_id = 30, title = "NOT", desc = "Moo", bid_end_date = later, deadline = n_days(2), status= "active")
	
	project31.new_project(client_id = client6.get_id(), bid_id = 31, title = "NO", desc = "I have a lot of money", bid_end_date = later, deadline = n_days(2), status= "active")
	project32.new_project(client_id = client7.get_id(), bid_id = 32, title = "MORE", desc = "I have a lot of money, too?", bid_end_date = later, deadline = n_days(2), status= "active")
	project33.new_project(client_id = client8.get_id(), bid_id = 33, title = "PROJECT", desc = "I have more money than the other guy", bid_end_date = later, deadline = n_days(2), status= "active")
	project34.new_project(client_id = client9.get_id(), bid_id = 34, title = "OR", desc = "Don't listen to any of them, I have the most", bid_end_date = later, deadline = n_days(2), status= "active")
	project35.new_project(client_id = client10.get_id(), bid_id = 35, title = "NOT", desc = "Moo", bid_end_date = later, deadline = n_days(2), status= "active")
	
	project36.new_project(client_id = client6.get_id(), bid_id = 36, title = "NO", desc = "I have a lot of money", bid_end_date = later, deadline = n_days(2), status= "active")
	project37.new_project(client_id = client7.get_id(), bid_id = 37, title = "MORE", desc = "I have a lot of money, too?", bid_end_date = later, deadline = n_days(2), status= "active")
	project38.new_project(client_id = client8.get_id(), bid_id = 38, title = "PROJECT", desc = "I have more money than the other guy", bid_end_date = later, deadline = n_days(2), status= "active")
	project39.new_project(client_id = client9.get_id(), bid_id = 39, title = "OR", desc = "Don't listen to any of them, I have the most", bid_end_date = later, deadline = n_days(2), status= "active")
	project40.new_project(client_id = client10.get_id(), bid_id = 40, title = "NOT", desc = "Moo", bid_end_date = later, deadline = n_days(2), status= "active")
	
	project41.new_project(client_id = client6.get_id(), bid_id = 41, title = "NO", desc = "I have a lot of money", bid_end_date = later, deadline = n_days(2), status= "active")
	project42.new_project(client_id = client7.get_id(), bid_id = 42, title = "MORE", desc = "I have a lot of money, too?", bid_end_date = later, deadline = n_days(2), status= "active")
	project43.new_project(client_id = client8.get_id(), bid_id = 43, title = "PROJECT", desc = "I have more money than the other guy", bid_end_date = later, deadline = n_days(2), status= "active")
	project44.new_project(client_id = client9.get_id(), bid_id = 44, title = "OR", desc = "Don't listen to any of them, I have the most", bid_end_date = later, deadline = n_days(2), status= "active")
	project45.new_project(client_id = client10.get_id(), bid_id = 45, title = "NOT", desc = "Moo", bid_end_date = later, deadline = n_days(2), status= "active")
	
	project46.new_project(client_id = client6.get_id(), bid_id = 46, title = "NO", desc = "I have a lot of money", bid_end_date = later, deadline = n_days(2), status= "active")
	project47.new_project(client_id = client7.get_id(), bid_id = 47, title = "MORE", desc = "I have a lot of money, too?", bid_end_date = later, deadline = n_days(2), status= "active")
	project48.new_project(client_id = client8.get_id(), bid_id = 48, title = "PROJECT", desc = "I have more money than the other guy", bid_end_date = later, deadline = n_days(2), status= "active")
	project49.new_project(client_id = client9.get_id(), bid_id = 49, title = "OR", desc = "Don't listen to any of them, I have the most", bid_end_date = later, deadline = n_days(2), status= "active")
	project50.new_project(client_id = client10.get_id(), bid_id = 50, title = "NOT", desc = "Moo", bid_end_date = later, deadline = n_days(2), status= "active")
	
	#################################################################################################################
	#################################################################################################################
	#ADDING USE TO PROJECT
	#################################################################################################################
	#################################################################################################################
	#team0
	team0.add_project_ids(project0.get_id())
	user1.add_project_ids(project0.get_id())
	user2.add_project_ids(project0.get_id())
	user3.add_project_ids(project0.get_id())
	user4.add_project_ids(project0.get_id())
	#team1
	team1.add_project_ids(project1.get_id())
	user5.add_project_ids(project1.get_id())
	user15.add_project_ids(project1.get_id())
	user20.add_project_ids(project1.get_id())
	#team2
	team2.add_project_ids(project2.get_id())
	user6.add_project_ids(project2.get_id())
	user16.add_project_ids(project2.get_id())
	#team3
	team3.add_project_ids(project3.get_id())
	user7.add_project_ids(project3.get_id())
	user17.add_project_ids(project3.get_id())
	#team4
	team4.add_project_ids(project4.get_id())
	user8.add_project_ids(project4.get_id())
	user18.add_project_ids(project4.get_id())
	#team5
	team5.add_project_ids(project5.get_id())
	user9.add_project_ids(project5.get_id())
	user19.add_project_ids(project5.get_id())
	#team6
	team6.add_project_ids(project6.get_id())
	user10.add_project_ids(project6.get_id())
	user21.add_project_ids(project6.get_id())
	#team7
	team7.add_project_ids(project7.get_id())
	user11.add_project_ids(project7.get_id())
	#team8
	team8.add_project_ids(project8.get_id())
	user12.add_project_ids(project8.get_id())
	user23.add_project_ids(project8.get_id())
	#team9
	team9.add_project_ids(project9.get_id())
	user13.add_project_ids(project9.get_id())
	#team10
	team5.add_project_ids(project10.get_id())
	user26.add_project_ids(project10.get_id())
	user27.add_project_ids(project10.get_id())
	user28.add_project_ids(project10.get_id())
	user29.add_project_ids(project10.get_id())
	user30.add_project_ids(project10.get_id())
	#other older projects
	
	
	#################################################################################################################
	#################################################################################################################
	#CREATING BID
	#################################################################################################################
	#################################################################################################################
	bid0.new_bid(0, bid_log = [[now, client0.get_id(), 10, later]])
	bid1.new_bid(1, bid_log = [[now, client1.get_id(), 10, later]])
	bid2.new_bid(2, bid_log = [[now, client2.get_id(), 10, later]])
	bid3.new_bid(3, bid_log = [[now, client3.get_id(), 10, later]])
	bid4.new_bid(4, bid_log = [[now, client4.get_id(), 10, later]])
	bid5.new_bid(5, bid_log = [[now, client5.get_id(), 10, later]])
	bid6.new_bid(6, bid_log = [[now, client6.get_id(), 10, later]])
	bid7.new_bid(7, bid_log = [[now, client7.get_id(), 10, later]])
	bid8.new_bid(8, bid_log = [[now, client8.get_id(), 10, later]])
	bid9.new_bid(9, bid_log = [[now, client9.get_id(), 10, later]])
	bid10.new_bid(10, bid_log = [[now, client10.get_id(), 100, later]])
	bid11.new_bid(11, bid_log = [[now, client11.get_id(), 100, later]])
	bid12.new_bid(12, bid_log = [[now, client12.get_id(), 100, later]])
	bid13.new_bid(13, bid_log = [[now, client13.get_id(), 100, later]])
	bid14.new_bid(14, bid_log = [[now, client14.get_id(), 100, later]])
	bid15.new_bid(15, bid_log = [[now, client15.get_id(), 100, later]])
	# bid16.new_bid(16, bid_log = [[now, client16.get_id(), 100, later]])
	# bid17.new_bid(17, bid_log = [[now, client17.get_id(), 100, later]])
	# bid18.new_bid(18, bid_log = [[now, client18.get_id(), 100, later]])
	# bid19.new_bid(19, bid_log = [[now, client19.get_id(), 100, later]])
	# bid20.new_bid(20, bid_log = [[now, client20.get_id(), 100, later]])
	# bid21.new_bid(21, bid_log = [[now, client21.get_id(), 100, later]])
	# bid22.new_bid(22, bid_log = [[now, client22.get_id(), 100, later]])
	# bid23.new_bid(23, bid_log = [[now, client23.get_id(), 100, later]])
	# bid24.new_bid(24, bid_log = [[now, client24.get_id(), 100, later]])
	# bid25.new_bid(25, bid_log = [[now, client25.get_id(), 100, later]])
	# bid26.new_bid(26, bid_log = [[now, client26.get_id(), 100, later]])
	# bid27.new_bid(27, bid_log = [[now, client27.get_id(), 100, later]])
	# bid28.new_bid(28, bid_log = [[now, client28.get_id(), 100, later]])
	# bid29.new_bid(29, bid_log = [[now, client29.get_id(), 100, later]])
	
	
	#################################################################################################################
	#################################################################################################################
	#CREATING ISSUE
	#################################################################################################################
	#################################################################################################################
	issue0.new_issue(referred_id = 1, issue_desc ="new user")
	issue1.new_issue(referred_id = 2, issue_desc ="new user", admin_review = "user denied", date_resolved = now)
	issue2.new_issue(referred_id = 2, issue_desc ="new user")
	issue3.new_issue(referred_id = 5, issue_desc ="quit request")