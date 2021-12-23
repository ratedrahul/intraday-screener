from tkinter import*
import time
import pandas as pd
from numpy import * 
import threading
import requests
from bs4 import BeautifulSoup
from math import floor, ceil 
import winsound
import json
# from datetime import date
import datetime
# from Bullish8_and_engulf_latest import *
from global_data_adr import adr_global_data
from NIFTY_LIST import *
import os   
# from Rated_Screener import eng_r
# from stock_function2 import *
# from Rated_Live_Data import *
from functools import partial
# command=partial(change_label_number, 2)

window= Tk()
window.geometry("1900x950+0+5")
window.title("Rinku bhai Stock screener")
window.configure(bg="#8B008B")
window.wm_iconbitmap('D:\\rated screener\\Auto wala.ico')

header = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

slideword = ""
count = 0
# NIFTY102 = ['ACC', 'ABBOTINDIA', 'ALKEM', 'AMBUJACEM', 'ASIANPAINT', 'AUROPHARMA', 'DMART', 'AXISBANK','BAJFINANCE', 'BAJAJFINSV', 'BAJAJHLDNG', 'BANDHANBNK', 'BANKBARODA', 'BERGEPAINT', 'BPCL', 'BHARTIARTL', 'BIOCON', 'BOSCHLTD', 'BRITANNIA', 'CADILAHC', 'CIPLA', 'COALINDIA', 'COLPAL', 'CONCOR', 'DLF', 'DABUR', 'DIVISLAB', 'DRREDDY', 'EICHERMOT', 'GAIL', 'GICRE', 'GODREJCP', 'GRASIM', 'HCLTECH', 'HDFCAMC', 'HDFCBANK', 'HDFCLIFE', 'HAVELLS', 'HEROMOTOCO', 'HINDALCO', 'HINDPETRO', 'HINDUNILVR', 'HINDZINC', 'HDFC', 'ICICIBANK', 'ICICIGI', 'ICICIPRULI', 'ITC', 'IOC', 'IGL', 'INDUSINDBK', 'NAUKRI', 'INFY', 'INDIGO', 'JSWSTEEL', 'KOTAKBANK', 'LTI', 'LT', 'LUPIN', 'MARICO', 'MARUTI', 'MOTHERSUMI', 'MUTHOOTFIN','NCC', 'NMDC', 'NTPC', 'NESTLEIND', 'ONGC', 'OFSS', 'PETRONET', 'PIDILITIND', 'PEL', 'PFC', 'POWERGRID', 'PGHH', 'PNB', 'RELIANCE', 'SBICARD', 'SBILIFE', 'SHREECEM', 'SIEMENS', 'SBIN', 'SUNPHARMA', 'TCS', 'TATACONSUM', 'TATAMOTORS', 'TATASTEEL', 'TECHM', 'TITAN', 'TORNTPHARM', 'UPL', 'ULTRACEMCO', 'UBL', 'WIPRO','ZEEL']
# NIFTY102 = ['AARTIIND', 'ACC', 'ADANIENT', 'ADANIPORTS', 'ALKEM', 'AMARAJABAT', 'AMBUJACEM', 'APLLTD', 'APOLLOHOSP', 'APOLLOTYRE', 'ASHOKLEY', 'ASIANPAINT', 'AUBANK', 'AUROPHARMA', 'AXISBANK','BAJAJFINSV', 'BAJFINANCE', 'BALKRISIND', 'BANDHANBNK', 'BANKBARODA', 'BATAINDIA', 'BEL', 'BERGEPAINT', 'BHARATFORG', 'BHARTIARTL', 'BHEL', 'BIOCON', 'BOSCHLTD', 'BPCL', 'BRITANNIA', 'CADILAHC', 'CANBK', 'CHOLAFIN', 'CIPLA', 'COALINDIA', 'COFORGE', 'COLPAL', 'CONCOR', 'CUB', 'CUMMINSIND', 'DABUR', 'DEEPAKNTR', 'DIVISLAB', 'DLF', 'DRREDDY', 'EICHERMOT', 'ESCORTS', 'EXIDEIND', 'FEDERALBNK', 'GAIL', 'GLENMARK', 'GMRINFRA', 'GODREJCP', 'GODREJPROP', 'GRANULES', 'GRASIM', 'GUJGASLTD', 'HAVELLS', 'HCLTECH', 'HDFC', 'HDFCAMC', 'HDFCBANK', 'HDFCLIFE', 'HEROMOTOCO', 'HINDALCO', 'HINDPETRO', 'HINDUNILVR', 'IBULHSGFIN', 'ICICIBANK', 'ICICIGI', 'ICICIPRULI', 'IDEA', 'IDFCFIRSTB', 'IGL', 'INDIGO', 'INDUSINDBK', 'INDUSTOWER', 'INFY', 'IOC', 'IRCTC', 'ITC', 'JINDALSTEL', 'JSWSTEEL', 'JUBLFOOD', 'KOTAKBANK', 'LALPATHLAB', 'LICHSGFIN', 'LT', 'LTI', 'LTTS', 'LUPIN', 'MANAPPURAM', 'MARICO', 'MARUTI', 'MCDOWELL-N', 'MFSL', 'MGL', 'MINDTREE', 'MOTHERSUMI', 'MPHASIS', 'MRF', 'MUTHOOTFIN','NATIONALUM', 'NAUKRI', 'NAVINFLUOR', 'NESTLEIND', 'NMDC', 'NTPC', 'ONGC', 'PAGEIND', 'PEL', 'PETRONET', 'PFC', 'PFIZER', 'PIDILITIND', 'PIIND', 'PNB', 'POWERGRID', 'PVR', 'RAMCOCEM', 'RBLBANK', 'RECLTD', 'RELIANCE', 'SAIL', 'SBILIFE', 'SBIN', 'SHREECEM', 'SIEMENS', 'SRF', 'SRTRANSFIN', 'SUNPHARMA', 'SUNTV', 'TATACHEM', 'TATACONSUM', 'TATAMOTORS', 'TATAPOWER', 'TATASTEEL', 'TCS', 'TECHM', 'TITAN', 'TORNTPHARM', 'TORNTPOWER', 'TRENT', 'TVSMOTOR', 'UBL', 'ULTRACEMCO', 'UPL', 'VEDL', 'VOLTAS', 'WIPRO', 'ZEEL']
# NIFTY102_all = ['AARTIIND', 'ACC', 'ADANIENT', 'ADANIPORTS', 'ALKEM', 'AMARAJABAT', 'AMBUJACEM', 'APLLTD', 'APOLLOHOSP', 'APOLLOTYRE', 'ASHOKLEY', 'ASIANPAINT', 'AUBANK', 'AUROPHARMA', 'AXISBANK', 'BAJAJFINSV', 'BAJFINANCE', 'BALKRISIND', 'BANDHANBNK', 'BANKBARODA', 'BATAINDIA', 'BEL', 'BERGEPAINT', 'BHARATFORG', 'BHARTIARTL', 'BHEL', 'BIOCON', 'BOSCHLTD', 'BPCL', 'BRITANNIA', 'CADILAHC', 'CANBK', 'CHOLAFIN', 'CIPLA', 'COALINDIA', 'COFORGE', 'COLPAL', 'CONCOR', 'CUB', 'CUMMINSIND', 'DABUR', 'DEEPAKNTR', 'DIVISLAB', 'DLF', 'DRREDDY', 'EICHERMOT', 'ESCORTS', 'EXIDEIND', 'FEDERALBNK', 'GAIL', 'GLENMARK', 'GMRINFRA', 'GODREJCP', 'GODREJPROP', 'GRANULES', 'GRASIM', 'GUJGASLTD', 'HAVELLS', 'HCLTECH', 'HDFC', 'HDFCAMC', 'HDFCBANK', 'HDFCLIFE', 'HEROMOTOCO', 'HINDALCO', 'HINDPETRO', 'HINDUNILVR', 'IBULHSGFIN', 'ICICIBANK', 'ICICIGI', 'ICICIPRULI', 'IDEA', 'IDFCFIRSTB', 'IGL', 'INDIGO', 'INDUSINDBK', 'INDUSTOWER', 'INFY', 'IOC', 'IRCTC', 'ITC', 'JINDALSTEL', 'JSWSTEEL', 'JUBLFOOD', 'KOTAKBANK', 'LALPATHLAB', 'LICHSGFIN', 'LT', 'LTI', 'LTTS', 'LUPIN', 'MANAPPURAM', 'MARICO', 'MARUTI', 'MFSL', 'MGL', 'MINDTREE', 'MOTHERSUMI', 'MPHASIS', 'MRF', 'MUTHOOTFIN', 'NATIONALUM', 'NAUKRI', 'NAVINFLUOR', 'NESTLEIND', 'NMDC', 'NTPC', 'ONGC', 'PAGEIND', 'PEL', 'PETRONET', 'PFC', 'PFIZER', 'PIDILITIND', 'PIIND', 'PNB', 'POWERGRID', 'PVR', 'RAMCOCEM', 'RBLBANK', 'RECLTD', 'RELIANCE', 'SAIL', 'SBILIFE', 'SBIN', 'SHREECEM', 'SIEMENS', 'SRF', 'SRTRANSFIN', 'SUNPHARMA', 'SUNTV', 'TATACHEM', 'TATACONSUM', 'TATAMOTORS', 'TATAPOWER', 'TATASTEEL', 'TCS', 'TECHM', 'TITAN', 'TORNTPHARM', 'TORNTPOWER', 'TRENT', 'TVSMOTOR', 'UBL', 'ULTRACEMCO', 'UPL', 'VEDL', 'VOLTAS', 'WIPRO', 'ZEEL']
NIFTY102 = ['AARTIIND', 'ACC', 'ADANIENT', 'ADANIPORTS', 'ALKEM', 'AMARAJABAT', 'AMBUJACEM', 'APOLLOHOSP', 'APOLLOTYRE', 'ASHOKLEY', 'ASIANPAINT','AUROPHARMA', 'AXISBANK', 'BAJAJFINSV', 'BAJFINANCE', 'BALKRISIND', 'BANDHANBNK', 'BANKBARODA', 'BATAINDIA', 'BEL', 'BERGEPAINT', 'BHARATFORG', 'BHARTIARTL', 'BHEL', 'BIOCON', 'BPCL', 'BRITANNIA', 'CADILAHC', 'CANBK', 'CHOLAFIN', 'CIPLA', 'COALINDIA', 'COFORGE', 'COLPAL', 'CONCOR', 'CUMMINSIND', 'DABUR','DIVISLAB', 'DLF', 'DRREDDY', 'EICHERMOT', 'ESCORTS', 'EXIDEIND', 'FEDERALBNK', 'GAIL', 'GLENMARK', 'GODREJCP', 'GODREJPROP','GRASIM', 'GUJGASLTD', 'HAVELLS', 'HCLTECH', 'HDFC', 'HDFCAMC', 'HDFCBANK', 'HDFCLIFE', 'HEROMOTOCO', 'HINDALCO', 'HINDPETRO', 'HINDUNILVR', 'IBULHSGFIN', 'ICICIBANK','ICICIPRULI', 'IDEA', 'IGL', 'INDIGO', 'INDUSINDBK', 'INDUSTOWER', 'INFY', 'IOC', 'IRCTC', 'ITC', 'JINDALSTEL', 'JSWSTEEL', 'JUBLFOOD', 'KOTAKBANK', 'LICHSGFIN', 'LT', 'LTI','LUPIN', 'MANAPPURAM', 'MARICO', 'MARUTI','MFSL', 'MGL', 'MINDTREE', 'MOTHERSUMI', 'MPHASIS', 'MRF', 'MUTHOOTFIN', 'NAUKRI', 'NESTLEIND', 'NMDC', 'NTPC', 'ONGC', 'PAGEIND', 'PEL', 'PETRONET', 'PFC','PIDILITIND', 'PNB', 'POWERGRID', 'PVR', 'RAMCOCEM', 'RBLBANK', 'RELIANCE','SAIL','SBILIFE', 'SBIN', 'SHREECEM', 'SIEMENS','SRTRANSFIN', 'SUNPHARMA', 'TATACHEM', 'TATACONSUM', 'TATAMOTORS', 'TATAPOWER', 'TATASTEEL', 'TCS', 'TECHM', 'TITAN', 'TORNTPHARM', 'TORNTPOWER', 'TRENT', 'TVSMOTOR', 'UBL', 'ULTRACEMCO', 'UPL', 'VEDL', 'VOLTAS', 'WIPRO', 'ZEEL']

