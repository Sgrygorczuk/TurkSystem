from User import *
from Project import *
from Team import *
from jsonIO import *
from Issue import *
import ezcommands as ez
import math

import tkinter.messagebox
from tkinter import *
from datetime import datetime
from datetime import timedelta
from tkinter import filedialog as fd
import os

class GUI():

	def __init__(self):
		self.origin = Tk()
		
		self.colors = ["white", "#C3CBDE", "#3b0c0c"] #white, blue, red 

		self.top_three_teams_id = [0,1,2]
		self.top_three_devs_id = [1,2,3]
		self.top_three_clients_id = [5,6,7]
		self.software_statistic = [170, 85, 85, 55, 2.88, 623]
		
		#Set up the general screen
		self.origin.title("The Turk System")
		self.frame_over_lay = Frame(self.origin, bg = "#3b0c0c")
		self.frame_current = Frame(self.origin)
		self.frame_profile = Frame(self.origin, bg = "white")
		self.frame_make_team = Frame(self.origin, bg = "white")
		
		#Items form overlay that will need to be called back
		self.frame_user_login_input = Frame(self.frame_over_lay, bg = "#3b0c0c")
	
		self.frame_logged_in = Frame(self.frame_over_lay, bg = "#3b0c0c", cursor = "hand2")
		
		
		self.logged_in_user = User().get_all() 
		self.profile_user = {"id" : "Nan", "name": "", "interest": "", "team_id" : -2}   
		self.profile_project = Project().get_all()
		self.profile_team = Team().get_all()
		#0 - Normal view, 1 - edit, 2 withdraw, 3 deposit, 4 dispute  
		self.proflie_state = 0
		#0 - User, 1 - Team, 2 - Project, 3 - Search  
		self.profile_type = 0
		self.project_index = 0
		#0 - Accept, 1 - Warning, 2 - Quit, 3 - Blacklist, 4 Grade+Payment  
		self.SU_state = 0
		self.path = ""
		
		#Creates all the items
		self.set_up_top_user_chart()
		self.set_up_overlay()
		

	def set_up_overlay(self, error = 0, error_message = ""):
		color = "#3b0c0c"
		button_home = Button(self.frame_over_lay, text = "The Turk System", relief = FLAT, bg = color, fg = "white", cursor = "hand2")  
		self.entry_search_bar = Entry(self.frame_over_lay)
		button_search = Button(self.frame_over_lay, text = "Search", bg = "green", fg = "white", cursor = "hand2")
		button_search.bind("<Button-1>", self.search_button)
		
		self.frame_user_login_input.destroy()
		self.frame_user_login_input = Frame(self.frame_over_lay, bg = "#3b0c0c")
		self.entry_username = Entry(self.frame_user_login_input)
		self.entry_password = Entry(self.frame_user_login_input)
		
		self.v = IntVar()
		self.v.set(0)
		button_user = Radiobutton (self.frame_over_lay, text = "User", bg = color, activebackground = color, fg = "white", cursor = "hand2", variable=self.v, value = 0)
		button_team = Radiobutton (self.frame_over_lay, text = "Team", bg = color, activebackground = color, fg = "white",cursor = "hand2", variable=self.v, value = 1)
		button_project = Radiobutton (self.frame_over_lay, text = "Project", bg = color, activebackground = color, fg = "white",cursor = "hand2", variable=self.v, value = 2)
		
		
		labeL_error_message = Label(self.frame_user_login_input, text = error_message,bg = color, fg = "white")
		label_username = Label(self.frame_user_login_input, text = "Username: ",bg = color, fg = "white")
		label_password = Label(self.frame_user_login_input, text = "Password: ",bg = color, fg = "white")
		button_log_in = Button(self.frame_user_login_input, text = "Login", relief = FLAT, bg = color, fg = "white", cursor = "hand2")
		button_create_account = Button(self.frame_user_login_input, text = "Create Account", relief = FLAT, bg = color, fg = "white", cursor = "hand2")
		
		button_home.bind("<Button-1>", self.home_button)
		button_log_in.bind("<Button-1>", self.log_in)
		button_create_account.bind("<Button-1>", self.new_account_button)
		
		self.frame_over_lay.grid(row = 0, column = 0, sticky = E+W)
		button_home.grid(row = 1, column = 0, sticky = W)
		self.entry_search_bar.grid(row = 1, column = 1, padx = 10)
		button_user.grid(row = 0, column = 2, sticky = W)
		button_team.grid(row = 1, column = 2, sticky = W)
		button_project.grid(row = 2, column = 2, sticky = W)
		button_search.grid(row = 1, column = 3, sticky = E)
		self.frame_user_login_input.grid(row = 1, column = 4)
		if error != 0:
			labeL_error_message.grid(row = 0, column = 0, columnspan = 5)
		label_username.grid(row = 1, column = 0)
		self.entry_username.grid(row = 1, column = 1)
		label_password.grid(row = 1, column = 2)
		self.entry_password.grid(row = 1, column = 3)
		button_log_in.grid(row = 1, column = 4,padx = 10)
		button_create_account.grid(row = 1, column = 5,padx = 10)

	def set_up_overlay_profile(self, user, message = ""):
		color = "#3b0c0c"
		self.frame_logged_in.destroy()
		self.frame_logged_in = Frame(self.frame_over_lay, bg = "#3b0c0c", cursor = "hand2")
		if "user_type" in user:
			image = PhotoImage(file = ez.get_pic(user['id'], user["user_type"]))
		else:
			image = PhotoImage(file = ez.get_pic(user['id'], "user"))
		image = image.subsample(12,12)
		label_image = Label(self.frame_logged_in, image = image, cursor = "hand2")
		label_image.image = image
		label_name = Button(self.frame_logged_in, text = user["name"]+ " " + str(ez.get_grade(user)), bg = color, fg = "white", cursor = "hand2")
		button_logout = Button(self.frame_logged_in, text = "Log Out", relief = FLAT, bg = color, fg = "white", cursor = "hand2")
		
		if message != "":
			label_message = Label(self.frame_logged_in, text = message, bg = color, fg = "white", cursor = "hand2")
			label_message.grid(row = 0, column = 0, columnspan = 3)
		
		
		button_logout.bind("<Button-1>", self.log_out)
		self.frame_logged_in.bind("<Button-1>", lambda event, arg = user: self.profile_button(event, arg))
		label_name.bind("<Button-1>", lambda event, arg = user: self.profile_button(event, arg))
		label_image.bind("<Button-1>", lambda event, arg = user: self.profile_button(event, arg))
		
		self.frame_logged_in.grid(row = 1, column = 4, padx = 60)
		label_image.grid(row = 1, column = 0)
		label_name.grid(row = 1, column = 1)
		button_logout.grid(row = 1, column = 2)
		
		
		
	def set_up_top_user_chart(self):
		self.frame_profile.destroy()
		self.frame_profile = Frame(self.origin, bg = "white")
		
		label_hall = Label(self.frame_profile, text = "Hall of Fame", bg = "white")
		label_top_team = Label(self.frame_profile, text = "Top 3 Teams", bg = "white")
		label_top_dev = Label(self.frame_profile, text = "Top 3 Developers", bg = "white")
		label_top_client = Label(self.frame_profile, text = "Top 3 Clients", bg = "white")
	
		counter = 2
		for team_id in self.top_three_teams_id:
			team = get_row("team_db", team_id)
			self.set_up_top_user_profile(row = counter, column = 0, dictonary =  team)
			counter += 1
			
		counter = 2
		for dev_id in self.top_three_devs_id:
			user = get_row("user_db", dev_id)
			self.set_up_top_user_profile(row = counter, column = 1, dictonary =  user)
			counter += 1
			
		counter = 2
		for client_id in self.top_three_clients_id:
			client = get_row("user_db", client_id)
			self.set_up_top_user_profile(row = counter, column = 2, dictonary =  client)
			counter += 1
		
		
		label_hall.grid(row = 0, column = 0, columnspan = 3, sticky = E+W+S+N)
		label_top_team.grid(row = 1, column = 0, sticky = W+E)
		label_top_dev.grid(row = 1, column = 1, sticky = W+E)
		label_top_client.grid(row = 1, column = 2, sticky = W+E)
		self.frame_profile.grid(row = 1, column = 0, sticky = S+W+N+E)
		
		self.set_up_software_stats()
		
	def set_up_top_user_profile(self,row,column, dictonary):
		color = "#3b0c0c"
		frame_temp = Frame(self.frame_profile, bg = color)
		if "user_type" in dictonary:
			image = PhotoImage(file = ez.get_pic(dictonary['id'], dictonary["user_type"]))
		else:
			image = PhotoImage(file = ez.get_pic(dictonary['id'], "user"))
		image = image.subsample(5,5)
		lable_image = Label(frame_temp, image = image, cursor = "hand2")
		lable_image.image = image
		rank = "Rank " + str(row-1)
		if (row-1) == 1:
			rank += "st"
		elif (row-1) == 2:
			rank += "nd"
		else:
			rank += "rd"
		label_rank = Label(frame_temp, text = rank, bg = color, fg = "white")
		label_name = Label(frame_temp, text = "Name: " + dictonary['name'], bg = color, fg = "white", wraplength = 150)
	
		label_grade = Label(frame_temp, text = "Grade: " + str(ez.get_grade(dictonary)), bg = color, fg = "white")
		
		if column == 0:
			label_teams = Label(frame_temp, text = "Team members: " + str(len(dictonary["dev_ids"])), bg = color, fg = "white")
			lable_image.bind("<Button-1>", lambda event, arg = dictonary: self.team_button(event, arg))
			label_teams.grid(row = 5, column = 0, sticky = W)
		else:
			if dictonary["team_id"] == "Nan" and dictonary["user_type"] == "dev":
				label_teams = Label(frame_temp, text = "Team: N/A", bg = color, fg = "white", wraplength = 150)
				label_teams.grid(row = 5, column = 0, sticky = W)
			elif dictonary["user_type"] == "dev":
				label_teams = Label(frame_temp, text = "Team: " + get_row("team_db", dictonary["team_id"])["name"], bg = color, fg = "white", wraplength = 150)
				label_teams.grid(row = 5, column = 0, sticky = W)
			lable_image.bind("<Button-1>", lambda event, arg = dictonary: self.profile_button(event, arg))
		
		label_projects = Label(frame_temp, text = "Projects Complete: " + str(len(dictonary['project_ids'])), bg = color, fg = "white")
		frame_temp.grid(row = row, column = column, sticky = N+S+E+W, padx = 10, pady = 10, ipadx = 40)
		label_rank.grid(row = 2, column = 2)
		lable_image.grid(row = 2, column = 0, sticky = N+S+W)
		label_name.grid(row = 3, column =0, sticky = W)
		label_grade.grid(row = 4, column = 0, sticky = W)
		label_projects.grid(row = 6, column = 0, sticky = W)
		
	def set_up_software_stats(self):
		color = "#1A5276"
		frame = Frame(self.frame_profile, bg = color)
		label_stats_title = Label(frame, text = "The Turk System Statistics", bg = color, anchor = NE, fg = "white")
		label_user_total =  Label(frame, text = "Total Users: " + str(self.software_statistic[0]), bg = color, fg = "white")
		label_user_devs =  Label(frame, text = "Total Developers: " + str(self.software_statistic[1]), bg = color, fg = "white")
		label_user_clients =  Label(frame, text = "Total Clients: " + str(self.software_statistic[2]), bg = color, fg = "white")
		label_user_teams =  Label(frame, text = "Total Teams: " + str(self.software_statistic[3]), bg = color, fg = "white")
		label_avg_grade =  Label(frame, text = "Average Grade: " + str(self.software_statistic[4]), bg = color, fg = "white")
		label_projects_completed =  Label(frame, text = "Projects Completed: " + str(self.software_statistic[5]), bg = color, fg = "white")
	
		frame.grid(row = 0, column = 4, rowspan = 20, columnspan = 3, sticky = S+N+W)
		label_stats_title.grid(row = 0, column = 0, sticky = E+W, ipady = 20)
		label_user_total.grid(row = 1, column = 0, sticky = W)
		label_user_devs.grid(row = 2, column = 0, sticky = W)
		label_user_clients.grid(row = 3, column = 0, sticky = W)
		label_user_teams.grid(row = 4, column = 0, sticky = W)
		label_avg_grade.grid(row = 5, column = 0, sticky = W)
		label_projects_completed.grid(row = 6, column = 0, sticky = W)
		
		
		
	def set_up_new_account(self, error_message = ""):
		color = "#C3CBDE"
		self.frame_profile.destroy()
		self.frame_profile = Frame(self.origin, bg = "#C3CBDE")
		self.frame_current = self.frame_profile
		
		self.var = IntVar()
		self.var.set(0)
		button_developer = Radiobutton (self.frame_profile, text = "Developer", bg = color, activebackground = color, cursor = "hand2", variable=self.var, value = 0)
		button_client = Radiobutton (self.frame_profile, text = "Client", bg = color, activebackground = color, cursor = "hand2", variable=self.var, value = 1)
		button_create = Button(self.frame_profile, text = "Create Account", bg = color )
		label_name = Label(self.frame_profile, text = "Name:", bg = color)
		label_username = Label(self.frame_profile, text = "Username:", bg = color)
		label_password = Label(self.frame_profile, text = "Password:", bg = color)
		label_balance = Label(self.frame_profile, text = "Balance:", bg = color)
		label_error_message = Label(self.frame_profile, text = error_message, bg = color)
		self.entry_name = Entry(self.frame_profile)
		self.entry_username_ac = Entry(self.frame_profile)
		self.entry_password_ac  = Entry(self.frame_profile)
		self.entry_balance = Entry(self.frame_profile)
		
		button_create.bind("<Button-1>", self.create_button_account)
		description = "Enter your name, a unique username, a password you can remember, place a postive balance you want to start your account off with and select your role, \na clinet is BLAH \nand \na developer is a BLAH"
		label_text = Label(self.frame_profile, text = description, bg = color, wraplength = 500)
		self.frame_profile.grid(row = 1, column = 0, sticky = S+E+W+N)
		label_text.grid(row = 0, column = 0, columnspan = 3, pady = 5)
		label_name.grid(row = 2, column = 0, pady = 5)
		self.entry_name.grid(row = 2, column = 1, sticky = W)
		label_username.grid(row = 3, column = 0,  pady = 5)
		self.entry_username_ac.grid(row = 3, column = 1, sticky = W)
		if error_message:
			label_error_message.grid(row = 1, column = 0, columnspan = 3, pady = 5)
		label_password.grid(row = 4, column = 0,pady = 5)
		label_balance.grid(row = 5, column = 0, pady = 5)
		self.entry_balance.grid(row = 5, column = 1, sticky = W)
		self.entry_password_ac.grid(row = 4, column = 1, sticky = W)
		button_developer.grid(row = 2, column = 2, sticky = W)
		button_client.grid(row = 3, column = 2, sticky = W)
		button_create.grid(row = 6, columnspan = 2, column = 0, sticky = E+W, pady = 5)
		
	def set_up_new_team(self, event):
		color = "#C3CBDE"
		self.frame_make_team.destroy()
		self.frame_make_team = Frame(self.origin, bg = "#C3CBDE")
		self.frame_profile.destroy()
		self.frame_profile = Frame(self.origin, bg = "#C3CBDE")
		self.frame_current = self.frame_make_team
		
		button_create = Button(self.frame_profile, text = "Create Team", bg = color )
		label_name = Label(self.frame_profile, text = "Team Name:", bg = color)
		label_desc = Label(self.frame_profile, text = "Description", bg = color)
		label_text = Label(self.frame_profile, text = "Enter the team name and description that best fit's you and your colleagues", bg = color)
		
		entry_name = Entry(self.frame_profile)
		entry_desc = Text(self.frame_profile, height=2, width=30)
		
		self.frame_profile.grid(row = 1, column = 0, columnspan = 3, sticky = S+E+N+W)
		
		label_text.grid(row = 0, column = 0, sticky = E+W, pady = 5, columnspan = 2)
		label_name.grid(row = 1, column = 0, sticky = W)
		entry_name.grid(row = 1, column = 1, sticky = W)
		label_desc.grid(row = 2, column = 0, sticky = W)
		entry_desc.grid(row = 2, column = 1, sticky = W)
		button_create.grid(row = 3, columnspan = 2, column = 0, sticky = E+W, pady = 5)
		
		
	def set_up_new_project(self, event):
		color = "#C3CBDE"
		self.frame_make_team.destroy()
		self.frame_make_team = Frame(self.origin, bg = "#C3CBDE")
		self.frame_profile.destroy()
		self.frame_profile = Frame(self.origin, bg = "#C3CBDE")
		self.frame_current = self.frame_make_team
		
		button_create = Button(self.frame_make_team, text = "Create Project", bg = color )
		button_create.bind("<Button-1>", self.create_button_project)
		label_name = Label(self.frame_make_team, text = "Project Name:", bg = color)
		label_desc = Label(self.frame_make_team, text = "Description", bg = color)
		label_money = Label(self.frame_make_team, text = "Maximum Payment Offer", bg = color)
		label_date = Label(self.frame_make_team, text = "Maximum Deadline Offer", bg = color)
		label_text = Label(self.frame_make_team, text = "Enter the informations about the project such as it's name, a short description of what it should do including a way to contact you,\n how long you are willing to wait for it and how much you are willing to pay for it\n you will not be able to change this infromation", bg = color)
		
		self.entry_name = Entry(self.frame_make_team)
		self.entry_desc = Text(self.frame_make_team, height=2, width=30)
		self.entry_money = Entry(self.frame_make_team)
		self.entry_time =Entry(self.frame_make_team)
		self.frame_make_team.grid(row = 1, column = 0, sticky = S+E+N+W)
		
		label_text.grid(row = 0, column = 0, sticky = E+W, pady = 5, columnspan = 2)
		label_name.grid(row = 1, column = 0, sticky = W)
		self.entry_name.grid(row = 1, column = 1, sticky = W)
		label_desc.grid(row = 2, column = 0, sticky = W)
		self.entry_desc.grid(row = 2, column = 1, sticky = W)
		label_money.grid(row = 3, column = 0, sticky = W)
		self.entry_money.grid(row = 3, column = 1, sticky = W)
		label_date.grid(row = 4, column = 0, sticky = W)
		self.entry_time.grid(row = 4, column = 1, sticky = W)
		button_create.grid(row = 5, columnspan = 2, column = 0, sticky = E+W, pady = 5)
		
		
	def set_up_new_bid(self, event):
		color = "#C3CBDE"
		self.frame_make_team.destroy()
		self.frame_make_team = Frame(self.origin, bg = "#C3CBDE")
		self.frame_profile.destroy()
		self.frame_profile = Frame(self.origin, bg = "#C3CBDE")
		self.frame_current = self.frame_make_team
		frame = Frame(self.frame_make_team, bg = "white")
		
		client = get_row("user_db", self.profile_project["client_id"])
		bid = get_row("bid_db", self.profile_project['id'])
		log = ez.get_bid_log(self.profile_project['id'])
		
		label_project_name_static = Label(frame, text = "Project Name: " + self.profile_project["title"], bg = "white")
		label_project_client_name_static = Label(frame, text = "Client Name: " + client["name"], bg = "white")
		label_project_client_grade_static = Label(frame, text = "Grade: " + str(ez.get_grade(client)), bg = "white", justify = LEFT)
		label_project_decsription_static = Label(frame, text = "Decsription: " + self.profile_project["desc"], bg = "white")
		label_project_max_pay_static = Label(frame, text = "Client's Maximum Offer: $" + str(log[0][2]), bg = "white")
		label_project_submission_date_static = Label(frame, text = "Client's Max Due Date: " + log[0][3], bg = "white")
		button_back = Button(frame, text = "Back", bg = "red")
		button_back.bind("<Button-1>", self.back_button)
		
		label_project_name_static.grid(row = 1, column = 0, sticky = W)
		label_project_client_name_static.grid(row = 2, column = 0, sticky = W)
		label_project_client_grade_static.grid(row = 2, column = 1, sticky = W)
		label_project_decsription_static.grid(row = 3, column = 0, sticky = W)
		label_project_max_pay_static.grid(row = 4, column = 0, sticky = W)
		label_project_submission_date_static.grid(row = 5, column = 0, sticky = W)
		button_back.grid(row = 1, column = 1, sticky = W)
		
		button_create = Button(self.frame_make_team, text = "Create Bid", bg = color )
		button_create.bind("<Button-1>", self.create_button_bid)
		label_money = Label(self.frame_make_team, text = "Maximum Payment Offer", bg = color)
		label_date = Label(self.frame_make_team, text = "Maximum Days Of Work Offer", bg = color)
		label_text = Label(self.frame_make_team, text = "Enter info on how much you wish to bet", bg = color)
		
		self.entry_money = Entry(self.frame_make_team)
		self.entry_time =Entry(self.frame_make_team)
		self.frame_make_team.grid(row = 1, column = 0, sticky = S+E+N+W)
		frame.grid(row = 0, column = 0, columnspan = 2)

		label_money.grid(row = 3, column = 0, sticky = W)
		self.entry_money.grid(row = 3, column = 1, sticky = W)
		label_date.grid(row = 4, column = 0, sticky = W)
		self.entry_time.grid(row = 4, column = 1, sticky = W)
		button_create.grid(row = 5, columnspan = 2, column = 0, sticky = E+W, pady = 5)
	   
	   
	   
	   
	def set_up_search(self, matches):
		self.frame_profile.destroy()
		color = "white"
		self.profile_type = 3
		self.frame_profile = Frame(self.origin)
		self.frame_profile.grid(row = 1, column = 0, sticky = S+E+W+N)
		frame = Frame(self.frame_profile, bg = color)
		frame.grid(row = 0, column = 0, sticky = S+E+W+N)
		if self.v.get() == 0:
			label_name = Label(frame, text = "User Name", bg = color).grid(row = 0, column = 0, padx = 40, sticky =E+W)
			label_grade = Label(frame, text = "Grade", bg = color).grid(row = 0, column = 1, padx = 40, sticky =E+W)
			label_type = Label(frame, text = "User Type", bg = color).grid(row = 0, column = 2, padx = 40, sticky =E+W)
			label_team = Label(frame, text = "Team", bg = color).grid(row = 0, column = 3, padx = 40, sticky =E+W)
			self.set_up_search_lists(self.frame_profile, matches,self.set_up_user_search)
		elif self.v.get() == 1: 
			label_name = Label(frame, text = "Team Name", bg = color).grid(row = 0, column = 0, padx = 40, sticky =E+W)
			label_grade = Label(frame, text = "Grade", bg = color).grid(row = 0, column = 1, padx = 40, sticky =E+W)
			label_members = Label(frame, text = "Member Count", bg = color).grid(row = 0, column = 2, padx = 40, sticky =E+W)
			self.set_up_search_lists(self.frame_profile, matches,self.set_up_team_search)
		else:
			label_name = Label(frame, text = "Project Name", bg = color).grid(row = 0, column = 0, padx = 40, sticky =E+W)
			label_status = Label(frame, text = "Status", bg = color).grid(row = 0, column = 1, padx = 40, sticky =E+W)
			label_client_name = Label(frame, text = "Client Name", bg = color).grid(row = 0, column = 2, padx = 40, sticky =E+W)
			label_client_grade = Label(frame, text = "Client Grade Average", bg = color).grid(row = 0, column = 3, padx = 40, sticky =E+W)
			self.set_up_search_lists(self.frame_profile, matches,self.set_up_project_search)
			
	def set_up_user_search(self, Row , id):
		if Row%2 == 0:
			color =  "white"
		else: 
			color = "#C3CBDE"
		user = ez.get_row(User(), id)
		frame = Frame(self.frame_profile, bg = color)
		frame.grid(row = Row, column = 0, sticky = S+E+W+N, pady = 2)
		button_name = Button(frame, text = user['name'], bg = color, justify = LEFT)
		button_name.grid(row = 0, column = 0, padx = 40, sticky =E+W)
		label_grade = Label(frame, text = ez.get_grade(user), bg = color, justify = LEFT).grid(row = 0, column = 1, padx = 40, sticky =E+W)
		label_type = Label(frame, text = user['user_type'].title(), bg = color, justify = LEFT).grid(row = 0, column = 2, padx = 40, sticky =E+W)
		if user['team_id'] != "Nan":
			team = get_row("team_db", user["team_id"])
			label_team = Label(frame, text = team["name"], bg = color, justify = LEFT).grid(row = 0, column = 3, padx = 40, sticky =E+W)
		else:
			label_team = Label(frame, text = "N/A", bg = color, justify = LEFT).grid(row = 0, column = 3, padx = 40, sticky =E+W)
			
		button_name.bind("<Button-1>", lambda event, arg = user: self.profile_button(event, arg))
		   
	def set_up_team_search(self, Row, id):
		if Row%2 == 0:
			color =  "white"
		else: 
			color = "#C3CBDE"
		team = get_row("team_db", id)
		frame = Frame(self.frame_profile, bg = color)
		frame.grid(row = Row, column = 0, sticky = S+E+W+N)
		button_name = Button(frame, text = team["name"], bg = color, justify = LEFT)
		button_name.grid(row = 0, column = 0, padx = 40, sticky =E+W)
		label_grade = Label(frame, text = ez.get_grade(team), bg = color, justify = LEFT).grid(row = 0, column = 1, padx = 40, sticky =E+W)
		label_members = Label(frame, text = len(team['dev_ids']), bg = color, justify = LEFT).grid(row = 0, column = 2, padx = 40, sticky =E+W)
		
		button_name.bind("<Button-1>", lambda event, arg = team: self.team_button(event, arg))
		
	def set_up_project_search(self, Row, id):
		if Row%2 == 0:
			color =  "white"
		else: 
			color = "#C3CBDE"
		project = get_row("project_db", id)
		frame = Frame(self.frame_profile, bg = color)
		frame.grid(row = Row, column = 0, sticky = S+E+W+N)
		button_name = Button(frame, text = project['title'], bg = color, justify = LEFT)
		button_name.grid(row = 0, column = 0, padx = 40, sticky =E+W)
		label_status = Label(frame, text = project['status'], bg = color, justify = LEFT).grid(row = 0, column = 1, padx = 40, sticky =E+W)
		user = get_row("user_db", project['client_id'])
		label_client_name = Label(frame, text = user['name'], bg = color, justify = LEFT).grid(row = 0, column = 2, padx = 40, sticky =E+W)
		label_client_grade = Label(frame, text = ez.get_grade(user), bg = color, justify = LEFT).grid(row = 0, column = 3, padx = 40, sticky =E+W)
		
		button_name.bind("<Button-1>", lambda event, arg = id: self.project_button(event, arg))
		
	def set_up_search_lists(self, frame, list, function):
		page_amount = math.ceil((len(list))/10)
		print(len(list))
		if page_amount == 0:
			frame_no = Frame(self.frame_profile, bg = "#C3CBDE")
			frame_no.grid(row = 1, column = 0, sticky = S+E+W+N)
			label_no = Label(frame_no, text = "No Result", bg = "#C3CBDE").grid(row = 1, column = 0, sticky = E+W)
			page_amount = 1 
		amount = 0
		n = 1
		Index = self.project_index
		if len(list)-Index >= 10:
			amount = 10*(int((self.project_index/10))+1)
		else:
			amount = len(list)
		while(Index < amount):
			function(Index+1, list[Index])
			n += 1
			Index = Index + 1
		
		self.set_up_project_scroll(frame, int((self.project_index/10))+1, page_amount) 
	
	
	
	def set_up_super_user(self):
		self.frame_profile.destroy()
		self.frame_profile = Frame(self.origin, bg = "white")
		self.frame_current = self.frame_profile
		self.profile_type = 4
	
		button_accepts = Button (self.frame_profile, text = "Resolve Temp Status") #0
		button_dispute_warning = Button (self.frame_profile, text = "Resolve Warning Dispute") #1
		button_quit_req = Button (self.frame_profile, text = "Resolve Quit Request") #2
		button_blacklist = Button (self.frame_profile, text = "Resolve Blacklist Remove") #3
		button_grade = Button (self.frame_profile, text = "Resolve Grade-Payment") #4
		
		button_accepts.bind("<Button-1>",self.button_accepts_screen)
		button_dispute_warning.bind("<Button-1>",self.button_dispute_warning_screen)
		button_quit_req.bind("<Button-1>",self.button_quit_req_screen)
		button_blacklist.bind("<Button-1>",self.button_blacklist_screen)
		button_grade.bind("<Button-1>",self.button_grade_screen)
		
		self.frame_profile.grid(row = 1, column = 0)
		button_accepts.grid(row = 0, column = 0)
		button_dispute_warning.grid(row = 0, column = 1)
		button_quit_req.grid(row = 0, column = 2)
		button_blacklist.grid(row = 0, column = 3)
		button_grade.grid(row = 0, column = 4)
		print(self.SU_state)
		if self.SU_state == 0: 
			label_title = Label(self.frame_profile, text = "Resolve Temp Status Page")
			matches = ez.search_matches(Issue(), "new user")
		elif self.SU_state == 1:
			label_title = Label(self.frame_profile, text = "Resolve Warning Dispute Page")
			matches = ez.search_matches(Issue(), "warning")
		elif self.SU_state == 2:
			label_title = Label(self.frame_profile, text = "Resolve Quit Request Page")
			matches = ez.search_matches(Issue(), "quit")
		elif self.SU_state == 3:
			label_title = Label(self.frame_profile, text = "Resolve Blacklist Remove Page")
			matches = ez.search_matches(Issue(), "blacklisted")
		elif self.SU_state == 4:
			label_title = Label(self.frame_profile, text = "Resolve Grade-Payment Page")
			matches = ez.search_matches(Issue(), "payment")
		self.set_up_SU_pages( self.frame_profile, matches)
		label_title.grid(row = 1, column = 0, columnspan = 5, sticky = E+W)
	
	def set_up_SU_pages(self, frame, list):
		page_amount = math.ceil((len(list))/3)
		if page_amount == 0:
			label_no_issue = Label(frame, text = "No Issues Found")
			label_no_issue.grid(row = 2, column = 0, columnspan = 5, sticky = E+W )
			page_amount = 1 
		amount = 0
		n = 0
		Index = self.project_index
		if len(list)-Index >= 3:
			amount = 3*(int((self.project_index/3))+1)
		else:
			amount = len(list)
		while(Index < amount):
			if self.SU_state >= 0 and self.SU_state < 4:
				self.set_up_SU_generic(self.frame_profile, n+2, list[Index])
			elif self.SU_state == 4:
				self.set_up_SU_payment(self.frame_profile, n+2, list[Index])
			n += 1
			Index = Index + 1
		
		self.set_up_project_scroll(frame, int((self.project_index/3))+1, page_amount)
	
	def set_up_SU_generic(self, frame_pass, Row, id):
		statments = ["Temp user wishes to be part of the Turk System", "This user belvies they unfarily were given a warning and want it removed", 
				 "This user wishes to quit out of The Turk System", "This user is about to be placed on the Blacklist and ask you to stop this action"]
		frame = Frame(frame_pass, bg =  self.colors[1], pady = 6)
		frame.grid(row = Row, column = 0, pady = 6, columnspan = 5)
		
		issue = get_row("issue_db", id)
		user = get_row("user_db",issue['referred_id'])
		
		dictonries = [issue, user]
		
		profile_button = Button(frame, text = user['name'], bg =  self.colors[1])
		profile_button.bind("<Button-1>", lambda event, arg = user: self.profile_button(event, arg))
		self.text_reason = Text(frame, height=3, width=30)
		label_reason = Label(frame, text = "Why did you choose this option?", bg =  self.colors[1])
		label_type = Label(frame, text = user["user_type"], bg =  self.colors[1])
		label_message = Label(frame, text =  statments[self.SU_state] + ",are you going to accept or reject their request?", bg =  self.colors[1])
		accept_button = Button(frame, text = "Accept", bg =  "green")
		reject_button = Button(frame, text = "Reject", bg =  "red")
		accept_button.bind("<Button-1>", lambda event, arg = dictonries: self.SU_generic_choice_accept(event, arg))
		reject_button.bind("<Button-1>", lambda event, arg = dictonries: self.SU_generic_choice_reject(event, arg))
		
		profile_button.grid(row = 0, column = 0)
		label_type.grid(row = 0, column = 1)
		label_message.grid(row = 1, column = 0, columnspan = 2)
		label_reason.grid(row = 2, column = 0)
		self.text_reason.grid(row = 2, column = 1)
		accept_button.grid(row = 3, column = 0)
		reject_button.grid(row = 3, column = 1)
	
	def set_up_SU_payment(self, frame_pass, Row, id):
			
		frame = Frame(frame_pass, bg =  self.colors[1], pady = 6)
		frame.grid(row = Row, column = 0, pady = 6, columnspan = 5)
		issue = get_row("issue_db", id)
		project = get_row("project_db",issue['referred_id'])
		bid = get_row("bid_db", issue['referred_id'])
		log = ez.get_bid_log(issue['referred_id'])
		client = get_row("user_db", project["client_id"])
		dev = get_row("user_db", log[bid['chosen_index']][1])
		if dev['team_id'] == "Nan":
			name = dev['name']
		else:
			team = get_row("team_db", dev['team_id'])
			name = team['name']
		
		button_client = Button(frame, text = "Client: " + client['name'], bg =  self.colors[1])
		button_dev = Button(frame, text = "Developer: " + name, bg =  self.colors[1])
		button_project = Button(frame, text = "Project: " + project["title"], bg =  self.colors[1])
		label_message =  Label(frame, text = "Client ," +client['name'] + ", has graded the efforts of " + name + " with the grade of " + str(project["team_rating"]) + " after disscussing the with both parites, what would be the amount that " + name + " recives?", bg =  self.colors[1])
		label_was_supposed_to = Label(frame, text =  name + " was suppposed to recive $" + str(log[bid["chosen_index"]][2]/2), bg =  self.colors[1])
		self.entry_new_payment = Entry(frame)
		self.entry_new_payment.grid(row = 2, column = 2)
		accept_button = Button(frame, text = "Accept", bg =  "green")
		#accept_button.bind("<Button-1>", lambda event, arg = dictonries: self.SU_generic_choice_accept(event, arg))
		
		
		button_client.grid(row = 1, column = 1, padx = 2)
		button_dev.grid(row = 1, column = 2, padx = 2)
		button_project.grid(row = 1, column = 3, padx = 2)
		
		label_message.grid(row = 0, column = 0, columnspan = 4)
		label_was_supposed_to.grid(row = 2, column = 0)
		accept_button.grid(row = 2, column = 3)
		
		
		
	
	def set_up_profile(self):
		self.frame_profile.destroy()
		self.frame_profile = Frame(self.origin, bg = "#C3CBDE")
		self.frame_current = self.frame_profile
		
		self.profile_type = 0
		self.set_up_profile_image(self.profile_user)
		self.set_up_user_profile_basic_info()
		if self.logged_in_user["id"] == self.profile_user["id"]:
			self.set_up_user_profile_logged_in_info()
		
		page_amount = self.set_up_projects(frame = self.frame_current, profile= self.profile_user, current_page= int((self.project_index/3))+1)
		self.set_up_project_scroll(self.frame_profile, int((self.project_index/3))+1, page_amount)
		self.frame_profile.grid(row = 1, column = 0, sticky = S+N+E+W)
	
	def set_up_user_profile_basic_info(self):
		color = "#C3CBDE"
		frame_basic_info = Frame(self.frame_profile, bg = color)
		frame_resume = Frame(self.frame_profile, bg = "white")
		button_edit = Button(frame_basic_info, text = "Edit", bg = color, cursor = "hand2")
		button_save = Button(frame_basic_info, text = "Save", bg = color, cursor = "hand2")
		button_cancel = Button(frame_basic_info, text = "Cancel", bg = color, cursor = "hand2")
		button_create_team = Button(frame_basic_info, text = "Create Team", bg = color, cursor = "hand2")
		label_name = Label(frame_basic_info, text = "Name", bg = color)
		label_users_name = Label(frame_basic_info, text = self.profile_user["name"], bg = color)
		if(self.profile_user["user_type"] == "dev"):
			type = "Developer"
		else:
			type = self.profile_user["user_type"]
		label_type = Label(frame_basic_info, text = type.title() + " - " + self.profile_user["status"].title(), bg = color)
		label_resume_name = Label(frame_resume, text = "Resume")
		label_resume = Label(frame_resume, text = self.profile_user["resume"], bg = "white", wraplength = 400, justify = LEFT)
		
		if ez.is_in_active_project(self.profile_user) :
			id = self.profile_user["project_ids"][len(self.profile_user["project_ids"]) - 1]
			project = get_row("project_db", id)
			label_active_project = Button(frame_basic_info, text = "Active Project: " + project["title"], bg = color, cursor = "hand2")
			label_active_project.bind("<Button-1>", lambda event, arg =  id: self.project_button(event, id))
		else: 
			label_active_project = Label(frame_basic_info, text = "No Active Project", bg = color)
	
		grade = ez.get_grade(self.profile_user)
		label_grade = Label(frame_basic_info, text =  "Grade: " + str(grade), bg = color)
		
		if self.profile_user["user_type"] == "dev":
			if self.profile_user["team_id"] == "Nan":
				label_team = Label(frame_basic_info, text = "Team: N/A", bg = color)
			else:
				team = get_row("team_db", self.profile_user["team_id"])
				label_team = Button(frame_basic_info, text = "Team: " + team["name"], bg = color, wraplength = 150, cursor = "hand2")
				label_team.bind("<Button-1>", lambda event, arg =  team: self.team_button(event, team))
			label_team.grid(row = 3, column = 0, sticky = W)
			

		label_users_bio = Label(frame_basic_info, text = self.profile_user["interests"], bg = color)
		label_biography = Label(frame_basic_info, text = "Interest", bg = color, )
		label_projects_complete = Label(frame_basic_info, text = "Projects Completed: " + str(len(self.profile_user["project_ids"])), bg = color)
		
		if self.proflie_state != 1:
			label_users_name.grid(row = 1, column = 1, sticky = W)
			label_users_bio.grid(row = 5, column = 1, sticky = W)
			label_resume.grid(row = 1, column = 0, sticky = W+E)
		else:
			
			self.profile_name_entry = Entry(frame_basic_info)
			self.proflie_bio_entry = Text(frame_basic_info, height=2, width=30)
			scroll = Scrollbar(frame_basic_info)
			scroll.config(command=self.proflie_bio_entry.yview)
			self.proflie_bio_entry.config(yscrollcommand=scroll.set)
		
			self.proflie_resume_text_box = Text(frame_resume, height=30, width=50)
			scroll_two = Scrollbar(frame_resume)
			scroll.config(command=self.proflie_resume_text_box.yview)
			self.proflie_bio_entry.config(yscrollcommand=scroll_two.set)
			self.profile_name_entry.insert(0, self.logged_in_user["name"])
			self.proflie_bio_entry.insert(END, self.logged_in_user["interests"])
			self.proflie_resume_text_box.insert(END, self.logged_in_user["resume"])
			
			self.profile_name_entry.grid(row = 1, column = 1)
			self.proflie_bio_entry.grid(row = 5, column = 1)
			self.proflie_resume_text_box.grid(row = 1, column = 0, sticky = W+E)
			
		if self.logged_in_user["id"] == self.profile_user["id"]:
			if self.proflie_state == 0 :
				button_edit.grid(row = 0, column = 2, sticky = E)
				if self.logged_in_user['user_type'] == "dev" and self.logged_in_user["team_id"] == "Nan" and self.logged_in_user['status'] == "active":
					button_create_team.grid(row = 3, column = 1) 
					button_create_team.bind("<Button-1>", self.set_up_new_team)
			elif self.proflie_state == 1:
				button_save.grid(row = 0, column = 2, sticky = E)
				button_cancel.grid(row = 0, column = 3, sticky = E)
				
				
		button_edit.bind("<Button-1>", self.edit_button)
		button_save.bind("<Button-1>", self.save_button)
		button_cancel.bind("<Button-1>", self.cancel_button)
				
		frame_basic_info.grid(row = 0, column = 1, sticky = N+E+W+S)
		frame_resume.grid(row = 0, column = 2, sticky = N+S+E+W, rowspan = 20)
		label_resume.grid(row = 1, column = 0, sticky = W+E)
		label_resume_name.grid(row = 0, column = 0, sticky = W+E)
		label_type.grid(row = 0, column = 0, sticky = W)
		label_name.grid(row = 1, column = 0, sticky = W)
		label_grade.grid(row = 2, column = 0, sticky = W)
		label_projects_complete.grid(row = 4, column = 0, sticky = W)
		label_biography.grid(row = 5, column = 0, sticky = W)
		label_active_project.grid(row = 6, column = 0, sticky = W)
		
	def set_up_user_profile_logged_in_info(self):
		color = "#C3CBDE"
		frame_logged_in = Frame(self.frame_profile, bg = color)
		button_cancel = Button(frame_logged_in, text = "Cancel", bg = color, cursor = "hand2")
		button_dispute = Button(frame_logged_in, text = "Dispute", bg = color,  cursor = "hand2")
		button_deposit = Button(frame_logged_in, text = "Deposit ", bg = color, cursor = "hand2")
		button_withdraw = Button(frame_logged_in, text = "Withdraw", bg = color, cursor = "hand2")
		button_deposit_submit = Button(frame_logged_in, text = "Deposit ", bg = color, cursor = "hand2")
		button_withdraw_submit = Button(frame_logged_in, text = "Withdraw", bg = color, cursor = "hand2")
		button_quit = Button(frame_logged_in, text = "Request Quit", bg = color, cursor = "hand2")
		button_create_new_project = Button(frame_logged_in, text = "Create New Project ", bg = color, cursor = "hand2")
		self.profile_username_entry = Entry(frame_logged_in)
		self.profile_password_entry = Entry(frame_logged_in)
		self.profile_cash_amount_entry = Entry(frame_logged_in)
		self.profile_username_entry.insert(0, self.logged_in_user["username"])
		self.profile_password_entry.insert(0, self.logged_in_user["password"])
		label_users_username = Label(frame_logged_in, text = self.logged_in_user["username"], bg = color)
		label_username = Label(frame_logged_in, text = "Username:", bg = color)
		label_users_password = Label(frame_logged_in, text = self.logged_in_user["password"], bg = color)
		label_password = Label(frame_logged_in, text = "Password:", bg = color)
		label_bank = Label(frame_logged_in, text = "Bank: $" + str(self.logged_in_user["balance"]), bg = color)
		label_warnings = Label(frame_logged_in, text = "Warnings: " + str(self.logged_in_user["warning"]), bg = color)
			
		button_cancel.bind("<Button-1>", self.cancel_button)
		button_withdraw.bind("<Button-1>", self.withdraw_button)
		button_withdraw_submit.bind("<Button-1>", self.withdraw_accept_button)
		button_deposit.bind("<Button-1>", self.deposit_button)
		button_deposit_submit.bind("<Button-1>", self.deposit_accept_button)
			
		if self.logged_in_user["warning"] > 0 : 
			button_dispute.config(state = NORMAL)
		elif self.logged_in_user["warning"] > 0 and self.logged_in_user.get_dispute_status: 
			button_dispute.config(state = DISABLED, cursor = 'arrow')
		else:
			button_dispute.config(state = DISABLED, cursor = 'arrow')
			
		if self.logged_in_user["balance"] <= 0:
			button_withdraw.config(state = DISABLED)
		
		
		#Need way to show that they requested to quit from system 
		###############
		#if self.logged_in_user.get_quit_status():
			#button_quit.config(state = DISABLED, cursor = 'arrow')
		#else:
			#button_quit.bind("<Button-1>", self.quit_button)
		#################
		
		frame_logged_in.grid(row = 1, column = 0, sticky =S+E+N+W)
		label_username.grid(row = 0, column = 0, sticky = W)
		label_users_username.grid(row = 0, column = 1, sticky = W)
		label_password.grid(row = 1, column = 0, sticky = W)
		label_bank.grid(row = 2, column = 0, sticky = W)
		label_warnings.grid(row = 3, column = 0, sticky = W)
			
		if self.proflie_state == 0:
			label_users_password.grid(row = 1, column = 1, sticky = W)
			button_deposit.grid(row = 2, column = 1)
			button_withdraw.grid(row = 2, column = 2)
			button_dispute.grid(row = 3, column = 1)
			button_quit.grid(row = 4, column = 0)
			if self.profile_user["user_type"] == "client" and self.profile_user["status"] == "active" and (not ez.is_in_active_project(self.profile_user)): #and self.profile_user["active_project_id"] = "Nan
				button_create_new_project.bind("<Button-1>",self.set_up_new_project)
				button_create_new_project.grid(row = 7, column = 3, sticky = E+W)
		elif self.proflie_state == 1:
			self.profile_password_entry.grid(row = 1, column = 1, sticky = W)
		elif self.proflie_state == 2:
			self.profile_cash_amount_entry.grid(row = 2, column = 1)
			button_withdraw_submit.grid(row = 2, column = 2)
			button_cancel.grid(row = 2, column = 3, sticky = E)
		elif self.proflie_state == 3:
			self.profile_cash_amount_entry.grid(row = 2, column = 1)
			button_deposit_submit.grid(row = 2, column = 2)
			button_cancel.grid(row = 2, column = 3, sticky = E)


	def set_up_team_profile(self):
		self.frame_profile.destroy()
		self.frame_profile = Frame(self.origin, bg = "#C3CBDE")
		self.frame_current = self.frame_profile
		
		self.profile_type = 1
		self.set_up_team_profile_basic_info()
		self.set_up_profile_image(self.profile_team)
		

		frame_members = Frame(self.frame_profile, bg = "white")
		frame_admins = Frame(self.frame_profile, bg = "white")
		frame_requests = Frame(self.frame_profile, bg = "white")
		label_members = Label(frame_members, text = "Members", bg = "white")
		label_admins = Label(frame_admins, text = "Administrators", bg = "white")
		label_requests = Label(frame_requests, text = "Join Requests" , bg = "white")
		
		self.set_up_team_lists(frame_members, self.profile_team['dev_ids'], 0)
		self.set_up_team_lists(frame_admins, self.profile_team['admin_ids'], 1)
		if self.logged_in_user["team_id"] == self.profile_team['id'] and ez.is_admin(self.logged_in_user):
			self.set_up_team_lists(frame_requests, self.profile_team['join_request_ids'], 2)
			label_requests.grid(row = 0, column = 0, sticky = E+W)
			frame_requests.grid(row = 0, column = 4, sticky = S+N+E+W, rowspan = 40, padx = 5)
			
			
		page_amount = self.set_up_projects(frame = self.frame_profile, profile= self.profile_team, current_page= int((self.project_index/3))+1)
		self.set_up_project_scroll(self.frame_profile, int((self.project_index/3))+1, page_amount)
		label_members.grid(row = 0, column = 0, sticky = E+W)
		label_admins.grid(row = 0, column = 0, sticky = E+W)
		frame_members.grid(row = 0, column = 2, sticky = S+N+E+W, rowspan = 40, padx = 5)
		frame_admins.grid(row = 0, column = 3, sticky = S+N+E+W, rowspan = 40, padx = 5)
		self.frame_profile.grid(row = 1, column = 0, sticky = S+N+E+W)
		
	def set_up_team_lists(self, frame, list, frame_num):
		page_amount = math.ceil((len(list))/10)
		if page_amount == 0:
			page_amount = 1 
		amount = 0
		n = 1
		Index = self.project_index
		if len(list)-Index >= 10:
			amount = 10
		else:
			amount = len(list)
		while(Index < amount):
			self.set_up_member_lists(frame, list[Index], frame_num, n)
			n += 1
			Index = Index + 1
		
		self.set_up_project_scroll(frame, int((self.project_index/10))+1, page_amount)
		
	def set_up_team_profile_basic_info(self):
		color = "#C3CBDE"
		frame_basic_info = Frame(self.frame_profile, bg = color)
		label_name_static = Label(frame_basic_info, text = "Name: ", bg = color)
		label_name = Label(frame_basic_info, text = self.profile_team['name'], bg = color)
		label_description_static = Label(frame_basic_info, text = "Description: ", bg = color)
		label_description = Label(frame_basic_info, text = self.profile_team["desc"], bg = color)
		button_edit = Button(frame_basic_info, text = "Edit", bg = color, cursor = "hand2")
		button_save = Button(frame_basic_info, text = "Save", bg = color, cursor = "hand2")
		button_cancel = Button(frame_basic_info, text = "Cancel", bg = color, cursor = "hand2")
		button_request_join = Button(frame_basic_info, text = "Request Join", bg = color, cursor = "hand2")
		button_quit_team = Button(frame_basic_info, text = "Quit Team", bg = color, cursor = "hand2")
		button_disband_team = Button(frame_basic_info, text = "Disband Team", bg = color, cursor = "hand2")
		self.profile_name_entry = Entry(frame_basic_info)
		self.profile_name_entry = Entry(frame_basic_info)
		self.proflie_bio_entry = Text(frame_basic_info, height=2, width=30)
		scroll = Scrollbar(frame_basic_info)
		scroll.config(command=self.proflie_bio_entry.yview)
		self.proflie_bio_entry.config(yscrollcommand=scroll.set)
		self.profile_name_entry.insert(0, self.profile_team['name'])
		self.proflie_bio_entry.insert(END, self.profile_team["desc"])
		
		if ez.is_in_active_project(self.profile_team):
			id = self.profile_team["project_ids"][len(self.profile_team["project_ids"]) - 1]
			project = get_row("project_db", id)
			label_active_project = Label(frame_basic_info, text = "Active Project: " + project["title"], bg = color, cursor = "hand2")
			label_active_project.bind("<Button-1>", lambda event, arg =  id: self.project_button(event, id))
		else: 
			label_active_project = Label(frame_basic_info, text = "No Active Project", bg = color)
		
		if self.proflie_state != 1:
			label_name.grid(row = 1, column = 1, sticky = W)
			label_description.grid(row = 2, column = 1, sticky = W)
		else:
			self.profile_name_entry.grid(row = 1, column = 1)
			self.proflie_bio_entry.grid(row = 2, column = 1)
		if self.logged_in_user["team_id"] == self.profile_team['id']:
			if self.proflie_state == 0 :
				if ez.is_admin(self.logged_in_user):
					button_edit.grid(row = 0, column = 2, sticky = E)
				button_quit_team.grid(row = 3, column = 2)
			elif self.proflie_state == 1:
				button_save.grid(row = 0, column = 2, sticky = E)
				button_cancel.grid(row = 0, column = 3, sticky = E)
				button_disband_team.grid(row = 3, column = 3)
		elif self.logged_in_user["team_id"] == "Nan"  and self.logged_in_user["user_type"] == "dev":
			button_request_join.grid(row = 0, column = 2, sticky = E)
			button_request_join.bind("<Button-1>", lambda event, arg = self.logged_in_user["id"]: self.request_join_team_button(event, arg))

		
		button_edit.bind("<Button-1>", self.edit_button)
		button_save.bind("<Button-1>", self.save_button)
		button_cancel.bind("<Button-1>", self.cancel_button)
		
		label_active_project.grid(row = 3, column = 0, sticky = W)
		label_name_static.grid(row = 1, column = 0, sticky = W)
		label_description_static.grid(row = 2, column = 0, sticky = W)
		frame_basic_info.grid(row = 0, column = 1)

	def set_up_member_lists(self, frame, id, frame_num, Row):
		if Row%2 == 0:
			color = "#C3CBDE"
		else: 
			color = "white"
		user = get_row("user_db",id)
		button_demote_team = Button(frame, text = "Demote", bg = color, cursor = "hand2")
		button_kick_team = Button(frame, text = "Kick", bg = color, cursor = "hand2")
		button_promote_team = Button(frame, text = "Promote", bg = color, cursor = "hand2")
		button_accept = Button(frame, text = "Accept", bg = color, cursor = "hand2")
		button_reject = Button(frame, text = "Reject", bg = color, cursor = "hand2")
		label_name = Label(frame, text = user['name'], bg = color, cursor = "hand2")
		label_grade = Label(frame,text = ez.get_grade(user), bg = color, cursor = "hand2")
		
		if self.logged_in_user["team_id"] == self.profile_team["id"] and ez.is_admin(self.logged_in_user) and user['id'] != self.logged_in_user["id"]:
			if frame_num == 0:
				button_kick_team.grid(row = Row, column = 3, sticky = W+E)
				button_kick_team.bind("<Button-1>", lambda event, arg = id: self.kick_button(event, arg))
				if not ez.is_admin(user):
					button_promote_team.grid(row = Row, column = 2, sticky = W+E)
					button_promote_team.bind("<Button-1>", lambda event, arg = id: self.promote_button(event, arg))
			elif frame_num == 1:
				button_demote_team.grid(row = Row, column = 2, sticky = W+E)
				button_kick_team.grid(row = Row, column = 3, sticky = W+E)
				button_kick_team.bind("<Button-1>", lambda event, arg = id: self.kick_button(event, arg))
				button_demote_team.bind("<Button-1>", lambda event, arg = id: self.demote_button(event, arg))
			else:
				button_accept.grid(row = Row, column = 2, sticky = W+E)
				button_accept.bind("<Button-1>", lambda event, arg = id: self.accept_team_button(event, arg))
				button_reject.bind("<Button-1>", lambda event, arg = id: self.reject_team_button(event, arg))
				button_reject.grid(row = Row, column = 3, sticky = W+E)
		
		label_name.bind("<Button-1>", lambda event, arg = user: self.profile_button(event, arg))
		
		label_name.grid(row = Row, column = 0, sticky = W+E, pady = 5)
		label_grade.grid(row = Row, column = 1, sticky = W+E)

	def set_up_project_profile(self):
		self.profile_type = 2
		self.frame_profile.destroy()
		self.frame_profile = Frame(self.origin, bg = "#C3CBDE")
		self.frame_current = self.frame_profile
		frame_title = Frame(self.frame_profile)
		frame_info = Frame(self.frame_profile, bg = "white")
		label_title = Label(frame_title, text = "Project and Client Info:")
		
		client = get_row("user_db", self.profile_project["client_id"])
		bid = get_row("bid_db", self.profile_project['id'])
		log = bid["bid_log"]
		
		if self.profile_project["status"] == "bidding":
			frame_bid_title = Frame(self.frame_profile)
			label_bid_title = Label(frame_bid_title, text = "Bidding ends: " + self.profile_project["bid_end_date"] + " | " + "Placed Bids: ")
			frame_bids = Frame(self.frame_profile, bg = "white")
			frame_bid_title.grid(row = 1, column = 1, sticky = S+N+E+W, padx = 5)
			label_bid_title.grid(row = 0, column = 0, sticky = S+N+E+W)
			frame_bids.grid(row = 2, column = 1, sticky = S+N+E+W, padx = 5)
			if self.logged_in_user['user_type'] == "dev":
				if ez.is_admin(self.logged_in_user) or self.logged_in_user["team_id"] == "Nan":
					bid_button = Button(frame_bid_title, text = "Make a Bid")
				elif self.logged_in_user["team_id"] != "Nan":
					bid_button = Button(frame_bid_title, text = "Make a Bid", state=DISABLED)
				bid_button.grid(row = 0, column = 1)
				bid_button.bind("<Button-1>", self.set_up_new_bid)
			self.set_up_bids(frame_bids, log)
		elif self.profile_project["status"] == "no bid":
			frame_winner =  Frame(self.frame_profile, bg = self.colors[1])
			label_lose = Label(frame_winner, text = "This project recived no bids \nProject Status: Closed")
			frame_winner.grid(row = 1, column = 1, sticky = S+N+E+W, padx = 5)
			label_lose.grid(row = 2, column = 0, sticky = W)
		else:
			frame_winner =  Frame(self.frame_profile, bg = self.colors[1])
			dev = get_row("user_db", log[bid["chosen_index"]][1])
			
			label_win = Label(frame_winner, text = "Congratulatons\nReason:" + bid["client_review"] +"\nProject Status: Active")
			
			if ez.is_admin(dev):
				team = get_row("team_db",  dev["team_id"])
				label_dev_name = Label(frame_winner, text ="Team: " + team['name'], bg = self.colors[1])
			else: 
				label_dev_name = Label(frame_winner, text = "Developer: " + dev["name"], bg = self.colors[1])
			label_bid_offer = Label(frame_winner, text = "Payment Offer: $"+str(log[bid['chosen_index']][2]), bg = self.colors[1])
			label_time_offer = Label(frame_winner, text = "Sumbission Date Offer: " + log[bid['chosen_index']][3], bg = self.colors[1])
			
			frame_winner.grid(row = 1, column = 1, sticky = S+N+E+W, padx = 5)
			
			label_dev_name.grid(row = 3, column = 0, sticky = W)
			label_bid_offer.grid(row = 4, column = 0, sticky = W)
			label_time_offer.grid(row = 5, column = 0, sticky = W)
			if self.profile_project["status"] == "active" and dev['team_id'] == self.logged_in_user['team_id']:
				if ez.is_admin(self.logged_in_user) or self.logged_in_user["id"] == dev['id']:
					self.path_entry = Entry(frame_winner)
					self.path_entry.insert(0, self.path)
					self.path_entry.grid(row = 6, column = 0, sticky =E+W)
					find_path_button = Button(frame_winner, text = "Find File")
					find_path_button.bind("<Button-1>", self.find_path)
					find_path_button.grid(row = 6, column = 1, sticky =E+W)
					
					label_grade = Label(frame_winner, text = "Review Grade: ")
					label_review = Label(frame_winner, text = "Review: ")
					self.text_review = Text(frame_winner, height=2, width=30)
					self.entry_grade = Entry(frame_winner)
					label_grade.grid(row = 7, column = 2, sticky =E+W)
					self.entry_grade.grid(row = 7, column = 3, sticky =E+W)
					label_review.grid(row = 7, column = 0, sticky =E+W)
					self.text_review.grid(row = 7, column = 1, sticky =E+W)
					
					submit_button = Button(frame_winner, text = "Submit")
					submit_button.bind("<Button-1>", self.submit_file)
					submit_button.grid(row = 8, column = 4, sticky =E+W, padx = 5)
				elif self.logged_in_user["team_id"] != "Nan":
					submit_button = Button(frame_winner, text = "Submit", state=DISABLED)
			if self.profile_project["status"] == "submitted" and self.profile_project["client_id"] == self.logged_in_user['id']:
				label_grade = Label(frame_winner, text = "Review Grade: ")
				label_review = Label(frame_winner, text = "Review: ")
				self.text_review = Text(frame_winner, height=2, width=30)
				self.entry_grade = Entry(frame_winner)
				label_grade.grid(row = 6, column = 2, sticky =E+W)
				self.entry_grade.grid(row = 6, column = 3, sticky =E+W)
				label_review.grid(row = 6, column = 0, sticky =E+W)
				self.text_review.grid(row = 6, column = 1, sticky =E+W)
				submit_button = Button(frame_winner, text = "Claim")
				submit_button.grid(row = 7, column = 4, sticky =E+W)
				submit_button.bind("<Button-1>", self.claim)
			elif self.profile_project["status"] == "incomplete":
				label_win = Label(frame_winner, text = "Congratulatons\nReason:" + bid["client_review"] +"\nProject Status: Closed")
				label_fail = Label(frame_winner, text = "Team Failed To Sumbit Project", bg = self.colors[1])
				label_fail.grid(row = 6, column = 0, sticky = W)
				self.set_up_profile_projects(3, self.profile_project['id'])
			elif self.profile_project["status"] == "complete":
				label_win = Label(frame_winner, text = "Congratulatons\nReason:" + bid["client_review"] +"\nProject Status: Closed")
				self.set_up_profile_projects(3, self.profile_project['id'])
			
			label_win.grid(row = 2, column = 0, sticky = W)
			
		label_project_name_static = Label(frame_info, text = "Name: " + self.profile_project["title"], bg = "white")
		label_project_client_name_static = Label(frame_info, text = "Client Name: " + client["name"], bg = "white")
		label_project_client_grade_static = Label(frame_info, text = "Grade: " + str(ez.get_grade(client)), bg = "white")
		label_project_decsription_static = Label(frame_info, text = "Decsription: " + self.profile_project["desc"], bg = "white")
		label_project_max_pay_static = Label(frame_info, text = "Maximum Offer: $" + str(log[0][2]), bg = "white")
		label_project_submission_date_static = Label(frame_info, text = "Max Due Date: " + log[0][3], bg = "white")
		
		
		label_project_name_static.grid(row = 1, column = 0, sticky = W)
		label_project_client_name_static.grid(row = 2, column = 0, sticky = W)
		label_project_client_grade_static.grid(row = 2, column = 1, sticky = W)
		label_project_decsription_static.grid(row = 3, column = 0, sticky = W)
		label_project_max_pay_static.grid(row = 4, column = 0, sticky = W)
		label_project_submission_date_static.grid(row = 5, column = 0, sticky = W)
		frame_title.grid(row = 1, column = 0, sticky = S+N+E+W, padx = 5)
		label_title.grid(row = 0, column = 0, sticky = S+N+E+W)
		frame_info.grid(row = 2, column = 0, sticky = S+N+E+W, padx = 5)
		self.frame_profile.grid(row = 1, column = 0, sticky = S+N+E+W, columnspan = 10)

	def set_up_bids(self, frame, log):
		frame_profile_projects = Frame(frame)
		label_no_bids = Label(frame_profile_projects, text = "No Bids Placed")
		amount = 0 
		page_amount = math.ceil((len(log)-1)/5)
		Index = self.project_index
		if page_amount == 0:
			label_no_bids.grid(row = 0, column = 0)
			frame_profile_projects.grid(row = 2, column = 0, columnspan = 2, sticky = N+E+W+S)
			page_amount = 1
		elif (len(log)-1)-Index >= 5:
			amount = 5*(int((self.project_index/5))+1)
		else:
			amount = len(log)-1
		if page_amount != 0:
			list_id = []
			n = 0 
			while(n < (len(log)-1)):
				list_id.append(log[n+1])
				n += 1
			n = 0
			while(Index < amount):
				self.make_bids((n+1), list_id[Index], frame)
				n += 1
				Index = Index + 1
	
		self.set_up_project_scroll(frame, int((self.project_index/5))+1, page_amount)
	
	def make_bids(self, Row, indexed_log, frame):
		bid_frame = Frame(frame, bg = self.colors[1])
		
		if self.logged_in_user['id'] == self.profile_project["client_id"]:
			button_select = Button(bid_frame, text = "Pick", bg = self.colors[1])
			button_select.grid(row = Row, column = 1, sticky = E)
			array = [self.profile_project['id'], indexed_log[1]]
			button_select.bind("<Button-1>", lambda event, arg = array: self.choose_bid_button(event, arg))
			
		
		dev = get_row("user_db", indexed_log[1])
		if ez.is_admin(dev):
			team = get_row("team_db",  dev["team_id"])
			label_dev_name = Label(bid_frame, text ="Team: " + team['name'], bg = self.colors[1])
		else: 
			label_dev_name = Label(bid_frame, text = "Developer: " + dev["name"], bg = self.colors[1])
		label_bid_offer = Label(bid_frame, text = "Payment Offer: $"+str(indexed_log[2]), bg = self.colors[1])
		label_time_offer = Label(bid_frame, text = "Sumbission Date Offer: " + indexed_log[3], bg = self.colors[1])
		label_time_made = Label(bid_frame, text = "Date Bid Was Made: " + indexed_log[0], bg = self.colors[1])
		
		bid_frame.grid(row = Row, column = 0, pady= 3, columnspan = 2, sticky = E+W)
		label_dev_name.grid(row = 1, column = 0, sticky = W)
		label_bid_offer.grid(row = 2, column = 0, sticky = W)
		label_time_offer.grid(row = 3, column = 0, sticky = W)
		label_time_made.grid(row = 4, column = 0, sticky = W)
			

	def set_up_profile_image(self, profile):
		frame_image = Frame(self.frame_profile, bg = "#C3CBDE")
		if "user_type" in profile:
			image = PhotoImage(file = ez.get_pic(profile['id'], profile["user_type"]))
		else:
			image = PhotoImage(file = ez.get_pic(profile['id'], "user"))
		image = image.subsample(4,4)
		label_image = Label(frame_image, image = image)
		label_image.image = image
		button_upload = Button(frame_image, text = "Upload Photo", bg = "#C3CBDE", cursor = "hand2")
		
		if self.proflie_state == 1:
			button_upload.grid(row = 1, column = 0)
		
		frame_image.grid(row = 0, column = 0)
		label_image.grid(row = 0, column = 0)    
	
	def set_up_projects(self, frame, profile, current_page):
		frame_profile_projects = Frame(frame)
		label_no_projects = Label(frame_profile_projects, text = "No Projects Attempted")
		amount = 0 
		n = 0 
		page_amount = math.ceil(len(profile["project_ids"])/3)
		list_id = profile["project_ids"]
		Index = self.project_index
		if page_amount == 0:
			label_no_projects.grid(row = 0, column = 0)
			frame_profile_projects.grid(row = 2, column = 0, columnspan = 2, sticky = N+E+W+S)
			page_amount = 1
		elif len(profile['project_ids'])-Index >= 3:
			amount = 3*current_page
		else:
			amount = len(profile["project_ids"])
		while(Index < amount):
			self.set_up_profile_projects((4*(n+1)), list_id[Index])
			n += 1
			Index = Index + 1
		return page_amount
		
	def set_up_profile_projects(self, Row, id):
		project = get_row("project_db", id)
		bid = get_row("bid_db", id)
		log = ez.get_bid_log(id)
		if bid["chosen_index"] != "Nan":
			dev = get_row("user_db", log[bid["chosen_index"]][1])
			client = get_row("user_db", project['client_id'])
			frame_profile_projects = Frame(self.frame_profile, bg = "white")
			
			label_description = Label(self.frame_profile, text = "Description " + project['desc'], justify= LEFT)
			
			if(project['status'] == "complete"):
				label_dev_review = Label(self.frame_profile, text = "Developer Review of Client: " + project['team_review'], justify= LEFT)
				label_cleint_review = Label(self.frame_profile, text = "Client Review of Developer: " + project['client_review'], justify= LEFT)
				label_dev_review.grid(row = Row+2, column = 0, columnspan = 2, sticky = W+E+N+S)
				label_cleint_review.grid(row = Row+3, column = 0, columnspan = 2, sticky = W+E+N+S)
				
			elif project['status'] == "no bid":
				label_no_bid = Label(self.frame_profile, text = "This Project Didn't Recive any bids", justify= LEFT)
				label_no_bid.grid(row = Row+2, column = 0, columnspan = 2, sticky = W+E+N+S)
			elif project['status'] == "incomplete":
				label_dev_review = Label(self.frame_profile, text = "Developer Review of Client: " + project['client_review'], justify= LEFT)
				label_cleint_review = Label(self.frame_profile, text = "Turk System: Project was not completed on time/nClient Review of Developer: " + project['client_review'], justify= LEFT)
				label_dev_review.grid(row = Row+2, column = 0, columnspan = 2, sticky = W+E+N+S)
				label_cleint_review.grid(row = Row+3, column = 0, columnspan = 2, sticky = W+E+N+S)
			if(ez.is_in_active_project(client) and client["project_ids"][len(client["project_ids"]) - 1] == id):
				label_active = Label(frame_profile_projects, text = "Active", justify= 'left', bg = "white")
				label_active.grid(row = 1, column = 0, sticky = E+W)
			if self.profile_project['id'] == project['id']:
				if ez.is_admin(dev):
					team = get_row("team_db", dev['team_id'])
					button_team_name = Button(frame_profile_projects, text = "Team: " + team["name"] + "Grade " + str(project["team_rating"]), bg = "white")
					button_team_name.grid(row = 0, column = 2, sticky = E+W)
					button_team_name.bind("<Button-1>", lambda event, arg = team: self.team_button(event, arg))
				else:
					button_developer_name = Button(frame_profile_projects, text = "Developer: " + dev["name"] + "Grade " + str(project["team_rating"]), bg = "white")
					button_developer_name.grid(row = 0, column = 2, sticky = E+W)
					button_developer_name.bind("<Button-1>", lambda event, arg = dev: self.profile_button(event, arg))
					
				button_client = Button(frame_profile_projects, text = "Client: " + client["name"] + "Grade " + str(project['client_rating']), bg = "white")
				button_client.bind("<Button-1>", lambda event, arg = client: self.profile_button(event, arg))
				button_client.grid(row = 0, column = 1, sticky = W+E+N+S) 
				label_project_name = Label(frame_profile_projects, text = "Project Name: "  + project["title"] + " ", bg = "white")  
				label_project_name.grid(row = 0, column = 0, sticky = W+E+N+S) 
			else:                
				if ez.is_admin(dev):
					team = get_row("team_db", dev['team_id'])
					label_team_name = Label(frame_profile_projects, text = "Team: " + team["name"], bg = "white")
					label__team_grade = Label(frame_profile_projects, text = "Grade " + str(project["team_rating"]) + "|"  , bg = "white")
					label_team_name.grid(row = 0, column = 3, sticky = E+W)
					label__team_grade.grid(row = 0, column = 4, sticky = E+W)
				else:
					label_developer_name = Label(frame_profile_projects, text = "Developer: " + dev["name"], bg = "white")
					label_dev_grade = Label(frame_profile_projects, text = "Grade " + str(project["team_rating"]) + "|"  , bg = "white")
					label_developer_name.grid(row = 0, column = 3, sticky = E+W)
					label_dev_grade.grid(row = 0, column = 4, sticky = E+W)
				button_project_name = Button(frame_profile_projects, text = "Project Name: "  + project["title"] + " ", bg = "white")  
				button_project_name.grid(row = 0, column = 0, sticky = W+E+N+S) 
				label_owner_name = Label(frame_profile_projects, text = "Client: " + client["name"] , bg = "white")
				label_owner_grade = Label(frame_profile_projects, text = "Grade " + str(project['client_rating'])+ " |" , bg = "white")
				label_owner_name.grid(row = 0, column = 1, sticky = W+E+N+S) 
				label_owner_grade.grid(row = 0, column = 2, sticky = W+E+N+S)
				button_project_name.bind("<Button-1>", lambda event, arg = id: self.project_button(event, arg))

		
			frame_profile_projects.grid(row = Row, column = 0, columnspan = 2, sticky = N+E+W+S)
			label_description.grid(row = Row+1, column = 0, columnspan = 2, sticky = W+E+N+S)
								  
		
	def set_up_project_scroll(self, frame, current_page, page_amount):    
		frame_page = Frame(frame, bg = "white")
		button_left = Button(frame_page, text = "<", bg = "white", relief = FLAT, cursor = "hand2")
		button_right = Button(frame_page, text = ">", bg = "white", relief = FLAT, cursor = "hand2")
		label_page = Label(frame_page, text = str(current_page) + "/" + str(page_amount), bg = "white")
		
		if page_amount == 1:
			button_left.config(state = DISABLED, cursor = 'arrow')
			button_right.config(state = DISABLED, cursor = 'arrow')
		elif current_page == 1:
			button_left.config(state = DISABLED, cursor = 'arrow')
			button_right.bind("<Button-1>", self.project_right)
		elif current_page == page_amount:
			button_right.config(state = DISABLED, cursor = 'arrow')
			button_left.bind("<Button-1>", self.project_left)
		else:
			button_left.bind("<Button-1>", self.project_left)
			button_right.bind("<Button-1>", self.project_right)
		
		frame_page.grid(row = 20, column = 0, columnspan = 2, sticky = E+W+S+N)
		button_left.grid(row = 0, column = 0, sticky = W)
		button_right.grid(row = 0, column = 2, sticky = E)
		label_page.grid(row = 0, column = 1)
	  
		
		
		
	def log_in(self, event):
		array = ez.verify(self.entry_username.get(), self.entry_password.get())
		if array[0] == 0 or array[0] == 10:
			if array[1]["user_type"] == "SU":
				self.set_up_super_user()
				self.set_up_overlay_profile(array[1])
			elif array[1]["warning"] == 2:
					self.set_up_overlay_profile(array[1], "Login successful, but has 2 warnings and not yet blacklisted\nOnce you log out your account will be placed on a blacklist.\nThis is your only chance to send an appeal to Super User")
			else:
					self.set_up_overlay_profile(array[1])
			self.frame_user_login_input.grid_forget()
			self.logged_in_user = array[1]
			self.project_index = 0
			if self.frame_current == self.frame_profile and self.profile_type == 0:
				self.set_up_profile()
			elif self.frame_current == self.frame_profile and self.profile_type == 1:
				self.set_up_team_profile()
			elif self.frame_current == self.frame_profile and self.profile_type == 2:
				self.set_up_project_profile()
		elif array[0] > 3:
			if array[1]["status"] == "blacklisted":
				self.set_up_overlay(array[0], "User found but blacklisted")
			elif array[1]["status"] == "rejected":
				self.set_up_overlay(array[0], "Login successful, but temporary user was rejected")
			elif array[1]["status"] == "inactive":
				self.set_up_overlay(array[0], "User found but deactivated")
		else:
			self.set_up_overlay(array[0], array[2])
		self.entry_username.delete(0,"end")
		self.entry_password.delete(0,"end")
	
	def log_out(self,event):
		if self.logged_in_user["warning"] == 2:
			self.logged_in_user["status"] = "blacklisted"
			set_row("user_db", self.logged_in_user)
		if self.logged_in_user['status'] == "SU":
			self.set_up_top_user_chart()
		self.frame_logged_in.grid_forget()
		self.logged_in_user = {"id" : "", "name": "", "interest": "", "team_id" : "Nan", "user_type" : ""} 
		self.proflie_state = 0
		self.logged_in_id = 0
		self.project_index = 0
		if self.frame_current == self.frame_profile and self.profile_type == 0:
			self.set_up_profile()
		elif self.frame_current == self.frame_profile and self.profile_type == 1:
			self.set_up_team_profile()
		elif self.frame_current == self.frame_profile and self.profile_type == 2:
			self.set_up_project_profile()
		elif self.frame_current == self.frame_profile and self.profile_type == 3:
			self.set_up_top_user_chart()
		if self.frame_current == self.frame_make_team:
			self.set_up_top_user_chart()
		self.frame_user_login_input.grid(row = 1, column = 4)


	def edit_button(self,event):
		self.proflie_state = 1
		if self.profile_type == 0:
			self.set_up_profile()
		elif self.profile_type == 1:
			self.set_up_team_profile()
	
		
	def save_button(self, event):
		self.proflie_state = 0
		if self.profile_type == 0:
			self.logged_in_user["name"] = self.profile_name_entry.get()
			self.logged_in_user['interest'] = self.proflie_bio_entry.get("1.0",END)
			self.logged_in_user["password"] = self.profile_password_entry.get()
			self.logged_in_user["resume"] = self.proflie_resume_text_box.get("1.0",END)
			self.profile_user = self.logged_in_user
			set_row("user_db", self.logged_in_user)
			self.set_up_profile()
			self.set_up_overlay_profile(self.logged_in_user)
		elif self.profile_type == 1:
			self.profile_team["name"] = self.profile_name_entry.get()
			self.profile_team['desc'] = self.proflie_bio_entry.get("1.0",END)
			set_row("team_db", self.profile_team)
			self.set_up_team_profile()
			
	def cancel_button(self, event):
		self.proflie_state = 0
		if self.profile_type == 0:
			self.set_up_profile()
		elif self.profile_type == 1:
			self.set_up_team_profile()

	def deposit_button(self, event):
		self.proflie_state = 3
		self.set_up_profile()
	
	def deposit_accept_button(self, event):
		self.proflie_state = 0
		self.profile_user["balance"] = self.logged_in_user["balance"] = self.logged_in_user["balance"] + float(self.profile_cash_amount_entry.get())
		set_row("user_db", self.logged_in_user)
		self.set_up_profile()
		
	def withdraw_button(self, event):
		self.proflie_state = 2
		self.set_up_profile()
	
	def withdraw_accept_button(self, event):
		self.proflie_state = 0
		if self.logged_in_user["balance"] - float(self.profile_cash_amount_entry.get()) > 0:
			self.profile_user["balance"] = self.logged_in_user["balance"] = self.logged_in_user["balance"] - float(self.profile_cash_amount_entry.get())
			set_row("user_db", self.logged_in_user)
		self.set_up_profile()
		
	def quit_button(self, event):
		tkinter.messagebox.showinfo("Quit Request", "Your request has been sent to the Admin they will review your account and respond shortly")
		self.logged_in_user.request_quit()
		self.user_table.update(self.logged_in_user.get_id(), self.logged_in_user.get_dictonary())
		self.set_up_profile()
		
	def project_left(self, event):
		if self.profile_type == 0:
			self.project_index -= 3
			self.set_up_profile()
		elif self.profile_type == 1:
			self.project_index -= 10
			self.set_up_team_profile()
		elif self.profile_type == 3:
			self.project_index -= 10
			self.set_up_search(self.matches)
		elif self.profile_type == 2:
			self.project_index -= 5
			self.set_up_project_profile()
		elif self.profile_type == 4:
			self.project_index -= 3
			self.set_up_super_user()
		
		
	def project_right(self, event):
		if self.profile_type == 0:
			self.project_index += 3
			self.set_up_profile()
		elif self.profile_type == 1:
			self.project_index += 10
			self.set_up_team_profile()
		elif self.profile_type == 3:
			self.project_index += 10
			self.set_up_search(self.matches)
		elif self.profile_type == 2:
			self.project_index += 5
			self.set_up_project_profile()
		elif self.profile_type == 4:
			self.project_index += 3
			self.set_up_super_user()
			
	def create_button_account(self,event):
		if self.var.get() == 0:
			type = "dev"
		else:
			type = "client"
		output = ez.register_user(self.entry_name.get(), self.entry_username_ac.get(), self.entry_password_ac.get(), type, self.entry_balance.get())
		if isinstance(output,str):
			self.set_up_new_account(output)
		else :
			self.logged_in_user = self.profile_user = output
			self.set_up_profile()
			self.frame_user_login_input.grid_forget()
			self.set_up_overlay_profile(output)
			
	def create_button_project(self,event):
		if self.entry_name.get() != "" and self.entry_desc.get("1.0",END) != ""  and  self.entry_time.get() != "" and self.entry_money.get() != ""  and float(self.entry_money.get()) < self.profile_user['balance']:
			project = ez.create_project(self.logged_in_user['id'], self.entry_name.get(), self.entry_desc.get("1.0",END)) #client_id, title, desc)
			datetime_object = datetime.strptime(project["bid_end_date"],"%Y-%m-%d %H:%M:%S")
			datetime_object = datetime_object + timedelta(days=int(self.entry_time.get()))
			datetime_object = datetime_object.strftime("%Y-%m-%d %H:%M:%S")
			
			bid  = ez.create_bid(project["client_id"], project["id"], datetime_object, int(self.entry_money.get())) #project_id, end_date, initial_bid, start_date = now
			if bid != "Nan":
				project["bid_id"] = project['id']
				set_row("project_db", project)
				self.logged_in_user = get_row("user_db", self.logged_in_user["id"])
				self.profile_project = project
				self.set_up_project_profile()
			else:
				del_row("project_db", project['id'])
					
		elif self.entry_money.get():
			print("Bid Incomplete:\nPlease enter how what monetray rewards you are willing to complete the project for")
		elif self.entry_time.get() == "":
			print("Bid Incomplete:\nPlease enter how many days you will take to complete project")
		elif self.entry_desc.get("1.0",END) != "":
			print("Bid Incomplete:\nPlease enter the description for the project")
		elif self.entry_name.get() == "":
			print("Bid Incomplete:\nPlease enter title for the project")
		   
	def create_button_bid(self,event):
		self_log = ez.get_bid_log(self.profile_project['id'])
		if self.entry_time.get() != "" and self.entry_money.get() != "" :
			
			datetime_object = datetime.strptime(self.profile_project["bid_end_date"],"%Y-%m-%d %H:%M:%S")
			datetime_object = datetime_object + timedelta(days=int(self.entry_time.get()))
			if datetime_object <= datetime.strptime(self_log[0][3],"%Y-%m-%d %H:%M:%S") and int(self.entry_money.get()) <= self_log[0][2]:
				datetime_object = datetime_object.strftime("%Y-%m-%d %H:%M:%S")
				log  = ez.create_bid(self.logged_in_user['id'], self.profile_project["id"], datetime_object, int(self.entry_money.get())) #project_id, end_date, initial_bid, start_date = now
				if log != "Nan":
					bid = get_row("bid_db", self.profile_project['id'])
					bid['bid_log'] = log
					set_row("bid_db", bid)
					self.set_up_project_profile()
			elif datetime_object > datetime.strptime(self_log[0][3],"%Y-%m-%d %H:%M:%S"):
				print("Time Larger than client offered")
			elif int(self.entry_money.get()) > self_log[0][2]:
				print("Sum Larger than client offered")
		elif self.entry_money.get() == "" and self.entry_time.get() == "":
			print("Bid Incomplete:\nPlease fill out the bid criteria")
		elif self.entry_money.get():
			print("Bid Incomplete:\nPlease enter how what monetray rewards you are willing to complete the project for")
		elif self.entry_time.get() == "":
			print("Bid Incomplete:\nPlease enter how many days you will take to complete project")
			
	def SU_generic_choice_accept(self, event, array):
		if self.text_reason.get("1.0",END) != "Nan":
			if self.SU_state == 0:
				array[1]["status"] = "active"
			if self.SU_state == 1:
				array[1]["warning"] = 0
			if self.SU_state == 2:
				array[1]["status"] = "inactive"
			if self.SU_state == 3: 
				array[1]["status"] = "active"
				array[1]["warning"] = 1
			array[0]['resolved'] = True
			set_row("user_db", array[1])
			set_row("issue_db", array[0])
		else:
			print("Please enter a reason")
		self.set_up_super_user()
			
	def SU_generic_choice_reject(self, event, array):
		if self.text_reason.get("1.0",END) != "Nan":
			if self.SU_state == 0:
				array[1]["status"] = "rejected"
			if self.SU_state == 1:
				array[1]["warning"] = 1
			if self.SU_state == 2:
				array[1]["status"] = "active"
			if self.SU_state == 3: 
				array[1]["status"] = "blacklist"
				array[1]["warning"] = 2
			array[0]['resolved'] = True
			set_row("user_db", array[1])
			set_row("issue_db", array[0])
		else:
			print("Please enter a reason")
		self.set_up_super_user()
		
	def promote_button(self, event, id):
		ez.promote(self.profile_team, id)
		self.set_up_team_profile()

		
	def demote_button(self, event, id):
		ez.demote(self.profile_team, id)
		self.set_up_team_profile()
	
	def choose_bid_button(self, event, array):
		ez.choose_bid(array[0],array[1]) #choose_bid(bid_id, dev_id, reason = "lowest bidder"): modifies bid_db and changes states
		self.set_up_project_profile()
		
	def find_path(self, event):
		self.path = fd.askopenfilename()
		self.set_up_project_profile()
		
	def claim(self, event):
		if self.entry_grade != "Nan" and self.text_review != "Nan" and int(self.entry_grade.get()) > 0 and int(self.entry_grade.get()) < 5:
			ez.submit(os.path.dirname(self.path), os.path.basename(self.path) , self.profile_project['id'])
			project = ez.make_rating(self.logged_in_user['id'], float(self.entry_grade.get()),self.text_review.get("1.0",END))
			set_row("project_db", project)
			
		self.set_up_project_profile()
		
	def submit_file(self, event):
		if self.path != "Nan" and self.entry_grade != "Nan" and self.text_review != "Nan" and int(self.entry_grade.get()) > 0 and int(self.entry_grade.get()) < 5 :
			ez.submit(os.path.dirname(self.path), os.path.basename(self.path) , self.profile_project['id'])
			project = ez.make_rating(self.logged_in_user['id'], float(self.entry_grade.get()),self.text_review.get("1.0",END))
			set_row("project_db", project)
			
		self.set_up_project_profile()
		
	def kick_button(self, event, id):
		ez.kick(self.profile_team, id)
		self.set_up_team_profile()
	
	def request_join_team_button(self, event, id):
		self.profile_user = self.logged_in_user = ez.request_join(self.profile_team, id)
		self.set_up_team_profile()
		
	def accept_team_button(self, event, id):
		ez.accept_team(self.profile_team, id)
		self.set_up_team_profile()
		
	def reject_team_button(self, event, id):
		ez.reject_team(self.profile_team, id)
		self.set_up_team_profile()
		
	def button_accepts_screen(self,event):
		self.SU_state = 0
		self.set_up_super_user()
		
	def button_dispute_warning_screen(self,event):
		self.SU_state = 1
		self.set_up_super_user()
		
	def button_quit_req_screen(self,event):
		self.SU_state = 2
		self.set_up_super_user()
		
	def button_blacklist_screen(self,event):
		self.SU_state = 3
		self.set_up_super_user()
		
	def button_grade_screen(self,event):
		self.SU_state = 4
		self.set_up_super_user()
		
	def page_deafult(self):
		self.proflie_state = 0
		self.project_index = 0 
		self.SU_state = 0
		self.profile_team = Team().get_all()
		self.profile_project = Project().get_all()
		self.profile_user = User().get_all()
		self.path = ""
		
	def home_button(self,event):
		self.page_deafult()
		self.set_up_top_user_chart()
		self.project_index = 0
		
	def profile_button(self,event, user):
		if user["user_type"] == "SU":
			self.set_up_super_user()
		else:
			self.page_deafult()
			self.profile_user = user
			self.set_up_profile()
		
	def back_button(self, event):
		if self.profile_type == 2:
			self.set_up_project_profile()
		
	def project_button(self, event, project_id):
		self.page_deafult()
		self.profile_project = get_row("project_db", project_id)
		self.set_up_project_profile()
		
	def team_button(self, event, team):
		self.page_deafult()
		self.profile_team = team
		self.set_up_team_profile()
		
	def new_account_button(self, event):
		self.page_deafult()
		self.set_up_new_account("")
	
	def search_button(self, event):
		self.page_deafult()
		matches = []
		if self.v.get() == 0:
			matches = ez.search_matches(User(), self.entry_search_bar.get())
		elif self.v.get() == 1:
			matches = ez.search_matches(Team(), self.entry_search_bar.get())
		else:
			matches = ez.search_matches(Project(), self.entry_search_bar.get()) 
		self.matches = matches     
		self.set_up_search(matches)
		
	
start = GUI()
start.origin.mainloop()