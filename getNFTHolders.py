# AUTHOR Bojangly 6.5.2023
# This script retrieves all holders of an NFT and writes to a file holders.txt
#
# Uses Alchemy API:
#   
# https://docs.alchemy.com/reference/getownersforcollection

import requests
import json

# REPLACE THESE VALUE
ALCHEMY_API_KEY="INSERT_API_KEY_HERE"
CONTRACT_ADDRESS="INSERT_CONTRACT_ADDRESS_HERE" 

url = "https://eth-mainnet.g.alchemy.com/nft/v2/"+ALCHEMY_API_KEY+"/getOwnersForCollection?contractAddress="+CONTRACT_ADDRESS+"&withTokenBalances=true"

headers = {"accept": "application/json"}

holders = requests.get(url, headers=headers)
holdersJson = json.loads(holders.text)

# If number of holders is desired uncomment this
# print(len(holdersJson["ownerAddresses"]))

f = open("holders.txt", "w+")
for owner in holdersJson["ownerAddresses"]:
    f.write(owner["ownerAddress"]+"\n")
f.close()
