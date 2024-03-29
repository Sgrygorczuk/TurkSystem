from User import *
from Project import *
from Team import *
from Bid import *
from Issue import *
from jsonIO import *
import os
import shutil
import inspect
from datetime import datetime
from datetime import timedelta


now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
dt_now = datetime.strptime(now, "%Y-%m-%d %H:%M:%S")
img_folder = os.getcwd()+"/images"
prj_folder = os.getcwd()+"/projects"

##########################################################################
##########################################################################
########                        NOTES:                              ########
####                                                                  ####
####    Use this functions to ensure that the creation of your           ####
####  classes does not conflict with other classes, all the other     ####
####    classes are updated if they share the same key.                  ####
####                                                                  ####
####    This will also makes sure that there no duplicates and           ####
####     blacklisted user/project/bid... so forth are created.          ####
####                                                                  ####
####        Finally this class will aid in other calculations.          ####
########                                                          ########
##########################################################################
##########################################################################

###########################DIRECTORY OF FUNCTIONS#########################
#post: prints all available commands
def get_commands():
    print ('''-------------------------------------------------------------------------------------
Direct Database Access
    get_value(obj, key, id = 'Nan'): gets value
    get_all_db(obj): gets all from db
    get_row(obj, key): gets an entire row
    get_col(obj, key): returns the whole column of an attribute
    print_table(m): prints the table given a dictionary or a list of it
-------------------------------------------------------------------------------------
SU
    user_report(user, id = 'Nan'): returns status of the user:
        user_type, status, warning, and balance
    verify(username, password = ""): returns [case number, user, message]
    verify_blacklisted(user_id): reset user's status and warnings and returns true if it was done so
    quit_request(issue_id): user is removed and will call quit_team
    quit_team(user_id): doesnt matter if admin or user, but will kick devs if he's last admin
        and update their team_ids
-------------------------------------------------------------------------------------
State Changes
    fsm_project(project_id): changes state and returns 1 or 0 depending on if it was done
-------------------------------------------------------------------------------------
Class Creation
    user_exists(username): returns 1 if user exist else returns 0
    register_user(name, username, password, user_type, deposit):
        places new temp_user in SU tasks
    create_team(admin_ids, dev_ids, name, pic, desc):
        will also create an issue instance
    create_project(client_id, title, desc, deadline):
        will return and make a new project
    create_bid(project_id, end_date, initial_bid, start_date = now): returns a new bid
    set_pic(src, new_img, user_id, user_type): will make/ upadate user's pic
    get_pic(user_id, user_type): either error message or returns path of image
-------------------------------------------------------------------------------------
Teams
    disactivate_empty_team(team_id): will disactivate team if there is no admin and return true
        will also kick developers out and update their team_id to 'Nan'
        else it will return false
    kick(team_dict, user_id):  will remove user from team and update both user and team db
    request_join(team_dict, user_id):  will add user to the team and update team's dev_ids
    accept_team(team_dict, user_id): user's team_id will be updated and team's request list will shrink
    reject_team(team_dict, user_id): team's request list will shrink
    promote(team_dict, user_id): user becomes admin in team
    demote(team_dict, user_id): admin becomes user
        will either return available files if file not stated
-------------------------------------------------------------------------------------
Bid and Project Process
    bid_timeout(bid_id): returns if the bid was over with 1 otherwise 0
    make_bid(user_id, bid_id, amount, suggested_time):     wil append to the bid_log 
        when project status is "bidding"
        chosen_index != 'Nan', then call end_bid
    choose_bid(bid_id, dev_id, reason = "lowest bidder"): modifies bid_db and changes states
    get_bid_log(bid_id, only_id = False):  returns the entire bid_log
    get_chosen_bid(project_id, only_id = False): gets bid_log of winner bidder
    end_bid(bid_id): if not chosen_index but has bids in bid log it will update it
        set project to "active" if bid on else "no bid"
        set user status to "active" who were in bid
        transfer the initial funds 
    transfer_fund_request(from_user_id, to_user_id, amount):
        will make an issue for user to resolve in order to transfer funds
    transfer_initial_bid_funds(from_user_id, to_user_id, amount): it will modify both 
         balances and create task. Check below for more details.
         #resolves payment issues
    submit(src, new_project, project_id): will make/ update project
        if exist, it will no longer allow submission
    get_submission(dst, project_id): either error message or returns project and set project to "Complete"
    make_rating(user_id, rating, comment = ""): if rating <= 2 dev explain himself
        if rating <= 3 client explain himself
        calls set_warning to take care of the warnings
    finalize_funds(project_id): transfers the remaining funds after the 
        completion/ incompletion of project
    set_warning(user_dict, prj_dict, rating = 'Nan'): user's warning will increase depending on inputs
        check user's out_ratings and will increase warnings too
-------------------------------------------------------------------------------------
Engines
    search_matches(obj, input_name): Uses the search engine to find name
    recommendation(user_dict): will suggest client a dev, and for dev a project
-------------------------------------------------------------------------------------
Metrics
    get_grade(user): returns the average rating of dev, team, or client
    get_total_commision(obj,dic=false): returns the money made 
        by all projects from user/ team
    bayesian_avg(user, m, c): returns the bayesian average of the user's grade(rating)
    avg_out_rating(user_dict): returns average out rating from a user
    total_user(user_type): returns the total number of rows if user_type is one of 'dev', 'client', or 'team'
    total_completed_projects(): returns the total number of project that has been completed
-------------------------------------------------------------------------------------
Helper functions
    find_row(db, key, value): returns row of given key value
    val_print(values): support method for print_table metho
    get_now(): returns current date time in Y-m-d H:M:S form and updates it
    string_to_datetime(time): returns datetime form
    datetime_to_string(dt_time): returns string form
    get_n_days_later(time, n): return string with added days 
    transfer_funds(from_user, to_user, amount): it will modify both balances
    is_in_active_project(user): check if user is active
    is_admin(dic): returns true if user is team admin
    set_file(src, new_file = None, dst = None, old_file = None, obj_id = None, obj_type = None):
        will either return available files if file not stated
        else return success/failure message
    grade_log(user): return a list of user's project grades
    get_m_c(user_type): return [m, c] for bayesian_avg(user, m, c)
''')

#############################################################################

#/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\
#/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\
#/\/\/\/\DIRECT DATABASE ACCESS/\/\/\/\DIRECT DATABASE ACCESS/\/\/\/\DIRECT DATABASE ACCESS/\/\/\/\/\/\/\/\/\
#/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\
#/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\

#pre: given an instance of a class, key, and id (unless id is initialized in object)
#post: get attribute from a class 
#       else return 'Nan'
#ex: get_value(User(), "name", 0)
#     returns: System Admit
def get_value(obj, key, id = 'Nan'):
    if id == 'Nan':
        id = obj.get_id()
        if not key:
            print("Key not stated")
            return 'Nan'
        elif id == 'Nan':
            print("ID not initialized")
            return 'Nan'
        else:
            #can pull from user
            method = 'get_'+key
            try:
                value = getattr(obj, method)()
                return value
            except:
                print("No such key exist")
                return 'Nan'
    #otherwise just search db
    value = jsonIO.get_value(obj.db, id, key)
    if value == None:
        print("Either the id or key does not exist")
    return value
