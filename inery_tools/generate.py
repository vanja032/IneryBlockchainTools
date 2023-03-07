import subprocess
import json
from time import sleep

# all inery account 
# inery
# inery.bpay    
# inery.msig    
# inery.names   
# inery.ram     
# inery.ramfee  
# inery.saving  
# inery.stake   
# inery.token   
# inery.vpay    
# inery.wrap    

def create_accounts():

    # password mora se getovati
    wallet_password = "PW5HvNwPsZBF6hsLjqfqxiHVYYxEFbqmarmocKcgwYTw55Kpua7HSroot"
    system_accounts = '[ \n'

    my_list = ['inery.bpay',
            'inery.msig',
            'inery.names',
            'inery.ram',
            'inery.ramfee',
            'inery.saving',
            'inery.stake',
            'inery.token',
            'inery.vpay',
            'inery.wrap',
            'inery.rex',
            'inery.reserv']

    subprocess.run(["cline", "wallet", "unlock", "--password", f"{wallet_password}"], stdout=subprocess.PIPE)

    for el in my_list:
        key_pair    = subprocess.Popen(["cline", "create", "key", "--to-console"], stdout=subprocess.PIPE)
        output      = key_pair.communicate()[0].decode().strip()
        private_key = output[13:64].strip()
        public_key  = output[77:].strip()

        system_accounts += '{'
        system_accounts += f'"NAME": "{el}",\n "PRIVATE_KEY": "{private_key}",\n "PUBLIC_KEY": "{public_key}"\n'
        system_accounts += '},\n'

        subprocess.run(["cline", "create", "account", "inery", f"{el}", f"{public_key}"], stdout=subprocess.PIPE)
        subprocess.run(["cline", "wallet", "import", "--private-key", f"{private_key}"], stdout=subprocess.PIPE)
        sleep(2)

    system_accounts = system_accounts[0:len(system_accounts) - 2]
    system_accounts += '\n]'

    json_data = json.loads(system_accounts)
    
    with open('system_accounts.json', 'w+') as f:
        json.dump(json_data, f, indent=4)

if __name__ == '__main__':  

    create_accounts()

