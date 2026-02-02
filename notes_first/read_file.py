import csv
while True:
    try:
        with open("notes_first/reading.txt", "r") as file:
            for line in file:
                print(f"Hello {line.strip()}")
    except:
        print("That file can't be found")
    else:
        print("code ends")
        break

try:
    with open("notes_first/sample.csv", mode ="r") as csv_file:
        content = csv.reader(csv_file)
        headers = next(content)
        rows = []
        for line in content:
            rows.append({headers[0]: line[0], headers[1]: line[1]})
except:
    print("Can't find the CSV")
else:
    for line in rows:
        print(line)