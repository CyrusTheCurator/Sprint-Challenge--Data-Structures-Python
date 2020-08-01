import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements
set_saves_us_all = set(names_2)
for i, name_1 in enumerate(names_1):
    if name_1 in set_saves_us_all:
        duplicates.append(name_1)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
#                                                                                   
#                                               88                                  
#                                        ,d     ""                                  
#                                        88                                         
# 8b,dPPYba,  88       88  8b,dPPYba,  MM88MMM  88  88,dPYba,,adPYba,    ,adPPYba,  
# 88P'   "Y8  88       88  88P'   `"8a   88     88  88P'   "88"    "8a  a8P_____88  
# 88          88       88  88       88   88     88  88      88      88  8PP"""""""  
# 88          "8a,   ,a88  88       88   88,    88  88      88      88  "8b,   ,aa  
# 88           `"YbbdP'Y8  88       88   "Y888  88  88      88      88   `"Ybbd8"'  
                                                                                  
#                                                                                   : 0.005002021789550781 seconds


#*(PSST! I USED SET!!! AAAAAA!!!!)