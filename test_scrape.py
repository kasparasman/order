from crewai_tools import ScrapeWebsiteTool

# Point it at a specific Amazon product
tool = ScrapeWebsiteTool(website_url="https://www.amazon.com/Nordic-Naturals-Ultimate-Support-Healthy/dp/B002CQU54Q")

import re

# Run it
try:
    result = tool.run()
    # Find all image URLs (common patterns for Amazon images)
    image_urls = re.findall(r'https?://[^\s<>"]+?\.(?:jpg|jpeg|png|gif)', result)
    
    print(f"Scrape successful. Total length: {len(result)}")
    print("\n--- First 1000 characters of output ---")
    print(result[:1000])
    
    # Find all image URLs (common patterns for Amazon images)
    image_urls = re.findall(r'https?://[^\s<>"]+?\.(?:jpg|jpeg|png|gif)', result)
    # ... rest of the script

except Exception as e:
    print(f"Error scraping: {e}")
