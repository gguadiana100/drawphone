from brownie import AdvancedCollectible
from scripts.helpful_scripts import fund_advanced_collectible

def main():
    advanced_collectible = AdvancedCollectible(len(AdvancedCollectible)-1) # get the most recently deployed contract
    fund_advanced_collectible(advanced_collectible)
