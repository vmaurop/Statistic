try:


    mylist = raw_input('Enter your list: ')
    mylist = [int(x) for x in mylist.split(',')] #dwse tous arithmous me koma



    sum1 = 0.0
    sum2=0.0





#mylist.remove(max(mylist))	#to exw valei se sxolia gia arxh..meta ta vgazoyme(afairei to max 2 fores k to min 2 fores)
	

#mylist.remove(max(mylist)) 

#mylist.remove(min(mylist))
#mylist.remove(min(mylist))



    for i in mylist:
        sum1 = sum1 + i
    mesitimi = float(sum1 / len(mylist)) #mesi timi tis listas

#print(mesitimi)







    y = [(i-mesitimi)**2 for i in mylist] #afairese apo kathe timi th mesi timi k meta ipswse tetragwno


    for i in y:                   #ypologise th nea mesi timi ths listas y
        sum2 = sum2 + i

    mesitimi2 = float(sum2/len(mylist))

    from math import sqrt #tetragwniki riza

    z=sqrt(mesitimi2) #apoklisi


    z=str(z) #to allazw morfi se str gia na to typwsw me logia

    print ('h apoklisi einai:'+z)

except:
    print("error")

