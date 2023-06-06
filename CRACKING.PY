########################
#import libs
import subprocess
import sys
import termcolor
from termcolor import colored
import time
from time import sleep
import os
import string
import itertools
from itertools import product
#finshed
###########################
def banner():
    f1='''
        ======================MAZINF7😎===================== 
    '''
    print(colored(f1,'green'))
banner()
################
print(colored(' Make Wordlist ✍🏿','blue'))
choice_first_work=int(input(colored('press 1 and enter to open the tool >>>>  ','green')))
if choice_first_work == 1:
    def make_file():
        os.system('clear')
        banner()
        File_name=input(colored("ENTER THE FILE NAME 👨‍💻>> ",'green'))
        min_length=int(input(colored("ENTER Minimum Password Length  👨‍💻>>  ",'green')))
        max_length=int(input(colored("ENTER Maximum Password Length👨‍💻>>  ",'green')))
        count=0
        random_pass=string.ascii_lowercase+string.ascii_uppercase+string.digits+string.punctuation
        choice_sp_col=int(input(colored(" if you have information of vactim enter 1 if you do not have information enter 2>>  ",'green')))
        if choice_sp_col ==1:
            spechil_characters=input(colored("ENTER THE SPEICIAL CHARACTERS FOR VICTIM 😈>>  ",'green'))
            spechil_numbers=input(colored("ENTER THE SPEICIAL NUMBERS FOR VICTIM 😈>>  ",'green'))
            spechil_sympol=input(colored("ENTER THE SPEICIAL SYMBOL FOR VICTIM 😈>>  ",'green'))
            spechil_collection=spechil_characters+spechil_numbers+spechil_sympol
            file =open(File_name+".txt",'w')
            for i in range(min_length,max_length+1):
                for j in product(spechil_collection,repeat=i):
                    password="".join(j)
                    file.write(password)
                    file.write("\n")
                    count+=1
            sleep(1.5)
            print(colored("YOUR WORDLIST HAVE {} PASSWORDS .".format(count),'blue'))
        elif choice_sp_col ==2:
            file =open(File_name+".txt",'w')
            for i in range(min_length,max_length+1):
                for j in product(random_pass,repeat=i):
                    password="".join(j)
                    file.write(password)
                    file.write("\n")
                    count+=1
            sleep(1.5)
            print(colored("YOUR WORDLIST HAVE {} PASSWORDS .".format(count),'blue'))
        else:
            print(colored("your choice is unvailable please restart the tool and try again .","red"))
    make_file()
else:
    print(colored("your choice is unvailable please restart the tool and try again .","red"))
