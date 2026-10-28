\# Phase 4: Conversation Memory Improvement Results



\*\*Project:\*\* AI-Powered IT Help Desk Assistant  

\*\*Date:\*\* October 26, 2026  

\*\*Improvement:\*\* Context-aware troubleshooting follow-ups  

\*\*Evaluation file:\*\* `evaluation\_memory\_phase4.csv`



\## 1. Problem Identified



During Phase 3 volunteer testing, the assistant frequently repeated generic clarification questions when users provided follow-up information.



For example, a user could describe a Wi-Fi problem and then respond with only their operating system. The assistant would treat that response as an unrelated question rather than continuing the original troubleshooting process.



The first volunteer specifically recommended improving conversational memory.



\## 2. Improvement Implemented



The application was updated to pass the previous user message from Streamlit's session history to the troubleshooting engine.



The `troubleshoot()` function now accepts an optional `previous\_issue` parameter.



When the current message appears to be a short follow-up, the engine can consider the previous issue when selecting a troubleshooting guide.



The implementation also recognizes several phrases indicating a new problem, helping prevent unrelated troubleshooting scenarios from being combined.



Existing security escalation rules were retained.



\## 3. Evaluation Method



A separate evaluation script, `evaluate\_memory.py`, was created to test 10 conversation scenarios.



Each scenario was evaluated in two ways:



\- \*\*Before:\*\* The engine received only the current message.

\- \*\*After:\*\* The engine received the current message and the previous issue.



The evaluation compared the selected troubleshooting category against an expected category.



The test scenarios included follow-up questions, operating-system clarification, DNS troubleshooting, slow-computer issues, printer troubleshooting, switching problems, and security escalation.



\## 4. Results



| Measurement | Before | After |

|---|---:|---:|

| Passing scenarios | 4/10 | 10/10 |

| Pass rate | 40% | 100% |

| Improvement | | +60 percentage points |



Six scenarios that failed without conversation context passed when the previous issue was supplied.



The four scenarios that originally passed continued to pass.



\### Additional Testing



Five manual conversation tests passed:



1\. Wi-Fi troubleshooting follow-up.

2\. Operating-system clarification.

3\. Security escalation.

4\. Explicitly switching to a new problem.

5\. Switching from Wi-Fi to printer troubleshooting.



All five existing automated unit tests also passed.



\## 5. What Improved



The assistant demonstrated better recognition of short follow-up messages.



Users can provide information such as "Windows 10" or "It still isn't working" without immediately losing the previous troubleshooting category.



The targeted evaluation also showed that the tested security escalation and new-problem scenarios continued to work.



\## 6. Remaining Limitations



The assistant currently considers only the immediately preceding user message rather than maintaining a complete structured conversation history.



The evaluation measures troubleshooting-category selection, not the accuracy or effectiveness of every troubleshooting instruction.



The 10 scenarios were designed specifically to evaluate conversation handling and are not a representative sample of all possible support requests.



Operating-system-specific instructions and environmental context recognition remain areas for future improvement.



The original Phase 2 rule-based evaluation score of 225/240 (93.75%) is a separate baseline and should not be directly compared with the 10-scenario memory evaluation.



\## 7. Conclusion



The conversation-memory improvement addressed a specific weakness identified during real-user testing.



The targeted evaluation improved from 4/10 to 10/10 passing scenarios, while the existing automated tests continued to pass.



These results provide evidence of a meaningful improvement in short follow-up handling, although broader testing is still necessary before claiming general improvements in troubleshooting accuracy.



**Status:** Improvement implemented, evaluated, deployed to Render, and successfully tested on the public application on October 26, 2026.

