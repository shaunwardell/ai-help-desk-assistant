\# AI-Powered IT Help Desk Assistant

\## Product Development Case Study



\*\*Project:\*\* DeVry AI-Powered IT Help Desk Assistant

\*\*Date:\*\* October 26, 2026

\*\*Developer:\*\* Shaun Wardell

\*\*Live Application:\*\* https://ai-help-desk-assistant.onrender.com

\*\*GitHub Repository:\*\* https://github.com/shaunwardell/ai-help-desk-assistant



\### 1. Problem and Opportunity



Many students and everyday computer users experience technical problems but do not always know where to begin troubleshooting. Common issues involving Wi-Fi connections, DNS resolution, slow computers, and printers can be frustrating, particularly for users with limited technical experience.



Traditional troubleshooting resources often require users to search through multiple websites or understand unfamiliar technical terminology. This creates an opportunity for a simple, accessible assistant that provides structured guidance through a conversational interface.



The goal of this project was to design, build, evaluate, and launch an AI-powered IT Help Desk Assistant that helps users identify common technical issues while maintaining appropriate safety boundaries.



Rather than attempting to replace professional IT support, the assistant was designed as an educational troubleshooting tool that offers initial guidance and recommends human assistance when necessary.



\### 2. Product Solution



The solution is a web-based troubleshooting assistant developed using Python and Streamlit.



Users describe their technical problems through a chat interface. A rule-based troubleshooting engine analyzes their messages and selects guidance from predefined categories, including Wi-Fi connectivity, DNS resolution, slow Windows computers, and printer issues.



The application provides numbered troubleshooting instructions, relevant cautions, and information about the source of its guidance.



For potentially sensitive security incidents, such as suspected hacking, ransomware, or phishing, the assistant recommends contacting qualified IT or security personnel rather than attempting risky automated remediation.



An optional local AI explanation feature was developed using Ollama and the Qwen2.5 0.5B model. However, the public Render deployment operates in rule-based mode because the locally hosted AI model is not available in that environment.



This distinction is important: the publicly deployed product provides guided troubleshooting but does not generate live AI explanations.



\### 3. Development and Evaluation



The project was developed in Python, with separate components for the Streamlit interface, troubleshooting engine, and optional AI explanations.



GitHub was used for source control, and Render was selected to host the public application.



During development, a 30-scenario evaluation dataset was created to assess the assistant's behavior across common troubleshooting requests, challenging situations, and security-related questions.



The original rule-based evaluation produced a score of 225 out of 240 points, equivalent to 93.75%, based on the project's scoring rubric.



Additional testing explored AI-generated explanations and guardrails. These experiments demonstrated the importance of validating model-generated content rather than assuming that an AI response is accurate or safe.



Security protections were incorporated to prioritize escalation for sensitive incidents and discourage unsafe troubleshooting behavior.



\### 4. Product Launch and User Feedback



The application was successfully deployed to a public Render URL.



Initial production monitoring included five manually timed tests, producing an average response time of approximately 0.952 seconds while the application was active.



Because the application uses Render's free hosting tier, it may experience substantially longer startup delays after periods of inactivity. The measured response time should therefore not be interpreted as a guaranteed production response time.



The first volunteer tester evaluated the public application through a series of realistic troubleshooting questions.



The tester provided the following ratings:



\- Ease of use: 4/5

\- Accuracy: 4/5

\- Clarity: 5/5

\- Response time: Very quick



The tester found the application useful for introductory troubleshooting but identified several weaknesses.



The most significant issue was the assistant's inability to maintain conversational context. When users supplied additional details or reported that a previous troubleshooting step had not worked, the assistant sometimes repeated generic clarification questions.



Other problems included Windows-specific instructions appearing in responses to macOS or Linux users and failure to recognize environmental details, such as a wireless router located across the house.



These findings demonstrated the value of testing realistic conversations rather than relying exclusively on isolated questions.



\### 5. Improvement Based on Feedback



Based on the volunteer's feedback, conversation handling was selected as the first meaningful product improvement.



The original application stored chat messages for display, but its troubleshooting engine processed only the newest message.



The application was updated to pass the previous user message to the troubleshooting engine when evaluating a new request.



The engine was also modified to recognize short follow-up messages and phrases indicating that a user was starting a different problem.



This improvement allowed the assistant to interpret statements such as "Windows 10" or "It still isn't working" in the context of an earlier troubleshooting question.



The implementation was designed to preserve the existing security escalation behavior and avoid carrying information into explicitly unrelated problems.



\### 6. Measuring the Improvement



A separate 10-scenario evaluation was developed to compare troubleshooting-category selection with and without the previous-message context.



The results were:



| Measurement | Before | After |

|---|---:|---:|

| Passing scenarios | 4/10 | 10/10 |

| Pass rate | 40% | 100% |

| Improvement | | +60 percentage points |



Six scenarios that originally failed passed after the improvement, while four previously passing scenarios continued to pass.



Five manual conversation tests and five existing automated unit tests also passed.



The updated code was committed to GitHub, deployed to Render, and tested successfully through the public application.



These findings demonstrate improvement on the targeted conversation-memory scenarios. They do not establish that the overall application is 100% accurate or that all troubleshooting problems have been resolved.



The original 93.75% evaluation score and the new 10-scenario memory evaluation measure different aspects of product quality and should not be directly compared.



\### 7. Challenges and Lessons Learned



One of the greatest lessons from this project was that a technically functional application can still struggle during realistic user interactions.



The original troubleshooting engine performed well on several isolated scenarios but lacked the context needed to interpret natural follow-up questions.



Real-user testing exposed this weakness more clearly than the initial evaluation dataset.



The project also highlighted the importance of maintaining safety protections during product improvements. A feature that improves convenience should not weaken the assistant's ability to recognize security-sensitive requests.



Another lesson involved deployment and monitoring. A successful local test does not guarantee that an updated feature is running publicly. GitHub commits, Render deployments, and live application behavior must each be verified.



Finally, the project reinforced the value of separating measurable results from broader claims. The targeted evaluation showed a clear improvement in conversation handling, but additional testing is required to understand performance across a wider range of users and technical problems.



\### 8. Future Improvements



Several opportunities remain for further development.



The assistant currently considers only the immediately preceding user message rather than maintaining a complete structured conversation history.



Future versions could track the active troubleshooting issue, operating system, completed steps, and previous outcomes across multiple turns.



Operating-system-specific guidance would also improve accuracy for macOS and Linux users.



Additional troubleshooting categories could address hardware problems, battery performance, keyboard failures, and wireless signal strength.



The product would also benefit from broader volunteer testing, accessibility improvements, and more comprehensive production monitoring.



\### 9. Conclusion



The AI-Powered IT Help Desk Assistant progressed from a local Python prototype to a publicly deployed troubleshooting application.



The project demonstrated the complete product-development cycle: identifying a user problem, designing a solution, implementing safeguards, evaluating performance, launching a public product, gathering feedback, and delivering a measurable improvement.



The most significant result was improving targeted conversation-handling performance from 40% to 100% across 10 evaluation scenarios.



More importantly, the project demonstrated how real-user feedback can guide practical engineering decisions and produce measurable improvements.



The assistant remains an educational prototype with clearly defined limitations, but it provides a foundation for continued development into a more capable and context-aware IT support tool.

