#helllo aman
import pickle
import os
print('\t\tWELCOME TO THE HOTEL BOOKING SYSTEM')
print('\t\t---BOOK YOUR DESTINATION RIGHT HERE---')
print('CREDITS: SUBARNA SUTRADHAR\n')
#-----------------------------------------------

pas_sgn=[]
username=''
password=''
usertype=""
#universal(cust/owner)---------------------------------
name=[]
pas_l=[]


hot01=[]
hot02=[]
hot03=[]
hot04=[]
hot05=[]
hot06=[]
hot07=[]
hot08=[]
hot09=[]
hot10=[]


def pcls():
    print('\n1.NEW DELHI')
    print('2.MUMBAI')
    print('3.GOA')
    print('4.KOKLKATA')
    print('5.SHIMLA')
    print('6.RAJASTHAN')
    print('7.GUJRAT')
    print('8.JAMMU & KASHMIR')
    print('9.TAMIL NADU')
    print('10.HYDERABAD\n')

def rooms():
    amount=0
    print('\n-------ROOM TYPE-------')
    print('\n1.SINGLE BED----NON-AC')
    print('RENT PER NIGHT----->2500')
    print('2.DOUBLE BED----NON-AC')
    print('RENT PER NIGHT----->3000')
    print('3.SINGLE BED----AC')
    print('RENT PER NIGHT----->4500')
    print('4.DOUBLE BED----AC')
    print('RENT PER NIGHT----->6000\n')

    room_inp=int(input('ENTER THE CORRESPONDING ROOM TYPE: '))
    if room_inp==1:
        dys=int(input('ENTER THE NUMBER OF DAYS FOR STAYING: '))
        cost=2500*dys
    elif room_inp==2:
        dys=int(input('ENTER THE NUMBER OF DAYS FOR STAYING: '))
        cost=3000*dys
    elif room_inp==3:
        dys=int(input('ENTER THE NUMBER OF DAYS FOR STAYING: '))
        cost=4500*dys
    elif room_inp==4:
        dys=int(input('ENTER THE NUMBER OF DAYS FOR STAYING: '))
        cost=6000*dys
    else:
        print('\n----ROOM TYPE DOES NOT EXTST----\n')

    print('\nTOTAL AMOUNT TO BE PAID IS-----> ',cost)
    amount=amount+cost

    print('\n----PROCEED TO THE PAYMENT----\n')

    pmnt=input("CONFIRM PAYMENT(Y/N): ")
    if pmnt=="n" or pmnt=="N":
        print("\nPAYMENT UNSUCCESSFUL")
        print("TRY AGAIN\n")
        pcls()
    else:
        print("\nPAYMENT SUCCESSFUL")
        
        dt04=open("OWNER_amount.dat",'wb+')
        pickle.dump(amount,dt04,pickle.HIGHEST_PROTOCOL)
        dt04.close()
        print("----HOTEL ROOM BOOKED----")
        print("HOTEL BOOKED AT: ",plctochs)
        print("STAYING PREIOD: ",dys)
        print("AMOUNT PAID: ",cost)
    

        
#----------------------------------------------------------------

def dashes():
    print('---------------------------------------------')

class sign_det:
    def __init__(self,unm,utyp):
        self.unm=username
        self.utyp=usertype
        name.append(self.unm)
        
    def password_log(self):#pas_l
        self.password=input('ENTER THE LOG-IN PASSWORD: ')
        pas_l.append(self.password)
    def pass_sign(self):#pas_sgn
        self.password=input('ENTER THE PASSWORD: ')
        pas_sgn.append(self.password)



