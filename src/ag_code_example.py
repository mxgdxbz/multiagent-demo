import asyncio
from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.teams import RoundRobinGroupChat
from autogen_ext.models.openai import OpenAIChatCompletionClient
from autogen_ext.agents.web_surfer import MultimodalWebSurfer
from autogen_agentchat.conditions import TextMentionTermination
from autogen_core.models import ModelInfo
from autogen_agentchat.ui import Console
from autogen_core.models import ModelFamily

agent = AssistantAgent(
    name="Assistant Agent",
    model_client=OpenAIChatCompletionClient(
        model="deepseek/deepseek-r1:free",
        api_key="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",
        base_url="https://openrouter.ai/api/v1",
        model_info=ModelInfo(vision=False, function_calling=True, json_output=True, family=ModelFamily.R1),
    ),
)

surfer = MultimodalWebSurfer(
    "WebSurfer",
    model_client=OpenAIChatCompletionClient(
        model="deepseek/deepseek-r1:free",
        api_key="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",
        base_url="https://openrouter.ai/api/v1",
        model_info=ModelInfo(vision=False, function_calling=True, json_output=True, family=ModelFamily.R1),
    ),
)

agent_team = RoundRobinGroupChat([agent, surfer], termination_condition=TextMentionTermination("TERMINATE"))

config = agent_team.dump_component()

with open("/workspaces/multiagent-demo/src/ag_code_example_config.json", "w") as file:
    file.write(config.model_dump_json())

async def main(task = "Summarize the state of GLP-1 drug development"):
    await Console(agent_team.run_stream(task=task))

asyncio.run(main())    