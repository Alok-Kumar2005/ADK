from google.adk.agents.llm_agent import Agent
from pydantic import BaseModel

class Enquiry(BaseModel):
    name: str
    email: str
    interested_in: str
    budget: int


root_agent = Agent(
    model='gemini-3.5-flash',
    name='root_agent',
    description='A helpful assistant for user questions.',
    instruction='Answer user questions to the best of your knowledge',
    output_schema= Enquiry,
)