class all_places:
    
    """name of hotels of cities"""
    def dlh(self):
        self.hot01=['1.HOTEL KINGDOM---(4STAR)','2.KING RESIDENCE---(5STAR)','3.HOTEL MARINES---(3STAR)']
        self.pl01=open('NEW DELHI.dat','wb+')
        pickle.dump(self.hot01,self.pl01,pickle.HIGHEST_PROTOCOL)
        self.pl01.close()

    def mum(self):
        self.hot02=['1.HOTEL MUMBAI INTRERNATIONAL---(5STAR)','2.CHATEU WINDSOR HOTEL---(4STAR)','3.CITIZEN HOTEL---(2STAR)']
        self.pl01=open('MUMBAI.dat','wb+')
        pickle.dump(self.hot02,self.pl01,pickle.HIGHEST_PROTOCOL)
        self.pl01.close()
    
    def goa(self):
        self.hot03=['1.GRAND HYATT GOA---(2STAR)','2.COZY WOOD HOTEL---(4STAR)','3.THE FERN KADAMBA---(5STAR)']
        self.pl01=open('GOA.dat','wb+')
        pickle.dump(self.hot03,self.pl01,pickle.HIGHEST_PROTOCOL)
        self.pl01.close()

    def kolkata(self):
        self.hot04=['1.AQUARIS---(5STAR)','2.THE OBEROI GRAND---(2STAR)','3.THE SENATOR HOTEL---(3STAR)']
        self.pl01=open('KOLKATA.dat','wb+')
        pickle.dump(self.hot04,self.pl01,pickle.HIGHEST_PROTOCOL)
        self.pl01.close()

    def shimla(self):
        self.hot05=['1.NISHAT HOTEL---(4STAR)','2.THE NILAYA---(3STAR)','3.WOODAYS HOTEL---(5STAR)']
        self.pl01=open('SHIMLA.dat','wb+')
        pickle.dump(self.hot05,self.pl01,pickle.HIGHEST_PROTOCOL)
        self.pl01.close()

    def rajasthan(self):
        self.hot06=['1.HILTON JAIPUR---(4STAR)','2.HOTEL RAJASTHAN PALACE---(5STAR)','3.UMAID BHAWAN HOTEL---(2STAR)']
        self.pl01=open('RAJASTHAN.dat','wb+')
        pickle.dump(self.hot06,self.pl01,pickle.HIGHEST_PROTOCOL)
        self.pl01.close()

    def gujrat(self):
        self.hot07=['1.HERITAGE HOTEL---(5STAR)','2.HOTEL GUJRAT---(3STAR)','3.REGENTA CENTRAL---(2STAR)']
        self.pl01=open('GUJRAT.dat','wb+')
        pickle.dump(self.hot07,self.pl01,pickle.HIGHEST_PROTOCOL)
        self.pl01.close()

    def jammu(self):
        self.hot08=['1.HOTEL RAGHUNATH---(3STAR)','2.THE GRAND DRAGON---(4STAR)','3.HOTEL FABULOUS KASHMIR---(5STAR)']
        self.pl01=open('JAMMU_KASHMIR.dat','wb+')
        pickle.dump(self.hot08,self.pl01,pickle.HIGHEST_PROTOCOL)
        self.pl01.close()

    def tamil(self):
        self.hot09=['1.HOTEL TEMPLE CITY---(4STAR)','2.HOTEL NEW REGENCY---(5STAR)','3.HOTEL THAJ REGENCY---(3STAR)']
        self.pl01=open('TAMILNADU.dat','wb+')
        pickle.dump(self.hot09,self.pl01,pickle.HIGHEST_PROTOCOL)
        self.pl01.close()

    def hyder(self):
        self.hot10=['1.THE PARK HYDERABAD---(4STAR)','2.AMRUTHA CASTLE---(5STAR)','3.THE ELLA HOTEL---(2STAR)']
        self.pl01=open('HYDERABAD.dat','wb+')
        pickle.dump(self.hot10,self.pl01,pickle.HIGHEST_PROTOCOL)
        self.pl01.close()
pl=all_places()

#--------------------------------------------------------------
"""assignning hotels""" 
pl.dlh()
pl.mum()
pl.goa()
pl.kolkata()
pl.shimla()
pl.rajasthan()
pl.gujrat()
pl.jammu()
pl.tamil()
pl.hyder()



#main prog---------------------------------------------------


