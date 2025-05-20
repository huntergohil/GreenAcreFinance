Hello, User! 

I am Jack, founder of GAF

I am no expert in code, so i am using outside support and tailoring it to our specifications to support the creation of our POC prior to funding. 
This branch was created to provide insight/actionable servicing of our concept and to support our primary tech lead Hunter with the process. 
It may be entirely useless. 

Purpose ! 

The notebook is designed to:
- Ingest **real macro and market data** (NewsAPI + Yahoo Finance)
- Train a basic **Random Forest** regression model
- Generate **automated investment insights** (e.g., sentiment, geopolitical risk)
- Explore how macroeconomic factors (like U.S. interest rate hikes) affect offshore energy firms (e.g., Equinor, DNO)

Now, onto our tech lead, Hunter! 

My name is Hunter Gohil, and I am the tech lead/primary developer of Green Acre Finance! 

Our mission is to provide top tier AI algorithms to the common user, taking back power from big banks! 

Technical details: 
Entire application will eventually be held on AWS (Amazon Web Services)
Databases will be created/managed using dynamoDB
AI will be hosted on EC2 (Likely Spot instance for cost effeciency)
Will likely use Alpaca API to support trading for full launch 

Resources:
Alpaca API Articles:
https://docs.alpaca.markets/docs/getting-started
https://alpaca.markets/learn

Python use case: 
Currently, the AI is running with Llama3 by Ollama. This is a suboptimal model used for testing, therefore, news_headlines.json must be trimmed 
and sp500_tickers will be limited to just a few stocks. 
Instructions for use: 
1. run webscrape.py. This gets the latest news stories for the AI. 
2. Trim news_headlines.json. Llama3 is incapable of running such a large file. Eventually, this will be upgraded to cut out this trimming. 
3. run llama3_stock_insights.py. This runs the AI analysis 

Common issues:
Bug with AI: Ollama often gives its responses with headers such as "Here is your list"
Remediation: Extract JSON blocks function should clean this up, but will require further testing 