#System health

import os
from rich.console import Console
from rich.text import Text

console = Console()

def load_avg():
	print("..................Load Average..............")
	data = os.popen("cat /proc/loadavg").read() # gets the load average details
	console.print(Text("Load Average :",style="bold green"))
	console.print(Text(data,style="bold green"))

def uptime():
	print(".....................Uptime...................")
	uptime = os.popen("uptime -s").read()
	console.print(Text("Uptime :",style="bold green")) # gets the time and date
	console.print(Text(uptime,style="bold green"))

def available_ram():
	print(".............Available RAM..................")
	cmd = "free -m"
	avail_ram = os.popen(cmd).read()
	console.print(Text("Available RAM :",style="bold green")) # gets the details of avaialble RAM
	console.print(Text(avail_ram,style="bold green"))

def hostname_details():
	print("...............Hostname Details...................")
	cmd = "hostnamectl status"
	host_detail = os.popen(cmd).read()
	console.print(Text("Hostname Details :",style="bold green")) # gets the host details
	console.print(Text(host_detail,style="bold green"))

def process_count():
	print(".................Process Count..................")
	cmd ="ps -e | wc -l"
	pro_count = os.popen(cmd).read()
	console.print(Text("Process Count :",style="bold green")) # gets the process count
	console.print(Text(pro_count,style="bold green"))


def menu():
	print("............Main Menu..................")
	console.print("1.Display available RAM ",style="bold green")
	console.print("2.Display Load avearge ",style="bold green")
	console.print("3.Display Hostname details ",style="bold green")
	console.print("4.Display All process count ",style="bold green")
	console.print("5.Display uptime ",style="bold green")
	console.print("6.Exit",style="bold green")

while True:
	menu()
	ch = int(input("Enter your choice"))
	if ch == 1:
		available_ram()
	elif ch == 2:
		load_avg()
	elif ch == 3:
		hostname_details()
	elif ch == 4:
		process_count()
	elif ch == 5:
		uptime()
	elif ch == 6:
		break
	else:
		console.print("Wrong choice",style="bold red")
