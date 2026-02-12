from crewai_tools import ScrapeElementFromWebsiteTool

# Try targeting the image container or different selectors
# .imgTagWrapper is the common container for the main image
tool = ScrapeElementFromWebsiteTool(
    website_url="https://www.amazon.com/Nordic-Naturals-Ultimate-Support-Healthy/dp/B002CQU54Q",
    css_element=".imgTagWrapper" 
)

try:
    result = tool.run()
    print("--- Scrape Container Result ---")
    print(f"Content found: {result if result else 'EMPTY RESULT'}")
except Exception as e:
    print(f"Error: {e}")
