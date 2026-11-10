# LangChain 2: Prompts and Chains

This module explores LangChain prompt templates, chat prompts, few-shot
prompting, chains, LangChain Expression Language, and output parsers using
xAI's Grok models.

## Setup

From the repository root, add your key to `.env`:

```env
XAI_API_KEY=your_xai_api_key
```

The notebook uses xAI's OpenAI-compatible endpoint:

```text
https://api.x.ai/v1
```

Install the module dependencies from `Langchain_1/requirements.txt`, then open
[`02_talk_with_llm_part2.ipynb`](./02_talk_with_llm_part2.ipynb) and run the
cells from top to bottom.

## Topics

- Prompt and chat prompt templates
- Few-shot chat prompting
- Runnable chains
- JSON and Pydantic output parsers
