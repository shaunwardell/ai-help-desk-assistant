**# Phase 3: Top Three Production Failure Modes**



\*\*Project:\*\* AI-Powered IT Help Desk Assistant

\*\*Date:\*\* October 26, 2026

\*\*Evidence:\*\* Structured feedback and chat transcript from volunteer tester Gilgamesh.



\## Failure Mode 1: Missing Conversation Memory



\*\*Observed behavior:\*\* The assistant did not retain enough context between user messages.



\*\*Example:\*\* After a user reported that google.com failed while 8.8.8.8 worked, the assistant requested clarification. When the user replied "windows 10," the assistant repeated the same clarification questions.



\*\*Impact:\*\* Frustrating troubleshooting experience and inability to progress naturally through follow-up questions.



\*\*Proposed improvement:\*\* Add session-based memory for the current troubleshooting issue, operating system, and previous responses.



\## Failure Mode 2: Operating-System Mismatch



\*\*Observed behavior:\*\* The assistant returned Windows-specific instructions for macOS and Linux troubleshooting requests.



\*\*Examples:\*\*

\- macOS High Sierra Wi-Fi issue received Command Prompt and ipconfig instructions.

\- Linux Mint website issue received Windows-specific ipconfig instructions.



\*\*Impact:\*\* Instructions may be unusable or confusing on unsupported operating systems.



\*\*Proposed improvement:\*\* Detect operating systems and provide compatible troubleshooting instructions or clearly identify unsupported platforms.



\## Failure Mode 3: Insufficient Environmental Context



\*\*Observed behavior:\*\* The assistant overlooked relevant details when selecting troubleshooting guidance.



\*\*Example:\*\* A user described intermittent Wi-Fi connectivity on a laptop located across the house from the router. The assistant provided general connectivity steps without addressing possible signal-strength or distance issues.



\*\*Impact:\*\* Recommendations may miss important contributing factors.



\*\*Proposed improvement:\*\* Recognize contextual details such as distance from the router, intermittent failures, and previous unsuccessful troubleshooting steps.



\## Additional Observation



The tester expressed concern about recommending Command Prompt instructions to inexperienced end users. Beginner-friendly checks should appear before advanced diagnostics, and operating-system compatibility should be made clear.



\## Conclusion



The first volunteer's feedback identified three actionable weaknesses: missing conversation memory, operating-system mismatches, and insufficient environmental context.



These findings provide a basis for selecting and evaluating a meaningful Phase 4 improvement.



\---



\## Additional Production Feedback: Tester 2



\*\*Tester:\*\* Cheyenne (BraveLittlePoptart)

\*\*Date:\*\* October 26, 2026

\*\*Source:\*\* DeVry WiCyS Discord community

\*\*Testing Status:\*\* Completed



\### Scenario 1: Monitor Displaying a Black Screen



Cheyenne asked the assistant why her monitor was displaying a black screen.



The assistant requested additional information, including the operating system, type of problem, and whether an error message appeared.



She provided the requested information, identifying Windows 10, describing the problem as hardware-related, and explaining that no error message appeared.



However, the assistant continued asking the same clarification questions instead of progressing with troubleshooting.



\*\*Result:\*\* Unsuccessful interaction.



\*\*Related failure mode:\*\* Failure Mode 1: Missing Conversation Memory.



\*\*Additional limitation:\*\* The application lacks dedicated troubleshooting guidance for certain display and hardware problems.



\### Scenario 2: Slow Computer



Cheyenne tested the assistant with a slow-computer troubleshooting question.



The application recommended checking system usage, restarting the computer, and running a malware scan.



She reported that these recommendations were helpful.



\*\*Result:\*\* Positive user feedback.



\### Overall Feedback



Cheyenne described the application positively, stating, "Overall it is great!!"



Her testing demonstrated that the application can provide useful guidance for supported troubleshooting scenarios while still struggling with unsupported hardware problems and repeated clarification questions.



