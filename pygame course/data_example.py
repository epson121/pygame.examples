#working with data
file = open("example_sorted_names.txt")

name_list = []
for line in file:
    line = line.strip()
    name_list.append(line)

file.close()

# Linear search
i=0
while i < len(name_list) and name_list[i] != "Morgiana the Shrew":
    i += 1
     
if i == len(name_list):
    print( "The name was not in the list." )
else:
    print( "The name is at position",i)
