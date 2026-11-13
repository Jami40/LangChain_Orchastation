import os
import sys
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq
from dotenv import load_dotenv, find_dotenv
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from langserve import add_routes
import uvicorn


sys.stdout.reconfigure(encoding="utf-8")

_ = load_dotenv(find_dotenv())
groq_api_key = os.environ["GROQ_API_KEY"]

llm = ChatGroq(model="openai/gpt-oss-120b", groq_api_key=groq_api_key)

parser = StrOutputParser()

system_template = "Translate the following into {language}:"

prompt_template = ChatPromptTemplate.from_messages([
    ('system', system_template),
    ('user', '{text}')
])

chain = prompt_template | llm | parser


app = FastAPI(
    title="Simple Translator",
    version="1.0",
    description="A colourful translation frontend powered by LangServe",
)


@app.get("/", response_class=HTMLResponse)
async def translator_frontend() -> str:
    return """
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Rainbow Translator</title>
  <style>
    :root {
      color-scheme: dark;
      font-family: Inter, ui-sans-serif, system-ui, sans-serif;
      background: #100d25;
      color: #f8f7ff;
    }
    * { box-sizing: border-box; }
    body {
      min-height: 100vh;
      margin: 0;
      display: grid;
      place-items: center;
      overflow-x: hidden;
      background:
        radial-gradient(circle at 15% 15%, #ff4d9d55, transparent 30%),
        radial-gradient(circle at 85% 20%, #5b7cfa55, transparent 28%),
        linear-gradient(135deg, #100d25, #21103e 55%, #101d3c);
    }
    .orb {
      position: fixed;
      width: 18rem;
      height: 18rem;
      border-radius: 50%;
      filter: blur(5px);
      opacity: .35;
      pointer-events: none;
      background: #24e1c5;
      animation: float 8s ease-in-out infinite;
    }
    .orb.one { top: -7rem; left: -5rem; }
    .orb.two { right: -6rem; bottom: -7rem; background: #ffb347; animation-delay: -3s; }
    @keyframes float { 50% { transform: translate(2rem, -1rem) scale(1.12); } }
    main {
      position: relative;
      width: min(92vw, 760px);
      padding: clamp(1.4rem, 5vw, 3rem);
      border: 1px solid #ffffff26;
      border-radius: 28px;
      background: #ffffff12;
      box-shadow: 0 24px 80px #00000055;
      backdrop-filter: blur(22px);
    }
    .eyebrow {
      margin: 0 0 .65rem;
      color: #68f7dc;
      font-size: .75rem;
      font-weight: 800;
      letter-spacing: .18em;
      text-transform: uppercase;
    }
    h1 { margin: 0; font-size: clamp(2.2rem, 7vw, 4.5rem); line-height: .95; }
    .subtitle { color: #d3cfee; margin: 1rem 0 2rem; }
    label { display: block; margin: 1rem 0 .45rem; color: #e8e4ff; font-weight: 700; }
    textarea, select {
      width: 100%;
      border: 1px solid #ffffff2e;
      border-radius: 14px;
      padding: 1rem;
      color: #fff;
      background: #090719aa;
      font: inherit;
      outline: none;
    }
    textarea { min-height: 145px; resize: vertical; }
    textarea:focus, select:focus { border-color: #68f7dc; box-shadow: 0 0 0 3px #68f7dc22; }
    .actions { display: flex; flex-wrap: wrap; gap: .75rem; margin-top: 1.3rem; }
    button {
      border: 0;
      border-radius: 999px;
      padding: .8rem 1.25rem;
      color: #160e2b;
      background: linear-gradient(100deg, #68f7dc, #a5f36d);
      font: inherit;
      font-weight: 800;
      cursor: pointer;
      transition: transform .2s, box-shadow .2s;
    }
    button:hover { transform: translateY(-2px); box-shadow: 0 8px 24px #68f7dc44; }
    button:disabled { cursor: wait; opacity: .65; transform: none; }
    .example { color: #fff; background: #ffffff18; }
    .result {
      display: none;
      margin-top: 1.8rem;
      padding: 1.2rem;
      border-left: 4px solid #ff7eb6;
      border-radius: 14px;
      background: #090719aa;
    }
    .result.visible { display: block; }
    .result h2 { margin: 0 0 .7rem; font-size: 1rem; color: #ff9ac4; }
    #output { margin: 0; white-space: pre-wrap; line-height: 1.7; }
    .status { min-height: 1.4rem; margin-top: .8rem; color: #f5bdd3; }
  </style>
</head>
<body>
  <div class="orb one"></div><div class="orb two"></div>
  <main>
    <p class="eyebrow">LangServe + Groq</p>
    <h1>Rainbow Translator</h1>
    <p class="subtitle">Turn your words into another language with a single colourful chain.</p>
    <label for="language">Translate to</label>
    <select id="language">
      <option>Bangla</option><option>Spanish</option><option>French</option>
      <option>German</option><option>Japanese</option><option>Arabic</option>
    </select>
    <label for="text">Your text</label>
    <textarea id="text" placeholder="Type something to translate...">Hello, my dog is cute</textarea>
    <div class="actions">
      <button id="translate">Translate ✨</button>
      <button class="example" type="button" id="example">Use an example</button>
    </div>
    <div class="status" id="status" role="status"></div>
    <section class="result" id="result">
      <h2>Translated result</h2>
      <p id="output"></p>
    </section>
  </main>
  <script>
    const language = document.querySelector("#language");
    const text = document.querySelector("#text");
    const translate = document.querySelector("#translate");
    const example = document.querySelector("#example");
    const status = document.querySelector("#status");
    const result = document.querySelector("#result");
    const output = document.querySelector("#output");

    example.addEventListener("click", () => {
      language.value = "Bangla";
      text.value = "Learning LangChain is an exciting journey.";
      text.focus();
    });

    translate.addEventListener("click", async () => {
      const value = text.value.trim();
      if (!value) {
        status.textContent = "Please enter some text first.";
        text.focus();
        return;
      }
      translate.disabled = true;
      status.textContent = "Translating...";
      result.classList.remove("visible");
      try {
        const response = await fetch("/chain/invoke", {
          method: "POST",
          headers: {"Content-Type": "application/json"},
          body: JSON.stringify({input: {language: language.value, text: value}})
        });
        const data = await response.json();
        if (!response.ok) throw new Error(data.detail || "The translation request failed.");
        output.textContent = data.output;
        result.classList.add("visible");
        status.textContent = "Done!";
      } catch (error) {
        status.textContent = error.message;
      } finally {
        translate.disabled = false;
      }
    });
  </script>
</body>
</html>
"""


add_routes(
    app,
    chain,
    path="/chain",
)

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)




# localhost:8000/chain/playground