#post: returns all items in a database
def get_all_db(obj):
    return jsonIO.read_rows(obj.db)

#pre: id must exist    (must include id unless id is initialized in object)
#post: returns all attribute of class
#      else return {}
def get_row(obj, id = 'Nan'):
    if id == 'Nan':
        id = obj.get_id()
        if id == 'Nan':
            print("ID not initialized")
            return {}
        else:
            #can pull from user
            return obj.get_all()
    elif isinstance(id, str):
        print("ID does not exits")
        return {}
    #otherwise just search db
    return jsonIO.get_row(obj.db, id)
    
#pre: needs valid instance of class and its key
#post: returns the whole column of an attribute
def get_col(obj, key):
    array = []
    #don't include SU (id = 0)
    n = 0
    if obj.__class__ == User:
        n += 1
    for id in range(n, jsonIO.get_last_id(obj.db)+1):
        attrib = jsonIO.get_value(obj.db, id, key)
        #if it exist
        if attrib!= None:
            array.append({"id": id, key: attrib})
    return array
####***************************might break at bid_log call*************    
#pre: any DB array    
#post: print table
def print_table(m):
    if not m:
        return 0
    if type(m) == list:
        keys = list(m[0].keys())
    else:
        keys = list(m.keys())
    values = []
    indents = "{:<15}"
    for i in range(0, len(keys)-1):
        indents += " {:<15}"
    print (indents.format(*keys))
    #is it a list of dictionary?
    if type(m) == list:
        for item in m:
            values = item.values()
            values = list(values)
            #from helper function (can be found all the way below)
            val_print(values)
    else: #it's a dictionary
        val_print(list(m.values()))
    return 1
    

#/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\
#/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\
#/\/\/\/\SU/\/\/\/\SU/\/\/\/\SU/\/\/\/\SU/\/\/\/\SU/\/\/\/\SU/\/\/\/\SU/\/\/\/\SU/\/\/\/\SU/\/\/\/\SU/\/\/\/\
#/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\
#/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\
               
#pre: needs a valid user of type user and could also do it from an id
#post: returns dictionary of status of the user: user_type, status, warning, and balance
#else returns {}
def user_report(user, id = 'Nan'):
    if user.__class__ != User:
        print("User is not of type User")
        return {}
    if id == 'Nan':
        id = user.get_id()
        if id == 'Nan':
            print("ID not initialized")
            return {}
        else:
            #can pull from user
            return {"user_type":user.get_user_type(), "status":user.get_status(),
            "warning":user.get_warning(), "balance":user.get_balance()}
    obj = jsonIO.get_row(user.db, id)
    if obj == None:
        return {}
    return {"user_type":obj["user_type"], "status":obj["status"],
    "warning":obj["warning"], "balance":obj["balance"]}

#authenticate user
#cond: will autheticate user: username or username and password for logging in
# and return [case number, user, message]
#pre: none
#post: will return [case number, user, message] along with a print
def verify(username, password = None):
    case = 1
    user = {}
    message = ""
    #empty inputs
    if not username:
        message = "Username field is empty"
    elif password == "":
        case = 2
        message = "Password field is empty"
    else:
        #check without password
        #find_row is a helper function (can be found all the way below)
        user = find_row("user_db", "username", username)
        if not user:
            case = 3
            message = "Username not found"
        elif user["status"] == "blacklisted":
            if(verify_blacklisted(user["id"])):
                case = 12
                message = "Welcome back, you are no longer blacklisted"
            else:
                case = 4
                message = "User found but blacklisted"
        elif user["status"] == "inactive":
            case = 5
            message = "User found but deactivated"
        elif password == None:
            if user["warning"] >= 2:
                if user["status"] != "blacklisted":
                    case = 6
                    message = "User found, but has 2 warnings and not yet blacklisted"
                #blacklisted already checked
            elif user["status"] == "rejected":
                case = 7
                message = "Temporary user found, but was rejected and password"
            else:
                case = 8
                message = "User found and has no warnings, password not yet verified"
        #check with password
        elif user["password"] != password:
            case = 9
            message = "Your password does not match"
        elif user["warning"] >= 2:
            if user["status"] != "blacklisted":
                case = 10
                message = "Login successful, but has 2 warnings and not yet blacklisted"
        elif user["status"] == "rejected":
                case = 11
                message = "Login successful, but temporary user was rejected"
        else: #user["password"] matches
            case = 0
            message = "Login successful"
    print(message)
    return [case, user, message]
    
#cond:    verify when he was last blacklisted in task and make him active again
#post:    reset user's status and warnings and returns true if it was done so
def verify_blacklisted(user_id):
    #find all taks with use's id in issue's referred_id
    issues = jsonIO.get_rows("issue_db", "referred_id", user_id)
    if not issues:
        print("User not found")  
    #see if the issue is blacklisted and compare time to now
    for issue in issues:
        date = issue["date_resolved"]
        if date:
            print(issue)
            one_year = string_to_datetime(date) + timedelta(days=365)
            if issue["issue_desc"] == "blacklisted" and one_year <= get_now(True):
                #if it has been 1 year since blacklisting set to active and warnings to o
                jsonIO.set_value("user_db", user_id, "status", "active")
                jsonIO.set_value("user_db", user_id, "warning", 0)
                jsonIO.del_row("issue_db", issue["id"])
                return 1
    return 0
    
#cond:
#pre:#check if balance == 0
    #check if warnings == 2, then
    #check if in the middle of a project
#post:
    #if not in middle of project
        #remove from team (admin/dev_ids)
        #remove from project (client)
    #modify user status
    #modify task (approved/denied)
def quit_request(issue_id):
    issue = jsonIO.get_row("issue_db", issue_id)
    if not issue:
        print ("The issue you are grabbing from does not exist")
        return ""
    user_id = issue["referred_id"]
    user = User()
    user.load_db(user_id)
    message = ""
    #check user_id exist
    if user.get_id() == 'Nan':
        print ("The user you are grabbing from does not exist")
        return ""
    #check if balance == 0
    if user.get_balance() != 0:
        message = "The user has unresolved balance (balance is not 0)"
    #check if warnings == 2
    elif user.get_warning == 2:
        message = "The user is or will be blacklisted"
    #check if in the middle of a project
    else:
        if user.get_project_ids():
            project = jsonIO.get_row("project_db", user.get_project_ids()[-1])
            if project["status"] == "active":
                message = "The user is in the middle of a project"
            #check if client is managing a bid
            elif user.get_user_type() == "client":
                if jsonIO.get_value("bid_db", project["id"], "status") == "active":
                    message = "The client is in the middle of a bid"
            #remove from team (admin/dev_ids)
            elif user.get_team_id():
                quit_team(user_id)
    if not message:
        message = "Done"
    #modify user status
    jsonIO.set_value("user_db", user_id, "status", "inactive") 
    #MUST modify the issue
    issue["admin_review"] = message
    issue["date_resolved"] = now
    issue["resolved"] = True
    jsonIO.set_row("issue_db", issue)
    return message
    
