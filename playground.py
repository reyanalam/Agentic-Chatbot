from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
from phi.playground import Playground
import phi
import uvicorn

import os
from dotenv import load_dotenv
load_dotenv()


openai_api_key = os.getenv("GROQ_API_KEY")
phi.api = os.getenv("API_KEY")

# Define Agents
websearch_agent = Agent(
    name="Web Search Agent",
    role="Search the web for information",
    model=Groq(id="llama3-70b-8192"),
    tools=[DuckDuckGo()],
    instructions=["Always include the source of the information"],
    show_tool_calls=True,
    markdown=True,
)

finance_agent = Agent(
    name="Finance Agent",
    model=Groq(id="llama3-70b-8192"),
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, company_info=True, company_news=True)],
    instructions=["Use tables to display data"],
    show_tool_calls=True,
    markdown=True,
)


app = Playground(
    agents=[finance_agent, websearch_agent] 
).get_app()



if __name__ == "__main__":
    uvicorn.run("playground:app", host="127.0.0.1", port=8000, reload=True)