url = f'https://in.finance.yahoo.com/quote/^NSEBANK'

page = requests.get(url,headers = header )
# print(page)
soup = BeautifulSoup(page.text,'lxml')
# <span class="Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)" data-reactid="32">14,137.35</span>
################ For Only Value #################
# for i in soup.find_all('span',class_="Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)"):
#         print(i.text)
banknifty_value = ''
Nifty_value = ''
Sensex_value =''
Dollor_value = ''
try:
    for i in soup.find_all('div',class_="D(ib) Mend(20px)"):
    # for i in soup.find_all('div',class_="Pos(r) Bxz(bb) Mstart(a) Mend(a) Ov(h)"):
        banknifty_value = i.text
        # print(banknifty_value)
    index_info = []
    for i in soup.find_all('h3',class_="Maw(160px)"):
    # for i in soup.find_all('div',class_="Pos(r) Bxz(bb) Mstart(a) Mend(a) Ov(h)"):
        index_info.append(i.text)
        # print(d_info)
    # print('dekho ye bina')
    try:
        Nifty_value = index_info[1][index_info[1].index('50')+2:]
        # print('nifty cleared ')
    except:
        pass

    Sensex_value = index_info[0][index_info[0].index('X')+1:]

    Dollor_value = index_info[2][index_info[2].index('NR')+2:]

except Exception as e:
    print(e)
    pass

# for i in NIFTY102:



# NIFTY50 =['ADANIPORTS', 'ASIANPAINT', 'AXISBANK', 'BAJAJ-AUTO', 'BAJFINANCE', 'BAJAJFINSV', 'BPCL', 'BHARTIARTL', 'BRITANNIA', 'CIPLA', 'COALINDIA', 'DIVISLAB', 'DRREDDY', 'EICHERMOT', 'GAIL', 'GRASIM', 'HCLTECH', 'HDFCBANK', 'HDFCLIFE', 'HEROMOTOCO', 'HINDALCO', 'HINDUNILVR', 'HDFC', 'ICICIBANK', 'ITC', 'IOC', 'INDUSINDBK', 'INFY', 'JSWSTEEL', 'KOTAKBANK', 'LT', 'M&M', 'MARUTI', 'NTPC', 'NESTLEIND', 'ONGC', 'POWERGRID', 'RELIANCE', 'SBILIFE', 'SHREECEM', 'SBIN', 'SUNPHARMA', 'TCS', 'TATAMOTORS', 'TATASTEEL', 'TECHM', 'TITAN', 'UPL', 'ULTRACEMCO', 'WIPRO']
####### DataFrame Generation of Last 201 Days(df1 is latest, df201 is last) ########################
count = 1
# import osimport pandas as pd

os.chdir('F:\\new_share_data')
# os.chdir('G:\\Soda')
day_list = os.listdir()
for i in day_list[-1:-3:-1]:
    i = '"'+i+'"'
    # print('doing for count',co unt)
    # try this if not works exec(f"df = pd.read_csv('{i}', names = ['symbol','date','open','high','low','close','volume'],index_col=0)")
    exec((f'df{count}=pd.read_csv({i})'))
    exec((f"df{count}.columns = ['Symbol','Date','Open','High','Low','Close','Volume']"))
    exec(f'df{count}=df{count}.set_index(df{count}["Symbol"])')
    count+=1

# print(df1)
# print(df1.loc['TCS'][4])

def output_old(display_text = 'Candle ',data_list = 'Data not found',font2 = "arial 22 bold",stock_inf= 'Stock info',event=None,opbg_color = 'red' ):
    liss = data_list
    t = ''
    for i in liss:
        try:
            t +=i
            t+='\n'

        except Exception as e:
            print(e)
    output = Tk()
    output.geometry("1600x1000+0+0")
    output.title("Result ")
    
    lab = Label(output,text="NSE || BSE",font="arial 28 bold",bg="#8B008B",fg ='yellow')
    lab.place(x=0,y=0)
    dl = Label(output,text = display_text,font="arial 28 bold",bg="#8B008B")
    dl.place(x=400,y = 10)
    
    if t.count('\n')<15:
        lab2 = Label(output,text=t,font=font2,bg=opbg_color,fg = 'black')
        lab2.place(x=500,y=200)
    else:
        count = 0
        text1=''
        text2 = ''
        text3 = ''
        text4 = ''
        for i in t:
            if i == '\n':
                count+=1
            if count<=14:
                text1+=i
            if 28>count >14:
                text2 += i
            if 58>count>=28:
                text3+=i
            if 58<=count:
                text4+=i
        lab2 = Label(output,text=text1,font=font2,bg=opbg_color,fg = 'black')
        lab2.place(x=0,y=200)
        lab2 = Label(output,text=text2,font=font2,bg=opbg_color,fg = 'black')
        lab2.place(x=400,y=200)
        lab2 = Label(output,text=text3,font=font2,bg=opbg_color,fg = 'black')
        lab2.place(x=800,y=200)
        lab2 = Label(output,text=text4,font=font2,bg=opbg_color,fg = 'black')
        lab2.place(x=1200,y=200)



    output.configure(bg = "brown")
    bqw = Button(output,text = 'quit',font="arial 16 bold",bg="white",fg = 'red',command= output.destroy)
    bqw.place(x=1300,y=950)

################## output Gold ##########################

# def share_info_display(liss = ['','','','','','','']):
#     r = Tk()
#     r.geometry('700x400')

#     l1 = Label(r,text=f'Company_symbol : {liss[0]}',font=("arial 19 bold"))
#     l1.pack()
#     l1 = Label(r,text=f'Date {liss[1][6:]}-{liss[1][4:6]}-{liss[1][:4]}',font=("arial 12 bold"))
#     l1.pack()
#     l1 = Label(r,text=f' LTP      {liss[-2]} ',font=("arial 19 bold"))
#     l1.pack()
#     l1 = Label(r,text=f'Open     {liss[2]}',font=("arial 12"))
#     l1.pack()
#     l1 = Label(r,text=f'{liss[4]} < ----------------- > {liss[3]}  ',font=("arial 12 bold"))
#     l1.pack()
#     if float(liss[2])<=float(liss[-2]):
#         r.config(bg = '#009900')
#     else:
#         r.config(bg = '#990000')


#     exit_button = Button(r, text=" Exit ", font=("arial 15 bold"),fg="green",bg='red',command=r.destroy)
#     exit_button.place(x=350, y=300)


def output_gold(display_text = 'Candle ',data_l = 'Data not found',font2 = "arial 22 bold",stock_inf= 'Stock info',event=None,opbg_color = 'red',sound = False):
    output = Tk()
    # Toplevel() 
    output.geometry("1600x1000+0+0")
    output.title("Result ")
    # p = PhotoImage(master = output,file = 'D:\\Projects ready for Git\\1.png',height = 1000,width = 1300)
    # k = Label(output,image = p)
    # k.place(x=0, y=0, relwidth=1, relheight=1)
    lab = Label(output,text="NSE || BSE",font="arial 28 bold",bg="#8B008B",fg ='yellow')
    lab.place(x=0,y=0)
    dl = Label(output,text = display_text,font="arial 28 bold",bg="#8B008B")
    dl.place(x=400,y = 10)
    # k.pack()
    liss = data_l
        # buy_list = liss[0]
        # sell_list = liss[1]
        # print('this is buy',buy_list)
        # print('this is sell',sell_list)
        # print(liss)
    def scroll(x, y):
        # share.yview(x,y)
        B1.yview(x,y)
    # m_textbox.yview(x,y)
        # buy1.yview(x,y)

    output.config(bg = '#8B008B')
    # label = Label(output, 
    #           text = f"   ", 
    #           font = ("Arial", 30,'bold'),  
    #           fg = 'white',bg = '#8B008B')
    # label.pack()
    scrollbar = Scrollbar(output)

    # def selected(event):
    #     widget = event.widget
    #     selection=widget.curselection()
    #     # print('selection [0] is',selection[0])
    #     picked = widget.get(selection[0])
    #     picked_symbol = picked.strip()
    #     # print('thisf is picked',picked_symbol)
    #     try:
    #         k = share_info(picked_symbol)
    #         share_info_display(k)
    #         # print('direct ',picked[0])
    #     except Exception as e:
    #         print(e)
        # print(event)


    B1 = Listbox(output, yscrollcommand = scrollbar.set,fg = 'black',bg = opbg_color)
    B1.config(font = ('Arial',19,'bold'))
    # B1.place(relx=0.25, rely=0.2,relwidth=.45,relheight=.8)
    B1.place(relx=0.1, rely=0.2,relwidth=.8,relheight=.8)
    # B1.bind('<<ListboxSelect>>',selected)
    # sell1 = Listbox(output, yscrollcommand = scrollbar.set)
    # sell1.config(font = ('Arial',16,'bold'),fg = 'black',bg = '#990000')
    # sell1.bind('<<ListboxSelect>>',selected)
    # sell1.place(relx=0.5, rely=0.1,relwidth=0.49,relheight=1)

    scrollbar.config(command = scroll)
    scrollbar.place(relx = 0.99, relwidth = 0.05,relheight = 1)

    for i in liss:
        B1.insert(END,'                      '+ str(i)+"\n")
    # for i in sell_list:
    #     sell1.insert(END,  str(i)+"\n")
        # m_textbox.insert(tk.INSERT, str(i)+"\n")
    #         list.insert(END, x[each_item]) 
    # list.itemconfig(each_item, bg = "lime") 
        B1.place()
        # m_textbox.place()
        # sell1.place()
    exit_button = Button(output, text=" Exit ", font=("arial 15 bold"),fg="green",bg='red',command=output.destroy)
    exit_button.place(x=1380, y=880)
    # output.mainloop()
    if sound == True:
        if len(liss) >= 1:
            winsound.PlaySound('D:\\rated screener\\pi.wav',winsound.SND_LOOP)


####################################################################################################
label = Label(window,text="Rated Intra-SCREENER",font=("arial 40 bold"),bg="#8B008B",fg="yellow")
label.place(x=500,y=0)




lab = Label(window,text="NSE || BSE",font="arial 20 bold",bg="#8B008B")
lab.place(x=0,y=0)
lab = Label(window,text="Nifty : "+Nifty_value,font="arial 11 bold",bg="#8B008B",fg = '#00FF00')
if '-' in Nifty_value:
    lab.config(fg = '#FF0000')
lab.place(x=0,y=40)
lab = Label(window,text="Sensex : "+Sensex_value,font="arial 10 bold",bg="#8B008B",fg = '#00FF00')
if '-' in Sensex_value:
    lab.config(fg = '#FF0000')
lab.place(x=0,y=70)
lab = Label(window,text="Dollor : "+Dollor_value,font="arial 10 bold",bg="#8B008B",fg = '#00FF00')
if '-' in Dollor_value:
    lab.config(fg = '#FF0000')
lab.place(x=0,y=100)

lab = Label(window,text="BankNifty : "+banknifty_value,font="arial 10 bold",bg="#8B008B",fg = '#00FF00')
if '-' in banknifty_value:
    lab.config(fg = '#FF0000')
lab.place(x=0,y=130)
latest_file = os.listdir()[-1][:10]+'  NSE'
dates = datetime.date.today()
label_class_3 = Label(window,text=f'Today : {dates}',font=("arial 20 bold"),bg="#8B008B")
label_class_3.place(x=1450,y=0)
label_class_4 = Label(window,text="DATA AVAILABLE",font=("arial 17 bold"),bg="#8B008B")
label_class_4.place(x=1480,y=50)
label_class_5 = Label(window,text=latest_file,font=("arial 20 bold"),bg="#8B008B")
label_class_5.place(x=1500,y=100) 
# N2 = ['ACC', 'ABBOTINDIA', 'ADANIGREEN', 'ADANIPORTS', 'ADANITRANS', 'ALKEM','ULTRACEMCO', 'UBL', 'MCDOWELL-N', 'WIPRO','ZEEL','NCC','ye','dfs','dasf','dasfdasf']
#############################################################################################################