#cond: will delete user but wont update the issue_db
#pre: user_id must exist
#      must not be in the middle of a project
#     must belong to a team
#post: will quit the team and will kick out devs if 
#      this admin was the last one
def quit_team(user_id):
    user = jsonIO.get_row("user_db", user_id)
    message = ""
    if not user:
        print ("User does not exist")
        return ""
    #check if in the middle of a project
    if user["project_ids"]:
        if jsonIO.get_value("project_db", user["project_ids"][-1], "status") == "active":
            message = "The user is in the middle of a project"
            return message
    #check if user is in team
    team = jsonIO.get_row("team_db", user["team_id"])
    if not team:
        print ("User does not belong to a team")
        return ""
    #if it is an admit, remove him
    for admin in team["admin_ids"]:
        if admin == user_id:
            jsonIO.set_value("team_db", team["id"], "admin_ids",
                            team["admin_ids"].remove(user_id))
    #support function see bottom
    #delete if he was the last admin and kick devs out
    if not disactivate_empty_team(team["id"]):
        #team not yet erased
        for dev in team["dev_ids"]:
            if dev == user_id:
                jsonIO.set_value("team_db", team["id"], "dev_ids", team["dev_ids"].remove(user_id))
    #modify user team_id to 'Nan'
    jsonIO.set_value("user_db", user_id, "team_id", 'Nan')
    if message == "":
        message = "Done"
    return message

    
#/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\
#/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\
#/\/\/\/\STATE CHANGES/\/\/\/\STATE CHANGES/\/\/\/\STATE CHANGES/\/\/\/\STATE CHANGES/\/\/\/\STATE CHANGES/\/
#/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\
#/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\

#post: changes state based on class types
def fsm_project(project_id):
    project = jsonIO.get_row("project_db", project_id)
    if not project:
        print("project does not exist")
        return 0
    if project["status"] == "complete" or project["status"] == "incomplete" or project["status"] == "no bid":
        print("project is in final state")
        return 0
    if project["status"] == "bidding":
        #check if bid is over
        if bid_timeout(project_id) or jsonIO.get("bid_db", project_id, "chosen_index") != 'Nan':
            if len(get_bid_log(project_id)) <= 1:
                jsonIO.set_value("project_db", project_id, "status", "no bid")
            else:
                jsonIO.set_value("project_db", project_id, "status", "active")
            end_bid(project_id)
        else:
            return 0
    elif project["status"] == "active":
        #check if the project is over
        if project["submission"]:
            jsonIO.set_value("project_db", project_id, "status", "submitted")
            finalize_funds(project_id)
        elif string_to_datetime(project["deadline"]) <= get_now(True):
            jsonIO.set_value("project_db", project_id, "status", "incomplete")
            finalize_funds(project_id)
        else:
            return 0
    # this should be covered by when customer gets project
    elif project["state"] == "submitted":
        print("The client must pick up his project")
    return 1    
    
    
#/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\
#/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\
#/\/\/\/\CLASS CREATION/\/\/\/\CLASS CREATION/\/\/\/\CLASS CREATION/\/\/\/\CLASS CREATION/\/\/\/\/\/\/\/\/\/\
#/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\
#/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\

#pre: none
#post: returns 1 if user exist else returns 0
def user_exists(username):
    return 1 if find_row("user_db", "username", username) else 0

#pre: takes required attribute of new user, username should not exist
#post: places new temp_user in SU issues or return message
def register_user(name, username, password, user_type, deposit):
    #empty inputs
    if username == "":
        return "Username field is empty"
    elif user_exists(username):
        return "That username already exists"
    elif password == "":
        return "Password field is empty"
    elif name == "":
        return "Name field is empty"
    #check values
    elif len(password) > 64:
        return "That password is too long"
    elif len(name) > 80:
        return "That name is too long"
    elif not name.isalpha():
        return "That name has numbers or special charaters"
    elif user_type != "client" and user_type != "dev" and user_type!= "SU":
        return "That is not a valid user type"
    #see if deposit is a positive integer
    else:
        try:
            val = float(deposit)
            #check deposit amount
            if val <= 0:
                return "The deposit is too low"
            #check deposit syntax
            val = str(deposit)
            if '.' in val:
                if len(val.rsplit('.')[-1]) > 2:
                    return "That is not a valid deposit"
            #create User and Ussue
            print ("User made")
            user = User(name = name, username = username, password = password, user_type = user_type, balance = float(deposit), status = "temp")
            Issue(user.get_id(),"new user")
            print(read_rows("issue_db"))
            return user.get_all()
        #this was when deposit was not right syntax
        except ValueError:
            return "That is not a valid deposit"

#post:    creates a new team
def create_team(admin_id, name, desc):
    #check if name field is filled
    if not name:
        return "must give a team name"
    #check if desc is filled
    if not desc:
        return "must give a team description"
    #create a new team and update the user's team_id 
    team = Team(admin_ids = [admin_id], dev_ids = [admin_id], name = name, desc = desc)
    user = jsonIO.get_row("user_db", admin_id)
    user['team_id'] = team.get_id()
    jsonIO.set_row("user_db",user)
    return team.get_all()

#pre: needs all the entries filled and an existing client id
#post: will return and make a new project, and add project_id to client
def create_project(client_id, title, desc):
    #check empty
    if title == "":
        return "Title field is empty"
    if desc == "":
        return "Description field is empty"
    if not find_row("user_db","id", client_id):
        print("User not found")
        return 'Nan'
    
    end_date = datetime.now() + timedelta(days=7)
    end_date = end_date.strftime("%Y-%m-%d %H:%M:%S")

    project = Project(client_id, title, desc, bid_end_date = end_date, status = "bidding")
    client = User()
    client.load_db(client_id)
    client.add_project_ids(project.get_id())
    return project.get_all()

#pre: must have client and project id for input and bid_id must be new
#    end>start date and client's balance >= bid
#post: returns a new bid
#      will also create an issue instance
def create_bid(bidder_id, project_id, end_date, initial_bid, start_date =  datetime.now().strftime("%Y-%m-%d %H:%M:%S")):
    project = jsonIO.get_row("project_db", project_id)
    user = jsonIO.get_row("user_db", bidder_id)
    bid = jsonIO.get_row("bid_db", project_id)
    s_date = string_to_datetime(start_date)
    e_date = string_to_datetime(end_date)
    #check empty
    if start_date == "":
        del_row("project_db", project_id)
        print("Start date field is empty")
        return 'Nan'
    elif end_date == "":
        del_row("project_db", project_id)
        return 'Nan'
    #check amount is positive
    elif initial_bid < 0:
        return 'Nan'
    #check id consistencies
    elif not project:
        print("Project not found")
        del_row("project_db", project_id)
        return 'Nan'
    elif bid:
        print("Bid already exists")
        log = get_bid_log(bid['id'])
        log.append([start_date, user["id"], initial_bid, end_date])
        print(log)
        return log
    elif not user:
        print("User not found")
        del_row("project_db", project_id)
        return 'Nan'
    #make sure client has money
    elif float(user["balance"]) < initial_bid:
        print("User does not have enough funds")
        del_row("project_db", project_id)
        return 'Nan'
    #make sure end time > start time
    #uses helper_function
    #make sure string is a valid date
    #uses helper_function
    elif not s_date or not e_date:
        del_row("project_db", project_id)
        return 'Nan'
    elif s_date >= e_date:
        del_row("project_db", project_id)
        print("The end date must be after the start date")
        return 'Nan'
    else:
        bid = Bid(project_id)
        bid.add_bid_log(start_date, user["id"], initial_bid, end_date)
        add_row("bid_db", bid.get_all())
        #create an issue for the SU
        issue = Issue(referred_id = user["id"], issue_desc = "payment")
        return bid.get_all()
        
        
