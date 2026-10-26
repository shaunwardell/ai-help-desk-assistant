import unittest
from engine import troubleshoot

class TestTroubleshooter(unittest.TestCase):
    def test_wifi(self):
        self.assertIn('Wi-Fi', troubleshoot('my wifi is broken')['title'])
    def test_dns(self):
        self.assertIn('DNS', troubleshoot('nslookup fails')['title'])
    def test_security_escalation(self):
        self.assertIn('Human', troubleshoot('I think I was hacked')['title'])
    def test_unknown(self):
        self.assertIn('questions', troubleshoot('something strange happened')['title'])
    def test_blank(self):
        self.assertIn('Tell me', troubleshoot('  ')['title'])

if __name__ == '__main__':
    unittest.main()

def test_dns_symptom_classification():
    message = (
        "I can connect to the internet using an IP address, "
        "but websites won't load when I type their names."
    )

    result = troubleshoot(message)

    assert result["title"] == "DNS and website name resolution"
    assert any("nslookup" in step for step in result["steps"])
