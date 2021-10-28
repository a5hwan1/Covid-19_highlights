import tkinter as tk
import requests
import json


window=tk.Tk()
window.title("Covid-19")
label1=tk.Label(window,text='Welcome to info. page.', foreground='Green', background='Black', width=40, height=2,font=(None,15))
label2=tk.Label(window,text='Total present active cases:-', foreground='Green', background='Black', width=40, height=2,font=(None,15))
label3=tk.Label(window,text='Total confirmed cases till yet:-', foreground='Green', background='Black', width=40, height=2,font=(None,15))
label4=tk.Label(window,text='Total Deaths till yet:-', foreground='Green', background='Black', width=40, height=2,font=(None,15))
label5=tk.Label(window,text='Confirmed cases yesterday:-', foreground='Green', background='Black', width=40, height=2,font=(None,15))
label6=tk.Label(window,text='Total Deaths yesterday:-', foreground='Green', background='Black', width=40, height=2,font=(None,15))
label7=tk.Label(window,text='Recovered cases yesterday:-', foreground='Green', background='Black', width=40, height=2,font=(None,15))
def clicked():
    url = "https://api.covid19india.org/data.json"
    page = requests.get(url)
    data = json.loads(page.text)
    label2.configure(text="Total present active cases:-"+data["statewise"][0]['active'])
    label3.configure(text="Total present active cases:-"+data["statewise"][0]['confirmed'])
    label4.configure(text="Total present active cases:-"+data["statewise"][0]['deaths'])
    label5.configure(text="Total present active cases:-"+data["statewise"][0]['deltaconfirmed'])
    label6.configure(text="Total present active cases:-"+data["statewise"][0]['deltadeaths'])
    label7.configure(text="Total present active cases:-"+data["statewise"][0]['deltarecovered'])

btn=tk.Button(window,text="Refresh",bd='5',bg='red',fg='black',width='33',height='2',font=(None,17),command=clicked)
label1.pack()
label2.pack()
label3.pack()
label4.pack()
label5.pack()
label6.pack()
label7.pack()
btn.pack()
window.mainloop()
