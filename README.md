# AI-Powered IT Help Desk Assistant

A beginner-friendly IT troubleshooting assistant built with Python and Streamlit.

The application uses rule-based troubleshooting to provide approved diagnostic guidance for common Wi-Fi, DNS, and network connectivity problems.

An optional AI explanation feature uses a locally hosted Ollama model (Qwen2.5:0.5b). AI responses are supplementary and subject to validation.

The public demo is designed to run in rule-based mode without requiring Ollama or external API keys.

## Run on Windows PowerShell

1. Install Python 3.11+ from python.org (or use an existing installation).
2. Open PowerShell in this folder.
3. Run:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -m streamlit run app.py
```

If PowerShell blocks activation, skip activation and run:

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m streamlit run app.py
```

A local browser page should open (typically http://localhost:8501).

## Test

```powershell
python -m unittest -v test_engine.py
```

## Evaluation and results

The prototype was evaluated using 30 test scenarios covering Wi-Fi, DNS, connectivity, challenging requests, and security-related questions.

- Original rule-based evaluation: 225/240 points (93.75%).
- Six security escalation regression tests passed after correcting the administrator-password detection rule.
- The original AI evaluation produced 17 generated responses, 8 validation fallbacks, and 5 security suppressions.
- The revised AI evaluation produced 10 generated responses, 14 validation fallbacks, and 6 security suppressions.

The prompt iterations did not demonstrate consistent improvement in AI response quality. These limitations are documented in `evaluation_findings.txt`.

## Safety features

- Uses predefined troubleshooting guidance.
- Escalates recognized security-sensitive requests to human IT support.
- Prevents AI generation for recognized escalation cases.
- Blocks certain command strings in AI explanations and substitutes a fallback response.
- Warns users not to submit passwords or confidential information.
- Public-demo mode disables local Ollama AI explanations.

## Limitations and roadmap

- Keyword matching cannot reliably understand every possible user request.
- Security keyword detection is not comprehensive.
- AI validation does not catch every incorrect or unsupported suggestion.
- The application does not execute troubleshooting commands.
- The application does not provide live document retrieval.
- Public deployment, real-user feedback, and production monitoring remain Phase 3 goals.
- Future improvements include stronger AI validation, better issue classification, and expanded evaluation coverage.

**Important:** This prototype is intended for educational purposes and low-risk troubleshooting. It is not a replacement for professional IT or security support.