from google.adk.agents.llm_agent import Agent
from google.adk.models.lite_llm import LiteLlm
from google.genai import types

# root_agent = Agent(
#     model='gemini-3.5-flash',
#     name='root_agent',
#     description='A helpful assistant for user questions.',
#     instruction='Answer user questions to the best of your knowledge',
# )

# # ways to run agents
# # 1. adk run firstAgent
# # 2. through web interface: adk web
# # 3. through api service: adk api_service


# root_agent = Agent(
#     model = LiteLlm(model = ""),
#     name='root_agent',
#     description='A helpful assistant for user questions.',
#     instruction='Answer user questions to the best of your knowledge',
# )



root_agent = Agent(
    model='gemini-3.5-flash',
    name='root_agent',
    description='A helpful assistant for user questions.',
    instruction='Answer user questions to the best of your knowledge',
    generate_content_config= types.GenerateContentConfig(
        temperature=0.3,
        max_output_tokens=120
    )
)