#pre:     src is destination of the user's file 
#        user_type is either team or user
#        new_img is the name of the file
#post:    will make/ upadate user's pic
def set_pic(src, new_img, user_id, user_type):
    if user_type == "team":
        pic = jsonIO.get_value("team_db", user_id, "pic")
    else:
        pic = jsonIO.get_value("user_db", user_id, "pic")
    #uses helper function
    return set_file(src, new_img, img_folder, pic, user_id, user_type)

#pre:    image must exist
#post:    either error message or returns path of image
def get_pic(user_id, user_type):    
    if user_type == "team":
        pic = img_folder+"/"+jsonIO.get_value("team_db", user_id, "pic")
    else:
        pic = img_folder+"/"+jsonIO.get_value("user_db", user_id, "pic")
    return os.path.join(img_folder, pic)

    
#/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\
#/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\
#/\/\/\/\TEAMS/\/\/\/\TEAMS/\/\/\/\TEAMS/\/\/\/\TEAMS/\/\/\/\TEAMS/\/\/\/\TEAMS/\/\/\/\TEAMS/\/\/\/\/\/\/\/\/
#/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\
#/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\

#cond: will disactivate if there is no admin and return a truth
#pre: the team_id is valid
#post: will disactivate team if there is no admin and return true
#      will also kick developers out and update their team_id to 'Nan'
#      else it will return false
def disactivate_empty_team(team_id):
    team = jsonIO.get_row("team_db", team_id)
    if not team:
        print ("Team does not exist")
        return 0
    if team["admin_ids"]:
        return 0
    if team["dev_ids"]:
        for dev_id in team["dev_ids"]:
            jsonIO.set_value("user_db", dev_id, "team_id", 'Nan')
    jsonIO.set_value("team_db", team_id, "status", "inactive")
    return 1

#pre: team and user must exit
#post: will remove user from team and update both user and team db
def kick(team_dict, user_id):
    team_dict["dev_ids"].remove(user_id)
    user = jsonIO.get_row("user_db", user_id)
    if user:
        if is_admin(user):
            team_dict["admin_ids"].remove(user_id)
        user["team_id"] = "Nan"
        set_row("user_db", user)
        set_row("team_db", team_dict)
        return 1
    print("User does not exist")
    return 0

#pre:  team and user must exist
#post: will add user to the team and update team's dev_ids
def request_join(team_dict, user_id):  
    team_dict["join_request_ids"].append(user_id)
    user = jsonIO.get_row("user_db", user_id)
    if user:
        user["team_id"] = team_dict["id"]
        print(user["team_id"])
        set_row("user_db", user)
        set_row("team_db", team_dict)
        return user
    print("User does not exist")
    return 'Nan'

#cond: accepts the user from the join request list
#pre: team and user exists
#post: user's team_id will be updated and team's request list will shrink
def accept_team(team_dict, user_id):
    team_dict["dev_ids"].append(user_id)
    team_dict["join_request_ids"].remove(user_id)
    user = jsonIO.get_row("user_db", user_id)
    user["team_id"] = team_dict["id"]
    set_row("user_db", user)
    set_row("team_db", team_dict)

#cond: rejects the user from the join request list
#pre: team and user exists
#post: team's request list will shrink
def reject_team(team_dict, user_id):
    team_dict["join_request_ids"].remove(user_id)
    user = jsonIO.get_row("user_db", user_id)
    user["team_id"] = "Nan"
    set_row("user_db", user)
    set_row("team_db", team_dict)

#post: user becomes admin in team
def promote(team_dict, user_id):
   team_dict["admin_ids"].append(user_id)
   set_row("team_db", team_dict)

#post: admin becomes user
def demote(team_dict, user_id):
   team_dict["admin_ids"].remove(user_id)
   set_row("team_db", team_dict)
 

#/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\
#/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\
#/\/\/\/\BID AND PROJECT PROCESS/\/\/\/\BID AND PROJECT PROCESS/\/\/\/\BID AND PROJECT PROCESS/\/\/\/\/\/\/\/\
#/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\
#/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\

def fsm_project(project_id):
    project = jsonIO.get_row("project_db", project_id)
    if not project:
        print("project does not exist")
        return 0
    if project["status"] == "complete" or project["status"] == "incomplete" or project["status"] == "no bid":
        print("project is in final state")
        return 0
    if project["status"] == "bidding":
        #check if bid is over
        if bid_timeout(project_id):
            if len(get_bid_log(project_id)) <= 1:
                jsonIO.set_value("project_db", project_id, "status", "no bid")
            else:
                jsonIO.set_value("project_db", project_id, "status", "active")
            end_bid(project_id)
        else:
            return 0
    elif project["status"] == "active":
        #check if the project is over
        if string_to_datetime(project["deadline"]) <= get_now(True):
            if project["submission"]:
                jsonIO.set_value("project_db", project_id, "status", "submitted")
            else:
                jsonIO.set_value("project_db", project_id, "status", "incomplete")
            finalize_funds(project_id)
        else:
            return 0
    # this should be covered by when customer gets project
    #elif project["state"] == "submitted":
    return 1
#post:    returns the bidder's index from last to first
def get_bidder_index(bid_id, bid_log, dev_id):
    for j in range(len(bid_log)-1, 0, -1):
        if bid_log[j][1] == dev_id:
            return j
    return 'Nan'

#post: returns if the bid was over with 1 otherwise 0
def bid_timeout(bid_id):
    project = jsonIO.get_row("project_db", bid_id)
    if not project:
        print("No such id exist")
        return 0
    #project must be in a bidding state
    if project["status"] != "bidding":
        return 0
    #calls helper function
    if string_to_datetime(project["bid_end_date"]) <= get_now(True):
        return 1
    else:
        return 0

#pre: amount < current_bid
#     dt_later >= dt_now
#post:will append to the bid_log when project status is "bidding"
#     chosen_index != 'Nan', then call end_bid
def make_bid(user_id, bid_id, amount, suggested_time):
    #calls helper function
    #if not bid_timeout
    if not bid_timeout(bid_id):
        bid = jsonIO.get_row("bid_db", bid_id)
        #check if amount < current_bid
        if amount >= bid["bid_log"][-1][2]:
            return "The bidder must give a valid amount"
        #check suggested time <= client_suggested_time
        if suggested_time >  bid["bid_log"][0][3]:
            return "The suggested time must be less than the client's"
        #check if user is in a team
        user = jsonIO.get_row("user_db", user_id)
        if user["team_id"] != 'Nan':
        #check if user is an admin
            team_id = user["team_id"]
            if team_id:
                admin_ids = jsonIO.get_value("team_db", team_id, "admin_ids")
                if admin_ids:
                    if user_id not in admin_ids:
                        return "Only your admin can bid"
        #check if the user is only bidding here or not all
        if get_bidder_index(bid_id, bid["bid_log"], user_id) == 'Nan':
            #if not bidding here check if he is active elsewhere
            status = user["status"]
            if status != "active":
                return "The bidder is currently doing another project"
            else:
                jsonIO.set_value("user_db", user_id, "status", "bidding")
        #make a bid
        bid["bid_log"].append([get_now(), user_id, amount, suggested_time])
        jsonIO.set_row("bid_db", bid)
        #return done message
        return "Done"
    #else call calls end_bid
    return "Bid was closed"        
    
