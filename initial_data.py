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

total_users = 65
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

issue0 = Issue()
issue1 = Issue()
issue2 = Issue()
issue3 = Issue()

def reload(reset = 0):
	super_user.load_db(0)
	reload_users()
	reload_teams()
	reload_projects()
	reload_bids()
	reload_issues()

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
def reload_issues():
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
	user12.new_user(name = "u12", username = "u12", password = 'u12', user_type = "dev", balance = 120, interests = ["security", "web", "mobile", "internet"], status = "bidding")
	user13.new_user(name = "u13", username = "u13", password = 'u13', user_type = "dev", balance = 130, interests = ["comedy", "radio", "security", "internet"], status = "bidding")
	user14.new_user(name = "u14", username = "u14", password = 'u14', user_type = "dev", balance = 140, interests = ["interent", "web", "mobile", "games"], status = "active")
	user15.new_user(name = "u15", username = "u15", password = 'u15', user_type = "dev", balance = 150, interests = ["data", "web", "games", "internet"], status = "active")
	user16.new_user(name = "u16", username = "u16", password = 'u16', user_type = "dev", balance = 110, interests = ["games", "web", "radio", "web"], status = "active")
	user17.new_user(name = "u17", username = "u17", password = 'u17', user_type = "dev", balance = 120, interests = ["security", "web", "mobile", "internet"], status = "active")
	user18.new_user(name = "u18", username = "u18", password = 'u18', user_type = "dev", balance = 130, interests = ["comedy", "radio", "security", "internet"], status = "active")
	user19.new_user(name = "u19", username = "u19", password = 'u19', user_type = "dev", balance = 140, interests = ["interent", "web", "mobile", "games"], status = "active")
	user20.new_user(name = "u20", username = "u20", password = 'u20', user_type = "dev", balance = 150, interests = ["data", "web", "games", "internet"], status = "active")
	user21.new_user(name = "u21", username = "u21", password = 'u21', user_type = "dev", balance = 110, interests = ["games", "web", "radio", "web"], status = "active")
	user22.new_user(name = "u22", username = "u22", password = 'u22', user_type = "dev", balance = 120, interests = ["security", "web", "mobile", "internet"], status = "bidding")
	user23.new_user(name = "u23", username = "u23", password = 'u23', user_type = "dev", balance = 130, interests = ["comedy", "radio", "security", "internet"], status = "bidding")
	user24.new_user(name = "u24", username = "u24", password = 'u24', user_type = "dev", balance = 140, interests = ["interent", "web", "mobile", "games"], status = "bidding")
	user25.new_user(name = "u25", username = "u25", password = 'u25', user_type = "dev", balance = 150, interests = ["data", "web", "games", "internet"], status = "bidding", warning = 2)
	
	user26.new_user(name = "u26", username = "u26", password = 'u26', user_type = "dev", balance = 110, interests = ["games", "web", "radio", "web"], status = "bidding")
	user27.new_user(name = "u27", username = "u27", password = 'u27', user_type = "dev", balance = 120, interests = ["security", "web", "mobile", "internet"], status = "bidding")
	user28.new_user(name = "u28", username = "u28", password = 'u28', user_type = "dev", balance = 130, interests = ["comedy", "radio", "security", "internet"], status = "active")
	user29.new_user(name = "u29", username = "u29", password = 'u29', user_type = "dev", balance = 140, interests = ["interent", "web", "mobile", "games"], status = "active")
	user30.new_user(name = "u30", username = "u30", password = 'u30', user_type = "dev", balance = 150, interests = ["data", "web", "games", "internet"], status = "active")
	
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

	
	##################################################################################################################
	#set images
	set_default_img()
	###################################################################################################################
	
	
	#################################################################################################################
	#################################################################################################################
	#CREATING PROJECT
	#################################################################################################################
	#################################################################################################################
	
	project0.new_project(client_id = client0.get_id(), bid_id = 0, title = "Turk System", desc = "Random group of four were able to make an awesome project", bid_end_date = now,  deadline = later, status= "complete")
	project1.new_project(client_id = client1.get_id(), bid_id = 1, title = "Hello", desc = "I have a lot of money", bid_end_date = later, deadline = n_days(2), status= "complete")
	project2.new_project(client_id = client2.get_id(), bid_id = 2, title = "World", desc = "I have a lot of money, too?", bid_end_date = later, deadline = n_days(2), status= "complete")
	project3.new_project(client_id = client3.get_id(), bid_id = 3, title = "Goodbye", desc = "I have more money than the other guy", bid_end_date = later, deadline = n_days(2), status= "complete")
	project4.new_project(client_id = client4.get_id(), bid_id = 4, title = "VR", desc = "Don't listen to any of them, I have the most", bid_end_date = later, deadline = n_days(2), status= "complete")
	project5.new_project(client_id = client5.get_id(), bid_id = 5, title = "Cow", desc = "Moo", bid_end_date = later, deadline = n_days(2), status= "incomplete")

	project6.new_project(client_id = client6.get_id(), bid_id = 6, title = "mack", desc = "I have a lot of money", bid_end_date = later, deadline = n_days(2), status= "active")
	project7.new_project(client_id = client7.get_id(), bid_id = 7, title = "EM", desc = "I have a lot of money, too?", bid_end_date = later, deadline = n_days(2), status= "active")
	project8.new_project(client_id = client8.get_id(), bid_id = 8, title = "WE", desc = "I have more money than the other guy", bid_end_date = later, deadline = n_days(2), status= "bidding")
	project9.new_project(client_id = client9.get_id(), bid_id = 9, title = "EWW", desc = "Don't listen to any of them, I have the most", bid_end_date = later, deadline = n_days(2), status= "bidding")
	project10.new_project(client_id = client10.get_id(), bid_id = 10, title = "Cow", desc = "Moo", bid_end_date = later, deadline = n_days(2), status= "bidding")
	
	project11.new_project(client_id = client11.get_id(), bid_id = 11, title = "NO", desc = "I have a lot of money", bid_end_date = later, deadline = n_days(2), status= "complete")
	project12.new_project(client_id = client12.get_id(), bid_id = 12, title = "MORE", desc = "I have a lot of money, too?", bid_end_date = later, deadline = n_days(2), status= "complete")
	project13.new_project(client_id = client13.get_id(), bid_id = 13, title = "PROJECT", desc = "I have more money than the other guy", bid_end_date = later, deadline = n_days(2), status= "complete")
	project14.new_project(client_id = client14.get_id(), bid_id = 14, title = "OR", desc = "Don't listen to any of them, I have the most", bid_end_date = later, deadline = n_days(2), status= "complete")
	project15.new_project(client_id = client15.get_id(), bid_id = 15, title = "Cow", desc = "Moo", bid_end_date = later, deadline = n_days(2), status= "complete")
	
	project16.new_project(client_id = client0.get_id(), bid_id = 16, title = "NO", desc = "I have a lot of money", bid_end_date = later, deadline = n_days(2), status= "complete")
	project17.new_project(client_id = client0.get_id(), bid_id = 17, title = "MORE", desc = "I have a lot of money, too?",  bid_end_date = later, deadline = n_days(2), status= "complete")
	project18.new_project(client_id = client0.get_id(), bid_id = 18, title = "PROJECT", desc = "I have more money than the other guy",  bid_end_date = later, deadline = n_days(2), status= "complete")
	project19.new_project(client_id = client0.get_id(), bid_id = 19, title = "OR", desc = "Don't listen to any of them, I have the most",  bid_end_date = later, deadline = n_days(2), status= "complete")
	project20.new_project(client_id = client1.get_id(), bid_id = 20, title = "NOT", desc = "Moo", bid_end_date = later, deadline = n_days(2), status= "complete")

	project21.new_project(client_id = client1.get_id(), bid_id = 21, title = "NO", desc = "I have a lot of money", bid_end_date = later, deadline = n_days(2), status= "complete")
	project22.new_project(client_id = client2.get_id(), bid_id = 22, title = "MORE", desc = "I have a lot of money, too?", bid_end_date = later, deadline = n_days(2), status= "complete")
	project23.new_project(client_id = client3.get_id(), bid_id = 23, title = "PROJECT", desc = "I have more money than the other guy", bid_end_date = later, deadline = n_days(2), status= "complete")
	project24.new_project(client_id = client4.get_id(), bid_id = 24, title = "OR", desc = "Don't listen to any of them, I have the most", bid_end_date = later, deadline = n_days(2), status= "complete")
	project25.new_project(client_id = client5.get_id(), bid_id = 25, title = "NOT", desc = "Moo", bid_end_date = later, deadline = n_days(2), status= "complete")
	
	project26.new_project(client_id = client10.get_id(), bid_id = 26, title = "NO", desc = "I have a lot of money", bid_end_date = later, deadline = n_days(2), status= "complete")
	project27.new_project(client_id = client10.get_id(), bid_id = 27, title = "MORE", desc = "I have a lot of money, too?", bid_end_date = later, deadline = n_days(2), status= "complete")
	project28.new_project(client_id = client10.get_id(), bid_id = 28, title = "PROJECT", desc = "I have more money than the other guy", bid_end_date = later, deadline = n_days(2), status= "complete")
	project29.new_project(client_id = client10.get_id(), bid_id = 29, title = "OR", desc = "Don't listen to any of them, I have the most", bid_end_date = later, deadline = n_days(2), status= "complete")
	project30.new_project(client_id = client10.get_id(), bid_id = 30, title = "NOT", desc = "Moo", bid_end_date = later, deadline = n_days(2), status= "complete")
	
	project31.new_project(client_id = client10.get_id(), bid_id = 31, title = "NO", desc = "I have a lot of money", bid_end_date = later, deadline = n_days(2), status= "bidding")
	project32.new_project(client_id = client10.get_id(), bid_id = 32, title = "MORE", desc = "I have a lot of money, too?", bid_end_date = later, deadline = n_days(2), status= "bidding")
	project33.new_project(client_id = client3.get_id(), bid_id = 33, title = "PROJECT", desc = "I have more money than the other guy", bid_end_date = later, deadline = n_days(2), status= "complete")
	project34.new_project(client_id = client4.get_id(), bid_id = 34, title = "OR", desc = "Don't listen to any of them, I have the most", bid_end_date = later, deadline = n_days(2), status= "complete")
	project35.new_project(client_id = client5.get_id(), bid_id = 35, title = "NOT", desc = "Moo", bid_end_date = later, deadline = n_days(2), status= "complete")
	
	project36.new_project(client_id = client11.get_id(), bid_id = 36, title = "NO", desc = "I have a lot of money", bid_end_date = later, deadline = n_days(2), status= "complete")
	project37.new_project(client_id = client11.get_id(), bid_id = 37, title = "MORE", desc = "I have a lot of money, too?", bid_end_date = later, deadline = n_days(2), status= "complete")
	project38.new_project(client_id = client11.get_id(), bid_id = 38, title = "PROJECT", desc = "I have more money than the other guy", bid_end_date = later, deadline = n_days(2), status= "complete")
	project39.new_project(client_id = client11.get_id(), bid_id = 39, title = "OR", desc = "Don't listen to any of them, I have the most", bid_end_date = later, deadline = n_days(2), status= "complete")
	project40.new_project(client_id = client11.get_id(), bid_id = 40, title = "NOT", desc = "Moo", bid_end_date = later, deadline = n_days(2), status= "complete")
	
	project41.new_project(client_id = client11.get_id(), bid_id = 41, title = "NO", desc = "I have a lot of money", bid_end_date = later, deadline = n_days(2), status= "incomplete")
	project42.new_project(client_id = client2.get_id(), bid_id = 42, title = "MORE", desc = "I have a lot of money, too?", bid_end_date = later, deadline = n_days(2), status= "incomplete")
	project43.new_project(client_id = client1.get_id(), bid_id = 43, title = "PROJECT", desc = "I have more money than the other guy", bid_end_date = later, deadline = n_days(2), status= "incomplete")
	project44.new_project(client_id = client1.get_id(), bid_id = 44, title = "OR", desc = "Don't listen to any of them, I have the most", bid_end_date = later, deadline = n_days(2), status= "incomplete")
	project45.new_project(client_id = client5.get_id(), bid_id = 45, title = "NOT", desc = "Moo", bid_end_date = later, deadline = n_days(2), status= "incomplete")
	
	project46.new_project(client_id = client11.get_id(), bid_id = 46, title = "NO", desc = "I have a lot of money", bid_end_date = later, deadline = n_days(2), status= "no bid")
	project47.new_project(client_id = client12.get_id(), bid_id = 47, title = "MORE", desc = "I have a lot of money, too?", bid_end_date = later, deadline = n_days(2), status= "no bid")
	project48.new_project(client_id = client13.get_id(), bid_id = 48, title = "PROJECT", desc = "I have more money than the other guy", bid_end_date = later, deadline = n_days(2), status= "no bid")
	project49.new_project(client_id = client14.get_id(), bid_id = 49, title = "OR", desc = "Don't listen to any of them, I have the most", bid_end_date = later, deadline = n_days(2), status= "no bid")
	project50.new_project(client_id = client15.get_id(), bid_id = 50, title = "NOT", desc = "Moo", bid_end_date = later, deadline = n_days(2), status= "no bid")
	
	#################################################################################################################
	#################################################################################################################
	#ADDING USER/TEAMS TO PROJECT
	#################################################################################################################
	#################################################################################################################
	add_project_to_team(0,[0])
	add_project_to_team(1,[1])
	add_project_to_team(2,[2])
	add_project_to_team(3,[3])
	add_project_to_team(4,[4])
	add_project_to_team(5,[5])
	add_project_to_team(6,[6])
	add_project_to_team(7,[7])
	add_project_to_team(8,[8])
	add_project_to_team(9,[9])
	add_project_to_team(10,[10])
	reload_teams()
	reload_users()
	#################################################################################################################
	#################################################################################################################
	#ADDING CLIENT PROJECT
	#################################################################################################################
	#################################################################################################################
	client0.set_project_ids([16,17,18,19,0])
	client1.set_project_ids([20,21,43,44,1])
	client2.set_project_ids([22,42,2])
	client3.set_project_ids([23,33,3])
	client4.set_project_ids([24,34,4])
	client5.set_project_ids([25,35,45,5])
	client6.set_project_ids([6])
	client7.set_project_ids([7])
	client8.set_project_ids([8])
	client9.set_project_ids([9])
	client10.set_project_ids([26,27,28,29,30,31,32,10]) #high rating
	client11.set_project_ids([46,36,37,38,39,40,41,11]) #low rating
	client12.set_project_ids([47,12])
	client13.set_project_ids([48,13])
	client14.set_project_ids([49,14])
	client15.set_project_ids([50,15])
	
	#################################################################################################################
	#################################################################################################################
	#CREATING BID
	#################################################################################################################
	#################################################################################################################
	#generic method: load from user and project into bid
	generate_bids()
	reload_bids()
	
	#################################################################################################################
	#################################################################################################################
	#CREATING ISSUE
	#################################################################################################################
	#################################################################################################################
	issue0.new_issue(referred_id = 1, issue_desc ="new user")
	issue1.new_issue(referred_id = 2, issue_desc ="new user", admin_review = "user denied", date_resolved = now)
	issue2.new_issue(referred_id = 2, issue_desc ="new user")
	issue3.new_issue(referred_id = 5, issue_desc ="quit request")

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
					bid_log = [[]]
					chosen_index = 'Nan'
					project = jsonIO.get_row("project_db", id)
					bid_log = [[ez.get_now(), user["id"], 100, project["deadline"]]]
					jsonIO.add_row("bid_db", {"id":id, "chosen_index": chosen_index, "bid_log":bid_log, "client_review":client_review})
			elif user["user_type"] == "dev" and (project["status"] == "complete" or project["status"] == "incomplete"):
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
def set_default_img():
	users = jsonIO.read_rows("user_db")
	teams = jsonIO.read_rows("team_db")
	for user in users:
		if not user["pic"]:
			user["pic"] = "default_user.png"
			jsonIO.set_row("user_db", user)
	for team in teams:
		if not team["pic"]:
			team["pic"] = "default_team.png"
			jsonIO.set_row("team_db", team)