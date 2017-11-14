print("\t\t********************************************************")
print("\t\t*       SCRIPT MADE BY HAWK                            *")
print("\t\t*       Presented By : www.hawksek.com                 *")
print("\t\t********************************************************")

responses = {}

polling_active = True
#set the flag to indicate the pooling
while polling_active:
    # prompt for the person name and response 
    name = input("\nWhat is Your Name ")
    response = input("Which Mountain Would you like to climb someday")
    
    #store the response in dictionary:
    responses[name] = response
    
    #find out if anyone else is going to take the poll 
    repeat = input("Would you like to let another person respond? (yes/no)")
    if repeat == 'no':
        polling_active = False 
        
#polling is complete . Show the Result
print("\n--- Poll Results ---")
for name, response in responses.items():
    print(name + "Would like to climb" + response + ".")
