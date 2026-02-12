from crewai_tools import ScrapegraphScrapeTool

# Note: This often requires a SCRAPEGRAPH_API_KEY in the environment
tool = ScrapegraphScrapeTool(
    website_url="https://www.amazon.com/Nordic-Naturals-Ultimate-Support-Healthy/dp/B002CQU54Q",
    user_prompt="Extract all product image URLs, product title, and description"
)

try:
    result = tool.run()
    print("--- Scrapegraph Result ---")
    print(result)
except Exception as e:
    print(f"Error using Scrapegraph: {e}")
    print("\nTip: This tool usually requires a SCRAPEGRAPH_API_KEY environment variable if using the cloud version.")