LTRADE = Button(window, text="Live Trades ", font=("arial 15 bold"),bg= 'yellow',fg= 'black')
LTRADE.place(x=0, y=350)
Profit_button = Label(window, text="On Breakout of ", font=("arial 15 bold"),bg= '#000055',fg= 'white')
Profit_button.place(x=0, y=410)
############## Getting Prev Day High Low ##########################################
# def pday_high(event = None,Bullish = True, Bearish = True):
    # pass
    # look_for()

    # output_LIST(display_text = 'Candle ',data_l = 'Data not found',font2 = "arial 22 bold",stock_inf= 'Stock info',event=None,opbg_color = 'red',SR_output = False )
    # data_l,msg = [['tcs','infy'],['wipro','techm']],'this stocks near high low'
    # # data_l,msg = Doji_finding()
    # display_text = 'All H&L at \n'+ msg
    # output(display_text,data_l)
    # high_low(display_text,data_l)    
    # output_LIST()
##############################################################################################################
def eng_all():
# def engulf_candle():
        ##########fieldnames = ['Symbol','Date','Open','High','Low','Close','Volume']
    Engulf_candle = []
    Body_engulf = []
    # Complete_engulf
    # ins_candle_weekly = []
    # k = []
    for sym in NIFTY100:
        if df2.loc[sym][3]>df1.loc[sym][3]:
            if df2.loc[sym][4]<df1.loc[sym][4]:
                Engulf_candle.append(sym)
                
    return Engulf_candle
##############################################################################################################


########################### Live Data ######################################################
def stock(symbol):
    url = f'https://query1.finance.yahoo.com/v8/finance/chart/{symbol}.NS'
    d = requests.get(url, headers = header)
    data = d.json()

    # symbol = data['chart']['result'][0]['meta']['symbol']
    # previousClose = data['chart']['result'][0]['meta']['chartPreviousClose']

    timestamp1min = data['chart']['result'][0]['timestamp']
    Last_candle_time = [datetime.datetime.fromtimestamp(tic).strftime('%c') for tic in timestamp1min]
    All_candle_open = data['chart']['result'][0]['indicators']['quote'][0]['open']
    All_candle_high = data['chart']['result'][0]['indicators']['quote'][0]['high']
    All_candle_low  = data['chart']['result'][0]['indicators']['quote'][0]['low']
    All_candle_volume = data['chart']['result'][0]['indicators']['quote'][0]['volume']
    All_candle_closing = data['chart']['result'][0]['indicators']['quote'][0]['close']
    
    ##########fieldnames = ['Symbol','Date','Open','High','Low','Close','Volume']

    All_Data_D = {'time':[Last_candle_time],'open':[All_candle_open],'high':[All_candle_high],'low':[All_candle_low],'close':[All_candle_closing],'volume':[All_candle_volume]}
    # print(vars()[symbol])
    symbol = 'dfl_'+symbol[:-3]
    vars()[symbol]=pd.DataFrame(All_Data_D)
    # return dfl_SBIN    ['time', 'open', 'high', 'low', 'close', 'volume']
    return vars()[symbol]

# for i in NIFTY50:
#     try:
#         if i == 'BAJAJ-AUTO':
#             exec(f"dfl_BAJAJAUTO = stock('{i}')")
#         elif i == 'M&M':
#             exec(f"dfl_MM = stock('{i}')")
 
#             # name = i[:i.index('-')]+'_'+i[i.index('-')+1:]
#             # print(name)
#         else:
#             exec(f"dfl_{i} = stock('{i}')")
#     except Exception as e:
#         print(e)
#         print('happening for ',i)
#         pass


################################ Graph Plot #########################################################
from matplotlib import pyplot as plt

def graph_plot(sym):
# print(dfl_GAIL)
    time_list = []
    close_list = []
    exec(f"dfl_{sym} = stock('{sym}')")
    exec(f"time_list.append(dfl_{sym}.loc[0][0])")
    exec(f"close_list.append(dfl_{sym}.loc[0][-2])")
    # print(time_list)
    # print(close_list)

    # def graph_plot(sym,d):
    # # plt.plot(Dates,ltp)
    time_list = time_list[0]
    tml = [x for x in range(len(time_list))]
    # print(time_list)
    # print(tml)
    close_list = close_list[0]
    # print(len(time_list))
    # print(len(close_list))
    # Sym,Dates,Open,High,Low,ltp,vol = get_symbol_data(symbol = sym,days = d)



    # Dates.sort()
    # Dates = [ str(x) for x in Dates]
    # Dates = [(x[-4:-2]+'/'+x[-6:-4]) for x in Dates]

    # Dates = [x for x in df1.loc['Symbol']]
    # print(Dates)
    # ltp.reverse()
    # High.reverse()
    # ltp = close_list[-1]

    try:
        mltp = max(filter(None,close_list))
        lltp = min(filter(None,close_list))
        mltp = round(mltp,3)
        lltp = round(lltp,3)
        ltp = round(close_list[-1],3)
        # print('here mltp is ',mltp)
        # print('here lltp is ',lltp)
    except:
        ltp = round(close_list[-2],3)

    fig = plt.figure(sym+' '+str(ltp))
    # # plt.legend()
    plow = float(df1.loc[sym][4])
    pclose = float(df1.loc[sym][5])
    phigh = float(df1.loc[sym][3])
    plt.title(f'(prevDay High {phigh})               {sym}      LTP  {str(round(ltp, 2))}           ({plow} prevDay Low)',fontsize=18)

    plt.xlabel(f'{time_list[0]}           to              {time_list[-1]} ',fontsize=18)
    plt.ylabel(f'{pclose} prevClose    ' ,fontsize=12,rotation = 0)

    # # plt.bar(Dates,vol)
    # plt.plot(plow,color = 'g')
    
    plt.plot(tml,close_list,color = 'b',label = 'High',linewidth = 4)
    # if close_list[-1]>float(phigh):
    #     plt.axhline(float(phigh), color='b')
    # else:
    #     plt.axhline(float(plow), color='r')

    # if ltp<phigh:
    #     plt.axhline(pclose, color='b')
    #     if .9*ltp<pclose:
    #         plt.axhline(pclose, color='y')

    if mltp >= phigh*.988 and mltp>pclose:
        plt.axhline(phigh, color='g')
    if ((lltp <= pclose*1.025) and (mltp>plow)) or ((mltp >= pclose*1.025) and (lltp < phigh)):
        plt.axhline(pclose, color='b')

    if lltp <=plow*1.025:
        plt.axhline(plow, color='r')




    # if ltp>phigh:
    #     plt.axhline(phigh, color='g')
    #     if lltp<pclose:
    #         plt.axhline(pclose, color='b')
        



    # if phigh>ltp>pclose:
    #     if abs(phigh-ltp)>abs(plow-ltp):
    #         plt.axhline(plow, color='r')
    #     else:
    #         plt.axhline(phigh, color='g')
    #     plt.axhline(pclose, color='b')


    # if pclose>ltp>plow:
    #     plt.axhline(pclose, color='b')
    #     if abs(ltp-plow)>abs(ltp-phigh):
    #         plt.axhline(phigh, color='g')
    #     else:
    #         plt.axhline(plow, color='r')

    # if ltp<plow:            
    #     plt.axhline(plow, color='r')
    #     if mltp>pclose:
    #         plt.axhline(pclose, color='b')


    # else:
    #     plt.axhline(plow, color='r')


    # ax.set_facecolor("orange")
    # ax.set_facecolor("orange")
    # OR
    # ax = plt.axes()
    # ax.set(facecolor = "#666666")

    plt.show()

#################################################################################################################
pos = 0
r = 0
f = Frame(window)
f.pack(side = BOTTOM)
for i in NIFTY102:
    # f.place(x = 0,y = 850)
    # command=partial(change_label_number, 2)
    # Profit_button = Button(f, text=' '+i, font=("arial 9 bold"),bg= '#FFFF00',fg= 'black',width = 12,command = partial(graph_plot,i))
    Profit_button = Button(f, text=' '+i, font=("arial 9 bold"),bg= '#FFFF00',fg= 'black',width = 12,command = partial(graph_plot,i))

    # Profit_button.grid(row=pos, y=850)    
    # print(pos)
    Profit_button.grid(row=r,column = pos,padx = 1,pady=1)    
    pos+=1
    if pos>=13:
        r+=1
        pos = 0
    # pos= 50+len(i)*50

# count = 0
# for i in range(3):
#     for j in range(3):
#         # if j < 3 and i<3:
#         count+=1
#         btn = Button(f1,text = count,font = font,width = 4,height = 1)
#         btn.grid(row = i, column = j,padx = 2,pady = 2)
#         btn.bind('<Button-1>',fn)

################# 5 min Analysis ########################################################
################# 5 min Analysis ########################################################
# sorted(kx)[:2:-1]

# from random import randint
# liss = [randint(1,21) for i in range(31)]
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29]

# print(liss)
# stock_name = 'RELIANCE'
# high_price_5min = []

