from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.teams import RoundRobinGroupChat
from autogen_ext.models.openai import OpenAIChatCompletionClient
from autogen_ext.agents.web_surfer import MultimodalWebSurfer
from autogen_agentchat.conditions import TextMentionTermination
from autogen_core.models import ModelInfo
import os

agent = AssistantAgent(
    name="weather_agent",
    model_client=OpenAIChatCompletionClient(
        model="deepseek/deepseek-r1:free",
        api_key=os.environ['API_KEY'],
        base_url="https://openrouter.ai/api/v1",
        model_info=ModelInfo(vision=False, function_calling=True, json_output=True, family="unknown"),
    ),
)

surfer = MultimodalWebSurfer(
    "WebSurfer",
    model_client=OpenAIChatCompletionClient(
        model="deepseek/deepseek-r1:free",
        api_key=os.environ['API_KEY'],
        base_url="https://openrouter.ai/api/v1",
        model_info=ModelInfo(vision=False, function_calling=True, json_output=True, family="unknown"),
    ),
)

agent_team = RoundRobinGroupChat([agent], termination_condition=TextMentionTermination("TERMINATE"))
config = agent_team.dump_component()

with open("/workspaces/multiagent-demo/src/ag_code_example_config.json", "w") as file:
    file.write(config.model_dump_json())