# 🧱 LangChain 1: LLM Fundamentals

This module introduces the core workflow for calling large language models
with LangChain. The notebook starts with simple completion prompts and moves
through streaming, temperature, chat messages, response inspection, and Groq
alternatives.

## 📓 Notebook

Open [`01_talk_with_llm.ipynb`](./01_talk_with_llm.ipynb) and run the cells in
order.

## ✨ What you will learn

- Load environment variables with `python-dotenv`
- Call completion models with `OpenAI`
- Generate responses with `.invoke(...)`
- Stream output with `.stream(...)`
- Control creativity using `temperature`
- Use `ChatOpenAI` with system and human messages
- Inspect response content, metadata, and schemas
- Use `ChatGroq` as an alternative chat provider

## ⚙️ Setup

From the repository root:

```powershell
conda create -n llmapp python=3.11 -y
conda activate llmapp
python -m pip install -r .\Langchain_1\requirements.txt
```

Create a root `.env` file:

```powershell
copy .env.example .env
```

Add the provider key required by the notebook section you want to run:

```env
OPENAI_API_KEY=your_openai_api_key
GROQ_API_KEY=your_groq_api_key
```

Keep `.env` private. It is ignored by Git.

## 🧪 Core examples

### Invoke a model

```python
response = llmModel.invoke(
    "Tell me one interesting fact about the Kennedy family."
)
print(response)
```

### Stream a response

```python
for chunk in llmModel.stream("Write a short poem about LangChain."):
    print(chunk, end="", flush=True)
```

### Use chat messages

```python
messages = [
    ("system", "You are a helpful history expert."),
    ("human", "Tell me one curious fact about JFK."),
]
response = chatModel.invoke(messages)
print(response.content)
```

### Use Groq

```python
from langchain_groq import ChatGroq

llamaChatModel = ChatGroq(
    model="openai/gpt-oss-120b",
    groq_api_key=os.environ["GROQ_API_KEY"],
)
```

## 🗂️ Project files

```text
Langchain_1/
├── 01_talk_with_llm.ipynb
├── GENAI_Langchain_1.pdf
├── requirements.txt
└── README.md
```

## 🛠️ Troubleshooting

### `ModuleNotFoundError`

Make sure VS Code is using the environment where the requirements were
installed:

```powershell
python -m pip install -r .\Langchain_1\requirements.txt
```

### API key errors

Check that the required key exists in the root `.env`, then restart the
notebook kernel.

### Model errors

Provider model names change over time. Check the provider's model list and
replace unavailable model names in the relevant notebook cell.

## 📚 References

- [LangChain documentation](https://python.langchain.com/)
- [OpenAI integrations](https://python.langchain.com/docs/integrations/llms/openai/)
- [Groq documentation](https://console.groq.com/docs/)
