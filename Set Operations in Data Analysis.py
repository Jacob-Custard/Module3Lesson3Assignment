# Task 1 Duplicate Entries Cleanup: You are given a list of customer IDs, some of which are duplicated.
#Write a Python script to remove duplicates and display the unique customer IDs.

customer_ids = ["C001", "C002", "C003", "C002", "C001", "C004", "C005", "C002", "C006", "C006", "C001", "C003", "C004"]              #initial list with duplicates

nodupes_customer_ids = set(customer_ids)                                                                                             #turning the list into a set which will remove duplicates 

print(nodupes_customer_ids)                                                                                                          #printing the set                            

for id in nodupes_customer_ids:                                                                                                      #initilaized a 'for' loop to print the set in a slightly more formatted way
    print(id)

