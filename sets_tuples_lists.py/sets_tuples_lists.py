#collection = single "variable" used to store multiple values
#list = [] ordered and changeable. duplicates OK
# set =() unordered and imutable, but add/remove OK. NO dupelicates
#tuple=() ordered and unchangeable. Duplicates OK. FASTER

fruits=["apple","orange","banana","coconut","kiwi","strawberry"]
#print(dir(fruits))# tells us all the methods that come with it
#print(help(fruits))#
#print(len(fruits))# tells us the length
#print("pineapple" in fruits) #tells us if pineapple is in fruits

#fruits[0]="pineapple" #Reasign values

#print(fruits[0]) 
#print(fruits[4])

#fruits[0]="pineapple"
#fruits.append("pineapple")#this adds pineapple to a list
#fruits.remove("apple")#this takes apple from the list
#fruits.insert(0,"pineapple")
#fruits.sort()#this sorts into alpabetical order
#fruits.reverse()#this reverses
#fruits.clear()
#print(fruits.index('coconut'))
#print(fruits)

#for x in fruits: print(x)


#cars=("bmw","maserati","audi","mercades","ferrari")
#print(f"these are a list of cars {cars}")
#print(f"the first car is {cars[0]}")

#changing value of the list
#cars[0]="toyota"
#print(f"the first car is{cars[0]}")

#print(f"the last car is{cars[-1]}")
#cars[-1]="lamborgihini"
#print(f"the last car is{cars[-1]}")

#adding a new value to the text
#cars.apend("bugatti")
#print (cars)
#cars.remove("maserati")
#print(cars)

#looping through the list
#otherwid3e called iterating through the list
#for car in cars:
#print(len(car))
#print(car) 
    #carRequest = input("add a new car please:")
    #cars.append(carRequest)
    #print(cars)
    #print(len(cars))
    #print(cars.upper())
    #print(cars)
    #if len(cars)>10:
           # break
    
    #challenge
    #create a list of friends
    #make sure the initial list is none
friends=[]
    #add a new friend to the lsit, add at least 5 friends
friends.append("Abel")
friends.append("Lorenzo")
friends.append("Angel")
friends.append("Alex")
friends.append("Oscar")
    #remove a friend
friends.remove("Abel")
    #insert a friend at a specifi index maybe 2
friends[2]="Abel"
    #print the list of friends
    
    
        #loop through the lsit and print the friends name
for friend in friends:
            friendMore= input("add a new friend please:")
            friends.append(friendMore)
            print(friends)
         #see if a particular friend is in the list(boolean value)
            print("Abel"in friends)
            #if the lsit is grater than 10 break the loop
            if len(friends)>10:
                    break
