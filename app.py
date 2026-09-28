from langchain.chat_models import init_chat_model
from langchain.agents import create_agent
from langchain_tavily import TavilySearch
import requests
import json
from langchain.tools import tool
# Step 1: Initialize the Model
from dotenv import load_dotenv
import os
load_dotenv()
api_key=os.getenv("GEMINI_API_KEY")
model = init_chat_model(
    "gemini-3.8-flash",
    model_provider="google_genai"
)


tavily_api_key=os.getenv("TAVILY_API_KEY")
# Step 2: Create Skill Demand Search Tool (Tavily)
skill_demand_tool =TavilySearch(
    max_results=5,
    search_depth="advanced",
    tavily_api_key=tavily_api_key
)
result = skill_demand_tool.invoke({"query": "generative ai skills demand 2025"})
print(result)


# Step 3: Create Custom Job Search Tool
@tool
def search_jobs(skill: str, location: str) -> list:
    """Search for jobs requiring a specific skill and location."""

    rapidapi_key = os.getenv("RAPIDAPI_KEY")

    url = "https://jsearch.p.rapidapi.com/search-v2"

    headers = {
        "accept": "application/json",
        "x-rapidapi-host": "jsearch.p.rapidapi.com",
        "x-rapidapi-key": rapidapi_key,
        "x-rapidapi-ua": "RapidAPI-Playground"
    }

    querystring = {
        "query": f'"{skill}" OR "AI Engineer" OR "Generative AI Engineer" OR "LLM Engineer" OR "Machine Learning Engineer" in {location}',
    "page": "1",
    "country": "in",
    "employment_types": "INTERN,FULLTIME",
    "job_requirements": "no_experience,under_3_years_experience"
    }

    response = requests.get(
        url,
        headers=headers,
        params=querystring
    )

    data = response.json()

    jobs =  data.get("data", {}).get("jobs", [])

    result = []
    print("Found", len(jobs), "jobs")
    for job in jobs:
        result.append({
            "title": job.get("job_title"),
            "company": job.get("employer_name"),
            "location": job.get("job_city"),
            "apply_link": job.get("job_apply_link")
        })
    return result

# Step 4: Define System Prompt

system_prompt = """You are a Skill-to-Career Mapping assistant that helps students understand skill demand and find matching job opportunities.

You have access to these tools:
- skill_demand_tool: Search for industry demand, salary insights, and career trends
- search_jobs: Find actual job listings requiring specific skills

Help the student by researching the skill they ask about and finding relevant opportunities.

Present results in a clean, readable format with clear sections and proper spacing. Include all job details with apply links. Don't use markdown format."""




agent=create_agent(
    model = model, 
    tools = [search_jobs],
    system_prompt = system_prompt
)
user_query = "What's the demand for generative ai in the industry and show me related job openings in India"

response = agent.invoke({
    "messages": [{"role": "user", "content": user_query}]
})
print(response.content)



# Step 5: Create and Run the Agent

