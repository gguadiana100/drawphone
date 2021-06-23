from brownie import AdvancedCollectible, accounts, config
from scripts.helpful_scripts import get_breed
import time

STATIC_SEED = 123

def main():
    dev = accounts.add(config['wallets']['from_key'])
    advanced_collectible = AdvancedCollectible[len(AdvancedCollectible) - 1]
    transaction = advanced_collectible.createCollectible("None", STATIC_SEED, {"from": dev})
    transaction.wait(1) # wait for one confirmation so you can get the breed
    time.sleep(35)
    requestId = transaction.events['requestedCollectible']['requestId']
    token_Id = advanced_collectible.requestIdToTokenId(requestId)
    breed = get_breed(advanced_collectible.tokenIdToBreed(tokenId))
    print('Dog breed of tokenId {} is {}'.format(token_Id, breed))
