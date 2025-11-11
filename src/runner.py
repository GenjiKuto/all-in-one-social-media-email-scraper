thonimport json
import time
from extractors.social_media_parser import SocialMediaParser
from outputs.exporters import Exporter
from config.settings import load_settings

def main():
    # Load settings from config file
    settings = load_settings('config/settings.example.json')

    # Initialize social media parser and email exporter
    parser = SocialMediaParser(settings)
    exporter = Exporter()

    # Run the scraper
    while True:
        try:
            data = parser.scrape()
            if data:
                exporter.export_to_file(data, 'output.json')
            time.sleep(settings['scrape_interval'])
        except Exception as e:
            print(f"Error: {e}")
            time.sleep(settings['retry_delay'])

if __name__ == '__main__':
    main()