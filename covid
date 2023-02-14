import requests
import json
import compile_data
###############################################################
# I have created multiple functions to perform the calculations
# and data pulling. The main funciton that is used to output
# the data is 'main' at the bottom of the file. Thanks!
###############################################################
print("\nCovid confirmed cases statistics\n")

def average(st):
    avg_total = 0
    for i in st:
        avg_total += int(i["positiveIncrease"])
    return round(float(avg_total) / float(len(st)),2)
    #This funcitons totals all the values and divides them by how many
    #dates were used.
        

def date_highest(st):
    max_date = 0
    max_val = 0
    for i in st:
        if int(i["positiveIncrease"]) > max_val:
            max_val = int(i["positiveIncrease"])
            max_date = i["date"]
    return [max_date, max_val]
    #This function performs a sort algorithim and ouputs the date
    #with the highest number of new cases

def recent_no_new(st):
    recent = 0
    for i in st:
        if int(i["positiveIncrease"]) == 0:
            recent = i["date"]
            return recent
    #This function starts from the most recent date and checks if 
    #the new cases are zero. If so, it breaks the functions by returning
    #that date

def month_highest(st):
    high = []
    month_list = []
    for i in st:
        if str(i["date"])[0:6] not in month_list:
            month_list.append(str(i["date"])[0:6])
    #This function has three sections
    #This section of the function creates a list of months by
    #indexing the first 6 characters in each 'date'
            
    for i in month_list:
        total = 0
        for j in st:
            if str(j["date"])[0:6] == i:
                total += int(j["positiveIncrease"])
        high.append([i, total])
    #This section of the function adds values to a running
    #total depending on the date
    
    h_val = 0
    h_name = 0            
    for i in high:
       
        if i[1] > h_val:
            h_val = i[1]
            h_name = i[0]
    
    return [h_name, h_val]
    #This section of the funciton sorts and returns the highest month
    
        

def month_lowest(st):
    low = []
    month_list = []
    for i in st:
        if str(i["date"])[0:6] not in month_list:
            month_list.append(str(i["date"])[0:6])
    #This function has three sections
    #This section of the function creates a list of months by
    #indexing the first 6 characters in each 'date'
    #Additionally, it makes sure that no month is added more than once.
            
    for i in month_list:
        total = 0
        for j in st:
            if str(j["date"])[0:6] == i:
                total += int(j["positiveIncrease"])
        low.append([i, total])
    #This section of the function adds values to a running
    #total depending on the date
    
    l_val = low[0][1]
    l_name = 0            
    for i in low:
        
        if i[1] < l_val:
            l_val = i[1]
            l_name = i[0]

    return [l_name, l_val]
    #This section of the funciton sorts and returns the lowest month

def main():
    abv = ["ca", "ut", "il", "az", "tx"]
    dict_states = {"ca": "California", "ut": "Utah", "il": "Illinois", "az": "Arizona", "tx": "Texas"}
    #I am using a list of states, so that a user can swap out
    #states they might want to use, along with a dictionary
    #That provides the full state name form the abbreviation
    
    compile_data.compile() #this will compile the data using a seperate .py file

    
    for state in abv:
        file = open("/home/ubuntu/environment/hw3/" + state + ".json", "r")
        data = json.load(file)
        #This loads the .json file into a dictionary
        print("State name: %s" % str(dict_states[state]))
        print("Average number of new daily confirmed cases for the entire state dataset: %s" % str(average(data)))
        print("Date with the highest new number of confirmed cases: %s" % date_highest(data)[0])
        print("Most recent date with no new confirmed cases: %s " % recent_no_new(data))
        print("Month with the highest new number of confirmed cases: %s" % month_highest(data)[0])
        print("Month with the lowest new number of confirmed cases: %s\n" % month_lowest(data)[0])
        #all of the previously defined funcions are called here and
        #printed at the same time
        
main()
