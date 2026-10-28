
import csv
from engine import troubleshoot

# Each scenario contains a previous message and a new message.
# We compare the engine's behavior with and without conversation memory.
test_cases = [
    ("Wi-Fi follow-up", "My Wi-Fi keeps disconnecting.",
     "It still isn't working.", "Wi-Fi and internet connection"),

    ("Operating system follow-up", "My Wi-Fi keeps disconnecting.",
     "Windows 10", "Wi-Fi and internet connection"),

    ("DNS follow-up", "I have a DNS error.",
     "The issue persists.", "DNS and website name resolution"),

    ("Slow computer follow-up", "My computer is running slow.",
     "I restarted but it still happens.", "Slow Windows computer"),

    ("Printer follow-up", "My printer is not printing.",
     "Still not working.", "Printer not working"),

    ("New printer issue", "My Wi-Fi keeps disconnecting.",
     "My printer is not printing.", "Printer not working"),

    ("New slow computer issue", "My Wi-Fi keeps disconnecting.",
     "New problem: My computer is very slow.", "Slow Windows computer"),

    ("Security escalation", "My Wi-Fi keeps disconnecting.",
     "I think my computer has been hacked.", "Human IT support recommended"),

    ("Unrelated unsupported issue", "My Wi-Fi keeps disconnecting.",
     "New problem: My keyboard is broken.", "A few questions first"),

    ("Short follow-up", "My printer is not printing.",
     "Windows 11", "Printer not working"),
]

results = []
before_passes = 0
after_passes = 0

for name, previous_issue, current_message, expected in test_cases:
    before = troubleshoot(current_message)
    after = troubleshoot(current_message, previous_issue=previous_issue)

    before_pass = before["title"] == expected
    after_pass = after["title"] == expected

    before_passes += before_pass
    after_passes += after_pass

    results.append({
        "scenario": name,
        "previous_issue": previous_issue,
        "current_message": current_message,
        "expected_title": expected,
        "before_title": before["title"],
        "after_title": after["title"],
        "before_pass": before_pass,
        "after_pass": after_pass,
    })

    print(f"\n{name}")
    print(f"  Before: {before['title']} | {'PASS' if before_pass else 'FAIL'}")
    print(f"  After:  {after['title']} | {'PASS' if after_pass else 'FAIL'}")

total = len(test_cases)

print("\n=== PHASE 4 MEMORY EVALUATION ===")
print(f"Before memory: {before_passes}/{total}")
print(f"After memory:  {after_passes}/{total}")
print(f"Change:        {after_passes - before_passes:+d} passing scenarios")

with open("evaluation_memory_phase4.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=results[0].keys())
    writer.writeheader()
    writer.writerows(results)

print("\nResults saved to evaluation_memory_phase4.csv")
