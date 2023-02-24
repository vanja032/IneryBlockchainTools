import subprocess
import json

def get_keys(account):
    public_key = json.loads(subprocess.Popen(["cline", "get", "account", account, "--json"], stdout = subprocess.PIPE).communicate()[0].decode())["permissions"][0]["required_auth"]["keys"][0]["key"]
    subprocess.run(["cline", "wallet", "unlock", "--password", "<wallet private key>"])
    keys = json.loads(subprocess.Popen(["cline", "wallet", "private_keys"], stdout = subprocess.PIPE).communicate()[0].decode())
    for key_pair in keys:
        if key_pair[0] == public_key:
            print("Public key: " + key_pair[0] + "\n" + "Private key: " + key_pair[1])



if __name__ == "__main__":
    account = input("Search account name: ")
    try:
        get_keys(account)
    except:
        print("Account does not exist!")
