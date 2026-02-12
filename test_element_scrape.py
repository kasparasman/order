from crewai_tools import ScrapeElementFromWebsiteTool

# Target the main product image on Amazon
tool = ScrapeElementFromWebsiteTool(
    website_url="https://www.amazon.com/Nordic-Naturals-Ultimate-Support-Healthy/dp/B002CQU54Q",
    css_element="img#landingImage"  # More specific ID for the main product image
)

try:
    result = tool.run()
    print("--- Scrape Element Result ---")
    print(result)
except Exception as e:
    print(f"Error scraping element: {e}")
