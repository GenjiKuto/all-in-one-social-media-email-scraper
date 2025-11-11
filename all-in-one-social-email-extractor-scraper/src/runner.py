thonimport json
from extractors.linkedin_extractor import LinkedInExtractor
from extractors.facebook_extractor import FacebookExtractor
from extractors.youtube_extractor import YouTubeExtractor
from extractors.twitter_extractor import TwitterExtractor
from extractors.instagram_extractor import InstagramExtractor
from extractors.reddit_extractor import RedditExtractor
from extractors.pinterest_extractor import PinterestExtractor
from extractors.tiktok_extractor import TikTokExtractor
from outputs.exporters import export_data

def main():
    # Example input, in practice this would come from user input or a file
    profiles = [
        "https://www.linkedin.com/in/john-doe/",
        "https://www.facebook.com/mark.zuckerberg"
    ]
    
    # Extract data
    linkedin_extractor = LinkedInExtractor(profiles)
    facebook_extractor = FacebookExtractor(profiles)

    linkedin_data = linkedin_extractor.extract_emails()
    facebook_data = facebook_extractor.extract_emails()

    # Combine results
    all_data = linkedin_data + facebook_data

    # Export results to file
    export_data(all_data)

if __name__ == "__main__":
    main()