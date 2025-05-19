import json
import subprocess
import re

def load_json(file_path):
    with open(file_path, "r") as f:
        return json.load(f)

def format_prompt(headlines, tickers):
    headline_text = "\n".join([f"- {h['title']} ({h['url']})" for h in headlines])
    ticker_text = ", ".join(tickers)

    return f"""
You are a financial analyst AI.

Your job is to analyze the headlines and stock tickers below and return a single valid JSON object.

This JSON MUST contain exactly the following 3 keys:

1. "topStories": an array of exactly 4 news stories, with:
   - title
   - link
   - reason (why it's important)

2. "topStocks": an array of exactly 3 stocks to buy now, with:
   - ticker
   - forecast (e.g., "+4.3%")
   - sentiment (e.g., "bullish", "neutral")
   - recommendation (e.g., "Strong Buy", "Buy", "Hold", "Sell")

3. "allStocks": an array of forecasts for all the tickers, with:
   - ticker
   - forecast
   - sentiment
   - recommendation

⚠️ IMPORTANT:
- Do not leave out any of the 3 keys
- Each array MUST have the exact number of entries requested
- Only return valid JSON — no commentary, no markdown

Headlines:
{headline_text}

Tickers:
{ticker_text}
"""



def call_ollama(prompt):
    result = subprocess.run(
        ["ollama", "run", "llama3"],
        input=prompt.encode("utf-8"),
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    output = result.stdout.decode("utf-8")
    return output

import json
import re

def extract_json_blocks(text):
    try:
        # Remove any markdown or intro text
        if "```" in text:
            text = text.split("```")[1].strip()
        if "Here is the JSON" in text:
            text = text.split("Here is the JSON")[-1].strip()
        if not text.startswith("{"):
            match = re.search(r"\{.*\}", text, re.DOTALL)
            if match:
                text = match.group(0)

        data = json.loads(text)
        return {
            "topStories.json": data.get("topStories", []),
            "topStocks.json": data.get("topStocks", []),
            "allStocks.json": data.get("allStocks", [])
        }

    except json.JSONDecodeError as e:
        print("JSON parsing failed.\n")
        print("RAW response:\n", text)
        return {}



def main():
    headlines = load_json("news_headlines.json")
    tickers = load_json("sp500_tickers.json")

    prompt = format_prompt(headlines, tickers)
    raw_response = call_ollama(prompt)
    blocks = extract_json_blocks(raw_response)

    for filename, data in blocks.items():
        with open(filename, "w") as f:
            json.dump(data, f, indent=2)
        print(f"Wrote: {filename}")

if __name__ == "__main__":
    main()
