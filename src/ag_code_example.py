import asyncio
from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.teams import RoundRobinGroupChat
from autogen_ext.models.openai import OpenAIChatCompletionClient
from autogen_ext.agents.web_surfer import MultimodalWebSurfer
from autogen_agentchat.conditions import TextMentionTermination
from autogen_core.models import ModelInfo
from autogen_agentchat.ui import Console
from autogen_core.models import ModelFamily
import os

agent = AssistantAgent(
    name="AssistantAgent",
    model_client=OpenAIChatCompletionClient(
        model="deepseek/deepseek-r1:free",
        api_key=os.environ['OPENROUTER_API_KEY'],
        base_url="https://openrouter.ai/api/v1",
        model_info=ModelInfo(vision=False, function_calling=True, json_output=True, family=ModelFamily.R1),
    ),
)

surfer = MultimodalWebSurfer(
    "WebSurfer",
    model_client=OpenAIChatCompletionClient(
        model="google/gemini-2.0-flash-exp:free",
        api_key=os.environ['OPENROUTER_API_KEY'],
        base_url="https://openrouter.ai/api/v1",
        model_info=ModelInfo(vision=False, function_calling=True, json_output=True, family=ModelFamily.UNKNOWN),
    ),
)

agent_team = RoundRobinGroupChat([agent, surfer], termination_condition=TextMentionTermination("TERMINATE"))

config = agent_team.dump_component()

with open("/workspaces/multiagent-demo/src/ag_code_example_config.json", "w") as file:
    file.write(config.model_dump_json())

async def main(task = "Search the web and summarize the current state of GLP-1 drug development"):
    await Console(agent_team.run_stream(task=task))

asyncio.run(main())    