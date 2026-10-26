"""Transparent, offline troubleshooting decision support. No LLM/API calls."""
from dataclasses import dataclass

@dataclass(frozen=True)
class Guide:
    title: str
    clues: tuple[str, ...]
    steps: tuple[str, ...]
    caution: str

GUIDES = (
    Guide('Wi-Fi and internet connection', ('wifi','wi-fi','internet','offline','wireless','network','connection'), (
        'Check whether Wi-Fi is enabled and airplane mode is off.',
        'See whether another device on the same network can connect.',
        'Open Command Prompt and run `ipconfig /all` to inspect the adapter, gateway, and DNS settings.',
        'Try `ping 1.1.1.1` to test basic reachability; blocked ICMP can make this test inconclusive.',
        'If other devices are also offline, contact your network provider or administrator.'),
        'Do not share passwords, public IP addresses, or complete network configuration screenshots.'),
    Guide('DNS and website name resolution', ('dns','nslookup','domain','resolve','website','site not found'), (
        'Check whether multiple websites are affected.',
        'Run `nslookup example.com` and note whether a DNS answer or error appears.',
        'Run `ping 1.1.1.1`; a response here but not from a domain name may suggest a DNS issue.',
        'Check the DNS server entries using `ipconfig /all`.',
        'If you are on a managed school or work network, ask IT before changing DNS settings.'),
        'Avoid changing managed network settings without permission.'),
    Guide('Slow Windows computer', ('slow','lag','freeze','performance','startup','memory','storage'), (
        'Restart the computer if it is safe to close your work.',
        'Open Task Manager and check CPU, memory, and disk usage.',
        'Check free space in Settings > System > Storage.',
        'Review startup applications; disable only apps you recognize and do not need at startup.',
        'Check Windows Update and run a trusted malware scan if performance remains poor.'),
        'Save open work before restarting; do not disable security software.'),
    Guide('Printer not working', ('printer','printing','print','spooler'), (
        'Confirm the printer is powered on and has paper.',
        'Check its USB or Wi-Fi connection.',
        'Open Windows Settings > Bluetooth & devices > Printers & scanners.',
        'Check for paused or stuck jobs in the print queue.',
        'Use the built-in Windows printer troubleshooter if available.'),
        'Do not install drivers from untrusted download sites.'),
)

ESCALATE = ('ransomware','hacked','compromised','password reset','admin password', 'administrator password', 'data breach','phishing','malware infection')

def troubleshoot(message: str, previous_issue: str = "") -> dict:
    message = message.strip()
    if not message:
        return {'title': 'Tell me what happened', 'steps': ['Describe the symptom, your operating system, and any error message.'], 'caution': '', 'source': 'Guided local rules'}
    lowered = message.lower()
        # Recognize when the user starts a different problem.
    new_issue_phrases = (
        "new problem",
        "new issue",
        "new question",
        "next issue",
        "next problem",
        "different problem",
    )

    starting_new_issue = any(
        phrase in lowered for phrase in new_issue_phrases
    )

    # Short follow-ups can reuse the previous troubleshooting issue.
    follow_up_phrases = (
        "still",
        "persists",
        "same issue",
        "same problem",
        "not working",
        "didn't work",
        "did not work",
    )

    is_short_follow_up = (
        len(message.split()) <= 8
        or any(phrase in lowered for phrase in follow_up_phrases)
    )

    if previous_issue and is_short_follow_up and not starting_new_issue:
        lowered = f"{previous_issue.lower()} {lowered}"
    if any(term in lowered for term in ESCALATE):
        return {'title': 'Human IT support recommended', 'steps': ['Disconnect from suspicious links or attachments.', 'Do not share passwords, authentication codes, or sensitive files.', 'Contact your organization’s IT or security team using a trusted channel.', 'Record the error message and approximate time without exposing private data.'], 'caution': 'This prototype cannot investigate or remediate security incidents.', 'source': 'Guided local rules'}
    # Prioritize specific DNS symptoms over generic internet keywords.
    dns_phrases = (
        "websites won't load when i type their names",
        "websites wont load when i type their names",
        "using an ip address",
        "by ip address but not by name",
        "domain names don't work",
        "domain names dont work",
        "dns error",
        "name resolution",
        "cannot resolve",
        "can't resolve",
        "cant resolve",
    )

    if any(phrase in lowered for phrase in dns_phrases):
        guide = next(g for g in GUIDES if g.title == 'DNS and website name resolution')
        return {
            'title': guide.title,
            'steps': list(guide.steps),
            'caution': guide.caution,
            'source': 'Built-in troubleshooting guide; verify with official documentation'
        }
    ranked = sorted(((sum(len(c) for c in g.clues if c in lowered), g) for g in GUIDES), key=lambda x: x[0], reverse=True)
    if ranked[0][0] == 0:
        return {'title': 'A few questions first', 'steps': ['Are you using Windows 10, Windows 11, or another system?', 'Is the issue with internet, DNS, computer speed, or a printer?', 'What exact error message do you see (without private details)?'], 'caution': 'No changes have been made to your computer.', 'source': 'Guided local rules'}
    guide = ranked[0][1]
    return {'title': guide.title, 'steps': list(guide.steps), 'caution': guide.caution, 'source': 'Built-in troubleshooting guide; verify with official documentation'}
