import re
import flight
import datetime


#leksiko gia na emfanizetai h xwra anti tou kwdikou
dictionary = {'ATH':'ATHENS' , 'SMI':'SAMOS' , 'SKG':'THESSALONIKI' , 'LIS':'LISBON' , 'LGW':'LONDON GATWICK',
                'EDI':'EDINBURGH' ,  'LAS':'LAS VEGAS' ,  'LAX':'LOS ANGELES' ,  'SFO':'SAN FRANCISCO' ,
                  'MAD':'MADRID' ,  'NAP':'NAPLES'}

menu ={}

flights = []
#pattern gia reg expressions pou vriskei opoia grammh ksekinaei me digit
pattern = re.compile(r'^\d')

for i in open(r"flights.txt"):
    for j in re.finditer(pattern, i):
      #replace ola ta tab kai afairesh kenwn
        k = i.replace('\t',' ')
        x = ' '.join(k.split())
        res = x.split()

        #format twn dates
        dtime = datetime.datetime(int(res[2][0:4]) , int(res[2][4:6]) , int(res[2][6:8]) , int(res[2][8:10]), int(res[2][10:12]))
        atime = datetime.datetime(int(res[3][0:4]) , int(res[3][4:6]) , int(res[3][6:8]) , int(res[3][8:10]), int(res[3][10:12]))
        #gemisma listas me antikeimena
        flights.append(flight.Flight(res[0], dictionary[res[1][0:3]], dictionary[res[1][4:7]], dtime , atime, 
        res[4], res[5], res[6]))
        



for r in flights:
  print(r.__repr__())



menu['1'] = "Choose agency to see details"
menu['2'] = "Exit"

sum = 0
while True:
  options = menu.keys()
  for entry in sorted(options):
      print(entry, menu[entry])

  selection = input("Please Select:")
  if selection == '1':
      # enfanizei ta praktoreia
      print('\nAgency 1: 47352\nAgency 2: 78963\nAgency 3: 25532\nAgency 4: 85721')
      code = input("Choose agency code: ")
      for m in flights:
        #an o kwdikos pou dwsame tairiazei me auto twn pthsewn
        if code == m.cid:
          print(m.__repr__())
          #prosthetoume ola ta eisithria
          sum += float(m.price)
      print('Total ticket price: ', sum)
  elif selection == '2':
      break
  else:
      print("Unknown Option Selected!")
       
        