def five_min_scan(interval):

    # close_list5 = []
    high_vol_5min = []
    def vol_scan(stock_name = 'RELIANCE',interval = 5):

        vol_list5 = []
        exec(f"dfl_{stock_name} = stock('{stock_name}')")
        # exec(f"time_list.append(dfl_{sym}.loc[0][0])")
        # exec(f"close_list5.append(dfl_{stock_name}.loc[0][-2])")
        exec(f"vol_list5.append(dfl_{stock_name}.loc[0][-1])")
        # vol_list5[-1]

        # print(vol_list5)
        kx = []
        # count = 5
        count = interval
        ki = 0
        # for i in range(0,len(liss)//5):
            # kx.append(sum(liss[ki:count]))
        #     count+=5
        #     ki+=5
        # print(len(vol_list5))
        vol_list5 =vol_list5[0]
        # for i in range(0,len(vol_list5)//5):
        for i in range(0,len(vol_list5)//interval):

        #     # print(sum(liss[ki:count]))
            # print('here i',i,len(vol_list5))
            try:
                kx.append(sum(vol_list5[ki:count]))
            except:
                # sum(filter(None, [1,2,3,None]))
                # kx.append(sum(filter(None,vol_list5[ki:count])))
                continue
            count+=interval
            ki+=interval

        last_vol = kx[-1]
        # if last_vol in sorted(kx)[:2:-1]:
        # if last_vol in sorted(kx)[:-4:-1]:
        if kx[-1] in sorted(kx)[:-4:-1]:
            high_vol_5min.append(stock_name)


        # print('all kx ',kx)
        # print(dfl_RELIANCE)
        return high_vol_5min

    for i in NIFTY102[:20]:
        # print('doing for ',i)
        data_l = vol_scan(i,interval)
    # print('All stocks with higher volume in last 15 min ',high_vol_5min)
    output_old(display_text = f'Higher Volume Candle in Last {interval} min time',data_list = data_l) 

# five_min_scan(interval=20)
################################ Bullish min Scan #################################################

def bullish_min_scan(interval):

    # close_list5 = []
    bullish_min = []
    def bullish_scan(stock_name = 'RELIANCE',interval = 5):

        bullish_list5 = []
        exec(f"dfl_{stock_name} = stock('{stock_name}')")
        # exec(f"time_list.append(dfl_{sym}.loc[0][0])")
        # exec(f"close_list5.append(dfl_{stock_name}.loc[0][-2])")
        exec(f"bullish_list5.append(dfl_{stock_name}.loc[0][-2])")
        # bullish_list5[-1]

        # print(bullish_list5)
        kx = []
        # count = 5
        count = interval
        ki = 0
        # for i in range(0,len(liss)//5):
            # kx.append(sum(liss[ki:count]))
        #     count+=5
        #     ki+=5
        # print(len(bullish_list5))
        bullish_list5 =bullish_list5[0]
        # for i in range(0,len(bullish_list5)//5):
        for i in range(0,len(bullish_list5)//interval):

        #     # print(sum(liss[ki:count]))
            # print('here i',i,len(bullish_liqt5))
            try:
                kx.append(sum(bullish_list5[ki:count]))
            except:
                # sum(filter(None, [1,2,3,None]))
                # kx.append(sum(filter(None,bullish_list5[ki:count])))
                continue
            count+=interval
            ki+=interval

        last_bullish = kx[-1]
        # if last_bullish in sorted(kx)[:2:-1]:
        # if last_bullish in sorted(kx)[:-4:-1]:
        if kx[-1] in sorted(kx)[:-4:-1]:
            bullish_min.append(stock_name)


        # print('all kx ',kx)
        # print(dfl_RELIANCE)
        return bullish_min

    for i in NIFTY102:
        # print('doing for ',i)
        data_l = bullish_scan(i,interval)
    # print('All stocks with higher volume in last 15 min ',bullish_min)
    output_old(display_text = f'Higher Price Candle in Last {interval} min time',data_list = data_l) 

###################################     Bearish        ########################################################

def bearish_min_scan(interval):

    # close_list5 = []
    bearish_min = []
    def bearish_scan(stock_name = 'RELIANCE',interval = 5):

        bearish_list5 = []
        exec(f"dfl_{stock_name} = stock('{stock_name}')")
        # exec(f"time_list.append(dfl_{sym}.loc[0][0])")
        # exec(f"close_list5.append(dfl_{stock_name}.loc[0][-2])")
        exec(f"bearish_list5.append(dfl_{stock_name}.loc[0][-2])")
        # bearish_list5[-1]

        # print(bearish_list5)
        kx = []
        # count = 5
        count = interval
        ki = 0
        # for i in range(0,len(liss)//5):
            # kx.append(sum(liss[ki:count]))
        #     count+=5
        #     ki+=5
        # print(len(bearish_list5))
        bearish_list5 =bearish_list5[0]
        # for i in range(0,len(bearish_list5)//5):
        for i in range(0,len(bearish_list5)//interval):

        #     # print(sum(liss[ki:count]))
            # print('here i',i,len(bearish_list5))
            try:
                kx.append(sum(bearish_list5[ki:count]))
            except:
                # sum(filter(None, [1,2,3,None]))
                # kx.append(sum(filter(None,bearish_list5[ki:count])))
                continue
            count+=interval
            ki+=interval

        last_bearish = kx[-1]
        # if last_bearish in sorted(kx)[:2:-1]:
        # if last_bearish in sorted(kx)[:-4:-1]:
        if kx[-1] in sorted(kx)[:3]:
            bearish_min.append(stock_name)


        # print('all kx ',kx)
        # print(dfl_RELIANCE)
        return bearish_min

    for i in NIFTY102:
        # print('doing for ',i)
        data_l = bearish_scan(i,interval)
    # print('All stocks with higher volume in last 15 min ',bullish_min)
    output_old(display_text = f'Bearish Price Candle in Last {interval} min time',data_list = data_l) 

###########################################################################################
###########################################################################################
l1 = Label(window,text = 'Volume',font = ('arial 15 bold'),bg ="#8B008B",fg = 'yellow')
l1.place(x = 1790, y = 190)
Profit_button = Button(window, text=" 3 min", font=("arial 12 bold"),bg= 'gray',fg= 'white',command = partial(five_min_scan,3))
Profit_button.place(x=1800, y=240)
Profit_button = Button(window, text=" 5 min", font=("arial 12 bold"),bg= 'gray',fg= 'white',command = partial(five_min_scan,5))
Profit_button.place(x=1800, y=300)
Profit_button = Button(window, text="15 min", font=("arial 12 bold"),bg= 'gray',fg= 'white',command = partial(five_min_scan,15))
Profit_button.place(x=1800, y=360)
Profit_button = Button(window, text="30 min", font=("arial 12 bold"),bg= 'gray',fg= 'white',command = partial(five_min_scan,30))
Profit_button.place(x=1800, y=420)

#####################################################################################
#####################################################################################
#####################################################################################
l1 = Label(window,text = 'Bullish',font = ('arial 15 bold'),bg ="#8B008B",fg = '#00FF00')
l1.place(x = 1490, y = 190)
Profit_button = Button(window, text=" 3 min", font=("arial 12 bold"),bg= 'gray',fg= 'white',command = partial(bullish_min_scan,3))
Profit_button.place(x=1500, y=240)
Profit_button = Button(window, text=" 5 min", font=("arial 12 bold"),bg= 'gray',fg= 'white',command = partial(bullish_min_scan,5))
Profit_button.place(x=1500, y=300)
Profit_button = Button(window, text="15 min", font=("arial 12 bold"),bg= 'gray',fg= 'white',command = partial(bullish_min_scan,15))
Profit_button.place(x=1500, y=360)
Profit_button = Button(window, text="30 min", font=("arial 12 bold"),bg= 'gray',fg= 'white',command = partial(bullish_min_scan,30))
Profit_button.place(x=1500, y=420)

#####################################################################################
l1 = Label(window,text = 'Bearish',font = ('arial 15 bold'),bg ="#8B008B",fg = 'red')
l1.place(x = 1640, y = 190)
Profit_button = Button(window, text=" 3 min", font=("arial 12 bold"),bg= 'gray',fg= 'white',command = partial(bearish_min_scan,3))
Profit_button.place(x=1650, y=240)
Profit_button = Button(window, text=" 5 min", font=("arial 12 bold"),bg= 'gray',fg= 'white',command = partial(bearish_min_scan,5))
Profit_button.place(x=1650, y=300)
Profit_button = Button(window, text="15 min", font=("arial 12 bold"),bg= 'gray',fg= 'white',command = partial(bearish_min_scan,15))
Profit_button.place(x=1650, y=360)
Profit_button = Button(window, text="30 min", font=("arial 12 bold"),bg= 'gray',fg= 'white',command = partial(bearish_min_scan,30))
Profit_button.place(x=1650, y=420)

#################  Top Gainer & Loosers             ####################################################################


def top_gainer_pd():
    # p = df1.sort_values(by = 'Close')
    global per_change
    per_change = {}
    per_change_liss = []

    # x = current_value , x*100/y

    for i in NIFTY102:
        exec(f"per_change[i] = (float(df1.loc[i][-2])*100/float(df2.loc[i][-2]))")
    # print(per_change)
    # sorted(d.items(), key=lambda x: x[1], reverse=True)
    # print('*'*323)
    y = sorted(per_change.items(), key=lambda x: x[1], reverse=True)
    # print(type(y))
    try:
        dt = []
        exec(f"dt.append(str(df1.loc['TCS'][1]))")
        dt = str(dt[0][-2:]+'/'+dt[0][-4:-2]+'/'+dt[0][:-4])
        # print(dt,'dt')
        # exec(f"dt.append(str(df1.loc['TCS'][1])[-2:]+'/'+str(df1.loc['TCS'][1])[-4:-2])+'/'+str(df1.loc['TCS'][1])[:-4])")
        display_text = 'Top Gainer on Date   '+dt[0]
        for i in y:
            # pchange = round(i[1]%100,3)
            pchange = round(i[1],3)
            # Date = str(df1.loc['{i[0]}'][1])
            # Date = Date[6:]+"-"+Date[4:6]+"-"+Date[:4]
            # print('this is DAte ',Date)
            if pchange>100:
                # print('here pchange is ',pchange,'>100')
                # per_change_liss.append(i[0]+' '+str(pchange))
                exec(f"per_change_liss.append(i[0]+'                  '+str(round(pchange%100,2))+'%  '+'------------- >'+str(df1.loc['{i[0]}'][-2]))")
                # exec(f"per_change_liss.append(i[0]+' '+str(pchange%100)%+'  '+ str(df1.loc['{i[0]}'][1])+' close price '+str(df1.loc['{i[0]}'][-2])')")
            # per_change_liss.append(i[0]+str(i[1]%100))
        # print('Final ',per_change_liss)
    except Exception as e:
        print(e)

    output_gold(data_l = per_change_liss, display_text = 'Top Gainer on date '+dt,opbg_color = 'green')
#################################################################################################
def top_loser_pd():
    # p = df1.sort_values(by = 'Close')
    global per_change
    per_change = {}
    per_change_liss = []

    # x = current_value , x*100/y

    for i in NIFTY102:
        exec(f"per_change[i] = (float(df1.loc[i][-2])*100/float(df2.loc[i][-2]))")
    # print(per_change)
    # sorted(d.items(), key=lambda x: x[1], reverse=True)
    # print('*'*323)
    y = sorted(per_change.items(), key=lambda x: x[1])
    # print(type(y))
    try:
        dt = []
        exec(f"dt.append(str(df1.loc['TCS'][1]))")
        dt = str(dt[0][-2:]+'/'+dt[0][-4:-2]+'/'+dt[0][:-4])
        # print(dt,'dt')
        # exec(f"dt.append(str(df1.loc['TCS'][1])[-2:]+'/'+str(df1.loc['TCS'][1])[-4:-2])+'/'+str(df1.loc['TCS'][1])[:-4])")
        display_text = 'Top Gainer on Date   '+dt[0]
        for i in y:
            # pchange = round(i[1]%100,3)
            pchange = round(i[1],3)
            # Date = str(df1.loc['{i[0]}'][1])
            # Date = Date[6:]+"-"+Date[4:6]+"-"+Date[:4]
            # print('this is DAte ',Date)
            # print(pchange,' pchange')
            if pchange<100:
                # print('here pchange is ',pchange,'>100')
                # per_change_liss.append(i[0]+' '+str(pchange))
                exec(f"per_change_liss.append(i[0]+'                  '+str(round(pchange-100,2))+'%  '+'------------- >'+str(df1.loc['{i[0]}'][-2]))")
                # exec(f"per_change_liss.append(i[0]+' '+str(pchange%100)%+'  '+ str(df1.loc['{i[0]}'][1])+' close price '+str(df1.loc['{i[0]}'][-2])')")
            # per_change_liss.append(i[0]+str(i[1]%100))
        # print('Final ',per_change_liss)
    except Exception as e:
        print(e)

    output_gold(data_l = per_change_liss, display_text = 'Top Looser on date '+dt,opbg_color = 'red')

##############################Live Top Gainer                 ###################################################################
# def live_top_gainer():
#     global per_change
#     per_change = {}
#     per_change_liss = []

#     # x = current_value , x*100/y

#     for i in NIFTY102:
#         exec(f"per_change[i] = (float(df1.loc[i][-2])*100/float(df2.loc[i][-2]))")
#     # print(per_change)
#     # sorted(d.items(), key=lambda x: x[1], reverse=True)
#     # print('*'*323)
#     y = sorted(per_change.items(), key=lambda x: x[1], reverse=True)
#     # print(type(y))
#     try:
#         dt = []
#         exec(f"dt.append(str(df1.loc['TCS'][1]))")
#         dt = str(dt[0][-2:]+'/'+dt[0][-4:-2]+'/'+dt[0][:-4])
#         # print(dt,'dt')
#         # exec(f"dt.append(str(df1.loc['TCS'][1])[-2:]+'/'+str(df1.loc['TCS'][1])[-4:-2])+'/'+str(df1.loc['TCS'][1])[:-4])")
#         display_text = 'Top Gainer on Date   '+dt[0]
#         for i in y:
#             # pchange = round(i[1]%100,3)
#             pchange = round(i[1],3)
#             # Date = str(df1.loc['{i[0]}'][1])
#             # Date = Date[6:]+"-"+Date[4:6]+"-"+Date[:4]
#             # print('this is DAte ',Date)
#             if pchange>100:
#                 # print('here pchange is ',pchange,'>100')
#                 # per_change_liss.append(i[0]+' '+str(pchange))
#                 exec(f"per_change_liss.append(i[0]+'                  '+str(round(pchange%100,2))+'%  '+'------------- >'+str(df1.loc['{i[0]}'][-2]))")
#                 # exec(f"per_change_liss.append(i[0]+' '+str(pchange%100)%+'  '+ str(df1.loc['{i[0]}'][1])+' close price '+str(df1.loc['{i[0]}'][-2])')")
#             # per_change_liss.append(i[0]+str(i[1]%100))
#         # print('Final ',per_change_liss)
#     except Exception as e:
#         print(e)

#     output_gold(data_l = per_change_liss, display_text = 'Top Gainer on date '+dt,opbg_color = 'green')
#################################################################################################
####################### Live High ############################################
def live_high():
    global per_change
    per_change = {}
    per_change_liss = []

    # x = current_value , x*100/y


 # ['time', 'open', 'high', 'low', 'close', 'volume']
    for i in NIFTY102:
##############################################################################################
        url = f'https://query1.finance.yahoo.com/v8/finance/chart/{i}.NS'
        d = requests.get(url, headers = header)
        data = d.json()
        All_candle_high = data['chart']['result'][0]['indicators']['quote'][0]['high']
        previousClose = data['chart']['result'][0]['meta']['chartPreviousClose']

        high_lmax = max(filter(None,All_candle_high))
        # print('here high_l ',high_lmax)
        y = exec(f"per_change[i] = ({high_lmax}*100/{previousClose})")
        # exec(f"per_change[i] = (float(df1.loc[i][-2])*100/float(df2.loc[i][-2]))")
    # print(per_change)
        y = sorted(per_change.items(), key=lambda x: x[1], reverse=True)
    # print('*'*323)
    # print(type(y))
    try:
        display_text = 'Top High made Today   '
        for ki in y:
            # pchange = round(i[1]%100,3)
            pchange = round(ki[1],3)
            if pchange>100:
                # print('here pchange is ',pchange,'>100')
                # per_change_liss.append(i[0]+' '+str(pchange))
                exec(f"per_change_liss.append(ki[0]+'                  '+str(round(pchange%100,2))+'%  '+'------------- >'+str(df1.loc['{ki[0]}'][-2]))")
                # exec(f"per_change_liss.append(i[0]+' '+str(pchange%100)%+'  '+ str(df1.loc['{i[0]}'][1])+' close price '+str(df1.loc['{i[0]}'][-2])')")
            # per_change_liss.append(i[0]+str(i[1]%100))
        # print('Final ',per_change_liss)
    except Exception as e:
        print(e)
    output_gold(data_l = per_change_liss, display_text = display_text,opbg_color = 'green')










#################################################################################################
################################ Live Low            #################################################################
def live_low():
    global per_change
    per_change = {}
    per_change_liss = []

    # x = current_value , x*100/y


 # ['time', 'open', 'high', 'low', 'close', 'volume']
    for i in NIFTY102:
##############################################################################################
        url = f'https://query1.finance.yahoo.com/v8/finance/chart/{i}.NS'
        d = requests.get(url,headers = header)
        data = d.json()
        All_candle_low = data['chart']['result'][0]['indicators']['quote'][0]['low']
        previousClose = data['chart']['result'][0]['meta']['chartPreviousClose']
        low_lmax = min(filter(None,All_candle_low))
    
        y = exec(f"per_change[i] = ({low_lmax}*100/{previousClose})")
        y = sorted(per_change.items(), key=lambda x: x[1])
    try:
        dt = []
        exec(f"dt.append(str(df1.loc['TCS'][1]))")
        dt = str(dt[0][-2:]+'/'+dt[0][-4:-2]+'/'+dt[0][:-4])
        display_text = 'Top Low made Today   '
        for ki in y:
            pchange = round(ki[1],3)
            if pchange<100:
                # print('here pchange is ',pchange,'>100')
                exec(f"per_change_liss.append(ki[0]+'                  '+str(round(100-pchange,2))+'%  '+' from pDay close ------------- >'+str(df1.loc['{ki[0]}'][-3]))")
    except Exception as e:
        print(e)
    output_gold(data_l = per_change_liss, display_text = display_text+dt,opbg_color = 'red')

##########################################################################################################################
######################   Top Gainer              ####################################################################################################
def top_gainer_today ():
    global per_change
    per_change = {}
    per_change_liss = []
    # x = current_value , x*100/y
 # ['time', 'open', 'high', 'low', 'close', 'volume']
    for i in NIFTY102:
##############################################################################################
        url = f'https://query1.finance.yahoo.com/v8/finance/chart/{i}.NS'
        d = requests.get(url,headers = header)
        data = d.json()
        previousClose = data['chart']['result'][0]['meta']['chartPreviousClose']
        close_latest = data['chart']['result'][0]['indicators']['quote'][0]['close'][-1]
        if close_latest == None:
            close_latest = data['chart']['result'][0]['indicators']['quote'][0]['close'][-2]
            # close_latest = max(filter(None,All_candle_high))
        # close_latest = All_candle_closing[-1]
        # if close_latest == None:
        #     close_latest = All_candle_closing[-2]
        # print('here high_l ',high_lmax)
        y = exec(f"per_change[i] = ({close_latest}*100/{previousClose})")
        # exec(f"per_change[i] = (float(df1.loc[i][-2])*100/float(df2.loc[i][-2]))")
    # print(per_change)
    y = sorted(per_change.items(), key=lambda x: x[1], reverse=True)
    try:
        # exec(f"dt.append(str(df1.loc['TCS'][1])[-2:]+'/'+str(df1.loc['TCS'][1])[-4:-2])+'/'+str(df1.loc['TCS'][1])[:-4])")
        display_text = 'Top Gainer Live Today   '
        for ki in y:
            # pchange = round(i[1]%100,3)
            pchange = round(ki[1],3)
            # Date = str(df1.loc['{i[0]}'][1])
            # Date = Date[6:]+"-"+Date[4:6]+"-"+Date[:4]
            # print('this is DAte ',Date)
            if pchange>100:
                # print('here pchange is ',pchange,'>100')
                # per_change_liss.append(i[0]+' '+str(pchange))
                exec(f"per_change_liss.append(ki[0]+'                  '+str(round(pchange%100,2))+'%  '+'From ------- >'+str(df1.loc['{ki[0]}'][-2]))")
                # exec(f"per_change_liss.append(i[0]+' '+str(pchange%100)%+'  '+ str(df1.loc['{i[0]}'][1])+' close price '+str(df1.loc['{i[0]}'][-2])')")
            # per_change_liss.append(i[0]+str(i[1]%100))
        # print('Final ',per_change_liss)
    except Exception as e:
        print(e)

    dt = []
    exec(f"dt.append(str(df1.loc['TCS'][1]))")
    dt = str(dt[0][-2:]+'/'+dt[0][-4:-2]+'/'+dt[0][:-4])
    output_gold(data_l = per_change_liss, display_text = display_text+dt,opbg_color = 'green')


##########################################################################################################################

############   Top Looser      #############################################################################################################
def top_looser():
    global per_change
    per_change = {}
    per_change_liss = []

    # x = current_value , x*100/y


 # ['time', 'open', 'high', 'low', 'close', 'volume']
    for i in NIFTY102:
##############################################################################################
        url = f'https://query1.finance.yahoo.com/v8/finance/chart/{i}.NS'
        d = requests.get(url,headers = header)
        data = d.json()
        # All_candle_closing = data['chart']['result'][0]['indicators']['quote'][0]['close']
        previousClose = data['chart']['result'][0]['meta']['chartPreviousClose']

        close_latest = data['chart']['result'][0]['indicators']['quote'][0]['close'][-1]
        if close_latest == None:
            close_latest = data['chart']['result'][0]['indicators']['quote'][0]['close'][-2]
        # low_lmax = min(filter(None,All_candle_low))
        y = exec(f"per_change[i] = ({close_latest}*100/{previousClose})")
    y = sorted(per_change.items(), key=lambda x: x[1])
    try:
        dt = []
        exec(f"dt.append(str(df1.loc['TCS'][1]))")
        dt = str(dt[0][-2:]+'/'+dt[0][-4:-2]+'/'+dt[0][:-4])
        display_text = 'Top Looser today   '
        for ki in y:
            pchange = round(ki[1],3)
            if pchange<100:
                # print('str(pchange)+ ^^ +str(previousClose) ',str(pchange)+' ^^ '+str(previousClose))
                # print('instead ',str(pchange)+' ^^ '+str(previousClose))
                # print('here pchange is ',pchange,'>100')
                # exec(f"per_change_liss.append(ki[0]+'            '+str(round(100-pchange,2))+'%  '+'------------- >'+str(df1.loc['{ki[0]}'][-2])+'('+str(pchange)+' ^^ '+str(previousClose)+')')")
                exec(f"per_change_liss.append(ki[0]+'            '+str(round(100-pchange,2))+'%  '+'From ----- >'+str(df1.loc['{ki[0]}'][-2]))")

    except Exception as e:
        print(e)
    output_gold(data_l = per_change_liss, display_text = display_text+dt,opbg_color = 'red')

##########################################################################################################################

Profit_button = Button(window, text="Live Gainer", font=("arial 12 bold"),bg= 'green',fg= 'white',command = top_gainer_today)
Profit_button.place(x=1080, y=380)
Profit_button = Button(window, text="High", font=("arial 12 bold"),bg= 'green',fg= 'white',command = live_high)
Profit_button.place(x=1240, y=380)
Profit_button = Button(window, text="pday-Gainer", font=("arial 12 bold"),bg= 'green',fg= 'white',command = top_gainer_pd)
Profit_button.place(x=1320, y=380)
Profit_button = Button(window, text="Live Looser", font=("arial 12 bold"),bg= '#AA0000',fg= 'white',command = top_looser)
Profit_button.place(x=1080, y=440)
Profit_button = Button(window, text="Low", font=("arial 12 bold"),bg= '#AA0000',fg= 'white',command = live_low)
Profit_button.place(x=1240, y=440)
Profit_button = Button(window, text="pday Looser", font=("arial 12 bold"),bg= '#AA0000',fg= 'white',command = top_loser_pd)
Profit_button.place(x=1320, y=440)





#####################################################################################3
#####################################################################################3
# def look_for(stocks = NIFTY50):
def pday_high(Bullish,Bearish,event = None):
    # print('Bearish status ',Bearish)
    # print('Bullish status ',Bullish)
    # import threading
# import numpy as np
# from tkinter import *
# import requests
# from bs4 import BeautifulSoup
# import winsound
# import time
    mylist = []
    name = 'High Low Breakout'
    window= Tk()
    window.geometry("1120x960+800+320")
    window.title(name)
    window.configure(bg="#8B008B")
    my_nifty = ['AARTIIND', 'ACC', 'ADANIENT', 'ADANIPORTS', 'ALKEM', 'AMARAJABAT', 'AMBUJACEM', 'APOLLOHOSP', 'APOLLOTYRE', 'ASHOKLEY', 'ASIANPAINT','AUROPHARMA', 'AXISBANK', 'BAJAJFINSV', 'BAJFINANCE', 'BALKRISIND', 'BANDHANBNK', 'BANKBARODA', 'BATAINDIA', 'BEL', 'BERGEPAINT', 'BHARATFORG', 'BHARTIARTL', 'BHEL', 'BIOCON', 'BPCL', 'BRITANNIA', 'CADILAHC', 'CANBK', 'CHOLAFIN', 'CIPLA', 'COALINDIA', 'COFORGE', 'COLPAL', 'CONCOR', 'CUMMINSIND', 'DABUR','DIVISLAB', 'DLF', 'DRREDDY', 'EICHERMOT', 'ESCORTS', 'EXIDEIND', 'FEDERALBNK', 'GAIL', 'GLENMARK', 'GODREJCP', 'GODREJPROP','GRASIM', 'GUJGASLTD', 'HAVELLS', 'HCLTECH', 'HDFC', 'HDFCAMC', 'HDFCBANK', 'HDFCLIFE', 'HEROMOTOCO', 'HINDALCO', 'HINDPETRO', 'HINDUNILVR', 'IBULHSGFIN', 'ICICIBANK','ICICIPRULI', 'IDEA', 'IGL', 'INDIGO', 'INDUSINDBK', 'INDUSTOWER', 'INFY', 'IOC', 'IRCTC', 'ITC', 'JINDALSTEL', 'JSWSTEEL', 'JUBLFOOD', 'KOTAKBANK', 'LICHSGFIN', 'LT', 'LTI','LUPIN', 'MANAPPURAM', 'MARICO', 'MARUTI', 'MGL', 'MINDTREE', 'MOTHERSUMI', 'MPHASIS', 'MRF', 'MUTHOOTFIN', 'NAUKRI', 'NESTLEIND', 'NMDC', 'NTPC', 'ONGC', 'PAGEIND', 'PEL', 'PETRONET', 'PFC','PIDILITIND', 'PNB', 'POWERGRID', 'PVR', 'RAMCOCEM', 'RBLBANK', 'RELIANCE','SBILIFE', 'SBIN', 'SHREECEM', 'SIEMENS','SRTRANSFIN', 'SUNPHARMA', 'TATACHEM', 'TATACONSUM', 'TATAMOTORS', 'TATAPOWER', 'TATASTEEL', 'TCS', 'TECHM', 'TITAN', 'TORNTPHARM', 'TORNTPOWER', 'TRENT', 'TVSMOTOR', 'UBL', 'ULTRACEMCO', 'UPL', 'VEDL', 'VOLTAS', 'WIPRO', 'ZEEL']
    # window.lift()
    # window.wm_iconbitmap('F:\\rated screener\\Auto wala.ico')

    # liss = [i for i in range(1,19)]
    count = 1
    # import os
    os.chdir('F:\\new_share_data')
    day_list = os.listdir()
    for i in day_list[-1:-3:-1]:
        i = '"'+i+'"'
        # print('doing for count',co unt)
        exec((f'df{count}=pd.read_csv({i})'))
        exec((f"df{count}.columns = ['Symbol','Date','Open','High','Low','Close','Volume']"))
        exec(f'df{count}=df{count}.set_index(df{count}["Symbol"])')
        count+=1
        break

    def yo(alert1 = None,symboll = 'HDFCBANK'):
        # print(symboll)
         # global count
        # if alert1:
        name = symboll
        global count
        l21.config(text = symboll)
        window.update()
        # window.attributes('-topmost',True)
        # l1 = Label(window,text = ' ',font = ('LED',15,'bold'))
        # l1.place(x = 50,y = 50)
        # l1.pack(side = TOP)
        url = f'https://query1.finance.yahoo.com/v8/finance/chart/{name}.NS'
        d = requests.get(url,headers = header)
        data = d.json()
        l_high = data['chart']['result'][0]['indicators']['quote'][0]['high']
    # data['chart']['result'][0]['indicators']['quote'][0]['high']
        latest_high = l_high[-1]
        if latest_high == None:
            latest_high = l_high[-2]

        l_low = data['chart']['result'][0]['indicators']['quote'][0]['low']
    # data['chart']['result'][0]['indicators']['quote'][0]['low']
        latest_low = l_low[-1]
        if latest_low == None:
            latest_low = l_low[-2]

        # if (df1.loc[symboll]['high'])*.99 >= latest_high and ((df1.loc[symboll]['high'])*100.05 <= latest_high):
        #   print(f'{symboll} is near it\'s previous day high of {df1.loc["symboll"]["high"]} and now at {latest_high} ')
        prev = df1.loc[symboll]
        p_high = float(prev[3])
        p_low = float(prev[4])
        mltp = max(filter(None,l_high))
        lltp = min(filter(None,l_low))
        # print(' high and low ',p_high,p_low,'and ',prev)
        # print(f'{symboll} is near it\'s previous day high of {df1.loc[symboll]["high"]} and now at {latest_high} ')
        # Bullish = True
        if Bullish:

            # print('this is in bullish')
            if (p_high*.9995<latest_high) and (p_high*1.003)>=latest_high:
                # print(p_high*.9995,'<',latest_high,'<',p_high*1.003)
                # print(f'Stock {symboll} is near to prev day high of {p_high} now trading at {latest_high}')
                # mph = float(max(p_high))
                # mph = max(filter(None,p_high))
                mylist.append('high'+symboll)   
                t = f"{symboll}  close to  pday High {p_high} now @{round(latest_high,3)} Today High {round(mltp,3)} "
                if mltp <= p_high:
                    t = f"{symboll}  close to  pd-High {p_high} now @{round(latest_high,3)}   DayHigh = {round(mltp,3)} crossed=False)"



                p1 = Label(window,text = t,font = ('LED',15,'bold'),bg = 'green')           
                p1.pack()
        if Bearish:
            

            # print('this is in Bearish')
            if (p_low*.9995<=latest_low) and (p_low*1.003>=latest_low):
                # print(p_low*.9995,'<',latest_low,'<',p_low*1.003)
                # lph = max(filter(None,p_low))
                # if lph*.9995> latest_low:
                #   crossed = 'yes'
                # else:
                #   crossed = 'no'
                # print(f'Stock {symboll} is near to prev day low of {p_low} now trading at {latest_low}')
                mylist.append('loww'+symboll)
                tt = f"{symboll}  close to  pday Low {p_low} now @{round(latest_low,3)} Today Low {round(lltp,3)}"
                if lltp>=p_low:
                    tt = f"{symboll}  close to  pday Low {p_low} now @{round(latest_low,3)} DayLow = {round(lltp,3)} crossed = False"

                p1 = Label(window,text = tt,font = ('LED',15,'bold'),bg = '#990000')            
                p1.pack()


        # l1 = Label(window,text = round(latest_high,3),font = ('LED',22,'bold'))
        # l1 = Label(window,text = i,font = ('LED',15,'bold'))
        # l1.place(x = 40,y = 60)
        # l1.pack(side = BOTTOM)

        exit_button = Button(window, text="quit", font=("arial 10 bold"),fg="green",bg='red',command=window.destroy)
        exit_button.place(x = 1060,y =900)
        # print(alert, 'alert')
        # print('latest type',type(latest),' alert type',type(alert))
        # if alert == True:
        #   print('alert baja')

        # # try:

        # if alert1:
        #     alert = float(alert1[:-1])
        #     condition = alert1[-1]
        #     if condition == '-' and count<=2:
        #         if latest <=alert:
        #             # print('alert baja')
        #             winsound.PlaySound('F:\\rated screener\\pi.wav',winsound.SND_LOOP)
        #             count+=1
        #     else:
        #         if latest >= alert and count<=2:
        #             # print('alert baja jyada ke liye')
        #             winsound.PlaySound('F:\\rated screener\\sai.wav',winsound.SND_LOOP)
        #             count+=1

        # # def scroll(x, y,event = None):

        #   # share.yview(x,y)
        #   B1.yview(x,y)
        # scrollbar = Scrollbar(window)
        # B1 = Listbox(window, yscrollcommand = scrollbar.set,fg = 'black')
        # scrollbar.place(relx = 0.99, relwidth = 0.05,relheight = 1)
        # scrollbar.config(command = scroll)


        # except:
        #   pass

    # def yo1():
    #     time.sleep(1)



     

    name = 'HDFCBANK'

    l21 = Label(window,text = name,font = ('LED',15,'bold'))
    l21.pack(side= TOP)

    # for i in range(500):
    for sym in my_nifty:

        # threading.Thread(target=yo1).start()
        # yo(symboll = sym,Bullish = True, Bearish = True)
        yo(symboll = sym)



#####################################################################################3
#####################################################################################3
#####################################################################################3
#####  Look for              ################################################################################3
#old look_for
# def look_for(stocks = NIFTY50):
    
#     onBreakout_liss_low = []
#     onBreakout_liss_high = []
#     for i in stocks:
#         url = f'https://query1.finance.yahoo.com/v8/finance/chart/{i}.NS'
#         d = requests.get(url)
#         data = d.json()
#         # All_candle_closing = data['chart']['result'][0]['indicators']['quote'][0]['close']
#         # previousClose = data['chart']['result'][0]['meta']['chartPreviousClose']

# # This below code can also be used

#         # low_latest = data['chart']['result'][0]['indicators']['quote'][0]['low'][-1]

#         # if low_latest == None:
#         #     low_latest = data['chart']['result'][0]['indicators']['quote'][0]['low'][-2]


#         # high_latest = data['chart']['result'][0]['indicators']['quote'][0]['high'][-1]
#         # if high_latest == None:
#         #     high_latest = data['chart']['result'][0]['indicators']['quote'][0]['high'][-2]
#         latest = data['chart']['result'][0]['indicators']['quote'][0]['close'][-1]
#         if latest == None:
#             latest = data['chart']['result'][0]['indicators']['quote'][0]['close'][-2]


#         plow = float(df1.loc[i][4])
#         pclose = float(df1.loc[i][5])
#         phigh = float(df1.loc[i][3])
#         # print(i,' ka high he ',phigh)
#         # print(i+' close to Previous Day Low of '+str(plow)+'at '+str(low_latest),'which is ',str(plow*.8)+'>'+str(low_latest)+'<'+str(plow*1.3))
#         # print(i+' close to Previous Day high of '+str(phigh)+' at '+str(high_latest))
#         # if (plow*.998<low_latest) and (low_latest<plow*1.002):
#         #     onBreakout_liss.append(i+' close to Previous Day Low of '+str(plow)+'at '+str(low_latest))

#         # if (phigh*.998<high_latest) and (high_latest<phigh*1.002):
#         #     onBreakout_liss.append(i+' close to Previous Day high of '+str(phigh)+' at '+str(high_latest))
#         if (plow*.998<latest) and (latest<plow*1.002):
#             onBreakout_liss_low.append(i+' close to Previous Day Low of '+str(plow)+'at '+str(latest))

#         if (phigh*.998<latest) and (latest<phigh*1.002):
#             onBreakout_liss_high.append(i+' close to Previous Day high of '+str(phigh)+' at '+str(latest))

#             # print()
#         # exec(f"per_change[i] = (float(df1.loc[i][-2])*100/float(df2.loc[i][-2]))")
#         # low_lmax = min(filter(None,All_candle_low))
#         # y = exec(f"per_change[i] = ({low_latest}*100/{previouslow})")
#     # y = sorted(per_change.items(), key=lambda x: x[1])
#     print("onBreakout_liss ")
#     onBreakout_liss = onBreakout_liss_high+[' ']+onBreakout_liss_low
#     for i in onBreakout_liss:
#         print(i)
#     # output_gold(data_l = onBreakout_liss, opbg_color = '#99FF99',sound = True)
#     try:
#         dt = []
#         exec(f"dt.append(str(df1.loc['TCS'][1]))")
#         dt = str(dt[0][-2:]+'/'+dt[0][-4:-2]+'/'+dt[0][:-4])
#         display_text = 'On Breakdown of previous Low   '+dt
#     #     for ki in y:
#         # print('final breakout list ',onBreakout_liss)

#         # output_gold
#         data_l = onBreakout_liss
#         opbg_color = '#99FF99'
#         sound = True
#         # output_gold()
#         output_gold(data_l = onBreakout_liss, opbg_color = '#99FF99',sound = True)
#         # output_gold(data_l = onBreakout_liss, opbg_color = '#99FF99')
#         # santra = (data_l,display_text,opbg_color,sound)
#         # threading.Thread(target=output_gold,args = (santra,)).start()
#         # if len(onBreakout_liss) >= 1:
#         #     winsound.PlaySound('D:\\rated screener\\pi.wav',winsound.SND_LOOP)

#     except Exception as e:
#         print(e)

# #####################################################################################3
###########    Today Alerts                 ##########################################################################3

def today_live(stocks = NIFTY50,diff =3):
    
    onBreakout_liss = []
    onBreakdown_liss = []
    for i in stocks:
        url = f'https://query1.finance.yahoo.com/v8/finance/chart/{i}.NS'
        d = requests.get(url,headers = header)
        data = d.json()
        candle_closing = data['chart']['result'][0]['indicators']['quote'][0]['close'][-1]
        # print('here i',i)
        if candle_closing == None:
            candle_closing = data['chart']['result'][0]['indicators']['quote'][0]['close'][-2]

        # previousClose = data['chart']['result'][0]['meta']['chartPreviousClose']

        low_all = data['chart']['result'][0]['indicators']['quote'][0]['low']
        low_latest = data['chart']['result'][0]['indicators']['quote'][0]['low'][-1]
        if low_latest == None:
            low_latest = data['chart']['result'][0]['indicators']['quote'][0]['low'][-2]


        high_all = data['chart']['result'][0]['indicators']['quote'][0]['high']
        high_latest = data['chart']['result'][0]['indicators']['quote'][0]['high'][-1]
        if high_latest == None:
            high_latest = data['chart']['result'][0]['indicators']['quote'][0]['high'][-2]


        today_low = min(low_all[:-diff])
        today_high = max(high_all[:-diff])
        # plow = float(df2.loc[i][4])
        # pclose = float(df2.loc[i][5])
        # phigh = float(df2.loc[i][3])

        # print(i+' close to Previous Day Low of '+str(plow)+'at '+str(low_latest),'which is ',str(plow*.8)+'>'+str(low_latest)+'<'+str(plow*1.3))
        # print(i+' close to Previous Day high of '+str(phigh)+' at '+str(high_latest))
        # str(round(100-pchange,2))
        if (today_low*.98<low_latest) and (low_latest<today_low*1.005):
            onBreakdown_liss.append(i+' close to Today Low of '+str(round(today_low,2))+'at '+str(round(low_latest,2)))

        if (today_high*.98<high_latest) and (high_latest<today_high*1.005):
            onBreakout_liss.append(i+' close to Today Day high of '+str(round(today_high,2))+' at '+str(round(high_latest,2)))

            # print()
        # exec(f"per_change[i] = (float(df1.loc[i][-2])*100/float(df2.loc[i][-2]))")
        # low_lmax = min(filter(None,All_candle_low))
        # y = exec(f"per_change[i] = ({low_latest}*100/{previouslow})")
    # y = sorted(per_change.items(), key=lambda x: x[1])
    if diff !=3:
        display_text = "onBreakout_liss at diff "+str(diff)
        print("onBreakout_liss at diff ",diff)
    else:
        display_text = "onBreakout_liss of Today's Data"
        print("onBreakout_liss of Today's Data")

    print('\n\n')
    print('*'*88)
    print('Resistance\n')
    for i in onBreakout_liss:
        print(i)
    print('\n\n')
    print('Support\n')
    for i in onBreakdown_liss:
        print(i)
    print('\n')
    print('*'*88)
    # output_gold(data_l = onBreakout_liss, opbg_color = '#99FF99',sound = True)
    try:
        dt = []
        exec(f"dt.append(str(df1.loc['TCS'][1]))")
        dt = str(dt[0][-2:]+'/'+dt[0][-4:-2]+'/'+dt[0][:-4])
        # display_text = 'On Breakdown of previous Low   '
    #     for ki in y:
        # print('final breakout list ',onBreakout_liss)

        # output_gold
        # data_l = onBreakout_liss
        # display_text = display_text+dt
        # opbg_color = '#99FF99'
        # sound = True
        # output_gold()
        onBreakout_liss.extend(onBreakdown_liss)
        # output_gold(data_l = onBreakout_liss,display_text = display_text, opbg_color = '#99FF99',sound = True)
        output_gold(data_l = onBreakout_liss,display_text = display_text, opbg_color = '#99FF99',sound = False)
        # santra = (data_l,display_text,opbg_color,sound)
        # threading.Thread(target=output_gold,args = (santra,)).start()
        # if len(onBreakout_liss) >= 1:
        #     winsound.PlaySound('D:\\rated screener\\pi.wav',winsound.SND_LOOP)

    except Exception as e:
        print(e)

# today_live(stocks = NIFTYBANK)
#####################################################################################3
#####################################################################################3

################# alert condition                 ####################################################################3

def scan_price(sym = 'RELIANCE'):
    # latest_ltp_list = []
    latest_ltp_array = array([])
    for sym in NIFTY102:
        url = f'https://query1.finance.yahoo.com/v8/finance/chart/{sym}.NS'
        d = requests.get(url,headers = header)
        data = d.json()
        candle_closing = data['chart']['result'][0]['indicators']['quote'][0]['close'][-1]
        # print('here i',i)
        if candle_closing == None:
            candle_closing = data['chart']['result'][0]['indicators']['quote'][0]['close'][-2]

        # latest_ltp_list.append(round(candle_closing,3))
        # llatest_ltp_list.append(round(candle_closing,3))
        latest_ltp_array = append(latest_ltp_array,round(candle_closing,2))
        # print(f'LTP of {sym} {candle_closing}')
    # print(latest_ltp_list)
    #################################################################################
    r = 0
    pos = 0
    k = 0
    # if len(latest_ltp_list) == len(NIFTY102):
    if len(latest_ltp_array) == len(NIFTY102):

        for i in latest_ltp_array:
            if len(NIFTY102[k])>=4:
                sym = NIFTY102[k][:7]
            else:
                sym = NIFTY102[k]

            Profit_label = Button(f, text=sym+' '+str(i), font=("arial 8 bold"),fg= 'black',bg = 'yellow',width = 12,command = partial(graph_plot,NIFTY102[k]))
            k+=1

            # Profit_button.grid(row=pos, y=850)    
            # print(pos)
            Profit_label.grid(row=r,column = pos,padx = 1,pady=1)    
            pos+=1
            if pos>=13:
                r+=1
                pos = 0
    #################################################################################

    



def stock_alert(stock_list = NIFTY102):
    alert_window = Tk()
    alert_window.geometry("1600x1000+0+0")
    alert_window.title("Live Scanner")
    alert_window.config(bg = '#AA0000')
    
    lab = Label(alert_window,text="NSE || BSE",font="arial 28 bold",bg="#8B008B",fg ='yellow')
    lab.place(x=0,y=0)
    # dl = Label(alert_window,text = display_text,font="arial 28 bold",bg="#8B008B")
    # dl.place(x=400,y = 10)
    bqw = Button(alert_window,text = 'quit',font="arial 16 bold",bg="white",fg = 'red',command= alert_window.destroy)
    bqw.place(x=1300,y=950)


    ######################################################################################################################

    # x = current_value , x*100/y


    # look_for()
 # ['time', 'open', 'high', 'low', 'close', 'volume']

    # partial(graph_plot,i))
    # lab = Label(alert_window,text="N ",font="arial 14 bold",bg="#8B008B",fg ='yellow',command = partial(look_for,))
    # lab.place(x=0,y=130) 
    ###############################################################################################################3
    def n5(ml):
        # ml = NIFTY50
        threading.Thread(target=look_for,args = (ml,)).start()

# today_live(stocks = NIFTY50,diff =3):
    lab = Label(alert_window,text="PreviousDay HL Scan",font="arial 24 bold",bg="black",fg ='yellow')
    lab.place(x=0,y=130)
    lab = Button(alert_window,text="NIFTY50 ",font="arial 14 bold",bg="#8B008B",fg ='yellow',command = partial(n5,NIFTY50))
    lab.place(x=500,y=130)
    lab = Button(alert_window,text="NIFTY102 ",font="arial 14 bold",bg="#8B008B",fg ='yellow',command = partial(n5,NIFTY102))
    lab.place(x=700,y=130)
    lab = Button(alert_window,text="BANKNIFTY ",font="arial 14 bold",bg="#8B008B",fg ='yellow',command = partial(n5,NIFTYBANK))
    lab.place(x=900,y=130)
    lab = Button(alert_window,text="NIFTYIT",font="arial 14 bold",bg="#8B008B",fg ='yellow',command = partial(n5,NIFTYIT))
    lab.place(x=1100,y=130)
    lab = Button(alert_window,text="NIFTYPHARMA",font="arial 14 bold",bg="#8B008B",fg ='yellow',command = partial(n5,NIFTYPHARMA))
    lab.place(x=1280,y=130)
    lab = Button(alert_window,text="NIFTYMETAL",font="arial 14 bold",bg="#8B008B",fg ='yellow',command = partial(n5,NIFTYMETAL))
    lab.place(x=500,y=200)
    lab = Button(alert_window,text="NIFTYENERGY",font="arial 14 bold",bg="#8B008B",fg ='yellow',command = partial(n5,NIFTYENERGY))
    lab.place(x=800,y=200)
    lab = Button(alert_window,text="NIFTYAUTO",font="arial 14 bold",bg="#8B008B",fg ='yellow',command = partial(n5,NIFTYAUTO))
    lab.place(x=1100,y=200)
    my_list = eng_all()
    # my_list = ['ITC','TCS']
    lab = Label(alert_window,text="Today's High Low",font="arial 24 bold",bg="black",fg ='yellow')
    lab.place(x=0,y=330)

    lab = Button(alert_window,text="NIFTY50 ",font="arial 14 bold",bg="red",fg ='yellow',command = partial(today_live,NIFTY50))
    lab.place(x=500,y=330)
    lab = Button(alert_window,text="NIFTY102 ",font="arial 14 bold",bg="red",fg ='yellow',command = partial(today_live,NIFTY102))
    lab.place(x=700,y=330)
    lab = Button(alert_window,text="BANKNIFTY ",font="arial 14 bold",bg="red",fg ='yellow',command = partial(today_live,NIFTYBANK))
    lab.place(x=900,y=330)
    lab = Button(alert_window,text="NIFTYIT ",font="arial 14 bold",bg="red",fg ='yellow',command = partial(today_live,NIFTYIT))
    lab.place(x=1100,y=330)
    lab = Button(alert_window,text="NIFTYPHARMA ",font="arial 14 bold",bg="red",fg ='yellow',command = partial(today_live,NIFTYPHARMA))
    lab.place(x=1300,y=330)

    lab = Label(alert_window,text="5 min diff",font="arial 14 bold",bg="black",fg ='yellow')
    lab.place(x=0,y=430)

    lab = Button(alert_window,text="NIFTY50 ",font="arial 10 bold",bg="red",fg ='yellow',command = partial(today_live,NIFTY50,5))
    lab.place(x=500,y=430)
    lab = Button(alert_window,text="NIFTY102 ",font="arial 10 bold",bg="red",fg ='yellow',command = partial(today_live,NIFTY102,5))
    lab.place(x=700,y=430)
    lab = Button(alert_window,text="BANKNIFTY ",font="arial 10 bold",bg="red",fg ='yellow',command = partial(today_live,NIFTYBANK,5))
    lab.place(x=900,y=430)
    lab = Button(alert_window,text="NIFTYIT ",font="arial 10 bold",bg="red",fg ='yellow',command = partial(today_live,NIFTYIT,5))
    lab.place(x=1100,y=430)
    lab = Button(alert_window,text="NIFTYPHARMA ",font="arial 10 bold",bg="red",fg ='yellow',command = partial(today_live,NIFTYPHARMA,5))
    lab.place(x=1300,y=430)


    lab = Label(alert_window,text="15 min diff",font="arial 14 bold",bg="black",fg ='yellow')
    lab.place(x=0,y=500)

    lab = Button(alert_window,text="NIFTY50 ",font="arial 10 bold",bg="red",fg ='yellow',command = partial(today_live,NIFTY50,15))
    lab.place(x=500,y=500)
    lab = Button(alert_window,text="NIFTY102 ",font="arial 10 bold",bg="red",fg ='yellow',command = partial(today_live,NIFTY102,15))
    lab.place(x=700,y=500)
    lab = Button(alert_window,text="BANKNIFTY ",font="arial 10 bold",bg="red",fg ='yellow',command = partial(today_live,NIFTYBANK,15))
    lab.place(x=900,y=500)
    lab = Button(alert_window,text="NIFTYIT ",font="arial 10 bold",bg="red",fg ='yellow',command = partial(today_live,NIFTYIT,15))
    lab.place(x=1100,y=500)
    lab = Button(alert_window,text="NIFTYPHARMA ",font="arial 10 bold",bg="red",fg ='yellow',command = partial(today_live,NIFTYPHARMA,15))
    lab.place(x=1300,y=500)

    lab = Label(alert_window,text="40 min diff",font="arial 14 bold",bg="black",fg ='yellow')
    lab.place(x=0,y=570)

    lab = Button(alert_window,text="NIFTY50 ",font="arial 10 bold",bg="red",fg ='yellow',command = partial(today_live,NIFTY50,40))
    lab.place(x=500,y=570)
    lab = Button(alert_window,text="NIFTY102 ",font="arial 10 bold",bg="red",fg ='yellow',command = partial(today_live,NIFTY102,40))
    lab.place(x=700,y=570)
    lab = Button(alert_window,text="BANKNIFTY ",font="arial 10 bold",bg="red",fg ='yellow',command = partial(today_live,NIFTYBANK,40))
    lab.place(x=900,y=570)
    lab = Button(alert_window,text="NIFTYIT ",font="arial 10 bold",bg="red",fg ='yellow',command = partial(today_live,NIFTYIT,40))
    lab.place(x=1100,y=570)
    lab = Button(alert_window,text="NIFTYPHARMA ",font="arial 10 bold",bg="red",fg ='yellow',command = partial(today_live,NIFTYPHARMA,40))
    lab.place(x=1100,y=570)


    lab = Label(alert_window,text="75 min diff",font="arial 14 bold",bg="black",fg ='yellow')
    lab.place(x=0,y=640)

    lab = Button(alert_window,text="NIFTY50 ",font="arial 10 bold",bg="red",fg ='yellow',command = partial(today_live,NIFTY50,75))
    lab.place(x=500,y=640)
    lab = Button(alert_window,text="NIFTY102 ",font="arial 10 bold",bg="red",fg ='yellow',command = partial(today_live,NIFTY102,75))
    lab.place(x=700,y=640)
    lab = Button(alert_window,text="BANKNIFTY ",font="arial 10 bold",bg="red",fg ='yellow',command = partial(today_live,NIFTYBANK,75))
    lab.place(x=900,y=640)
    lab = Button(alert_window,text="NIFTYIT ",font="arial 10 bold",bg="red",fg ='yellow',command = partial(today_live,NIFTYIT,75))
    lab.place(x=1100,y=640)
    lab = Button(alert_window,text="NIFTYPHARMA ",font="arial 10 bold",bg="red",fg ='yellow',command = partial(today_live,NIFTYPHARMA,75))
    lab.place(x=1100,y=640)


    lab = Label(alert_window,text="2 hour diff",font="arial 14 bold",bg="black",fg ='yellow')
    lab.place(x=0,y=710)

    lab = Button(alert_window,text="NIFTY50 ",font="arial 10 bold",bg="red",fg ='yellow',command = partial(n5,NIFTY50))
    lab.place(x=500,y=710)
    lab = Button(alert_window,text="NIFTY102 ",font="arial 10 bold",bg="red",fg ='yellow',command = partial(n5,NIFTY102))
    lab.place(x=700,y=710)
    lab = Button(alert_window,text="BANKNIFTY ",font="arial 10 bold",bg="red",fg ='yellow',command = partial(n5,NIFTYBANK))
    lab.place(x=900,y=710)
    lab = Button(alert_window,text="NIFTYIT ",font="arial 10 bold",bg="red",fg ='yellow',command = partial(n5,NIFTYBANK))
    lab.place(x=1100,y=710)
    lab = Button(alert_window,text="NIFTYPHARMA ",font="arial 10 bold",bg="red",fg ='yellow',command = partial(n5,NIFTYBANK))
    lab.place(x=1100,y=710)

    lab = Label(alert_window,text="4 hour diff",font="arial 14 bold",bg="black",fg ='yellow')
    lab.place(x=0,y=780)

    lab = Button(alert_window,text="NIFTY50 ",font="arial 10 bold",bg="red",fg ='yellow',command = partial(n5,NIFTY50))
    lab.place(x=500,y=780)
    lab = Button(alert_window,text="NIFTY102 ",font="arial 10 bold",bg="red",fg ='yellow',command = partial(n5,NIFTY102))
    lab.place(x=700,y=780)
    lab = Button(alert_window,text="BANKNIFTY ",font="arial 10 bold",bg="red",fg ='yellow',command = partial(n5,NIFTYBANK))
    lab.place(x=900,y=780)
    lab = Button(alert_window,text="NIFTYIT ",font="arial 10 bold",bg="red",fg ='yellow',command = partial(n5,NIFTYBANK))
    lab.place(x=1100,y=780)
    lab = Button(alert_window,text="NIFTYPHARMA ",font="arial 10 bold",bg="red",fg ='yellow',command = partial(n5,NIFTYBANK))
    lab.place(x=1100,y=780)


################################################################################################
    # my_list = ['ITC','TCS']
    my_list = eng_all()
    lab = Button(alert_window,text="Engulf_list ",font="arial 14 bold",bg="#8B008B",fg ='yellow',command = partial(n5,my_list))
    lab.place(x=700,y=130)
    
    # look_for()
    ######################################################################################################################



# def nifty_live_analysis():
#     nifty_live()
#     close_to_dayhigh = []
#     close_to_daylow = []
#     print('yo')


#     for names in NIFTY50:
#         # dfl_{names}.loc[0]['high'][-1]
#         try:
#             current_price = []
#             exec(f"current_price.append(dfl_{names}.loc[0]['high'][-1])")
#             current_price = float(current_price[0])
#             if float(df1.loc[names][3]) < current_price:
#                 print(names,' current price ',current_price,'is higher then pd high ',df1.loc[names][3])
#             else:
#                 print(names,' current price ',current_price,' pd high ',df1.loc[names][3])
#         except Exception as e:
#             print(e)

# kk  = stock('RELIANCE')
# print(kk)
# print(kk.columns)
# graph_plot('ITC')
# window.mainloop()
################ playing Sound ########################################################################################3
# import winsound
# def play():
#     # os.chdir("D:\\rated screener\\")
#     # winsound.PlaySound('D:\\rated screener\\new.wav',winsound.SND_LOOP)
#     winsound.PlaySound('D:\\rated screener\\pi.wav',winsound.SND_LOOP)
#     ##### For continue loop use command below
#     # winsound.PlaySound('D:\\rated screener\\bataomc.wav', winsound.SND_LOOP + winsound.SND_ASYNC)
#     # winsound.PlaySound('C:/Windows/Media/notify.wav', winsound.SND_LOOP + winsound.SND_ASYNC)
# # play = lambda: winsound.PlaySound('bataomc.wav', winsound.SND_FILENAME)
# button = Button(window, text = 'Play', command = play)

# button.place(x = 300,y = 300)
######################################################################################################################3
######################################################################################################################3
LTRADE.config(command = stock_alert)

ml = eng_all()
################# Engulf Breakout     ###############################################################################
###################################################################################################################
###################################################################################################################
engulf_list = []

def engulf_scan(stock_name = 'DRREDDY',interval = 5):
    global engulf_list
    All_high = []
    All_low = []
    exec(f"dfl_{stock_name} = stock('{stock_name}')")
    exec(f"All_high.append(dfl_{stock_name}.loc[0][-2])")
    exec(f"All_low.append(dfl_{stock_name}.loc[0][-3])")
    count=0
    nls = []
    new_high_list = []
    for x in All_high[0]:
        nls.append(x)
        count+=1
        if count == interval:
            count = 0

            if None in nls:
                total_none = nls.count(None)
                for i in range(total_none):
                    try:
                        nls[nls.index(None)] = nls[nls.index(None)-1]
                    except Exception as e:
                        print('all high wala ',e)
                        nls[nls.index(None)] = nls[nls.index(None)+1]
            new_high_list.append(nls)
            nls = []
    count1=0
    lexi = []
    new_low_list = []
    for x in All_low[0]:
        lexi.append(x)
        count1+=1
        if count1 == interval:
            count1 = 0
            if None in lexi:
                total_n = lexi.count(None)
                for i in range(total_n):
                    try:
                        lexi[lexi.index(None)] = lexi[lexi.index(None)-1]
                    except Exception as e:
                        print('All low wala ',e)
                        lexi[lexi.index(None)] = lexi[lexi.index(None)+1]
            new_low_list.append(lexi)
            lexi = []
    try:

        max1 = max(new_high_list[-1])
        max2 = max(new_high_list[-2])
        min1 = min(new_low_list[-1])
        min2 = min(new_low_list[-2])
    except Exception as e:
        # print('last wale me ',e)
        return
    print(max1,max2)
    print(min1,min2)
    if max1>max2:
        if min1<min2:
            print(stock_name)
            engulf_list.append(stock_name)

    
# for i in NIFTY102:
#     engulf_scan(i,15)

###################################################################################################################
###################################################################################################################
def to_krna(interval = 15):
    # threading.Thread(target=look_for,args = (ml,)).start()
    # engulf_scan(stock_name = 'DRREDDY',interval = 5)
    for i in NIFTY102:
        # threading.Thread(target=engulf_scan,args = (i,15)).start()
        engulf_scan(i,interval)
    print(engulf_list)
# Profit_button = Button(window, text="30 min", font=("arial 12 bold"),bg= 'gray',fg= 'white',command = partial(bullish_min_scan,30))
# Profit_button.place(x=1500, y=420)

# print('here ml is ',ml)
# Profit_button = Button(window, text="Engulf br", font=("arial 15 bold"),bg= '#00FFFF',fg= 'black',command = partial(look_for,ml))
# Profit_button = Button(window, text="Engulf br", font=("arial 15 bold"),bg= '#00FFFF',fg= 'black',command = threading.Thread(target=look_for,args = (ml,)).start())
# Profit_button = Button(window, text="Engulf br", font=("arial 15 bold"),bg= '#00FFFF',fg= 'black',command = threading.Thread(target=look_for,args = (ml,)).run())
Profit_button = Button(window, text="Engulf br", font=("arial 15 bold"),bg= '#00FFFF',fg= 'black',command = to_krna)
Profit_button.place(x=350, y=320)
Profit_button = Button(window, text="15 min", font=("arial 12 bold"),bg= 'blue',fg= 'white',command = partial(to_krna,15))
Profit_button.place(x=550, y=320)
Profit_button = Button(window, text="30 min", font=("arial 12 bold"),bg= 'blue',fg= 'white',command = partial(to_krna,30))
Profit_button.place(x=650, y=320)
Profit_button = Button(window, text="60 min", font=("arial 12 bold"),bg= 'blue',fg= 'white',command = partial(to_krna,60))
Profit_button.place(x=750, y=320)
# Profit_button = Button(window, text="15", font=("arial 15 bold"),bg= '#00FFFF',fg= 'black',command = to_krna)
# Profit_button.place(x=350, y=320)
# Profit_button = Button(window, text="Engulf br", font=("arial 15 bold"),bg= '#00FFFF',fg= 'black',command = to_krna)
# Profit_button.place(x=350, y=320)
Profit_button = Button(window, text="Engulf br", font=("arial 15 bold"),bg= '#00FFFF',fg= 'black',command = to_krna)
Profit_button.place(x=350, y=320)
Profit_button = Button(window, text="Scan Price", font=("arial 15 bold"),bg= '#FFA0CB',fg= 'black',command = scan_price)
Profit_button.place(x=1250, y=300)

#################################################################################################

Profit_button = Button(window, text="pDay High Low", font=("arial 15 bold"),bg= '#00FFFF',fg= 'black',command = partial(pday_high,Bullish = True, Bearish = True))
Profit_button.place(x=350, y=380)
Profit_button = Button(window, text="Bullish ", font=("arial 8 bold"),bg= 'green',command = partial(pday_high,Bearish = False,Bullish = True))
Profit_button.place(x=590, y=380)
Profit_button = Button(window, text="Bearish", font=("arial 8 bold"),bg= '#990000',command = partial(pday_high,Bullish = False,Bearish = True))
Profit_button.place(x=590, y=410)
Profit_button = Button(window, text="Global Mkt&ADR", font=("arial 15 bold"),bg= '#0044FF',fg= 'white',command = adr_global_data)
Profit_button.place(x=350, y=450)
exit_button = Button(window, text="E\nX\nI\nT", font=("arial 15 bold"),fg="green",bg='red',width=2,height = 4,command=window.destroy)
exit_button.place(x=1850, y=20)

############################################################################################################################
############################################################################################################################
# on_completed=lambda: self.root.after(5, on_task_done), 

# Profit_button = Label(window, text="Breakout", font=("arial 21 bold"),bg= '#AAAAFF',fg= 'black')
# Profit_button.place(x=890, y=280)
# Profit_button = Button(window, text="200 Days Breakout", font=("arial 15 bold"),bg= '#00FFFF',fg= 'black',command = threading.Thread(target=look_for,args = (ml,)).start())
# Profit_button.place(x=650, y=380)

# Profit_button = Button(window, text="200", font=("arial 15 bold"),bg= '#00FFFF',fg= 'black',command = threading.Thread(target=close_to_breakout,args = (200,)))
# Profit_button.place(x=1080, y=280)
# Profit_button = Button(window, text="100", font=("arial 15 bold"),bg= '#00FFFF',fg= 'black',command = threading.Thread(target=close_to_breakout,args = (100,)))
# Profit_button.place(x=1170, y=280)
# Profit_button = Button(window, text="50", font=("arial 15 bold"),bg= '#00FFFF',fg= 'black',command = threading.Thread(target=close_to_breakout,args = (50,)))
# Profit_button.place(x=1260, y=280)

####################################################################################################################
####################################################################################################################
