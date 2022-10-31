import subprocess
import json

clear = False

def fetch_users():
    global clear
    file = open("accounts.txt", "r")
    accounts = file.read().split("\n")
    #print(accounts)
    valid_accounts = []
    for account in accounts:
        try:
            account_actions = []
            valid_contract = subprocess.Popen(["cline", "get", "abi", account], stdout = subprocess.PIPE).communicate()[0].decode()
            valid_contract = json.loads(valid_contract)
            for action in valid_contract["actions"]:
                account_actions.append(action["name"])
            valid_actions = subprocess.Popen(["cline", "get", "actions", account, "0", "10", "-j", "--full"], stdout = subprocess.PIPE).communicate()[0].decode()
            valid_actions = json.loads(valid_actions)["actions"]
            for act in valid_actions:
                if act["action_trace"]["act"]["name"] in account_actions:
                    valid_accounts.append(account)
                    break
        except Exception as ex:
            #print(ex)
            pass
    if clear:
        subprocess.run(["clear"])
    print("Valid accounts:\n")
    for account in valid_accounts:
        print(account)

if __name__ == "__main__":
    fetch_users()
