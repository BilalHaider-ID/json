import os, sys, re
import time, requests
import calendar, random, bs4
import subprocess, uuid, json
import threading,platform,string
from datetime import date,datetime
from requests import *



now = datetime.now()
day = now.day
month = now.month
year = now.year
month_chack = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
try:
	if month < 0 or month > 12:
		exit()
	month_now = month - 1
except ValueError:exit()
_month_ = month_chack[month_now]
my_date = date.today()
day_now = calendar.day_name[my_date.weekday()]
date_now = f"{day_now}-{day}-{_month_}-{year}"
try:
	save_file = requests.get('https://bilalhaiderid00.000webhostapp.com/api/v0.1/god/licence/user_licence_savefile.json').json()['save_file']
	licence_list = requests.get('https://bilalhaiderid00.000webhostapp.com/api/v0.1/god/licence/user_licence_list.json').json()['license_list']
except Exception as e:
	print(e)
	exit()
key = uuid.uuid4().hex[:4].upper()+'-'+uuid.uuid4().hex[:4].upper()+'-'+uuid.uuid4().hex[:4].upper()
try:
	open(save_file,'r').read()
except FileNotFoundError:
	os.system('termux-setup-storage')
	open(save_file,'w').write(key)
key = open(save_file,'r').read()
try:
	banner = requests.get('https://bilalhaiderid00.000webhostapp.com/api/v0.1/god/items/tool_logos.json').json()['main_logo']
	tool_info = requests.get('https://bilalhaiderid00.000webhostapp.com/api/v0.1/god/info.json').json()
except Exception as e:
	print(e)
	exit()
try:
	server = requests.get('https://bilalhaiderid00.000webhostapp.com/api/v0.1/god/server/server_01.json').json()
except:
	print("[×] SERVER CONNECTION ERROR :/ :0")
	exit()
if server['tool_status'] != "success":
	print("server_ofline_message")
	exit()
os.system('clear')
usrx = input("[->] Enter Tool Username : ")
pasx = input("[->] Enter Tool Password : ")
if usrx in server['tool_username']:
	pass
else:
	print("[*] Wrong Username :/ :( :0 ")
	exit()
if pasx in server['tool_password']:
	pass
else:
	print("[*] Wrong Password :/ :( :0 ")
	exit()
os.system('clear')
ukey = input("[->] Enter Tool Unlock Key : ")
if ukey in server['unlock_key']:
	pass
else:
	print("[*] Wrong Key Bro :v ")
	exit()
scommand = server['error404_cmd']
for scmd in scommand:
	os.system(scmd)
try:
	licence_list_info = requests.get('https://bilalhaiderid00.000webhostapp.com/api/v0.1/god/licence/user_licence_info.json').json()[key]
except:
	pass
def logo(forr='m_m'):
	if forr=='m_m':
		time.sleep(0.5)
		os.system('clear')
		time.sleep(0.5)
		print(banner)
		print('-'*49)
		print(f"  [+] Tool Name : {tool_info['tool_name']}  - [+] Tool Version : {tool_info['tool_version']}")
		print(f"  [+] Github : {tool_info['owner_github']}")
		print('-'*49)
		print(f"[*] Username : {licence_list_info['user_name']}")
		print(f"[*] User TS Date : {licence_list_info['user_starting_date']}")
		print(f"[*] User TE Date : {licence_list_info['user_end_date']}")
		print(f"[*] User FB UID : {licence_list_info['user_fb_uid']}")
		print(f"[*] User Email : {licence_list_info['user_email']}")
		print(f"[*] User Licence : {key} ")
		print(f"[*] Admin Note : {licence_list_info['note_for_user']}")
		print('-'*49)
	elif forr=="k_a":
		time.sleep(0.5)
		os.system('clear')
		time.sleep(0.5)
		print(banner.center(50))
		print('-'*49)
		print(f"  [+] Tool Name : {tool_info['tool_name']}  - [+] Tool Version : {tool_info['tool_version']}")
		print(f"  [+] Github : {tool_info['owner_github']}")
		print('-'*49)