#pre:    dev_id must exist in bid_log and must have reason if not lowest
#post:    modifies bid_db, project and changes project state to active
def choose_bid(bid_id, dev_id, Index, reason = ""):
    bid = jsonIO.get_row("bid_db", bid_id)
    project = get_row(Project(), bid_id)
    if not bid:
        print("Bid does not exist")
        return ""
    #if the bidder chosen was the lowest, it returns the default reason
    print(bid["bid_log"][-1][1])
    if dev_id == bid["bid_log"][-1][1]:
        bid["chosen_index"] = Index
        if not reason:
            reason = "lowest bidder"
        add_project_to_devs(dev_id, bid_id)
    #check if reason was given
    else:
        if not reason:
            return "please give a valid reason"
        else:
            #find and set the index of the chosen dev 
            bid["chosen_index"] = Index
            if bid["chosen_index"] == 'Nan':
                print("not a valid dev_id")
                return ""
            add_project_to_devs(dev_id, bid_id)
    project["deadline"] = bid["bid_log"][bid["chosen_index"]][3]
    project["status"] = "active"
    bid["client_review"] = reason
    jsonIO.set_row("bid_db", bid)
    jsonIO.set_row("project_db", project)
    log = get_chosen_bid(bid_id)
    transfer_initial_bid_funds(project["client_id"], dev_id,log[2])
    return "Done"

def add_project_to_devs(dev_id, bid_id):
    dev = get_row(User(), dev_id)
    if is_admin(dev):
        team = jsonIO.get_row("team_db", dev['team_id'])
        team["project_ids"].append(bid_id)
        jsonIO.set_row("team_db", team)
        for member_id in team['dev_ids']:
            member =  get_row(User(), member_id)
            member["project_ids"].append(bid_id)
            jsonIO.set_row("user_db", member)
        else:
            dev["project_ids"].append(bid_id)
            jsonIO.set_row("user_db", dev)

#post: returns the entire bid_log
def get_bid_log(bid_id, only_id = False):
    if bid_id == None:
        return []
    bid_log = jsonIO.get_value("bid_db", bid_id, "bid_log")
    if not bid_log or bid_log == [[]]:
        return []
    if only_id:
        return bid_log[0][1]
    else:
        return bid_log    
    
#post:    returns the bid_log of the chosen bid
#        if only_id = True we only return the winner's id
def get_chosen_bid(project_id, only_id = False):
    chosen_index = jsonIO.get_value("bid_db", project_id, "chosen_index")
    if chosen_index == None:
        return []
    bid_log = jsonIO.get_value("bid_db", project_id, "bid_log")
    if not bid_log or bid_log == [[]]:
        return []
    if only_id:
        return bid_log[chosen_index][1]
    else:
        return bid_log[chosen_index]

#pre:    project status must be in no bid or active (by fsm_project)
#post:    if not chosen_index but has bids in bid log it will update it
#        set project to "active" if bid on else "no bid"
#        set user status to "active" who were in bid
#        transfer the initial funds
def end_bid(bid_id):
    project = jsonIO.get_row("project_db", bid_id)
    bid = jsonIO.get_row("bid_db", bid_id)
    #check if the project exist
    if not project:
        print ("Project does not exist")
        return 'Nan'
    if project["status"] != "active" and project["status"] != "no bid":
        print("Project is neither active or in no bid phase")
        return 'Nan'
    #check if project was bid on
    if project["status"] == "no bid":
        #PENALTY ON CLIENT
        to_user_id = 0
        amount = 10
        project["status"] = "no bid"
    #else we send the winner the money
    else:
        bid_log = get_chosen_bid(bid_id)
        print(bid_log)
        if not bid_log:
            bid["chosen_index"] = -1
            bid_log = bid["bid_log"][-1]
        to_user_id = bid_log[1]
        amount = bid_log[2]
        project["deadline"] = bid_log[3]
        #project is set to active
        project["status"] = "active"
        #set users who bid to active
        temp = bid["bid_log"][0]
        for bid_log in bid["bid_log"]:
            if any(bid_log[1] != e for e in temp):
                jsonIO.set_value("user_db", bid_log[1], "status", "active")
                temp.append(bid_log[1])
    jsonIO.set_row("project_db", project)
    jsonIO.set_row("bid_db", bid)
    return transfer_initial_bid_funds(project["client_id"], to_user_id, amount)

#post: will make an issue for user to resolve in order to transfer funds
def transfer_fund_request(from_user_id, to_user_id, amount):
    from_user = User()
    to_user = User()
    from_user.load_db(from_user_id)
    to_user.load_db(to_user_id)
    if amount <= 0:
        print("Must have a positive amount")
        return 0
    if from_user.get_balance() < amount:
        print("The user does not have enough funds")
        return 0
    issue = Issue(referred_id=from_user_id, issue_desc = "payment", admin_review=str(str(to_user_id)+",$"+str(amount)))


#cond: this is called at the beginning after the bid is done
#      the SU will withdraw the money and take 10% then give
#      half of the money to the team, and will add to SU issues.
#      It will be set as resolved, and set as unresolved when
#      the team submits their work or until the deadline.
#pre: from, to users exist and amount exists and is valid
#post: it will modify both balances and resolve payment issue.
def transfer_initial_bid_funds(from_user_id, to_user_id, amount = 10):
    from_user = jsonIO.get_row("user_db",from_user_id)
    to_user =  jsonIO.get_row("user_db", to_user_id)
    amount = float(amount)
    if amount <= 0:
        print("Must have a positive amount")
        return 0
    if from_user["balance"] < amount:
        print("The user does not have enough funds")
        return 0
    if not from_user["project_ids"]:
        print("The client has not initiated a project")
        return 0
    #takes money from the client
    from_user["balance"] -= amount
    #if it was because of the penalty
    if to_user_id == 0:
        to_user["balance"] += amount
        print("Penalty of $10 had been taken from client")
    #else it was success
    else:
        #take 10% and take 50% until completion of project
        deduction = round(amount*.1*.5, 2)
        amount -= deduction
        #keep it in superuser's bank
        su_balance = jsonIO.get_value("user_db", 0, "balance") + deduction
        jsonIO.set_value("user_db", 0, "balance", su_balance)
        print(amount)
        dev_split(to_user_id, amount/2)
        jsonIO.set_row("user_db", from_user)
        #retrieve the other 40% = 50%-10# fee
        print("Initial funds sent")
    #resolves payment issue if SU calls this function
    jsonIO.set_row("user_db", from_user)
    issue = find_issue(from_user["id"], "payment")
    if issue:
        issue["resolved"] = True
        jsonIO.set_row("issue_db", issue)
    return 1

