import csv
from engine import troubleshoot

# Load our evaluation dataset
with open("evaluation_dataset.csv", "r", encoding="utf-8-sig", newline="") as file:
    reader = csv.DictReader(file)
    test_cases = list(reader)

print(f"Loaded {len(test_cases)} evaluation scenarios.")
# Store evaluation results for later analysis
evaluation_results = []
# Run each scenario through the rule-based engine
for case in test_cases:
    test_id = case["test_id"]
    question = case["student_question"]

    result = troubleshoot(question)
    evaluation_results.append({
        "test_id": test_id,
        "category": case["category"],
        "student_question": question,
        "expected_behavior": case["expected_behavior"],
        "engine_title": result["title"],
        "engine_steps": " | ".join(result["steps"]),
        "engine_source": result["source"]
    })

    print(f"\nTest Case: {test_id}")
    print(f"Category: {case['category']}")
    print(f"Engine Response: {result['title']}")

print(f"\nTotal results collected: {len(evaluation_results)}")
# Save evaluation results to a CSV file
with open("evaluation_results.csv", "w", newline="", encoding="utf-8") as file:
    fieldnames = [
        "test_id",
        "category",
        "student_question",
        "expected_behavior",
        "engine_title",
        "engine_steps",
        "engine_source"
    ]

    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(evaluation_results)

print("Evaluation results saved to evaluation_results.csv")
# Create a separate worksheet for manual quality scoring
scoring_fields = [
    "test_id",
    "category",
    "student_question",
    "expected_behavior",
    "engine_title",
    "engine_steps",
    "engine_source",
    "accuracy",
    "relevance",
    "safety",
    "clarity",
    "review_notes"
]

with open("evaluation_scoring.csv", "w", newline="", encoding="utf-8-sig") as file:
    writer = csv.DictWriter(file, fieldnames=scoring_fields)
    writer.writeheader()

    for result in evaluation_results:
        row = result.copy()
        row["accuracy"] = ""
        row["relevance"] = ""
        row["safety"] = ""
        row["clarity"] = ""
        row["review_notes"] = ""
        writer.writerow(row)

print("Scoring worksheet created: evaluation_scoring.csv")
