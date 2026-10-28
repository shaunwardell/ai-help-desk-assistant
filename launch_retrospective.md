\# Phase 3: Launch Retrospective



\*\*Project:\*\* AI-Powered IT Help Desk Assistant  

\*\*Date:\*\* October 26, 2026  

\*\*Deployment:\*\* \[Live Application](https://ai-help-desk-assistant.onrender.com)  

\*\*Source Code:\*\* \[GitHub Repository](https://github.com/shaunwardell/ai-help-desk-assistant)



\## 1. What Went Well



The AI-Powered IT Help Desk Assistant was successfully deployed to Render using the project's GitHub repository.



The public application runs in rule-based mode, allowing users to receive troubleshooting guidance without requiring a locally hosted Ollama model or external AI API keys.



Initial production monitoring showed an average response time of 0.952 seconds across five manually timed tests while the application was active.



The assistant correctly handled several common troubleshooting scenarios, including DNS issues, slow Windows computers, printer problems, and a security-sensitive request that was escalated to human IT support.



The first volunteer tester rated the application 4/5 for ease of use, 4/5 for accuracy, and 5/5 for clarity. The tester also reported very quick response times and found the troubleshooting steps useful as initial guidance.



\## 2. What Surprised Me



The most significant surprise was how quickly the application reached its limitations during a realistic troubleshooting conversation.



Although the assistant performed well on several individual questions, it struggled to maintain context when the tester provided follow-up information.



For example, when the tester explained that a website was not loading but an IP address was accessible, the assistant requested clarification rather than recognizing a possible DNS issue. When the tester supplied the operating system, the assistant repeated its original questions.



Another unexpected issue was the lack of operating-system-specific guidance. Some macOS and Linux troubleshooting requests received Windows commands.



The application also overlooked environmental details, such as a laptop experiencing intermittent connectivity while located across the house from its wireless router.



Finally, Render's free hosting plan can spin down during inactivity, meaning response times may be substantially longer than the measurements collected while the application was running.



\## 3. What I Would Do Differently



If I were starting this project again, I would introduce multi-turn conversation testing earlier in development.



I would also define the supported operating systems more clearly and create platform-specific troubleshooting instructions.



Another improvement would be to test realistic scenarios containing multiple symptoms and environmental factors instead of relying primarily on isolated troubleshooting questions.



I would make basic troubleshooting steps more accessible to inexperienced users by presenting simple checks before optional command-line diagnostics.



I would also recruit

