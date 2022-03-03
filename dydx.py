from dydx.client import Client
import dydx.constants as consts
import dydx.util as utils

client = Client(
    private_key='0x4f3edf983ac636a65a842ce7c78d9aa706d3b113bce9c46f30d7d21715b23b1d',
    node='https://parity.expotrading.com' # Can use url of any Ethereum node
)

# deposit 10 ETH
tx_hash = client.eth.deposit(
  market=consts.MARKET_WETH,
  wei=utils.token_to_wei(10, consts.MARKET_WETH) # amounts are denominated in base units, e.g. 1 ETH = 10^18
)
receipt = client.eth.get_receipt(tx_hash) # waits for deposit transaction to be mined

# deposit 100 DAI
# for markets besides ETH, you'll need to set allowance first
tx_hash = client.eth.set_allowance(market=consts.MARKET_DAI) # must only be called once, ever
receipt = client.eth.get_receipt(tx_hash)

tx_hash = client.eth.deposit(
  market=consts.MARKET_DAI,
  wei=utils.token_to_wei(100, consts.MARKET_DAI)
)
receipt = client.eth.get_receipt(tx_hash)

# Get dYdX account balances
my_balances = client.get_my_balances()


# Create order to SELL 10 ETH for 2000 DAI (a price of 200 DAI/ETH)
created_order = client.create_order(
    makerMarket=consts.MARKET_DAI,
    takerMarket=consts.MARKET_WETH,
    makerAmount=utils.token_to_wei(2000, consts.MARKET_DAI),
    takerAmount=utils.token_to_wei(10, consts.MARKET_WETH)
)
