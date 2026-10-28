\# Phase 3: First 10 Production Interactions



Project: AI-Powered IT Help Desk Assistant

Date: October 26, 2026

Source: Volunteer tester Gilgamesh

Environment: Public Render deployment



Note: These interactions came from one volunteer testing session.

They are not ten independent users.



\## First 10 Production Interactions



\*\*Source:\*\* Gilgamesh's volunteer testing session  

\*\*Environment:\*\* Public Render deployment  

\*\*Method:\*\* Review of actual submitted questions and recorded application responses.



| # | User input | Bot response | Outcome |

|---|---|---|---|

| 1 | Mac with a black screen | Generic clarification questions | Failed to recognize an unsupported hardware/display issue. |

| 2 | Mac powered on with sound but no display; macOS High Sierra | Repeated generic clarification questions | Failed to incorporate additional information. |

| 3 | Windows 11 connected to Wi-Fi but unable to browse | Wi-Fi troubleshooting instructions | Relevant initial troubleshooting guidance. |

| 4 | google.com fails but 8.8.8.8 works | Generic clarification questions | Missed a potential DNS-related symptom. |

| 5 | Windows 10 | Repeated generic clarification questions | Did not retain context from the previous question. |

| 6 | MSI Windows 11 laptop with short battery life and slow performance | Slow Windows computer instructions | Addressed slow performance but not battery life. |

| 7 | Windows 7 laptop with intermittent Wi-Fi; router across the house | General Wi-Fi troubleshooting | Missed router distance and possible signal-strength issues. |

| 8 | Intermittent issue persists | Generic clarification questions | Did not continue the previous troubleshooting sequence. |

| 9 | Windows 11 keyboard not responding | Generic clarification questions | Keyboard troubleshooting outside supported categories. |

| 10 | Windows 11 Wi-Fi icon greyed out | General Wi-Fi troubleshooting | Correct general category, but did not address the disabled/greyed-out adapter specifically. |



\## What We Learned



1\. The application provides useful starting guidance for supported troubleshooting categories.

2\. It does not reliably retain context between consecutive messages.

3\. It struggles with requests outside its predefined troubleshooting categories.

4\. It can overlook environmental details, including distance from a wireless router.

5\. Multi-symptom questions may receive incomplete answers.



\## Important Limitations



\- These 10 interactions came from one volunteer, not 10 separate users.

\- The outcomes were assessed from the shared transcript.

\- No individual response-time measurements were available for this session.

\- The tester described response times as very quick.

\- The tester rated ease of use 4/5, accuracy 4/5, and clarity 5/5.



\## Conclusion



The first 10 observed production interactions demonstrate that the rule-based assistant provides useful introductory troubleshooting for supported problems but needs stronger conversational context handling and more specific issue recognition.



These observations will inform Phase 4 improvements.

