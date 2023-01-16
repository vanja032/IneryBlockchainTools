import re, json, subprocess

get_tokens = subprocess.Popen(["cline", "get", "currency", "balance", "inery.token", "inery"], stdout=subprocess.PIPE)
out = get_tokens.communicate()[0]
outp = out.decode().split("\n")
outp = outp[:-1]
tokens = {"rows" : []}
for curr in outp:
    re.sub(' +', ' ', curr)
    curr_tokens = curr.split(" ")
    curr_token = curr_tokens[1]
    get_token_acc = subprocess.Popen(["cline", "get", "currency", "stats", "inery.token", curr_token], stdout=subprocess.PIPE)
    stdout = get_token_acc.communicate()[0]
    out = json.loads(stdout.decode())
    acc = out[curr_token]["issuer"]
    max_supply = out[curr_token]["max_supply"]
    tokens["rows"].append({"account_name":acc, "max_supply" : max_supply})

tokens_json = json.dumps(tokens, indent=4)
with open('tokens.json', 'w') as outf : 
    outf.write(tokens_json)

