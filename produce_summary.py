file_list = ["um-deliveries-day-1.txt", "um-deliveries-day-2.txt", "um-deliveries-day-3.txt"]
                                    #Created an array with strings representing each file name 
                                    #to pull data from

for file in file_list:              #for loop to run through each string in the array
    day = file_list.index(file) + 1 #set a variable to match the number of day to the file number,
                                    #based on the index number of the array for each item in the loop
    print(f"Day {day}")             #print 'Day #', pulling from the variable to fill in the #

    the_file = open(file)           #new variable which runs function open() for each file in
                                    #the array, in order

    for line in the_file:           #nested for loop, pulling each line of text from .txt files
        line = line.rstrip()        #strips any white space off the end of the text line
        words = line.split('|')     #splits the string of each line, using | as a delimiter,
                                    #tokenizing each item into an array

        melon = words[0]            #these 3 create variables based on each item in the new array words
        count = words[1]
        amount = words[2]

        print(f"Delivered {count} {melon}s for total of ${amount}") #f-string to reproduce data from .txt
                                                                    #files based on variables above
    the_file.close()                #closes the file


# print("Day 2")
# the_file = open("um-deliveries-day-2.txt")
# for line in the_file:
#     line = line.rstrip()
#     words = line.split('|')

#     melon = words[0]
#     count = words[0]
#     amount = words[0]

#     print(f"Delivered {count} {melon}s for total of ${amount}")
# the_file.close()


# print("Day 3")
# the_file = open("um-deliveries-day-3.txt")
# for line in the_file:
#     line = line.rstrip()
#     words = line.split('|')

#     melon = words[0]
#     count = words[0]
#     amount = words[0]

#     print(f"Delivered {count} {melon}s for total of ${amount}")
# the_file.close()
