\# AI-Powered IT Help Desk Assistant

\## Post-Capstone Development Backlog



\*\*Created:\*\* October 28, 2026  

\*\*Project status:\*\* Completed DeVry capstone; continuing as a personal development project  

\*\*Priority:\*\* Improve conversation handling, troubleshooting accuracy, and user experience.



\### 1. Improve Conversation Memory and Context Handling

\*\*Priority: High\*\*



\*\*Problem:\*\* Multiple testers reported that the assistant repeated troubleshooting instructions, failed to acknowledge previously completed steps, or lost track of the original problem during follow-up questions.



\*\*Planned modifications:\*\*

\- Review how `app.py` stores conversation history using `st.session\_state`.

\- Review how `engine.py` receives and interprets previous troubleshooting information.

\- Track the user's current problem, device type, and completed troubleshooting steps.

\- Prevent the assistant from repeating steps the user has already completed.

\- Recognize follow-up statements such as "I already tried that" and "That didn't work."

\- Maintain context when users provide additional information.



\*\*Success criteria:\*\* The assistant recognizes completed steps and provides an appropriate next action without unnecessarily restarting troubleshooting.



\### 2. Improve Technical Intent Recognition

\*\*Priority: High\*\*



\*\*Problem:\*\* Tester Hunter-157 asked questions involving CGNAT, DNS connectivity, and TCP port 443. The assistant responded with generic DNS or Wi-Fi troubleshooting instructions instead of recognizing the more advanced technical requests.



\*\*Planned modifications:\*\*

\- Improve classification of user questions before selecting a troubleshooting guide.

\- Distinguish basic DNS problems from advanced network configuration requests.

\- Recognize terms such as CGNAT, TCP ports, port forwarding, port allocation, and web servers.

\- Avoid routing every networking-related question to generic Wi-Fi instructions.

\- Provide a clear explanation when a question falls outside the assistant's supported capabilities.



\*\*Success criteria:\*\* Advanced networking questions receive an accurate scope explanation rather than unrelated troubleshooting instructions.



\### 3. Add Device and Operating System Recognition

\*\*Priority: High\*\*



\*\*Problem:\*\* Testers reported receiving Windows Command Prompt instructions when discussing problems involving phones or other devices.



\*\*Planned modifications:\*\*

\- Detect whether the user is troubleshooting Windows, macOS, Linux, Android, iPhone, or another device.

\- Ask for the device type when it cannot be determined.

\- Only provide commands appropriate for the identified operating system.

\- Clearly explain when a device is outside the assistant's supported troubleshooting scope.



\*\*Success criteria:\*\* The assistant does not recommend Windows-specific commands for non-Windows devices.



\### 4. Improve Troubleshooting Progression

\*\*Priority: High\*\*



\*\*Problem:\*\* Some testers received lengthy lists of instructions or repeated the same troubleshooting process without progressing toward a solution.



\*\*Planned modifications:\*\*

\- Present one or two troubleshooting steps at a time.

\- Ask users to report the results before continuing.

\- Track which steps have been completed.

\- Provide alternative steps when previous attempts fail.

\- Escalate unresolved problems instead of repeating the same instructions indefinitely.



\*\*Success criteria:\*\* Troubleshooting progresses logically based on the user's responses.



\### 5. Improve Clarification Questions

\*\*Priority: Medium\*\*



\*\*Problem:\*\* The assistant sometimes entered clarification loops or asked basic questions after the user had already supplied relevant information.



\*\*Planned modifications:\*\*

\- Check existing conversation context before requesting information.

\- Avoid asking questions already answered by the user.

\- Make clarification questions specific to the reported problem.

\- Limit repeated clarification attempts.

\- Provide an appropriate escalation response when the issue remains unclear.



\*\*Success criteria:\*\* The assistant asks relevant questions without repeatedly requesting the same information.



\### 6. Improve Advanced-Question Handling and Scope Awareness

\*\*Priority: Medium\*\*



\*\*Problem:\*\* The assistant did not clearly explain its limitations when Hunter-157 asked about TCP port allocation and configuring port 443 for a web server.



\*\*Planned modifications:\*\*

\- Add a dedicated response category for unsupported advanced technical requests.

\- Explain which troubleshooting topics the assistant currently supports.

\- Recognize advanced topics without pretending to provide complete solutions.

\- Offer appropriate next steps or escalation recommendations.

\- Preserve existing safety restrictions against unauthorized system changes.



\*\*Success criteria:\*\* Unsupported requests receive clear, relevant explanations rather than generic troubleshooting guides.



\### 7. Expand Automated Testing

\*\*Priority: High\*\*



\*\*Problem:\*\* Phase 4 targeted conversation-context testing improved from 4/10 to 10/10, but real-world testing revealed additional weaknesses not covered by those scenarios.



\*\*Planned modifications:\*\*

\- Expand `evaluation\_dataset.csv` with real-world scenarios from all six testers.

\- Add tests for repeated instructions and completed troubleshooting steps.

\- Add tests for device and operating system mismatches.

\- Add tests for advanced networking questions.

\- Add tests for clarification loops.

\- Add multi-turn conversation tests that verify responses across several messages.

\- Compare future results against the existing Phase 4 baseline.



\*\*Success criteria:\*\* Automated tests reproduce the documented problems and confirm whether subsequent code changes resolve them.



\### 8. Improve Mobile User Experience

\*\*Priority: Low\*\*



\*\*Observation:\*\* Hunter-157 tested the deployed application through a mobile browser. Screenshots show that troubleshooting instructions were displayed, but the responses occupied considerable vertical space.



\*\*Planned modifications:\*\*

\- Review the mobile layout.

\- Reduce unnecessary scrolling where practical.

\- Consider shorter, progressive troubleshooting responses.

\- Verify that the message input and chat history remain easy to use on smaller screens.



\*\*Success criteria:\*\* The application remains readable and practical on mobile devices.



\*\*Note:\*\* Mobile usability was not explicitly identified as a problem by Hunter-157. This is a proposed enhancement based on the screenshots, not a confirmed defect.



\---



\## Recommended Development Order



| Order | Development task |

|---|---|

| 1 | Review existing conversation-memory implementation |

| 2 | Improve recognition of completed troubleshooting steps |

| 3 | Implement device and operating system detection |

| 4 | Improve technical intent classification |

| 5 | Add scope-aware handling of advanced questions |

| 6 | Implement progressive troubleshooting |

| 7 | Improve clarification handling |

| 8 | Expand automated regression tests |

| 9 | Review mobile usability |



\## Development Guidelines



\- Preserve the working production application.

\- Make improvements in small, testable increments.

\- Avoid introducing unsupported troubleshooting instructions.

\- Maintain existing security safeguards.

\- Test locally before deploying changes.

\- Document each improvement and its evaluation results.

\- Keep post-capstone development separate from the original DeVry submission.



\## Project Status



\*\*Original capstone:\*\* Complete and submitted October 27, 2026.



\*\*Post-capstone project:\*\* Active personal development.



\*\*Testing feedback:\*\* Six testers documented or reviewed.



\*\*Current development phase:\*\* Planning future improvements. No additional code modifications have been made as part of this backlog.



\*\*Primary objective:\*\* Transform the existing rule-based troubleshooting assistant into a more context-aware, reliable, and user-friendly IT support application while preserving its safety boundaries.

