import subprocess, time, json, os
from subprocess import Popen
import re, random

tokens = json.load(open('tokens.json', 'r'))

def create_token(who, max_supply) :
    print(os.system(f'cline push action inery.token create \'["{who}", "{max_supply}"]\' -p {who}@active'))

def issue_token(who, howmuch, sym) :
     os.system(f'cline push action inery.token issue \'["{who}", "{howmuch}.0000 {sym}", ""]\' -p {who}@active')


def create_tokens() :
    num = 0
    tlen = len(tokens["rows"])
    for t in tokens["rows"] :
        random_int = random.randint(1, 100000)
        name = t["account_name"]
        supply = t["max_supply"]

        symbol = supply.split(' ')[1]

        create_token(name, supply)
        issue_token(name, str(random_int), symbol )

        os.system(f'cline transfer {name} inery "1 {symbol}" -p {name}@active')
        time.sleep(1)

        num+=1
        print(num , '/', tlen)



if __name__ == "__main__" :
	create_tokens()
