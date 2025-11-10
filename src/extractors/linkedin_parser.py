thonimport asyncio
from src.extractors.utils_time import async_sleep
import random

class LinkedInParser:
    def __init__(self):
        pass

    async def fetch_profile(self, username: str) -> dict:
        # Simulate network call
        await async_sleep(random.uniform(0.5, 1.5))

        # Example dummy profile data
        profile = {
            "basic_info": {
                "location": {
                    "country": "United States",
                    "city": "San Francisco",
                    "full": "San Francisco Bay Area"
                }
            },
            "experience": [
                {"title": "Software Engineer", "company": "TechCorp", "duration": "2020 - Present"}
            ],
            "education": [
                {"school": "Stanford University", "degree": "Computer Science"}
            ],
            "languages": ["English"],
            "certifications": ["AWS Certified Developer"],
            "company": {"name": "TechCorp", "industry": "Software"}
        }
        return profile