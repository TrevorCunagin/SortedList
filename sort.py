#creates text file to contain sorted list
file2=open("Sorted.txt","w")

#reads each line of Sort Me.txt and places it into a list
with open("Sort Me.txt") as file1:
    file1list = file1.read().splitlines()

#first sorts alphabetically, then by length 
file1list.sort()
file1list.sort(key=len)

#writes items from sorted list into the Sorted.txt file
for items in file1list:
    file2.write("%s\n" %items)

print("File written successfully")

#close files
file1.close()
file2.close()