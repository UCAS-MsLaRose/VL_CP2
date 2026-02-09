
"""with open("notes_first\\proof.txt", 'r+') as file:
    content = file.read()
    content += "\nI wrote on my file"
    file.write(content)



with open("notes_first\\writing.txt", 'a') as file:
    file.write("\nThis is more on my file!")

print("code end")"""

import csv

with open("notes_first/sample.csv", 'r+', newline='') as csvfile:
    fieldnames = ['username', 'color']
    reader = csv.reader(csvfile)
    for line in reader:
        print(f"{fieldnames[0]}, {line[0]} favorite color {line[1]}")
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    #writer.writeheader()
    writer.writerow({'username': 'new1', 'color': 'pink'})
    writer.writerow({'username': 'new2', 'color': 'red'})
    writer.writerow({'username': 'new3', 'color': 'green'})
    writer.writerow({'username': 'new4', 'color': 'blue'})


print("Code is done")