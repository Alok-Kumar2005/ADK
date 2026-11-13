from datetime import datetime
from zoneinfo import ZoneInfo, ZoneInfoNotFoundError
from google.adk.agents.llm_agent import Agent
from google.adk.tools.google_search_tool import google_search
from google.adk.models.lite_llm import LiteLlm
from google.adk.code_executors import BuiltInCodeExecutor
from langchain_tavily import TavilySearch
from google.adk.tools.langchain_tool import LangchainTool
from google.genai import types

root_agent = Agent(
    model='gemini-3.5-flash',
    name='root_agent',
    description='A helpful assistant for user questions.',
    instruction=(
        'Answer user questions to the best of your knowledge'
        'Use google search when you need current information'
        'or need to verify facts'
        'Use tool ony 1 or 2 times in one call'
        ),
    tools=[google_search]  ## groq model not supported on tool calls
)

## build int code executor tools ( it ru ndifferent from other)
root_agent = Agent(
    model='gemini-3.5-flash',
    name='root_agent',
    description='A helpful assistant that can write and run python code',
    instruction=(
        'Answer user questions to the best of your knowledge'
        'when a question involves calculations, data analysis or anything that benefits from running code, write python and execute it'
        'then explain the result'
        ),
    code_executor=BuiltInCodeExecutor()
)


## third party tools
tavilty_search = TavilySearch(
    max_results = 5,
    topic = "general"
)
tavily_tool = LangchainTool(tool = tavilty_search)

root_agent = Agent(
    model='gemini-3.5-flash',
    name='root_agent',
    description='A helpful assistant that can search on internet',
    instruction=(
        'Answer user questions to the best of your knowledge'
        'use tavily tool when required to use web search'
        ),
    tools = [tavily_tool]
)


## Regular functions tools
def get_current_time(timezone: str)->dict:
    """Get the current data and time in a give time zone
    use this whenever the user asks what time or date it is somewhere
    
    Args:
        timezone: an IANA time zone name e.g. "Asis/Kolkata", "America/New_York", or "Europe/London" 
        
    Returns:
        A dict with status ("success" or "error"). on success it also has
        "timezone", "date", "time" and "weekday"
        and on error, it has "error_message 
    """
    try:
        now = datetime.now(ZoneInfo(timezone))
    except ZoneInfoNotFoundError:
        return {
            "status": "error",
            "error_message": f"Unknown time zone error {timezone}"
        }
    return {
        "status": "success",
        "timezone": timezone,
        "date": now.strftime("%Y-%m-%d"),
        "time": now.strftime("%H:%M"),
        "weekday": now.strftime("%A")
    }


root_agent = Agent(
    model='gemini-3.5-flash',
    name='root_agent',
    description='A helpful assistant that ..',
    instruction=(
        'Answer user questions to the best of your knowledge'
        'use ...'
        ),
    tools = [get_current_time]
)



## Multiple agent 
root_agent = Agent(
    model='gemini-3.5-flash',
    name='root_agent',
    description='A helpful assistant that ..',
    instruction=(
        'Answer user questions to the best of your knowledge'
        'use ...'
        ),
    tools = [get_current_time, tavily_tool, google_search],
    code_executor= BuiltInCodeExecutor(),

    generate_content_config= types.GenerateContentConfig(
        tools_config = types.ToolConfig(include_server_side_tool_invocations= True)  ## because google_search response came to gemini and other tool respond to adk, so to make all response to adk we add these
    )
)
