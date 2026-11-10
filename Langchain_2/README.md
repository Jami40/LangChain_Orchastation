# LangChain 2: Prompts and Chains

This module explores LangChain prompt templates, chat prompts, few-shot
prompting, chains, LangChain Expression Language, and output parsers using
Groq chat models.

## Setup

From the repository root, add your key to `.env`:

```env
GROQ_API_KEY=your_groq_api_key
```

The notebook uses LangChain's `ChatGroq` integration.
Run the notebook from the repository workspace so it can find the root `.env`
file. If you opened a copied notebook outside this repository, open the
tracked notebook from `Langchain_2` instead.

Install this module's dependencies before running the notebook:

```powershell
python -m pip install -r .\Langchain_2\requirements.txt
```

In VS Code, select the same Python environment for the notebook:

1. Open the Command Palette with `Ctrl+Shift+P`.
2. Select **Python: Select Interpreter**.
3. Choose the environment where the command above was run.
4. Restart the notebook kernel and run the cells again.

If the error says `No module named 'dotenv'`, install the dependency into the
active notebook environment:

```powershell
python -m pip install python-dotenv==1.0.1
```

Install the module dependencies from `Langchain_1/requirements.txt`, then open
[`02_talk_with_llm_part2.ipynb`](./02_talk_with_llm_part2.ipynb) and run the
cells from top to bottom.

## Topics

- Prompt and chat prompt templates
- Few-shot chat prompting
- Runnable chains
- JSON and Pydantic output parsers
