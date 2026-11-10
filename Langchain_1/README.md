# LangChain LLM Playground

> A practical introduction to calling completion models and chat models with
> [LangChain](https://www.langchain.com/), OpenAI, and Groq.

This project is a notebook-based learning module for experimenting with
large-language-model integrations. It starts with simple prompts and gradually
introduces streaming responses, creativity controls, structured chat messages,
response metadata, and alternative providers.

## ✨ What you will learn

- Load secrets safely from a `.env` file.
- Use LangChain completion models with `OpenAI`.
- Invoke an LLM with a prompt and stream its response token by token.
- Adjust model creativity with the `temperature` parameter.
- Use `ChatOpenAI` with system and human messages.
- Inspect response content, metadata, and schemas.
- Build equivalent chat requests with `SystemMessage` and `HumanMessage`.
- Switch between OpenAI and Groq-backed chat models.

## 📁 Project structure

```text
Langchain_1/
├── 01_talk_with_llm.ipynb  # Main hands-on notebook
├── requirements.txt         # Python dependencies
├── GENAI_Langchain_1.pdf    # Reference material
└── README.md                # Project documentation
```

## ✅ Prerequisites

- Python **3.11**
- An OpenAI API key for the OpenAI examples
- A Groq API key for the optional Groq examples
- Jupyter Notebook, JupyterLab, or another notebook-compatible editor

> API keys are optional only if you skip the cells that call the corresponding
> provider.

## 🚀 Installation

### Option 1: Conda

```bash
conda create -n llmapp python=3.11 -y
conda activate llmapp
pip install -r requirements.txt
```

### Option 2: Python virtual environment

```bash
python -m venv .venv
```

Activate it:

**Windows PowerShell**

```powershell
.\.venv\Scripts\Activate.ps1
```

**macOS/Linux**

```bash
source .venv/bin/activate
```

Then install the dependencies:

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

## 🔐 Configure API keys

Create a `.env` file in the `Langchain_1` directory:

```env
OPENAI_API_KEY=your_openai_api_key
GROQ_API_KEY=your_groq_api_key
```

The notebook loads these values with `python-dotenv`. Never commit `.env`,
hard-code API keys, or share them publicly.

If you only want to run the OpenAI section, you need only:

```env
OPENAI_API_KEY=your_openai_api_key
```

For the Groq section, create a key at
[console.groq.com](https://console.groq.com/) and add `GROQ_API_KEY`.

## ▶️ Run the notebook

Open [01_talk_with_llm.ipynb](./01_talk_with_llm.ipynb) in Jupyter Notebook,
JupyterLab, or VS Code, then run the cells from top to bottom.

From the project directory, start Jupyter with one of these commands:

```bash
jupyter notebook
```

```bash
jupyter lab
```

The notebook demonstrates:

1. Basic completion with `OpenAI`.
2. One-shot invocation with `.invoke(...)`.
3. Streaming output with `.stream(...)`.
4. Temperature-based creativity.
5. Chat completions with `ChatOpenAI`.
6. System and human message objects.
7. Alternative chat models through `ChatGroq`.

## 🧪 Example

```python
from dotenv import find_dotenv, load_dotenv
from langchain_openai import OpenAI

load_dotenv(find_dotenv())

llm = OpenAI()
response = llm.invoke("Tell me one interesting fact about the Kennedy family.")
print(response)
```

Streaming example:

```python
for chunk in llm.stream("Write a short poem about learning LangChain."):
    print(chunk, end="", flush=True)
```

Chat model example:

```python
from langchain_openai import ChatOpenAI

chat_model = ChatOpenAI(model="gpt-3.5-turbo-0125")
response = chat_model.invoke([
    ("system", "You are a helpful history expert."),
    ("human", "Tell me one curious fact about JFK."),
])

print(response.content)
```

## 🧰 Troubleshooting

### `ModuleNotFoundError`

Confirm that the intended environment is active, then reinstall dependencies:

```bash
python -m pip install -r requirements.txt
```

### API key errors

- Confirm that `.env` is in the same project directory as the notebook.
- Check that the variable name is exactly `OPENAI_API_KEY` or `GROQ_API_KEY`.
- Restart the notebook kernel after changing `.env`.
- Make sure the key is active and has available usage/quota.

### Model or access errors

Provider model names and availability can change. If a model is unavailable,
use a currently supported model from the provider's documentation and update
the corresponding notebook cell.

## 📚 Useful resources

- [LangChain documentation](https://python.langchain.com/)
- [LangChain LLM integrations](https://python.langchain.com/docs/integrations/llms/)
- [OpenAI platform documentation](https://platform.openai.com/docs/)
- [Groq documentation](https://console.groq.com/docs/)
- [python-dotenv documentation](https://pypi.org/project/python-dotenv/)

## ⚠️ Responsible use

Model responses can be inaccurate, incomplete, or outdated. Treat generated
content as a starting point, verify important claims, and avoid sending
private or sensitive information to external model providers.

## 📄 License

No license has been specified for this project yet. Add a license before
redistributing the source or its learning materials.
