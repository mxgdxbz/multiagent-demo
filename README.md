# Connecting the Bots: Multi-Agent AI Applications

## Jacob Albrecht  
### Applied Intelligence & Analytics, Bristol Myers Squibb  
#### April 12, 2025  

## ⚠️ Caveat ⚠️
AI Agents is a moving frontier: this snapshot of capabilities from Q1'25 will become obsolete!

---

## This Workshop Uses the Autogen Framework

Autogen is Microsoft's agentic framework designed to enable the development of intelligent agents. It provides tools and capabilities for creating autonomous systems that can interact, learn, and adapt to various tasks and environments.

### Requirements:
- Linux, Mac, or Windows machine with Python 3.10 or above
- An API key (e.g., from [OpenRouter.ai](https://openrouter.ai))
- Install dependencies:  
  ```sh
  pip install openai autogen-agentchat autogen-ext[openai,magentic_one] autogenstudio
  ```

### OR 👇

#### Quick Start Using GitHub
1. Use/create a personal GitHub.com account.
2. Create a Codespace from the repository at [https://github.com/chepyle/multiagent-demo](https://github.com/chepyle/multiagent-demo).

<img src="./images/qrcode_github.com.png" width="240">

---

## Running Locally

1. Download the project from [https://github.com/chepyle/multiagent-demo](https://github.com/chepyle/multiagent-demo).
2. Create a Python virtual environment.
3. Run:
   ```sh
   pip install -r requirements.txt
   ```

---

## Creating a GitHub Codespace (Recommended)

1. Go to [https://github.com/chepyle/multiagent-demo](https://github.com/chepyle/multiagent-demo) - contains all workshop materials.
2. Click "Fork Project" to create your own copy.
3. Click `Code > Codespaces > Start Codespace` from the main branch.

<img src="./images/start_codespace.png" width="240">

4. Wait for the Codespace to boot and install packages.

---

## ⚠️ Safety Caveat ⚠️

Autonomous agents carry risks:
- Arbitrary code execution
- High token utilization
- Sending LLM-generated results to the internet

### Mitigation:
- Use sandboxed environments (e.g., Docker, Codespace).
- Place limits on token utilization costs.
- Use a human-in-the-loop (`UserAgent`) for sensitive tasks.

---

## Quick Start: Tutorial

1. Go to [https://github.com/chepyle/multiagent-demo](https://github.com/chepyle/multiagent-demo).
2. Click "Fork Project" to create your own copy.
3. Click `Code > Codespaces > Start Codespace` from the main branch.
4. Wait for the Codespace to load.
5. Run:
   ```sh
   ./run.sh
   ```
6. Open the app at [https://localhost:8081](https://localhost:8081) (if running locally).


---

## Workshop Tasks

1. **Web Search**: "Search the web and summarize the current state of GLP-1 drug development."
2. **Coder/Analyst/Web**: Create a database-backed tool to monitor "innovation from China related to oncology."

---

## Example Agent Files

Finished versions of the workshop tasks are available in the `./final_app` folder.  
To use in Autogen Studio, run:
```sh
./run.sh final_app
```

---

## After the Workshop

The repository [https://github.com/chepyle/multiagent-demo](https://github.com/chepyle/multiagent-demo) will remain public, but API keys will be deactivated.


*Replace API keys and base URLs with your LLM provider's info to continue using the code.*

As Autogen Studio evolves, this code may become obsolete—keep learning!