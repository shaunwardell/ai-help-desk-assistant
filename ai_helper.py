import json
import urllib.request

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "qwen2.5:0.5b"


def ask_ai(question, approved_steps):
    prompt = f"""
You are an IT Help Desk Assistant for students using Windows laptops.

Student question:
{question}

Approved troubleshooting steps:
{approved_steps}
The approved troubleshooting steps are already provided above.
You have everything needed to explain their purpose.
Do not ask the student to provide these steps again.
Do not offer to guide the student through a new procedure.

Instructions:
- Explain WHY the approved troubleshooting steps are useful for the student's specific problem.
- Use exactly 2 to 4 short sentences in one paragraph.
- Explain the purpose of the steps without listing or repeating them.
- Do not suggest, modify, quote, or repeat any commands.
- Do not introduce new troubleshooting actions, tools, or procedures.
- The application displays approved steps and commands separately.
- Use clear, beginner-friendly language without technical jargon.
- Do not request passwords, account details, or personal information.
- Do not claim the problem is fixed or promise that the steps will work.
- If the approved steps are insufficient, recommend contacting human IT support.
- Do not include greetings, headings, numbered lists, or unrelated information.
Format:
- Write 2 to 4 short sentences.
- Explain why the approved troubleshooting steps are useful.
- Use plain English suitable for a beginner.
- Do not include numbered steps or command examples.
Examples:

Example 1:
Student question: Why do we check whether other devices can connect to Wi-Fi?
Good response: Checking another device helps determine whether the problem affects only your laptop or the entire network.

Example 2:
Student question: Why do we check DNS?
Good response: DNS helps your computer find websites using their names. Checking DNS can help determine whether website names are being translated correctly.

Example 3:
Student question: My Wi-Fi keeps disconnecting.
Approved steps: Check whether Wi-Fi is enabled; Restart the computer; Contact IT support if the problem continues.
Good response: These steps help check basic wireless connectivity and rule out a temporary computer issue. If the connection still fails, IT support can investigate further.
"""
    payload = {
        "model": MODEL_NAME,
        "prompt": prompt,
        "stream": False
    }

    data = json.dumps(payload).encode("utf-8")

    request = urllib.request.Request(
        OLLAMA_URL,
        data=data,
        headers={"Content-Type": "application/json"}
    )

    with urllib.request.urlopen(request, timeout=60) as response:
        result = json.loads(response.read().decode("utf-8"))

    explanation = result["response"]
    print("EVALUATION - Raw AI response:")
    print(explanation)
    print("EVALUATION - Blocked commands detected:")
    print([cmd for cmd in ("nslookup", "ipconfig", "ping ") if cmd in explanation.lower()])

    blocked_commands = ("nslookup", "ipconfig", "ping ")
    if any(command in explanation.lower() for command in blocked_commands):
        return "The AI explanation did not pass validation. Please follow the approved troubleshooting steps above."

    return result["response"]