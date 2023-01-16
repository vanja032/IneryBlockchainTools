import json

def parse_accounts(fileName: str, saveFileName: str ) -> str:

    file = open(str(fileName), 'r')
    data = json.load(file)
    file.close()

    # Iterating through the json
    accs = '['

    for i in data:
        accs += f'''{"{"}
\t"NAME":"{i}",
\t"PUBLIC_KEY":"{data[i]['public_key']}",
\t"PRIVATE_KEY":"{data[i]['private_key']}",
\t"PEER_ADDRESS": "{data[i]['server_ip']}",
\t"HTTP_ADDRESS": "0.0.0.0:8888",
\t"HOST_ADDRESS": "0.0.0.0:9010"
{"},"}
    '''

    accs += ']'

    print(accs)
    print('IMPORTAN!!!!! REMOVE LAST , ')

    with open(str(saveFileName), "w") as outfile:
        outfile.write(str(data))
    outfile.close()

if __name__ == '__main__':
    fileName = input('Enter file name to parse: ')
    saveFileName = input('Enter file name where you want to save parsed data: ')

    parse_accounts(fileName , saveFileName)