while True:
    ans01=input('CONTINUE? ')
    if ans01=='N' or ans01=='n':
        break
    else:
        print('\n1.LOG IN')
        print('2.SIGN IN\n')
        dashes()


        log_sign=int(input('ENTER THE CHOICE: '))
        if log_sign==1:
            print('\nLOGGING-IN')
            unm=input('ENTER THE USERNAME: ')
            utyp=input('ENTER THE USER-TYPE(OWNER/CUSTOMER): ')
            dt_own='{}_owner.dat'.format(unm)
            if utyp=="owner" or utyp=="OWNER":
                ownpass_inp=input("ENTER THE AUTHORIZED PASSWORD: ")
                av03=open(dt_own,'rb')
                try:
                    while True:
                        own_ld=pickle.load(av03)
                except EOFError:
                    pass
                if ownpass_inp==own_ld:
                    print("----WELCOME OWNER----\n")
                    print("----ALL INFO----\n")
                    dt04=open("OWNER_amount.dat","rb")
                    try:
                        while True:
                            amnt_opn=pickle.load(dt04)
                    except EOFError:
                        pass
                    print("PLACES AVAILABLE IN THE SYSTEM")
                    print("------------------------------")
                    pcls()
                    print("---TOTAL AMOUNT RECIEVED---")
                    print(amnt_opn)
                    dt04.close()
                else:
                    print("\nYOU ARE NOT AN AUTHORIZED OWNER")
                
            else:
                
            
                sg=sign_det(unm,utyp)
                sg.password_log()
                for l in pas_l:
                    l1=l
                for i in name:
                    nm=i
                dt01='{}.dat'.format(unm)
                if(os.path.exists(dt01)):
                    av01=open(dt01,'rb')
                    print('ALREADY A MEMBER\n')
                    try:
                        while True:
                            ld01=pickle.load(av01)
                    except EOFError:
                        pass
                    for k in ld01:
                        if k==l1:
                            print('LOGGED IN SUCCESSFULLY\n')
                            print('YOU HAVE ENTERED THE SYSTEM')
                            dashes()

                            #hotes booking starts--------------------------

                            """places for booking a hotel----displaying"""

                            print('\tAVAILABLE PLACES FOR BOOKING HOTEL')
                            print('\t---------------------------------')
                            pcls()

                            dashes()
                            """selecting the places"""

                            while True:
                                ans02=input('CONTINUE TO SEARCH HOTEL? ')

                                if ans02=='N' or ans02=='n':
                                    print('THANK YOU')
                                    print('VISIT AGAIN')
                                    break

                                else:

                                    plctochs=input('ENTER THE NAME OF A PLACE FROM ABOVE: ')
                                    print('\n')

                                    pls='{}.dat'.format(plctochs)
                                    if plctochs=='NEW DELHI' or plctochs=='new delhi':

                                        pl01=open('NEW DELHI.dat','rb')
                                        try:
                                            while True:
                                                ld02=pickle.load(pl01)
                                                for i in ld02:
                                                    print(i)
                                                    dashes()
                                        except EOFError:
                                            pass

                                        pl01.close()
                                        #ROOM TYPE----------------------------------------------------
                                        hot_inp=int(input('\nENTER THE CORRESPONDING HOTEL NUMBER: '))
                                        rooms()
                                        

                                        #-------------------------------------------------------------
                                    elif plctochs=='MUMBAI' or plctochs=='mumbai':

                                        pl01=open('MUMBAI.dat','rb')
                                        try:
                                            while True:
                                                ld02=pickle.load(pl01)
                                                for i in ld02:
                                                    print(i)
                                                    dashes()
                                        except EOFError:
                                            pass

                                        pl01.close()
                                        #ROOM TYPE----------------------------------------------------
                                        hot_inp=int(input('\nENTER THE CORRESPONDING HOTEL NUMBER: '))
                                        rooms()
                                    
                                    elif plctochs=='GOA' or plctochs=='goa':

                                        pl01=open('GOA.dat','rb')
                                        try:
                                            while True:
                                                ld02=pickle.load(pl01)
                                                for i in ld02:
                                                    print(i)
                                                    dashes()
                                        except EOFError:
                                            pass

                                        pl01.close()
                                        #ROOM TYPE----------------------------------------------------
                                        hot_inp=int(input('\nENTER THE CORRESPONDING HOTEL NUMBER: '))
                                        rooms()
                                    
                                    elif plctochs=='KOLKATA' or plctochs=='kolkata':

                                        pl01=open('KOLKATA.dat','rb')
                                        try:
                                            while True:
                                                ld02=pickle.load(pl01)
                                                for i in ld02:
                                                    print(i)
                                                    dashes()
                                        except EOFError:
                                            pass

                                        pl01.close()
                                        #ROOM TYPE----------------------------------------------------
                                        hot_inp=int(input('\nENTER THE CORRESPONDING HOTEL NUMBER: '))
                                        rooms()

                                    elif plctochs=='SHIMLA' or plctochs=='shimla':

                                        pl01=open('SHIMLA.dat','rb')
                                        try:
                                            while True:
                                                ld02=pickle.load(pl01)
                                                for i in ld02:
                                                    print(i)
                                                    dashes()
                                        except EOFError:
                                            pass

                                        pl01.close()
                                        #ROOM TYPE----------------------------------------------------
                                        hot_inp=int(input('\nENTER THE CORRESPONDING HOTEL NUMBER: '))
                                        rooms()

                                    elif plctochs=='RAJASTHAN' or plctochs=='rajasthan':

                                        pl01=open('RAJASTHAN.dat','rb')
                                        try:
                                            while True:
                                                ld02=pickle.load(pl01)
                                                for i in ld02:
                                                    print(i)
                                                    dashes()
                                        except EOFError:
                                            pass

                                        pl01.close()
                                        #ROOM TYPE----------------------------------------------------
                                        hot_inp=int(input('\nENTER THE CORRESPONDING HOTEL NUMBER: '))
                                        rooms()

                                    elif plctochs=='GUJRAT' or plctochs=='gujrat':

                                        pl01=open('GUJRAT.dat','rb')
                                        try:
                                            while True:
                                                ld02=pickle.load(pl01)
                                                for i in ld02:
                                                    print(i)
                                                    dashes()
                                        except EOFError:
                                            pass

                                        pl01.close()
                                        #ROOM TYPE----------------------------------------------------
                                        hot_inp=int(input('\nENTER THE CORRESPONDING HOTEL NUMBER: '))
                                        rooms()

                                    elif plctochs=='JAMMU & KASHMIR' or plctochs=='jammu & kashmir':

                                        pl01=open('JAMMU_KASHMIR.dat','rb')
                                        try:
                                            while True:
                                                ld02=pickle.load(pl01)
                                                for i in ld02:
                                                    print(i)
                                                    dashes()
                                        except EOFError:
                                            pass

                                        pl01.close()
                                        #ROOM TYPE----------------------------------------------------
                                        hot_inp=int(input('\nENTER THE CORRESPONDING HOTEL NUMBER: '))
                                        rooms()

                                    elif plctochs=='TAMIL NADU' or plctochs=='tamil nadu':

                                        pl01=open('TAMILNADU.dat','rb')
                                        try:
                                            while True:
                                                ld02=pickle.load(pl01)
                                                for i in ld02:
                                                    print(i)
                                                    dashes()
                                        except EOFError:
                                            pass

                                        pl01.close()
                                        #ROOM TYPE----------------------------------------------------
                                        hot_inp=int(input('\nENTER THE CORRESPONDING HOTEL NUMBER: '))
                                        rooms()

                                    elif plctochs=='HYDERABAD' or plctochs=='hyderabad':

                                        pl01=open('HYDERABAD.dat','rb')
                                        try:
                                            while True:
                                                ld02=pickle.load(pl01)
                                                for i in ld02:
                                                    print(i)
                                                    dashes()
                                        except EOFError:
                                            pass

                                        pl01.close()
                                        #ROOM TYPE----------------------------------------------------
                                        hot_inp=int(input('\nENTER THE CORRESPONDING HOTEL NUMBER: '))
                                        rooms()
                                    
                                    else:
                                        print('\n-----SORRY THE PLACE IS NOT REGISTERED-----')

                                    
                                    
                        else:
                            print('\nPLEASE ENTER CORRECT PASSWORD\n')
                    av01.close()
                else:
                    print('\nPLEASE SIGN-IN\n')
                dashes()
                
        else:
            print('\nSIGNNING-IN')


            unm=input('ENTER THE USERNAME: ')
            utyp=input('ENTER THE USER-TYPE(OWNER/CUSTOMER): ')
            dt01='{}.dat'.format(unm)
            if utyp=="owner" or utyp=="OWNER":
                own_pass=input("ENTER THE AUTHORIZATION PASSWORD: ")
                dt_own='{}_owner.dat'.format(unm)
                av03=open(dt_own,'wb+')
                pickle.dump(own_pass,av03,pickle.HIGHEST_PROTOCOL)
                av03.close()
            else:
                
                sg=sign_det(unm,utyp)
                sg.pass_sign()
                av01=open(dt01,'wb+')
                pickle.dump(pas_sgn,av01,pickle.HIGHEST_PROTOCOL)
                print('\nSIGNED IN SUCCESSFULLY')
                av01.close()