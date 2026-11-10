# 🦜🔗 LangChain Learning Lab

> Hands-on notebooks for learning LangChain, chat models, prompt engineering,
> chains, and structured LLM output.

This repository is a growing collection of practical LangChain modules. Each module is self-contained and focuses on one stage of building generative
AI applications—from the first model call to reusable prompt pipelines and
structured responses. This root README is the central documentation for the
entire repository.

## 🌟 Learning path

| Module | Focus | Main provider | Start here |
|---|---|---|---|
| [`Langchain_1`](./Langchain_1/) | LLM calls, streaming, temperature, chat messages, and provider integrations | OpenAI + Groq | [`01_talk_with_llm.ipynb`](./Langchain_1/01_talk_with_llm.ipynb) |
| [`Langchain_2`](./Langchain_2/) | Prompt templates, few-shot prompting, chains, LCEL, and output parsers | Groq | [`02_talk_with_llm_part2.ipynb`](./Langchain_2/02_talk_with_llm_part2.ipynb) |
| More modules coming soon | RAG, agents, tools, memory, and deployment | — | — |

## 🧠 Concepts covered

- **Model invocation** with `.invoke(...)`
- **Streaming** responses with `.stream(...)`
- **Temperature** and response creativity
- **Chat messages** using system, human, and AI roles
- **Prompt templates** with reusable variables
- **Few-shot prompting** with examples
- **Chains** that connect prompts, models, and parsers
- **LangChain Expression Language (LCEL)** using runnable pipelines
- **JSON output parsing**
- **Pydantic-based structured output**
- Secure environment-variable loading with `python-dotenv`

## 📁 Repository structure

```text
LangChain/
├── Langchain_1/
│   ├── 01_talk_with_llm.ipynb
│   ├── GENAI_Langchain_1.pdf
│   ├── requirements.txt
├── Langchain_2/
│   ├── 02_talk_with_llm_part2.ipynb
│   ├── requirements.txt
│   └── .gitkeep
├── .env.example
├── .gitignore
└── README.md
```

## 🚀 Quick start

### 1. Clone the repository

```bash
git clone https://github.com/Jami40/LangChain_Orchastation.git
cd LangChain_Orchastation
```

### 2. Create an environment

```bash
conda create -n llmapp python=3.11 -y
conda activate llmapp
```

Or use a Python virtual environment:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 3. Install module dependencies

For the first module:

```powershell
python -m pip install -r .\Langchain_1\requirements.txt
```

For the second module:

```powershell
python -m pip install -r .\Langchain_2\requirements.txt
```

### 4. Configure Groq

Create a root `.env` file from the template:

```powershell
copy .env.example .env
```

Add your key:

```env
GROQ_API_KEY=your_groq_api_key
```

The `GROQ_API_KEY` is loaded locally and is never committed. Create a key from
the [Groq Console](https://console.groq.com/).

### 5. Open a notebook

Open the module notebook in VS Code or Jupyter:

- [`01_talk_with_llm.ipynb`](./Langchain_1/01_talk_with_llm.ipynb)
- [`02_talk_with_llm_part2.ipynb`](./Langchain_2/02_talk_with_llm_part2.ipynb)

In VS Code, choose the same Python environment where the dependencies were
installed, restart the notebook kernel, and run cells from top to bottom.

> Documentation is maintained in this root README. The module folders contain
> notebooks and their dependency files only.

## 🔧 Current Groq model

`Langchain_2` uses:

```python
ChatGroq(
    model="openai/gpt-oss-120b",
    groq_api_key=groq_api_key,
)
```

Provider model availability can change. If Groq returns a `model_not_found`
error, check the [current Groq model list](https://console.groq.com/docs/models)
and update the notebook model name.

## 🛠️ Troubleshooting

### `ModuleNotFoundError: No module named 'dotenv'`

Install dependencies into the environment selected by the notebook:

```powershell
python -m pip install -r .\Langchain_2\requirements.txt
```

### `GROQ_API_KEY` is missing

- Confirm `.env` is in the repository root.
- Confirm the variable is exactly `GROQ_API_KEY`.
- Restart the notebook kernel after editing `.env`.
- Never add quotation marks or spaces around the variable name.

### `model_not_found`

The API key is working, but the selected model is unavailable to the account.
Use an active model listed in the Groq Console.

## 🔐 Security

Never commit `.env`, API keys, or private credentials. The repository ignores
secret files and notebook checkpoints. The shareable [`.env.example`](./.env.example)
contains only variable names and empty values.

## 📚 Resources

- [LangChain documentation](https://python.langchain.com/)
- [LangChain Expression Language](https://python.langchain.com/docs/concepts/lcel/)
- [Groq documentation](https://console.groq.com/docs/)
- [python-dotenv](https://pypi.org/project/python-dotenv/)

## ⚠️ Responsible use

LLM responses may be inaccurate or incomplete. Verify important information,
avoid sending sensitive data to external providers, and follow each provider's
terms and usage policies.

## 📄 License

No license has been specified yet. Add a license before redistributing this
repository or its learning materials.
