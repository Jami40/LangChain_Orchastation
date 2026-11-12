# 🦜🔗 LangChain Learning Lab

> Hands-on notebooks for learning LangChain, chat models, prompt engineering,
> chains, structured output, document loading, vector stores, retrieval, and RAG.

This repository is a growing collection of practical LangChain modules. Each module is self-contained and focuses on one stage of building generative
AI applications—from the first model call to reusable prompt pipelines and
structured responses. This root README is the central documentation for the
entire repository.

## 🌟 Learning path

| Module | Focus | Main provider | Start here |
|---|---|---|---|
| [`Langchain_1`](./Langchain_1/) | LLM calls, streaming, temperature, chat messages, and provider integrations | OpenAI + Groq | [`01_talk_with_llm.ipynb`](./Langchain_1/01_talk_with_llm.ipynb) |
| [`Langchain_2`](./Langchain_2/) | Prompt templates, few-shot prompting, chains, LCEL, and output parsers | Groq | [`02_talk_with_llm_part2.ipynb`](./Langchain_2/02_talk_with_llm_part2.ipynb) |
| [`Langchain_3`](./Langchain_3/) | Document loaders, text splitting, embeddings, vector stores, retrievers, and RAG | Groq + OpenAI | [`DataLoader_RAG_Implementation.ipynb`](./Langchain_3/DataLoader_RAG_Implementation.ipynb) |
| [`Langchain_4`](./Langchain_4/) | LCEL composition, built-in runnables, and retrieval chains | Groq + OpenAI | [`LCEL.ipynb`](./Langchain_4/LCEL.ipynb) |

## 🧠 Concepts covered

- **Model invocation** with `.invoke(...)`
- **Streaming** responses with `.stream(...)`
- **Temperature** and response creativity
- **Chat messages** using system, human, and AI roles
- **Prompt templates** with reusable variables
- **Few-shot prompting** with examples
- **Chains** that connect prompts, models, and parsers
- **LangChain Expression Language (LCEL)** using runnable pipelines
- **Built-in runnables** including `RunnablePassthrough`, `RunnableLambda`, and
  `RunnableParallel`
- **Dictionary-based chain inputs** with `itemgetter`
- **Composable retrieval chains** that pass context, questions, and extra
  instructions through one pipeline
- **JSON output parsing**
- **Pydantic-based structured output**
- **Document loading** from TXT, CSV, HTML, PDF, and Wikipedia
- **Text splitting** with character-based and recursive splitters
- **Embeddings** with OpenAI
- **Vector stores** with Chroma and FAISS
- **Similarity retrieval** with configurable result counts
- **Retrieval-Augmented Generation (RAG)** with LCEL
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
├── Langchain_3/
│   ├── DataLoader_RAG_Implementation.ipynb
│   ├── RAG_component.ipynb
│   ├── RAG_Implementation.ipynb
│   └── data/
├── Langchain_4/
│   ├── LCEL.ipynb
│   ├── LCEL_builtin_runnables.ipynb
│   └── LCEL_GenAI.pdf
├── requirements.txt
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

Confirm that the selected interpreter is Python 3.11 before installing:

```powershell
python --version
```

### 3. Install dependencies

Install the shared requirements:

```powershell
python -m pip install -r .\requirements.txt
```

The notebooks in `Langchain_3` also use the packages listed in
[`Langchain_1/requirements.txt`](./Langchain_1/requirements.txt), including
the Chroma and PDF integrations. Install that file as well when running the
vector-store and PDF examples:

```powershell
python -m pip install -r .\Langchain_1\requirements.txt
```

If `python --version` shows Python 3.13 or another version, select the
`llmapp` interpreter in VS Code first. This pinned LangChain learning stack is
tested with Python 3.11.

When a future module introduces a new import, add its package to this root
file and reinstall it in the same environment.

### 4. Configure provider keys

Create a root `.env` file from the template:

```powershell
copy .env.example .env
```

Add your key:

