import sys

if not sys.stdin.isatty():
    list = []
    for line in sys.stdin:
        #remove whitespace from each line
        line = line.strip()
        words = line.split()
        for word in words:
            list.append(word)
    list.sort()
    list.sort(key=len)
    for word in list:
        print(word)
else:
    #creates text file to contain sorted list
    file2=open("Sorted.txt","w")

    #reads each line of Sort Me.txt and places it into a list
    with open("SortMe.txt") as file1:
        file1listTemp = file1.read().splitlines()

    #removes extra whitespace in each string    
    file1list = []
    for item in file1listTemp:
        strip = item.replace(' ','')
        file1list.append(strip)

    #sorts alphabetically
    file1list.sort()

    #sorts by length either normally or in reverse depending on user input
    userChoice = ''
    while userChoice not in ['Y', 'y', 'N', 'n']:
        userChoice = input("Do you want to reverse the list? Y/N: ")
        if userChoice.upper() == 'Y':
            file1list.sort(key=len, reverse=True)
        elif userChoice.upper() == 'N':
            file1list.sort(key=len)

    #writes items from sorted list into the Sorted.txt file
    for items in file1list:
        file2.write("%s\n" %items)

    print("File written successfully")

    #close files
    file1.close()
    file2.close()