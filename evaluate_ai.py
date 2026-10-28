import csv
import time

from engine import troubleshoot
from ai_helper import ask_ai

with open("evaluation_dataset.csv", newline="", encoding="utf-8-sig") as file:
    test_cases = list(csv.DictReader(file))

results = []

for case in test_cases:
    question = case["student_question"]
    engine_result = troubleshoot(question)

    title = engine_result["title"]
    steps = engine_result["steps"]

    # Match the application's AI suppression rule.
    if title == "Human IT support recommended":
        ai_response = "AI SUPPRESSED - Human IT support required"
        ai_status = "suppressed"
    else:
        ai_response = ask_ai(question, steps)

        if ai_response.startswith("The AI explanation did not pass validation."):
            ai_status = "validation_fallback"
        else:
            ai_status = "generated"

    results.append({
        "test_id": case["test_id"],
        "category": case["category"],
        "student_question": question,
        "expected_behavior": case["expected_behavior"],
        "engine_title": title,
        "ai_status": ai_status,
        "ai_response": ai_response,
    })

    print(
        f"Test {case['test_id']}: {ai_status}",
        flush=True
    )

    time.sleep(0.2)

with open("ai_evaluation_results.csv", "w", newline="", encoding="utf-8-sig") as file:
    writer = csv.DictWriter(file, fieldnames=results[0].keys())
    writer.writeheader()
    writer.writerows(results)

print()
print("AI evaluation complete.")
print("Total scenarios:", len(results))
print("Results saved to ai_evaluation_results.csv")