```env
GROQ_API_KEY=your_groq_api_key
OPENAI_API_KEY=your_openai_api_key
```

`GROQ_API_KEY` is used by the chat and document-loader examples. The RAG
implementation uses `OPENAI_API_KEY` for OpenAI embeddings and `ChatOpenAI`.
Both keys are loaded locally and are never committed. Create keys from the
[Groq Console](https://console.groq.com/) and
[OpenAI platform](https://platform.openai.com/api-keys).

### 5. Open a notebook

Open the module notebook in VS Code or Jupyter:

- [`01_talk_with_llm.ipynb`](./Langchain_1/01_talk_with_llm.ipynb)
- [`02_talk_with_llm_part2.ipynb`](./Langchain_2/02_talk_with_llm_part2.ipynb)
- [`DataLoader_RAG_Implementation.ipynb`](./Langchain_3/DataLoader_RAG_Implementation.ipynb)
- [`RAG_component.ipynb`](./Langchain_3/RAG_component.ipynb)
- [`RAG_Implementation.ipynb`](./Langchain_3/RAG_Implementation.ipynb)
- [`LCEL.ipynb`](./Langchain_4/LCEL.ipynb)
- [`LCEL_builtin_runnables.ipynb`](./Langchain_4/LCEL_builtin_runnables.ipynb)

In VS Code, choose the same Python environment where the dependencies were
installed, restart the notebook kernel, and run cells from top to bottom.

The Langchain_3 notebooks expect the working directory to be
`Langchain_3` when relative paths such as `./data/...` are used. Select that
folder as the notebook root, or adjust the paths for your environment.

## 🔧 Current models

`Langchain_2` and the loader examples use Groq:

```python
ChatGroq(
    model="openai/gpt-oss-120b",
    groq_api_key=groq_api_key,
)
```

Provider model availability can change. If Groq returns a `model_not_found`
error, check the [current Groq model list](https://console.groq.com/docs/models)
and update the notebook model name.

`Langchain_3/RAG_Implementation.ipynb` uses OpenAI for both embeddings and the
chat model:

```python
OpenAIEmbeddings()
ChatOpenAI()
```

The notebook builds a FAISS index from a text document, retrieves relevant
chunks, and combines the retriever, prompt, model, and string parser into an
LCEL chain.

## 🔗 LCEL runnable examples

`Langchain_4` builds on the earlier RAG work with small, composable runnable
examples:

- `RunnablePassthrough` forwards the original input unchanged.
- `RunnableLambda` wraps a custom Python function for use in a chain.
- `RunnableParallel` computes multiple named values from the same input.
- `itemgetter` selects fields from dictionary inputs before passing them to a
  retriever or prompt.

The advanced example combines a FAISS retriever, `RunnableParallel`,
`ChatPromptTemplate`, `ChatOpenAI`, and `StrOutputParser`. It accepts a
question and a requested language, retrieves context for the question, and
returns the answer in that language. `LCEL.ipynb` also contrasts the modern
`prompt | model | parser` style with the deprecated `LLMChain` API.

## 🛠️ Troubleshooting

### `ModuleNotFoundError: No module named 'dotenv'`

Install dependencies into the environment selected by the notebook:

```powershell
python -m pip install -r .\requirements.txt
```

### `GROQ_API_KEY` is missing

- Confirm `.env` is in the repository root.
- Confirm the variable is exactly `GROQ_API_KEY`.
- Restart the notebook kernel after editing `.env`.
- Never add quotation marks or spaces around the variable name.

### `OPENAI_API_KEY` is missing

- Add `OPENAI_API_KEY` to the root `.env` file.
- Confirm the notebook is using the environment where `python-dotenv` is installed.
- Restart the notebook kernel after editing `.env`.

### `ModuleNotFoundError: No module named 'langchain_chroma'`

Install the module-specific requirements before running the Chroma examples:

```powershell
python -m pip install -r .\Langchain_1\requirements.txt
```

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
