# AUTHOR Bojangly 6.4.2023
# This script creates a list of holders for nfts that all share a certain trait value
# 
# Uses Alchemy API:
#   
# https://docs.alchemy.com/reference/getnftsforcollection
# https://docs.alchemy.com/reference/getownersforcollection



import requests
import json

# REPLACE WITH YOUR API KEY 
ALCHEMY_API_KEY="INSERT_API_KEY_HERE"

CONTRACT_ADDRESS="0xABCDB5710B88f456fED1e99025379e2969F29610"
COLLECTION_SUPPLY=5000
TARGET_TRAIT_TYPE="Arms"
TARGET_TRAIT_VALUE="blood"


# Fetches nfts and searchs for nfts with populated traits of type TARGET_TRAIT_TYPE then filters for trait values of TARGET_TRAIT_VALUE
headers = {"accept": "application/json"}
targetTokens = []
startIndex = 0
for x in range(int(COLLECTION_SUPPLY/100)): 
    url = "https://eth-mainnet.g.alchemy.com/nft/v2/"+ALCHEMY_API_KEY+"/getNFTsForCollection?contractAddress="+CONTRACT_ADDRESS+"&startToken="+str(startIndex)+"&limit=10000&withMetadata=true"
    nfts = requests.get(url, headers=headers)
    nftsJson = json.loads(nfts.text)
    for nft in nftsJson["nfts"]:
        tokenId = int(nft["id"]["tokenId"],16)
        trait = [tpl for tpl in nft["metadata"]["attributes"] if tpl['trait_type'] == TARGET_TRAIT_TYPE]
        if trait:
            if trait[0]['value'] == TARGET_TRAIT_VALUE:
                targetTokens.append(tokenId)
    startIndex = startIndex + 100

# If token ids are desired uncomment this line 
# print(targetTokens)

# If number of holders is desired uncomment this line  
# print(len(targetTokens))


# Fetches holders and filters to those that hold tokens with desired trait
url = "https://eth-mainnet.g.alchemy.com/nft/v2/"+ALCHEMY_API_KEY+"/getOwnersForCollection?contractAddress="+CONTRACT_ADDRESS+"&withTokenBalances=true"
headers = {"accept": "application/json"}
holders = requests.get(url, headers=headers)
holdersJson = json.loads(holders.text)

targetWallets = []
for owner in holdersJson["ownerAddresses"]:
    address = owner["ownerAddress"]
    for token in owner["tokenBalances"]:
        tokenId = int(token["tokenId"],16)
        if(tokenId in targetTokens):
            targetWallets.append(address)
            break

print(targetWallets)

# If number of holders is deisred uncomment this line
# print(len(targetWallets))