\### Relationship to Phase 4 Improvements



The previously implemented conversational follow-up improvement achieved 10/10 successful results across the targeted evaluation scenarios.



Cheyenne's black-screen test demonstrates that the improvement does not yet provide complete conversational memory or resolve every unsupported troubleshooting scenario.



This finding supports future development priorities:



\- Expand hardware and monitor troubleshooting coverage.

\- Improve retention of information provided across multiple messages.

\- Prevent repetitive clarification loops.



\### Updated Testing Progress



\*\*Tester 1:\*\* Gilgamesh (Justin) — Completed

\*\*Tester 2:\*\* Cheyenne — Completed

\*\*Total:\*\* 2 of 5 unique volunteer testers



\*\*Remaining:\*\* 3 additional testers.



\*\*Documentation Note:\*\* No application changes were made in response to this feedback. The findings are recorded as remaining limitations and potential future improvements.



\---



\## Additional Production Feedback: Tester 3



\*\*Tester:\*\* Volunteer Tester 3 (Family Member)

\*\*Date:\*\* October 26, 2026

\*\*Testing Status:\*\* Completed

\*\*Testing Environment:\*\* Public AI Help Desk Assistant



\### Scenario 1: Wi-Fi Troubleshooting



\*\*Question:\*\* "My wifi isn't working what are steps"



\*\*Tester Feedback:\*\*

\- Ease of use: Easy

\- Response time: Fast

\- Reported failures: None

\- Suggested improvements: None



\*\*Result:\*\* Positive usability feedback.



\### Scenario 2: Opening a Web Browser



\*\*Question:\*\* "Can you tell me how to bring up a browser"



\*\*Tester Feedback:\*\*

\- Ease of use: Easy

\- Response time: Fast

\- Reported failures: None

\- Suggested improvements: None



\*\*Result:\*\* Positive usability feedback.



\### Overall Findings



The tester reported that the application was easy to use, responded quickly, and did not exhibit any noticeable failures during either interaction.



No changes were recommended.



This feedback supports the application's usability from the perspective of a nontechnical user. However, successful resolution of either issue was not independently verified.



\*\*Tester Relationship:\*\* Family member of the project developer.



\### Updated Testing Progress



\*\*Completed:\*\* 3 of 5 unique testers.



\*\*Remaining:\*\* 2 additional testers.



\*\*Documentation Note:\*\* No application changes were required based on this feedback.



\## Additional Production Feedback: Tester 4



\*\*Tester:\*\* Arianna P. (Moose / Meeska Mooska)

\*\*Date:\*\* October 26, 2026

\*\*Testing Status:\*\* Completed

\*\*Testing Environment:\*\* Public AI Help Desk Assistant



\### Troubleshooting Scenarios



The tester asked the assistant about a slow internet connection and a slow laptop.



\### User Feedback



\- \*\*Ease of use:\*\* 3/5

\- \*\*Accuracy:\*\* Responses described as accurate; no numerical score provided.

\- \*\*Clarity:\*\* Instructions were clear, simple, and easy to follow.

\- \*\*Response time:\*\* Reportedly less than one second.

\- \*\*Observed problems:\*\* The assistant sometimes repeated its previous response when the tester asked follow-up questions or changed the prompt.



The tester reported needing to clear the chat and rewrite the question with additional information to continue troubleshooting.



\### Recommended Improvements



1\. Improve conversation handling so new information and follow-up questions produce appropriate responses without requiring users to clear the chat.

2\. Present troubleshooting instructions progressively, beginning with one or two steps instead of displaying five to seven steps simultaneously.

3\. Ask whether the initial troubleshooting steps worked before recommending additional actions.



\### Relationship to Phase 4 Improvements



The previously implemented conversation-context improvement achieved 10/10 passing results on its targeted evaluation.



However, this volunteer's experience demonstrates that the application still struggles with some realistic multi-turn conversations.



