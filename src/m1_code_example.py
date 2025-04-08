import asyncio
from autogen_agentchat.agents import AssistantAgent, CodeExecutorAgent, UserProxyAgent
from autogen_ext.models.openai import OpenAIChatCompletionClient
from autogen_ext.agents.web_surfer import MultimodalWebSurfer
from autogen_agentchat.conditions import TextMentionTermination
from autogen_core.models import ModelInfo, ModelFamily
from autogen_agentchat.teams import MagenticOneGroupChat
from autogen_ext.agents.file_surfer import FileSurfer
from autogen_ext.agents.magentic_one import MagenticOneCoderAgent
from autogen_ext.code_executors.local import LocalCommandLineCodeExecutor
from autogen_agentchat.ui import Console
import os


fs = FileSurfer(
    "FileSurfer",
    model_client=OpenAIChatCompletionClient(
        model="openrouter/quasar-alpha",
        api_key=os.environ['OPENROUTER_API_KEY'],
        base_url="https://openrouter.ai/api/v1",
        model_info=ModelInfo(vision=False, function_calling=True, json_output=True, family=ModelFamily.R1),
    ),
)

ws = MultimodalWebSurfer(
    "WebSurfer",
    model_client=OpenAIChatCompletionClient(
        model="openrouter/quasar-alpha",
        api_key=os.environ['OPENROUTER_API_KEY'],
        base_url="https://openrouter.ai/api/v1",
        model_info=ModelInfo(vision=False, function_calling=True, json_output=True, family=ModelFamily.R1),
    ),
)

coder = MagenticOneCoderAgent(
    "Coder",
    model_client=OpenAIChatCompletionClient(
        model="openrouter/quasar-alpha",
        api_key=os.environ['OPENROUTER_API_KEY'],
        base_url="https://openrouter.ai/api/v1",
        model_info=ModelInfo(vision=False, function_calling=True, json_output=True, family=ModelFamily.R1),
    ),
)

executor = CodeExecutorAgent(
    "Executor",
    code_executor=LocalCommandLineCodeExecutor(),
)

user_proxy = UserProxyAgent("User")

agent = AssistantAgent(
    name="assistant",
    model_client=OpenAIChatCompletionClient(
        model="openrouter/quasar-alpha",
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
        model_info=ModelInfo(vision=True, function_calling=True, json_output=True, family=ModelFamily.R1),
    ),
)

m1_team = MagenticOneGroupChat(
    [fs, agent, surfer, coder, executor],
    model_client=OpenAIChatCompletionClient(
        model="google/gemini-2.0-flash-exp:free",
        api_key=os.environ['OPENROUTER_API_KEY'],
        base_url="https://openrouter.ai/api/v1",
        model_info=ModelInfo(vision=True, function_calling=True, json_output=True, family=ModelFamily.R1),
    ),
    max_turns=10,
    termination_condition=TextMentionTermination("TERMINATE"),
)

config = m1_team.dump_component()


with open("/workspaces/multiagent-demo/src/m1_code_example_config.json", "w") as file:
    file.write(config.model_dump_json())


async def main(task = 'Create a database-backed tool to periodically monitor "innovation from China related to oncology"'):
    await Console(m1_team.run_stream(task=task))

asyncio.run(main())