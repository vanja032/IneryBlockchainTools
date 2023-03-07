#!/usr/bin/python3
import json
import subprocess

#with open("test.txt", "r+") as file:
#    block = json.loads(file.read())
#    count = len(block["transactions"])
#    print(f"Number of transactions in the block: {count}")

blocks = []
start_block = 7400000 # search from this block
stop_block = 7420000 # search to this block

for block in range(start_block, stop_block):
    result = json.loads(subprocess.Popen(["cline", "get", "block", f"{block}"], stdout=subprocess.PIPE).communicate()[0].decode())
    number = len(result["transactions"])
    if(number > 0):
        blocks.append({"block": block, "trx": number, "master": result["master"], "time": result["timestamp"]})
        print('{"block": ' + str(block) + ', "trx": ' + str(number) + '}')

with open("blocks.json", "w+") as file:
    json.dump(blocks, file, indent = 6)