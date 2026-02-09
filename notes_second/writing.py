
"""with open("notes_second\\sample.txt", 'a') as file:
    file.write("\nJoe\n")
    file.write("Israel\n")
    file.write("Zee\n")

print("run finished")"""
"""content = []
with open("notes_second/sample.txt", 'r+') as file:
    for line in file:
        content.append(line.strip())

    index = content.index('Tia')
    content[index] = "Torii"

    file.truncate(0)

    for name in content:
        file.write(name + "\n")

print("Code ends")"""

import csv
"""with open("notes_second/test.csv", 'w', newline='') as csvfile:
    fieldnames = ['username', 'favorite color']
    writer = csv.writer(csvfile)

    #writer.writerow(fieldnames)
    writer.writerow(["user1", "red"])
    writer.writerow(["user2", "orange"])"""
users = [
    {'username':"cosmic_voyager", 'favorite color': "indigo"},{'username':"cosmic_voyager", 'favorite color': "indigo"},
         {'username':"cosmic_voyager", 'favorite color': "indigo"},{'username':"cosmic_voyager", 'favorite color': "indigo"},{'username':"cosmic_voyager", 'favorite color': "indigo"}]
with open("notes_second/test.csv", 'r+', newline='') as csvfile:
    fieldnames = ['username', 'favorite color']
    reader = csv.reader(csvfile)
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    #writer.writeheader()
    #writer.writerow(fieldnames)
    writer.writerows(users)

"""import os
os.remove()"""