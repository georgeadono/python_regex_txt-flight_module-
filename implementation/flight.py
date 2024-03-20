class Flight:
    def __init__(self, cid, depport, arrport, depdate, arrdate, name , surname,price):
        self.cid = cid
        self.depport = depport
        self.arrport = arrport
        self.depdate = depdate
        self.arrdate = arrdate
        self.name = name 
        self.surname = surname
        self.price = price
        


    def __repr__(self):
        return ( 'Flight code: '+self.cid + ' '+self.name + ' ' +self.surname + ' From: ' + self.depport + ' Departure Date: ' + str(self.depdate) +'\n'
                +'To: ' + self.arrport + ' Arrival Date: ' + str(self.arrdate) + '\n' + 'Total Price: '
                + self.price )
