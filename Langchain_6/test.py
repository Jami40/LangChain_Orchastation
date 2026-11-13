import sys

from langserve import RemoteRunnable

sys.stdout.reconfigure(encoding="utf-8")

chain = RemoteRunnable("http://localhost:8000/chain/c/N4XyA")
res=chain.invoke({"language": "Bangla", "text": "Hello, my dog is cute"})
print(res)