The targeted evaluation results remain valid for the scenarios tested, but they do not establish complete conversational reliability.



\### Updated Testing Progress



\*\*Completed:\*\* 4 of 5 unique testers.



\*\*Remaining:\*\* 1 additional tester.



\*\*Documentation Note:\*\* These findings are recorded as remaining limitations and recommendations for future development. No additional application changes have been made based on this feedback.



\## Additional Production Feedback: Tester 5



\*\*Tester:\*\* Courtney Childers

\*\*Date:\*\* October 27, 2026

\*\*Testing Status:\*\* Completed

\*\*Testing Environment:\*\* Public AI Help Desk Assistant



\### Troubleshooting Scenarios



Courtney tested several realistic troubleshooting questions based on problems she had previously experienced:



1\. A printer printing slowly and losing its connection.

2\. A phone failing to connect to Wi-Fi while a computer remained connected.

3\. Follow-up questions indicating that the original troubleshooting steps had not resolved the problem.



\### User Feedback



\- \*\*Ease of use:\*\* 5/5

\- \*\*Accuracy and helpfulness:\*\* 3/5

\- \*\*Clarity:\*\* 5/5

\- \*\*Response time:\*\* Fast

\- \*\*Safety:\*\* Appreciated warnings about protecting personal information and downloading software from trusted sources.



\### Observed Problems



\*\*1. Repeated troubleshooting instructions\*\*



When Courtney explained that the initial printer troubleshooting steps had not worked, the assistant repeated the same information rather than suggesting a different approach.



\*\*2. Device-specific guidance mismatch\*\*



When she asked why her phone could not connect to Wi-Fi while her computer could, the assistant recommended general Wi-Fi troubleshooting steps that included Windows Command Prompt instructions.



These instructions were not appropriate for troubleshooting the phone itself.



\*\*3. Limited troubleshooting progression\*\*



Courtney reported that the assistant worked well as a basic troubleshooting guide but struggled when a problem required additional investigation or a continuing conversation.



\### Recommended Improvements



1\. Improve follow-up handling so the assistant recognizes when previously recommended steps have failed.

2\. Provide alternative troubleshooting actions based on the user's responses.

3\. Identify the device or operating system before recommending platform-specific commands.

4\. Use a more interactive troubleshooting process that asks relevant questions and progressively narrows the problem.



\### Relationship to Phase 4 Improvements



The Phase 4 conversation-context improvement achieved 10/10 passing results on its targeted evaluation.



However, Courtney's testing demonstrates that the application still has limitations when users report unsuccessful troubleshooting steps or ask about devices outside its original Windows-focused scope.



The targeted evaluation results remain valid for the scenarios tested but do not demonstrate complete conversational reliability.



\### Final User Testing Summary



\*\*Tester 1:\*\* Justin (Gilgamesh), completed.

\*\*Tester 2:\*\* Cheyenne (BraveLittlePoptart), completed.

\*\*Tester 3:\*\* Family member, completed.

\*\*Tester 4:\*\* Arianna (Moose), completed.

\*\*Tester 5:\*\* Courtney Childers, completed.



\*\*Total:\*\* 5 of 5 unique testers completed.



\### Final Findings



Across the five volunteer evaluations, users generally found the assistant accessible, understandable, and responsive.



Recurring limitations included:



\- Repetitive responses during multi-turn troubleshooting.

\- Incomplete recognition of previously attempted steps.

\- Device and operating-system mismatches.

\- Limited troubleshooting coverage for unsupported hardware.

\- Too many troubleshooting steps presented simultaneously.



These findings support future improvements involving structured conversation memory, device detection, progressive troubleshooting, and expanded technical coverage.



\*\*Documentation Note:\*\* All five user evaluations have been completed. Courtney's findings are documented as remaining limitations and future development recommendations. No additional application changes were made in response to this evaluation.

