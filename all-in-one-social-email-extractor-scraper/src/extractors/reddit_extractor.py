thonimport requests
from typing import List

class RedditExtractor:
    def __init__(self, profiles: List[str]):
        self.profiles = profiles

    def extract_emails(self):
        extracted_emails = []
        for profile in self.profiles:
            # Simulating email extraction from Reddit
            extracted_emails.append({
                "social_media_url": profile,
                "email_address": f"email{profile.split('/')[-1]}@reddit.com",
                "platform_name": "Reddit",
                "location": "Boston, MA",
                "domain_type": "Business"
            })
        return extracted_emails