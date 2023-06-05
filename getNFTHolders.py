# AUTHOR Bojangly 6.5.2023
# This script retrieves all holders of an NFT and writes to a file holders.txt
# Uses Alchemy API:
#   
# https://docs.alchemy.com/reference/getownersforcollection

import requests
import json

CONTRACT_ADDRESS="0xABCDB5710B88f456fED1e99025379e2969F29610" # Radbro

url = "https://eth-mainnet.g.alchemy.com/nft/v2/eG8kahc0OqFr7c1VFxk4BWCVJM4J0gx9/getOwnersForCollection?contractAddress="+CONTRACT_ADDRESS+"&withTokenBalances=true"

headers = {"accept": "application/json"}

holders = requests.get(url, headers=headers)

holdersJson = json.loads(holders.text)

addresses = []
print(len(holdersJson["ownerAddresses"]))
f = open("holders.txt", "a")
for owner in holdersJson["ownerAddresses"]:
    f.write(owner["ownerAddress"]+"\n")


f.close()
