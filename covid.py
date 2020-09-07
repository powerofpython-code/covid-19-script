from tabulate import  tabulate
from covid import Covid
from colorama import init,Fore, Back, Style
import os
init(convert=True) #to convert into color text 
os.system("cls")# clear the terminal screen
os.system("type ascii.txt")
print()#space to print table
try:
 	covid=Covid()
 	active=covid.get_total_active_cases()
 	confirmed = covid.get_total_confirmed_cases()
 	recovered=covid.get_total_recovered()
 	deaths=covid.get_total_deaths()
 	table=[								#table format
 		[Fore.CYAN+"Active",active],
 		[Fore.GREEN+"Confirmed",confirmed],
 		[Fore.YELLOW+"Recovered",recovered],
 		[Fore.RED+"Deaths",deaths]
 	]
 	print(tabulate(table,headers=["Types of cases","Status"],tablefmt="simple"))#finally printing the table
except Exception as e:
	print(Fore.YELLOW+e)