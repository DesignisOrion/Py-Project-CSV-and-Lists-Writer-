
# importing csv to file. Not needed for the list example below. Formatting was done.
import csv

# writing to list example


# Open the file by doing this.
f = open("test_file.txt", "w")
f.write("test text")
f.close()

# file permissions
# write : Overwrite any existing content
# append: add to the existing content
# "w" means write where as "r" means read only


# writing to CSV file example. be sure to add the import at the top before doing so.

# CSV file : Contains commas separated values
# Tuple: A sequence of immutable python objects


# Open the file by doing this
f = open("people.csv", "a", newline="")
tupl = ("bob", 19)
writer = csv.writer(f)
writer.writerow(tup1)
tupl = ("joe", 22)
writer = csv.writer(f)
writer.writerow(tup1)
f.close()

