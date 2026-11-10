# 🧩 LangChain 2: Prompts, Chains & Parsers

This module builds on the LLM fundamentals from `Langchain_1`. It demonstrates
how to turn raw model calls into reusable prompt pipelines with templates,
examples, chains, LCEL, and structured output parsers.

The notebook uses Groq through LangChain's `ChatGroq` integration and the
`openai/gpt-oss-120b` model currently available to this project.

## 🎯 Learning goals

- Create reusable `PromptTemplate` objects
- Build conversational prompts with `ChatPromptTemplate`
- Compare modern and older message-template styles
- Guide responses with few-shot examples
- Compose prompts and models into chains
- Use LangChain Expression Language (LCEL)
- Parse model output as JSON
- Validate structured output with Pydantic

## 📓 Notebook

Open [`02_talk_with_llm_part2.ipynb`](./02_talk_with_llm_part2.ipynb) and run
the cells from top to bottom.

## ⚙️ Setup

From the repository root:

```powershell
conda activate llmapp
python -m pip install -r .\Langchain_2\requirements.txt
```

Create `.env` in the repository root:

```env
GROQ_API_KEY=your_groq_api_key
```

The notebook loads the key with `python-dotenv`. In VS Code, select the same
Python interpreter where the requirements were installed, then restart the
notebook kernel.

## 🔗 Model configuration

```python
from langchain_groq import ChatGroq

chat_model = ChatGroq(
    model="openai/gpt-oss-120b",
    groq_api_key=groq_api_key,
)
```

The model name is provider-specific. If Groq returns `model_not_found`, check
the [active Groq models](https://console.groq.com/docs/models) and update the
notebook.

## 🧠 Notebook sections

### 1. Prompt templates

Use variables to reuse a prompt structure:

```python
from langchain_core.prompts import PromptTemplate

template = PromptTemplate.from_template(
    "Tell me a {adjective} story about {topic}"
)
```

### 2. Chat prompt templates

Build system, human, and AI messages with dynamic values:

```python
from langchain_core.prompts import ChatPromptTemplate

chat_template = ChatPromptTemplate.from_messages([
    ("system", "You are an expert on {topic}."),
    ("human", "{question}"),
])
```

### 3. Few-shot prompting

Provide input/output examples so the model can follow a desired pattern,
format, or tone.

### 4. Chains and LCEL

Connect prompt templates, models, and parsers into repeatable workflows rather
than manually passing each intermediate value.

### 5. Output parsers

The notebook demonstrates:

- `SimpleJsonOutputParser`
- `JsonOutputParser`
- Pydantic models with `Field` descriptions

These approaches help transform free-form model responses into application
friendly data.

## 🗂️ Project files

```text
Langchain_2/
├── 02_talk_with_llm_part2.ipynb
├── requirements.txt
└── README.md
```

## 🛠️ Troubleshooting

### `No module named 'dotenv'`

Install dependencies into the active notebook environment:

```powershell
python -m pip install -r .\Langchain_2\requirements.txt
```

### `GROQ_API_KEY` is missing

Confirm that the root `.env` contains:

```env
GROQ_API_KEY=your_groq_api_key
```

Then restart the notebook kernel.

### `model_not_found`

The key is recognized, but the chosen model is unavailable. Use an active
model from the Groq model list.

## 📚 Resources

- [LangChain prompts](https://python.langchain.com/docs/concepts/prompt_templates/)
- [LCEL](https://python.langchain.com/docs/concepts/lcel/)
- [Output parsers](https://python.langchain.com/docs/concepts/output_parsers/)
- [Groq documentation](https://console.groq.com/docs/)
