import csv

with open("evaluation_scoring.csv", encoding="utf-8-sig") as file:
    rows = list(csv.DictReader(file))

fields = ["accuracy", "relevance", "safety", "clarity"]

complete = [
    row for row in rows
    if all(row[field].strip() in ("0", "1", "2") for field in fields)
]

total_points = sum(
    sum(int(row[field]) for field in fields)
    for row in complete
)

maximum_points = len(rows) * 8

print("Total scenarios:", len(rows))
print("Fully scored:", len(complete))
print("Missing or invalid:", len(rows) - len(complete))
print("Points earned:", total_points)
print("Maximum possible:", maximum_points)

if len(complete) == len(rows) and maximum_points > 0:
    percentage = (total_points / maximum_points) * 100
    print("Baseline percentage:", round(percentage, 2))
else:
    print("Baseline percentage: PENDING")