def dev_split(dev_id, amount):
    dev = get_row(User(), dev_id)
    if is_admin(dev):
        print("A")
        team = jsonIO.get_row("team_db", dev['team_id'])
        amount = amount/len(team["dev_ids"])
        for member_id in team['dev_ids']:
            member =  get_row(User(), member_id)
            member["balance"] += amount
            jsonIO.set_row("user_db", member)
    else:
        print("B")
        dev["balance"] += amount
        set_row("user_db", dev)

#pre:     src is destination of the user's file 
#        new_project is the name of the file
#        checks if project is being submitted after the deadline
#post:    will make/ update project
#        if exist, it will no longer allow submission
#        changes the project's status to complete or incomplete
def submit(src, new_project, project_id):
    if jsonIO.get_value("project_db", project_id, "submission"):
        return "User has already submitted a project"
    deadline = jsonIO.get_value("project_db", project_id, "deadline")
    if string_to_datetime(deadline) <= get_now(True):
        jsonIO.set_value("project_db", project_id, "status", "incomplete")
        jsonIO.set_value("project_db", project_id, "client_rating", 1)
        return "The project cannot be sumitted after the deadline"
    jsonIO.set_value("project_db", project_id, "status", "complete")
    return set_file(src, new_project, prj_folder, None, project_id, "project")         
    
#pre:    project must exist and path must be valid
#post:    either error message or returns project
def get_submission(dst, project_id):
    project = jsonIO.get_row("project_db", project_id)
    file_name = project["submission"]
    if not file_name:
        return "Project has not been submitted yet"
    #check file path exist to image
    if not os.path.exists(dst):
        return "The file path: " + dst + " does not exist."
    #if file exist in folder rename to (1)
    path = os.path.join(prj_folder, file_name)
    if not os.path.exists(path):
        return "We couldn't find project in our database, contact admin"
    new_name = file_name
    if os.path.exists(os.path.join(dst, new_name)):
        n = 1
        new_name += "(" + str(n) + ")"
        #if still exist, keep incrementing number
        while os.path.exists(os.path.join(dst, new_name)):
            n += 1
            new_name = file_name + "(" + str(n) + ")"
        #copies the renamed file to file folder
        shutil.copy(path, os.path.join(dst, new_name))
    else:
        #copies the file to file folder
        shutil.copy(path, dst)
    #set project status to complete when retrieved
    if project["status"] == "submitted":
        jsonIO.set_value("project_db", project_id, "status", "complete")
        finalize_funds(project_id)
        print("Client has taken their project setting project to complete")
    #remove the project from the database
    #jsonIO.set_value("project_db", project_id, "submission", "")
    # if os.path.exists(path):
        # os.remove(path)
    return path    

#pre:    project must be in complete stage and respective ratings are empty
#post:    if rating <= 2 dev explain himself
#        if rating <= 3 client explain himself
#        calls set_warning to take care of the warnings
def make_rating(user_id, rating, comment = ""):
    #check if valid user
    user = jsonIO.get_row("user_db", user_id)
    if not user:
        print("User not valid")
        return 'Nan'
    if not user["project_ids"]:
        print("User has not done any projects")
        return 'Nan'
    #check for project completion
    project = jsonIO.get_row("project_db", user["project_ids"][-1])    #check if it is a client
    if user["user_type"] == "dev":
        #check rating < 3: make comment
        if rating < 3 and not comment:
            return "Rating was less than 3 please provide a justification"
        else:
            project["client_rating"] = rating
            project["client_review"] = comment
            project["status"] = "submitted"
    #check if it is a dev
    elif user["user_type"] == "client":
        #check rating <= 2: make comment
        if rating <= 2 and not comment:
            return "Rating was 2 or less please provide a justification"
        else:
            project["team_rating"] = rating
            project["team_review"] = comment
            project["status"] = "complete"
    jsonIO.set_row("project_db", project)
    set_warning(user, project, rating)
    return project 

#pre:    must have a valid bid and project must be complete
#post:    transfers the remaining funds after the completion/ incompletion of project
def finalize_funds(project_id):
    project = jsonIO.get_row("project_db", project_id)
    if not project:
        print("Project does not exist")
        return 0
    if project ["status"] == "submitted":
        print ("Client has not yet retrieved the submission. Please wait")
        return 0
    if project["status"] != "incomplete" and project["status"] != "complete":
        print("Project was not set to complete or incomplete")
        return 0
    bid_log = get_chosen_bid(project_id)
    if bid_log == []:
        print("Bid log does not exist")
        return 0
    amount = bid_log[2]
    #take 10% and take 50% until completion of project
    deduction = round(amount*.1*.5, 2)
    amount -= deduction
    #send back the money to client if incomplete
    if project["status"] == "incomplete":
        print("Project was incomplete so penalizing")
        transfer_funds(bid_log[1], project["client_id"], amount)
        transfer_funds(0, project["client_id"], deduction)
        jsonIO.set_value("project_db", project_id, "client_rating", 1)
        jsonIO.set_value("project_db", project_id, "client_review", "Project incomplete")
        return 1
    #if rating was lower than 3 talk to client to decide
    if project["team_rating"] < 3:
        print("Rating was less than 3, the client must talk to SU")
        Issue(project_id, "payment")
        return -1
    #else if complete send dev the money
    else:
        dev_split(bid_log[1], amount/2)
    print("transfer of funds to dev is complete")
    return 1

#cond:    uses the user and project dictionary to check rating of new project 
#pre:    must be called after incomplete project or after rating
#post:    user's warning will increase depending on inputs
#        check user's out_ratings and will increase warnings too
def set_warning(user_dict, prj_dict, rating = 'Nan'):
    #grabs all user from project if it is in a team
    if user_dict["team_id"] != 'Nan':
        users = []
        for user in jsonIO.get_value("team_db", user_dict["team_id"], "dev_ids"):
            users.append(jsonIO.get_row("user_db", user))
    else:
        users = [user_dict]
    #check if project is in incomplete state
    if prj_dict["status"] == "incomplete":
        #increment warning
        print("Project was incomplete")
        for user in users:
            user["warning"] += 1
    #check this user's average in rating
    for user in users:
        if get_grade(user) <= 2 and len(user["project_ids"]) >= 5:
            print("User was given low average rating")
            user["warning"] += 1
        #check this user's average out rating
        out_rate = avg_out_rating(user)
        if out_rate < 2 and len(user["project_ids"]) >= 8:
            print("User has given low average rating")
            user["warning"] += 1
        elif out_rate > 4 and len(user["project_ids"]) >= 8:
            print("User has given high average rating")
            user["warning"] += 1
        jsonIO.set_value("user_db", user["id"], "warning", user["warning"])
    
    
#/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\
#/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\
#/\/\/\/\ENGINES/\/\/\/\ENGINES/\/\/\/\ENGINES/\/\/\/\ENGINES/\/\/\/\ENGINES/\/\/\/\ENGINEENGINES/\/\/\/\/\/\
#/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\
#/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\

#post: Uses the search engine to find name
def search_matches(obj, input_name):
    matches = []
    names = get_col(obj, "id")
    if input_name == "":
        for name in names:
            matches.append(name["id"])
    else:
        for name in names:
            name = get_row(obj, name['id'])
            if obj.get_all() == Project().get_all():
                if name["title"] == input_name:
                    matches.append(name["id"]) 
            elif obj.get_all() == Issue().get_all():
                if name["issue_desc"] == input_name and not name["resolved"]:
                    matches.append(name["id"])
            elif obj.get_all() == User().get_all():
                if name["name"] == input_name:
                    matches.append(name["id"])
    return matches

