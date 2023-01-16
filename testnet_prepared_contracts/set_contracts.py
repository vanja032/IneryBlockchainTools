import subprocess
import time
import json

accounts = json.load(open("accounts.json", "r"))

for account in accounts:
    try:
        account = account["NAME"]
        subprocess.run(["cline", "set", "code", account, "contracts/" + account + ".wasm"])
        subprocess.run(["cline", "set", "abi", account, "contracts/" + account + ".abi"])
    except Exception as e:
        print(e)
