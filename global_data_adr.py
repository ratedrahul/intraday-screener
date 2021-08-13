# import os
from tkinter import*

def adr_global_data():

	import lxml
	import requests
	from bs4 import BeautifulSoup
	window_adr = Tk() 
	window_adr.geometry('2000x980')
	window_adr.config(bg = "#8B008B")
	window_adr.title('Global Data')
	f1 = Frame(window_adr,bg = 'black')
	f1.place(x = 0 ,y =100)
	# f1.pack(side = TOP)
	f2 = Frame(window_adr,bg = 'green')
	f2.place(x = 0,y =600)
	# f2.pack(side = LEFT)

	f3 = Frame(window_adr,bg = 'green')
	f3.place(x = 1100,y =600)
	# f3.pack(side = RIGHT)

		# print("so this is \n gonna be\n the most\nimportant")
		# url = f'https://www.nseindia.com/option-chain'
	try:
		def r1():

			url = f'https://www.moneycontrol.com/markets/global-indices/'
			# url = f'https://www.nseindia.com/option-chain?symbolCode=-10006&symbol=NIFTY&symbol=NIFTY&instrument=-&date=-&segmentLink=17&symbolCount=2&segmentLink=17'
			# try:

			page = requests.get(url)

			# print('yes fine')
			# print(page)
			soup = BeautifulSoup(page.text,'lxml')

			# print(soup.beautify())
			# print(soup.text)
			# print('Data of Adr DII and FII activity')
			liss = []
			for i in soup.find_all('div',class_="tab-pane fade in active"):
				d_fo = i.text
				liss.append(d_fo)

			# for i in soup.find_all(class_="robo_medium"):
			# 	print(i.text)
			glb = []
			for i in soup.find_all(class_="glob_indi_lft"):
				glb.append(i.text)

			# for i in soup.find_all(class_="stname"):
			# 	print(i.text)
			NIFTY = ''
			SENSEX = ''
			N = ''
			for i in soup.find_all(class_="nifysenw_cnt"):
				j = i.text
				NIFTY = (j[j.index('NIFTY'):j.index('SENSEX')]).strip()
				SENSEX = (j[j.index('SENSEX'):]).strip()

				# for k in j:
				# 	if k != '\n':
				# 	# print(i)
				# 		N+=k
			# print("final ",j)

			# Almost all
			# for i in soup.find_all(class_= "clearfix"):
			# 	print(i.text)
				# pass

				# liss.append(d_fo)

			# commodity = liss[0]
			# ADRs = liss[1]
			# FII = []
			############ FII main 
			# for i in liss[3]:
			#  	# FII.extend(k)
			#  	print(i,end = '')


			# comm = commodity.split('\n\n\n\n\n')
			# for i in comm[2]:
			# 	print(i,end = '')

			######################################################################
			# nGlobal Indices\n\n\n\n\nName\nCurrent Value\nChange\n            %Change\n\n%Change\nOpen\n            Prev.Close\n\nHigh\n            Low\nLow\nPrev.Close\n5 DAY Perf
			Nasdaq = glb[0][glb[0].index('Nasdaq'):glb[0].index('European')]

			# European Market
			FTSE = glb[0][glb[0].index('FTSE'):glb[0].index('CAC')]
			CAC =glb[0][glb[0].index('CAC'):glb[0].index('DAX')]
			DAX = glb[0][glb[0].index('DAX'):glb[0].index('Asian')]

			# ASIAN MARKET
			SGX_Nifty = glb[0][glb[0].index('SGX Nifty'):glb[0].index('Nikkei')]

			NIKKEI225 = glb[0][glb[0].index('Nikkei'):glb[0].index('Straits')]

			Straits_Times = glb[0][glb[0].index('Straits'):glb[0].index('Hang Seng')]

			Hang_Seng = glb[0][glb[0].index('Hang Seng'):glb[0].index('Taiwan')]

			Taiwan_weighted = glb[0][glb[0].index('Taiwan'):glb[0].index('KOSPI')]

			KOSPI = glb[0][glb[0].index('KOSPI'):glb[0].index('SET')]

			SET_COMPOSITE = glb[0][glb[0].index('SET'):glb[0].index('Jakarta')]

			JAKARTA_COMPOSITE = glb[0][glb[0].index('Jakarta'):glb[0].index('Shanghai Composite')]


			SHANGHAI_COMPOSITE = glb[0][glb[0].index('Shanghai Composite'):]
			GB_Market = [SGX_Nifty,Nasdaq,DAX,NIKKEI225,Hang_Seng,FTSE,CAC,Taiwan_weighted, KOSPI,JAKARTA_COMPOSITE,SHANGHAI_COMPOSITE, Straits_Times]
			# Commodity \nPrice \nChange \n% Chg 
			GOLD = liss[0][liss[0].index('GOLD'):liss[0].index('SILVER')]
			SILVER = liss[0][liss[0].index('SILVER'):liss[0].index('COTTON')]
			COTTON = liss[0][liss[0].index('COTTON'):liss[0].index('CRUDEOIL')]
			CRUDEOIL = liss[0][liss[0].index('CRUDEOIL'):liss[0].index('NATURALGAS')]
			NATURALGAS = liss[0][liss[0].index('NATURALGAS'):liss[0].index('ALUMINIUM')]
			ALUMINIUM = liss[0][liss[0].index('ALUMINIUM'):]
			Commodity_list = [GOLD, SILVER, COTTON, CRUDEOIL, NATURALGAS, ALUMINIUM]
			#########################
			##### ADR#########################
			# \n\n\n\n\nCompany \nClose Price ($) \nChange \n% Chg 
			Axis = liss[1][liss[1].index('Axis'):liss[1].index('Azure')]
			Azure_Power_Global = liss[1][liss[1].index('Azure'):liss[1].index('Dr')]
			Dr_Reddy_ = liss[1][liss[1].index('Dr'):liss[1].index('Eros')]
			HDFC_BANK = liss[1][liss[1].index('HDFC'):liss[1].index('ICICI'):]
			ICICI_BANK = liss[1][liss[1].index('ICICI'):liss[1].index('Infosys')]
			Infosys = liss[1][liss[1].index('Infosys'):liss[1].index('MakeMyTrip')]
			TataMotor = liss[1][liss[1].index('TATA MOTOR'):liss[1].index('Vedanta')]
			Vedanta = liss[1][liss[1].index('Vedanta'):liss[1].index('Wipro')]
			Wipro = liss[1][liss[1].index('Wipro'):liss[1].index('WNS')]
			SIFYTECH = liss[1][liss[1].index('SIFY'):liss[1].index('TATA')]
			ADR_list = [HDFC_BANK, ICICI_BANK, Axis, Dr_Reddy_,Vedanta, TataMotor, Infosys,Wipro,SIFYTECH]
			######################### 
			######################### 
			##### 

			def co(pr = None):
				pr = pr.strip()
				value = ''
				for i in pr:
					if i.isalnum() or i == ',' or i =='-' or i == '+' or i == '.':
						value += i
					elif i == '\n':
						value+='&'
				# print(fa)
				fa = value.split('&')
				ta = [x for x in fa if x !='']
				# print(ta)
				# print(fa)
				# print(len(fa))
				# fa = [x for x in fa if fa!='']
				return ta 
			print(r' nGlobal Indices\n\n\n\n\nName\nCurrent Value\nChange\n            %Change\n\n%Change\nOpen\n            Prev.Close\n\nHigh\n            Low\nLow\nPrev.Close\n5 DAY Perf')
			# print(co(Hang_Seng))
			# print(co(DAX))
			# print(value)
			gb_list = []
			for i in GB_Market:
				g = (co(i))
				# print('before delete ',g)
				del g[4]
				del g[5]
				del g[8]
				g[3] = g[3] + ' %'
				# g[0] =
				# print('ye append hoga bc ',g)
				gb_list.append(g)

				# gb_list.remove
				# print(len)

			print(r'# \n\n\n\n\nCompany \nClose Price ($) \nChange \n% Chg ')
			adr_t = []
			for i in ADR_list:
				p =(co(i))
				p[-1] = p[-1]+ ' %'
				adr_t.append(p)

			print(r'# Commodity \nPrice \nChange \n% Chg ')
			comm = []
			for i in Commodity_list:
				hihi = (co(i))
				hihi[-1] = hihi[-1] + ' %'
				comm.append(hihi)

			nn = co(NIFTY)
			ss = co(SENSEX)

			# take the data 

			# lst = [(1,'Raj','Mumbai',19), 
			#        (2,'Aaryan','Pune',18), 
			#        (3,'Vaishnavi','Mumbai',20), 
			#        (4,'Rachna','Mumbai',21), 
			#        (5,'Shubham','Delhi',21)] 
			   
			# find total number of rows and 
			# columns in list 
			def table_c(lst):
			  print('yo')
			  if lst == adr_t:
			  	li = ['Company','Close Price($)','Change','% Chg ']
			  	# print('final lst is ',lst)
			  	lst.insert(0,li)
			  elif lst == comm:
			  	li = ['Commodity','Date','Price','Change','% Chg ']
			  	lst.insert(0,li)
			  	# pass
			  elif lst == gb_list:
			  	li = ['Global Indices Name','Current Value','Change' , '%Change','Open','High','Low','Prev.Close']
			  	lst.insert(0,li)
			  total_rows = len(lst) 
			  total_columns = len(lst[0]) 
			     
			  # create window_adr window 

			          # code for creating table 
			  # first_index = first_index.insert()
			  for i in range(total_rows): 
			      for j in range(total_columns): 

			          if '-' in lst[i][3]:
				          e = Entry(f1, width=len(lst[i][j])+5, fg='red', bg = 'black',
				                         font=('Arial',14,'bold')) 

				          # print('yaha',lst[i])
				            

			          	# print('yo',lst[i][-1])
			          	# print(lst[i])
			          else:
			          	  e = Entry(f1, width=len(lst[i][j])+5, fg='#00FF00', bg = 'black',
				                         font=('Arial',14,'bold')) 
			          	  
			          	  # print('yaha',lst[i][3])
				        
			          e.grid(row=i, column=j) 
			          # e1 = Entry(window_adr, width = 5, fg='red', 
			          #                font=('Arial',8,'bold')) 
			            
			          if i == 0:
			          	e.config(fg = 'white')
			          # e1.grid(row=i, column=j) 
			          e.insert(END, lst[i][j]) 
			          # e1.insert(END, 'this') 
			  # Table(window_adr) 

			  # window_adr.mainloop()  
			def table_c2(lst,window,fo):
			  print('yo')
			  if lst == adr_t:
			  	li = ['Company','Close Price($)','Change','% Chg ']
			  	# print('final lst is ',lst)
			  	lst.insert(0,li)
			  elif lst == comm:
			  	li = ['Commodity','Date','Price','Change','% Chg ']
			  	lst.insert(0,li)
			  	# pass
			  elif lst == gb_list:
			  	li = ['Global Indices Name','Current Value','Change' , '%Change','Open','High','Low','Prev.Close']
			  	lst.insert(0,li)
			  total_rows = len(lst) 
			  total_columns = len(lst[0]) 
			     
			  # create window_adr window 

			          # code for creating table 
			  # first_index = first_index.insert()
			  for i in range(total_rows): 
			      for j in range(total_columns): 

			          if '-' in lst[i][3]:
				          e = Entry(window, width=len(lst[i][j])+5, fg='red', bg = 'black',
				                         font=('Arial',fo,'bold')) 
				          # print('yaha',lst[i])
				            

			          	# print('yo',lst[i][-1])
			          	# print(lst[i])
			          else:
			          	  e = Entry(window, width=len(lst[i][j])+5, fg='#00FF00', bg = 'black',
				                         font=('Arial',fo,'bold')) 
			          	  # print('yaha',lst[i][3])
				        
			          e.grid(row=i, column=j) 
			          # e1 = Entry(window_adr, width = 5, fg='red', 
			          #                font=('Arial',8,'bold')) 
			            
			          if i == 0:
			          	e.config(fg = 'white')
			          # e1.grid(row=i, column=j) 
			          e.insert(END, lst[i][j]) 
			          # e1.insert(END, 'this') 
			  # Table(window_adr) 

			  # window_adr.mainloop()  
			table_c2(adr_t,f2,14)
			table_c2(comm,f3,12)
			table_c(gb_list)
			# nn = nn[nn.index()]
			l1 = Label(window_adr ,text = nn,font=('Arial',19,'bold'),fg = 'white')
			if '-' in str(nn):
				l1.config(fg = 'red')
			l1.place(x = 0,y =0)

			l2 = Label(window_adr, text = ss,font=('Arial',19,'bold'),fg = 'white')
			if '-' in str(ss):
				l2.config(fg = 'red')
			l2.place(x = 650,y =0)
			# def adr_global_data1():
			# def refresh():
			#     window destroy()
			#     __init__()
	except Exception as e:
		print(e)

	# sleep(10)
	r1()
	Profit_button = Button(window_adr, text=" Refresh ", font=("arial 15 bold"),bg= 'yellow',fg= 'black',command = r1)
	Profit_button.place(x=1250, y=0)
	exit_button = Button(window_adr, text=" Quit ", font=("arial 15 bold"),bg= 'red',fg= 'white',command = window_adr.destroy)
	exit_button.place(x=1480, y=0)
			# print(gb_list)
		# adr_global_data()