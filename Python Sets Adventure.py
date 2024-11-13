# Task 1 FLight Route Comparison:Imagine you work for an airline and need to compare the flight
#routes of your airline with a competitor. You have two sets of flight destinations, one for each
#airline. Write a Python program to find out: 1. Destinations that both airlines fly, 2. Destinations
#unique to your airline, and 3. Wherther there are any destinations that neither airline shares.

our_routes = {"LAX", "JFK", "CDG", "DXB", "ATL", "BHM", "DFW", "DAB"}                                                 #defining the sets
competitor_routes = {"JFK", "CDG", "LHR", "BKK", "ATL", "ANC", "DFW", "FLL"}

def routes_comparison(routes1, routes2):                                                                              #setting up a function to compare the two different sets
    shared = routes1.intersection(routes2)                                                                            #intersection comparison on the sets to see what they have in common
    print(f"\nThese are the routes shred by both airlines: {shared}")                                                 #print statement to inform the user of the results

    unique = routes1.difference(routes2)                                                                              #difference comparison to set what is unique to the first set 
    print(f"\nThese routes are unique to our airline: {unique}")                                                      #another print statement letting the user know the results

    not_shared = routes1.symmetric_difference(routes2)                                                                #symmetric diff comparison to find out what is unique to each set
    print(f"\nThese routes are uniqe to each airline: {not_shared}")                                                  #final print statement letting the user know the results
 
routes_comparison(our_routes, competitor_routes)                                                                      #calling the funciton
