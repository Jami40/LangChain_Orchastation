# LangChain Learning Projects

> A growing collection of hands-on projects for learning and building with
> LangChain, large language models, and generative AI.

This repository contains independent LangChain experiments and learning
modules. Each folder focuses on a specific concept and includes its own
notebook, dependencies, and documentation where appropriate.

## 📚 Modules

| Module | Topics | Guide |
|---|---|---|
| [`Langchain_1`](./Langchain_1/) | LLM completion, streaming, temperature, chat models, OpenAI, and Groq | [`README.md`](./Langchain_1/README.md) |
| [`Langchain_2`](./Langchain_2/) | Prompt templates, few-shot prompting, chains, and output parsers with xAI Grok | [`02_talk_with_llm_part2.ipynb`](./Langchain_2/02_talk_with_llm_part2.ipynb) |
| *More modules coming soon* | Additional LangChain concepts and projects | — |

## 🗂️ Repository structure

```text
LangChain/
├── Langchain_1/
│   ├── 01_talk_with_llm.ipynb
│   ├── requirements.txt
│   ├── GENAI_Langchain_1.pdf
│   └── README.md
├── .gitignore
└── README.md
```

New projects can be added as separate folders, for example:

```text
Langchain_2/
Langchain_3/
RAG_Project/
Agents_Project/
```

## 🚀 Getting started

1. Open a module folder.
2. Read that folder's `README.md`.
3. Create and activate the recommended Python environment.
4. Install that module's dependencies.
5. Configure the required API keys.
6. Run the module's notebook or application.

Start here:

➡️ [`Langchain_1/README.md`](./Langchain_1/README.md)

## 🔐 Security

Create one repository-level `.env` file for shared provider credentials. Use
[`.env.example`](./.env.example) as the template:

```bash
copy .env.example .env
```

Then add your local keys:

```env
GROQ_API_KEY=your_groq_api_key
```

Never commit API keys or private credentials. The real `.env` file is ignored
by Git, while `.env.example` is safe to share.

`Langchain_2` uses Groq through LangChain's `ChatGroq` integration and the
`GROQ_API_KEY` environment variable.

## ⚠️ Responsible use

LLM output can be inaccurate or incomplete. Verify important information and
avoid sending private or sensitive data to external model providers.

## 📄 License

No license has been specified yet. Add a license before redistributing this
repository or its learning materials.