#post:     will recommend a dev a project and a client a dev
#        returns in this format [dict(of user/project), list of matching interests]
def recommendation(user_dict):
    interest_list = []
    #get all "active" users who are not the same user_type with the same interest
    for user in jsonIO.read_rows("user_db"):
        #if active, not same user type, and not the same person
        if user["status"] == "active" and user["user_type"] != user_dict["user_type"] and user["id"] != user_dict["id"]:
            interests = list(set(user["interests"]).intersection(user_dict["interests"]))
            #if matching interests
            if interests:
                #if client, get list of "active" devs and interest
                if user_dict["user_type"] == "client":
                    interest_list.append([user,interests])
                #if dev, get list of "bidding" projects and interest
                else:
                    project = jsonIO.get_row("project_db", user["project_ids"][-1])
                    #check if bidding
                    if project["status"] == "bidding":
                        interest_list.append([project,interests])
    return interest_list

def rank(user_type): 
    if user_type not in ['dev', 'client', 'team']:
        return []
    
    top3 = []
    top3_ids = []

    # arguemnts for bayesian_avg()
    m,c = get_m_c(user_type)
    
    # read the rows from database file
    DB = 'user_db'
    if (user_type == 'team'):
        DB = 'team_db'
    users = jsonIO.read_rows(DB)

    if users: # if any row exist in the database
        if (user_type == 'team'):
            users_with_grade = list(filter(lambda user: get_grade(user) > 0, users))
        else:
            users_with_grade = list(filter(lambda user: get_grade(user) > 0 and user['user_type'] == user_type, users))
            
    # find top 3 bayesian average grade among the user_type
        id_grade_tuples = [] # [(id,grade), ...]
        if len(users_with_grade) > 0:
            for user in users_with_grade:
                id_grade_tuples.append((user['id'], bayesian_avg(user, m, c)))
        top3_tuples = sorted(id_grade_tuples, key=lambda pair: pair[1])[-1:-4:-1]
        top3 = list(map(lambda tup: jsonIO.get_row(DB, tup[0]), top3_tuples))
    while len(top3) < 3:
        if user_type == "dev":
            top3.append(users[1])
        elif user_type == "client":
            top3.append(users[1])
        else:
            top3.append(users[1])
    for one in top3:
        top3_ids.append(one["id"])
    return top3_ids
#/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\
#/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\
#/\/\/\/\METRICS/\/\/\/\METRICS/\/\/\/\METRICS/\/\/\/\METRICS/\/\/\/\METRICS/\/\/\/\METRICS/\/\/\/\/\/\/\/\/\
#/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\
#/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\

#pre: user exists in "user_db" ,and user can be a team, a developer, or a client
#post: return average rating of the user
def get_grade(user):
    grade = 0 
    completed_project = len(user["project_ids"])
    if completed_project > 0:
        if is_in_active_project(user):
            completed_project = completed_project - 1
            
    if completed_project > 0:
        for project in user["project_ids"][:completed_project]:
            p = jsonIO.get_row("project_db", project)
            try:
                if user["user_type"] == "dev":     # developer grade
                    grade += p['team_rating']
                    #print(grade)
                elif user["user_type"] == 'client':# client grade
                    grade += p['client_rating']    
            except KeyError:                       # team grade
                grade += p['team_rating']
        grade = round(grade/completed_project, 1)
    return grade 
    
#cond: dev    total (dev)
#      team   total (team)
#pre: id must exists for all 
#post: return total comssion
def get_total_commision(obj, dict = 0):
    commision = 0
    #commision for class
    if not dict:
        for id in obj.get_project_ids():
            #bid_id = project_id
            bid = jsonIO.get_value("bid_db", id, "final_bid")
            if bid:
                commision += bid
    #commision for dict
    else:
        for id in obj["project_ids"]:
            #bid_id = project_id
            bid = jsonIO.get_value("bid_db", id, "final_bid")
            if bid:
                commision += bid
    #if commision exist return something
    return commision

# return an average grade of a user 
# using bayesian average = (sum_grades + c*m)/(n + c) where 
# 
# sum_grades = sum of all grades the user got
# n = the number of project the user finihsed
# m = mean grade across the user type <= get_m_c(user_type)[0]
# c = number of project the user type finished in average <= get_m_c(user_type)[1] 
def bayesian_avg(user, m, c):
    grades = grade_log(user)
    sum_grades = sum(grades)
    n = len(grades)
    
    if (n + c == 0):
        return 'Nan'
    
    return (sum_grades + c*m)/(n + c)

#post: returns the average grades user GIVES OUT TO OTHERS
def avg_out_rating(user_dict):
    if not user_dict["project_ids"]:
        return 0
    total = 0
    if user_dict["user_type"] == "client":
        rate_type = "client_rating"
    else:
        rate_type = "team_rating"
    for prj_id in user_dict["project_ids"]:
        total += jsonIO.get_value("project_db", prj_id, rate_type)
    return round(total/len(user_dict["project_ids"]), 1)

# pre: user_type is either 'dev', 'client', or 'team'
# post: returns the total number of rows if user_type is one of above.
#       otherwise, return 0
def total_user(user_type):
    user_number = 0 # total number of users
    if(user_type == 'dev'):
        developers = list(filter(lambda row: row['user_type'] == 'dev', jsonIO.read_rows("user_db")))
        user_number = len(developers)
    elif(user_type == 'client'):        
        clients = list(filter(lambda row: row['user_type'] == 'client', jsonIO.read_rows("user_db")))
        user_number = len(clients)
    elif(user_type == 'team'):
        user_number = len(jsonIO.read_rows("team_db"))
    return user_number
# post: returns the total number of project that has been completed in the system database
def total_completed_projects():

    completed_projects = 0;
    projects = jsonIO.read_rows("project_db")
    
    # complete project's status is "complete"
    completed_projects = list(filter(lambda project: project["status"] == "complete", projects))

    return len(completed_projects)

def total_bids():
    amount = 0
    bids = jsonIO.read_rows("bid_db")
    for bid in bids:
        amount += len(bid["bid_log"]) - 1
    return amount
    
def avg_rating():
    users = jsonIO.read_rows("user_db")
    rating = 0
    users = list(filter(lambda user: user["status"] == "active", users))
    for user in users:
        rating += get_grade(user)
    rating = rating/len(users)
    rating = round(rating, 2)
    return rating

#/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\
#/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\
#/\/\/\/\HELPER FUNTIONS/\/\/\/\HELPER FUNTIONS/\/\/\/\HELPER FUNTIONS/\/\/\/\HELPER FUNTIONS/\/\/\/\/\/\/\/\
#/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\
#/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\

#pre: must have a valid db, key and value
#post: returns row of given key value
def find_row(db, key, value):
    rows = jsonIO.get_rows(db, key, value)
    if rows:
        return rows[0]
    else:
        return {}

