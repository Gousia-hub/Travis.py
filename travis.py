known_users = ["Irfu","Alice","Emma","Siraj","Shabana"]

while True:
    print("Hi! My name is Travis")
    name = input("wat is ur name?: ").strip().capitalize()
    
    if name in known_users:
        print("name recognised")
        print("Hello!{}".format(name) )
        remove = input("Would u liked to be removed from the system?(yes/no): ").strip().lower()

        if remove == "yes":
            
           known_users.remove(name)
           print(known_users)
           

        elif:
            
            
            
            print("No problem! i didn't want u to leave anyway!")
    

    else:
        
        print("Hmmm I don't think i have met u yet {}".format(name))
        add = input("Would u like to get added in the system?(yes/no): ").strip().lower()
        
        if add == "yes":
            print(known_users)
            known_users.append(name)
            print(known_users)
            print("WELCOME to our system {}".format(name))
        elif :
            
            
            print("As u wish , hoping to see u around!")

            
        
















        




        
   


        
        


   
