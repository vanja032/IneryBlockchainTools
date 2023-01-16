import subprocess, time, json, os
from subprocess import Popen
import re, time

accounts = json.load(open('accounts.json', 'r'))

def import_key_to_wallet(key):
    process = Popen(['cline', 'wallet', 'import', '--private-key', key], stdout=subprocess.PIPE)
    stdout = process.communicate()[0]
    out = stdout.decode()
    return out

def import_keys_to_wallet():
    subprocess.run(["cline", "wallet", "unlock", "--password", "<wallet_password>"])
    for key in accounts:
        key = key["PRIVATE_KEY"]
        import_key_to_wallet(key)
        time.sleep(1)

def create_account(name, pkey):
    process = Popen(['cline', 'system', 'newaccount', 'createacc', name, pkey, pkey], stdout=subprocess.PIPE)
    stdout = process.communicate()[0]
    out = stdout.decode()
    return out

def recreate_accounts():
    num = 0
    for acc in accounts:
        num+=1
        name = acc["NAME"]
        pkey = acc["PUBLIC_KEY"]
        key = acc["PRIVATE_KEY"]
        #import_key_to_wallet(key)
        create_account(name, pkey)
        print(num, '/', len(accounts))
        time.sleep(1)

recreate_accounts()
