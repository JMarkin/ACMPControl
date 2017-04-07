import json
from urllib.request import urlopen
from bs4 import BeautifulSoup
from datetime import datetime
from tkinter import messagebox as mBox,Tk

def get_now_tasks(url):
    profile = urlopen(url)
    soap = BeautifulSoup(profile,'lxml')
    return soap.find_all('p')[1].__str__().count('main=task')

def get_past_tasks():
    prev_data={datetime.now().strftime('%d.%m.%Y %I:%M %p'):'0'}
    try:
        prev_data=json.load(open('stats.json','r'))
    except FileNotFoundError:
        print('This is a first day')
        with open('stats.json','w') as f:
            json.dump(prev_data,f)
    max_date=max(prev_data.keys())
    return int(prev_data[max_date])

def warnBox(deltasks):
    root = Tk()
    root.withdraw()
    mBox.showerror("You didn't worked","You did "+str(deltasks)+" for last day")

def main(url):
    past_tasks = get_past_tasks()
    if past_tasks>=700:
        return 'Yes'
    now_tasks = get_now_tasks(url)
    if now_tasks<=past_tasks+5:
        warnBox(now_tasks-past_tasks)
    dict_tasks=json.load(open('stats.json'))
    dict_tasks[datetime.now().strftime('%d.%m.%Y %I:%M %p')]=now_tasks
    with open('stats.json','w') as f:
        json.dump(dict_tasks,f)