#to be called by print_table
#values hold collection of values
def val_print(values):
    for j in range(len(values)):
        value = values[j]
        #is the value a list?
        if type(value) == list:
            if value == []:
                values[j] = '[]'
            else:
                values[j] =  ",".join(str(x) for x in value)
    print (indents.format(*values))

#post: updates now and returns now
def get_now(dt = False):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    dt_now = datetime.strptime(now, "%Y-%m-%d %H:%M:%S")
    if dt:
        return dt_now
    else:
        return now
    
#pre: needs String in Y-m-d H:M:S form
#post: returns datetime form
def string_to_datetime(time):
    try:
        return datetime.strptime(time, "%Y-%m-%d %H:%M:%S")
    except:
        print("String not in Y-m-d H:M:S form")
        return None

#pre: needs datetime in Y-m-d H:M:S form
#post: returns string form
def datetime_to_string(dt_time):
    try:
        return dt_time.strftime("%Y-%m-%d %H:%M:%S")
    except:
        print("Datetime not in Y-m-d H:M:S form")
        return 'Nan'
        
#pre: needs time in string and n days to be added
#post: return string with added days
def get_n_days_later(time, n):
    dt_time = string_to_datetime(time)
    dt_later = dt_time + timedelta(days = n)
    return datetime_to_string(dt_later)    

#pre: both user must exist, client must have enough funds, and amount must be valid 
#post: transfer money from user to user.
def transfer_funds(from_user_id, to_user_id, amount):
    from_user = User()
    to_user = User()
    from_user.load_db(from_user_id)
    to_user.load_db(to_user_id)
    if amount <= 0:
        print("Must have a positive amount")
        return 0
    if from_user.get_id() == 'Nan':
        print("The user you are grabbing from does not exist")
        return 0
    if to_user.get_id() == 'Nan':
        print("The user you are sending to does not exist")
        return 0
    if from_user.get_balance() < amount:
        print("The user does not have enough funds")
        return 0
    from_user.withdraw(amount)
    to_user.deposit(amount)
    return 1

#pre: user must exist
#post: check if user is active
def is_in_active_project(user):
   if len(user["project_ids"]) > 0:
       id = user["project_ids"][len(user["project_ids"]) - 1]
       project = jsonIO.get_row("project_db", id)
       if project["status"] == "active" or project["status"] == "submitted" or project["status"] == "bidding":
           return True
       else:
           return False
   return False
  
#cond: dict will contain a dict of user (has "team_id and id")
#pre: team_id must exits
#post: returns team admin
def is_admin(dict):
   if dict["team_id"] == "Nan":
       return False
   else:
       team = get_row(Team(), dict["team_id"])
       for admin in team["admin_ids"]:
           if dict["id"] == admin:
               return True
           
def is_on_quit_warning_list(dev_id, type):
    issues = read_rows("issue_db")
    print(issues)
    for issue in issues:
        print(issue)
        if issue["issue_desc"] == type and dev_id == issue['referred_id'] and issue['resolved'] == False:
            return True
    return False


#cond:  if obj_id is not defined, it will just print what is in the path
#        if obj_id is defined we proceed to copy obj
#        dst should be either img_folder or prj_folder
#        obj_type is project, team, or user
#        old_file is the previous name of the file that the obj had, otherwise it is None
#        if a file exist it will rename it
#        if the obj had a picture it will remove it
#pre: needs valid path
#post: will either return available files if file not stated
#   else return success/failure message
def set_file(src, new_file = None, dst = None, old_file = None, obj_id = None, obj_type = None):
    #if only path it will print availble files
    if not obj_id:
        list = os.listdir(src)
        print (list)
        return list
    #check file path exist to image
    new_name = new_file
    path = os.path.join(src, new_file)
    if not os.path.exists(path):
        return "The file path: " + path + " does not exist."
    #if dst does not exist, it will create it    
    if not os.path.exists(dst):
        print(dst + " does not exist, so making a new one")
        os.mkdir(dst)
    #if the user had a old_file it will remove it
    if old_file and old_file != "default_user.png":
        if os.path.exists(os.path.join(dst, old_file)):
            os.remove(os.path.join(dst, old_file))
    #if file exist in folder rename to (1)
    if os.path.exists(os.path.join(dst, new_file)):
        n = 1
        new_name += "(" + str(n) + ")"
        #if still exist, keep incrementing number
        while os.path.exists(os.path.join(dst, new_name)):
            n += 1
            new_name = new_file + "(" + str(n) + ")"
        #copies the renamed file to file folder
        shutil.copy(path, os.path.join(dst, new_name))
    else:
        #copies the file to file folder
        shutil.copy(path, dst)
    #set the name in the database
    if obj_type == "project":
        jsonIO.set_value("project_db", obj_id, "submission", new_name)
    elif obj_type == "team":
        jsonIO.set_value("team_db", obj_id, "pic", new_name)
    else:
        jsonIO.set_value("user_db", obj_id, "pic", new_name)
    return "File copied"
    
# helper function for bayesian_avg(user, m, c)
# pre: user is a valid row(dictionary) in database
# post: return a list of user's project grades that are inactive(graded)
def grade_log(user):
    grades = []
    
    # list may or may not have one active project as the current project
    completed_project = len(user["project_ids"]) 
    if completed_project > 0:
        if is_in_active_project(user): # list have one active project
            completed_project = completed_project - 1
    grades = []
    if completed_project > 0:
        for project in user["project_ids"][:completed_project]:
            p = jsonIO.get_row("project_db", project)
            try:
                if user["user_type"] == "dev":     # developer grade
                    grades.append(p['team_rating'])
                elif user["user_type"] == 'client':# client grade
                    grades.append(p['client_rating'])
            except KeyError:                       # team grade
                grades.append(p['team_rating'])
    return grades    
    
# helper function for rank()
# pre: user_type can be either 'dev', 'client', or 'team'
# post: return [m, c] where
#          m = the mean grade among the user type, 
#          c = the average number of project the user type finished
#       otherwise, return []
def get_m_c(user_type):
    
    if user_type not in ['dev', 'client', 'team']:
        return []
    
    DB = 'user_db'
    if (user_type == 'team'):
        DB = 'team_db'

    mean_grade = 0 
    mean_project_num = 0
    users = jsonIO.read_rows(DB)
    
    if users: # if any row exist in the database
        users_with_grade = []
        if (user_type == 'team'):
            users_with_grade = list(filter(lambda user: get_grade(user) > 0, users))
        else:
            users_with_grade = list(filter(lambda user: get_grade(user) > 0 and user['user_type'] == user_type, users))
        
        grades = list(map(lambda user: get_grade(user), users_with_grade))
        projects = list(map(lambda user: len(user["project_ids"]), users_with_grade))

        # calculate m, which is mean_grade
        if len(grades) != 0:
            mean_grade = sum(grades)/len(grades)
        # calculate c, which is mean_project_num
        if len(projects) != 0:
            mean_project_num = sum(projects)/len(projects)
        else:
            print("zero projects")
    return [mean_grade, mean_project_num]

def find_issue(referred_id, desc):
    issue_list = jsonIO.get_rows("issue_db", "referred_id", referred_id)
    if issue_list:
        for issue in issue_list:
            if issue["resolved"] == False and issue["issue_desc"] == desc:
                return issue
    return None