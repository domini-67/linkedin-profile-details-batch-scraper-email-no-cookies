thonimport asyncio
import json
from pathlib import Path
from src.extractors.linkedin_parser import LinkedInParser
from src.outputs.exporters import JSONExporter
from src.config.settings import Settings

async def main():
    settings = Settings()
    input_file = Path(settings.input_file)
    output_file = Path(settings.output_file)

    # Load usernames
    if not input_file.exists():
        print(f"Input file not found: {input_file}")
        return

    with input_file.open("r") as f:
        usernames = [line.strip() for line in f if line.strip()]

    if not usernames:
        print("No usernames provided in the input file.")
        return

    parser = LinkedInParser()
    results = []

    for username in usernames:
        try:
            profile_data = await parser.fetch_profile(username)
            results.append({username: profile_data})
            print(f"Processed: {username}")
        except Exception as e:
            print(f"Failed to process {username}: {e}")

    exporter = JSONExporter(output_file)
    exporter.save(results)
    print(f"Results saved to {output_file}")

if __name__ == "__main__":
    asyncio.run(main())