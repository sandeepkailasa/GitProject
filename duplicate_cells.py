import csv
from collections import defaultdict

cell_map = defaultdict(list)

with open("cells.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        library = row["library"]
        cell = row["cell"]

        cell_map[cell].append(library)

print("\nDuplicate Cells Report\n")

duplicate_found = False

for cell, libs in cell_map.items():
    if len(libs) > 1:
        duplicate_found = True
        print(f"Cell: {cell} appears in libraries: {', '.join(libs)}")

if not duplicate_found:
    print("No duplicate cells found.")
