import subprocess
import time
import json

accounts = json.load(open("accounts.json", "r"))

for account in accounts:
    try:
        account = account["NAME"]
        abi = subprocess.Popen(["cline", "get", "abi", account], stdout = subprocess.PIPE).communicate()[0].decode()
        code = subprocess.Popen(["cline", "get", "code", account], stdout = subprocess.PIPE).communicate()[0].decode()
        if len(abi) == 0 or len(code) == 0:
            continue
        abi_f = open("contracts/" + account + ".abi", "x")
        abi_f = open("contracts/" + account + ".abi", "w")
        abi_f.write(abi)
        abi_f.close()
        code_f = open("contracts/" + account + ".wasm", "x")
        code_f = open("contracts/" + account + ".wasm", "w")
        code_f.write(code)
        code_f.close()
    except Exception as e:
        print(e)

