import os
import subprocess
import re
import json

test = subprocess.Popen(["cline", "get", "currency", "balance", "inery.token", "inery"], stdout=subprocess.PIPE)
out = test.communicate()[0]
output = out.decode().split("\n")
output = output[:-1]

for tokens in output:
    re.sub(' +', ' ', tokens)
    current_token = tokens.split(" ")
    #print(current_token)
    current_token = current_token[1]
    get_currency = subprocess.Popen(["cline", "get", "currency", "stats", "inery.token", current_token], stdout=subprocess.PIPE)
    currency_out = get_currency.communicate()[0]
    currency_output = currency_out.decode()
    #print(currency_output)
    account = json.loads(currency_output)[current_token]["issuer"]
    print(current_token + " : " + account)
    #get_actions = subprocess.Popen(["cline", "get", "actions", account], stdout=subprocess.PIPE)
    #actions_out = get_actions.communicate()[0]
    #actions_output = actions_out.decode().split("\n")
    #for trx in actions_output:
    #    print(trx)
