#importing datetime module 
from datetime import datetime
#function for proper spacing in BillItems..
def padding(sr,l,s):#s=String,l=length,s=Spacing
    sr=str(sr)
    new_sr=(l-len(str(sr)))*" "
    if s=="S":
        new_sr=sr+new_sr
    return new_sr
def date():
    current_date_time=datetime.now()
    return current_date_time.strftime('%d-%b-%Y')#%d_date,%b_month,%Y_Year
#class for address
class Address:
    def __init__(self,street,city,country,postal_code):
        self.__street=street
        self.__city=city
        self.__country=country
        self.__potal_code=postal_code
    def __str__(self):
        v=str(self.__street)
        v+=" , "
        v+=str(self.__city)
        v+=" , "
        v+=str(self.__country)
        v+=" , "
        v+=str(self.__potal_code)
        return v
    @property
    def street(self):
        return self.__street
    @street.setter
    def street(self,s):
        self.__street=s
    @property
    def city(self):
        return self.__city
    @city.setter
    def city(self,c):
        self.__city=c
    @property
    def country(self):
        return self.__country
    @country.setter
    def country(self,c):
        self.__country=c
    @property
    def postal_code(self):
        return self.__postal_code
    @postal_code.setter
    def postal_code(self,p):
        self.__postal_code=p
#class Name
class Name:
    def __init__(self,fn,ln):
        self.__firstname=fn
        self.__lastname=ln
    def __str__(self):
        v=str(self.__firstname)
        v+=" "
        v+=str(self.__lastname)
        return v
    @property
    def fn(self):
        return self.__firstname
    @fn.setter
    def fn(self,f):
        self.__firstname=f
    @property
    def ln(self):
        return self.__lastname
    @ln.setter
    def ln(self,l):
        self.__lastname=l
#class for bill in the cash memo
class BillItem:
    amount=0
    def __init__(self,qt,prticlr,rt):
        self.__quantity=qt
        self.__particular=prticlr
        self.__rate=rt
        BillItem.amount=self.__quantity*self.__rate  
    def __str__(self):
        BillItem.amount=self.__quantity*self.__rate
        return f"{padding(str(self.__particular),30,"S")}{padding(self.__quantity,10,"S")}{padding(self.__rate,10,"S")}{padding(BillItem.amount,10,"S")}"
#Getters & Setters
    @property
    def qt(self):
        return self.__quantity
    @qt.setter
    def qt(self,q):
        Bill.Total-=self.__quantity*self.__rate
        self.__quantity=q
        BillItem.amount=self.__quantity*self.__rate
        Bill.Total+=self.__quantity*self.__rate
    @property
    def prticlr(self):
        return self.__particular
    @prticlr.setter
    def prticlr(self,p):
        self.__particular=p
    @property
    def rt(self):
        return self.__rate
    @rt.setter
    def rt(self,r):
        Bill.Total-=self.__quantity*self.__rate
        self.__rate=r
        BillItem.amount=self.__quantity*self.__rate
        Bill.Total+=self.__quantity*self.__rate
    @property
    def Amount(self):
        return BillItem.amount
#class bill item
class Bill:
    Billno=1
    Total=0
    def __init__(self,d,na,ad,itm):
        self.__date=d
        self.__name=na
        self.__address=ad
        self.__item=[]
        self.__item.extend(itm)
        self.__billno=Bill.Billno
        Bill.Billno+=1
        for i in self.__item:
            Bill.Total+=i.Amount
    def __str__(self):
        rs=f"MOBILO\nMobile City\nDeals in all kinds of MObiles & Accesories\nCellno-0321-0000000\nCASHMEMO\nNo:{self.__billno}\nDate:{self.__date}\nCustomer Name:{self.__name}\nCustomer Address:{self.__address}\n{padding("Particular:",30,"S")}{padding("Qty:",10,"S")}{padding("Rate:",10,"S")}{padding("Amount:",10,"S")}"
        for itm in self.__item:
            rs+='\n'+str(itm)
        return rs + "\n"+f"Total : {Bill.Total}"+"\n"+"Signature:________" + "\n"+" Address: Basement # 2, Allahwala Plaza, Markaz K8, Islamabad"
    @property
    def date(self):
        self.__date
    @date.setter
    def date(self,d):
        self.__date=d
    @property 
    def name(self):
        return self.__name
    @name.setter
    def name(self,n):
        self.__name=n
    @property
    def address(self):
        return self.__address
    @address.setter
    def address(self,a):
        self.__address=a
    @property
    def item(self):
        return self.__item
    @item.setter
    def item(self,i):
        self.__item=i
def main():
    n=Name(input("Enter firstname:"),input("Enter lastname:"))
    a=Address(input("Enter street no :"),input("enter city name:"),input("enter country name:"),input("enter postal code:"))
    num_items = int(input("How many items do you want? "))
#Bill item
    items = []
    for i in range(num_items):
        q = int(input(f"Enter quantity for item {i+1}: "))
        p = input(f"Enter particular for item {i+1}: ")
        r = int(input(f"Enter rate of item {i+1} : "))
        items.append(BillItem(q, p,r))
    print("=====================================================================")
    m=m=Bill(date(),n,a,items)
    print(m)
main()