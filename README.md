# uniswap-python

[![Build Status](https://travis-ci.org/shanefontaine/uniswap-python.svg?branch=master)](https://travis-ci.org/shanefontaine/uniswap-python)
[![Downloads](https://pepy.tech/badge/uniswap-python)](https://pepy.tech/project/uniswap-python)
[![License](http://img.shields.io/badge/license-MIT-blue.svg)](https://raw.githubusercontent.com/shanefontaine/uniswap-python/master/LICENSE)

The unofficial Python client for the [Uniswap](https://uniswap.io/).

_I am in no way affiliated with or funded by Uniswap, uniswap.io, or any subsidiaries or affiliates of any of the previously mentioned entities._

## Functionality
* A simple to use Python wrapper for all available contract functions and variables
* Simple parsing of data returned from the Uniswap contract

## Under Development
* Run tests on a private chain rather than Rinkeby
* Better error handling

## Getting Started
This README is documentation on the syntax of the python client presented in this repository. See function docstrings for full syntax details.
This API attempts to present a clean interface to Uniswap, but in order to use it to its full potential, you must familiarize yourself with the official Uniswap documentation.

* https://docs.uniswap.io/

You may manually install the project or use pip:

```python
pip install uniswap-python

# or

pip install git+git://github.com/shanefontaine/uniswap-python.git
```

### Environment Variables
The program expects an environment variables to be set in order to run the program. You can use an Infura node, since the transactions are being signed locally and broadcast as a raw transaction. The environment variable is:

```
PROVIDER  # HTTP Provider for web3
```

### Public Client
Only some endpoints in the API are available to everyone. The public endpoints can be reached using PublicClient

```python
import uniswap
uniswap_wrapper = uniswap.UniswapWrapper()
eth = "0x0000000000000000000000000000000000000000"
bat = "0x0D8775F648430679A709E98d2b0Cb6250d2887EF"
dai = "0x89d24A6b4CcB1B6fAA2625fE562bDD9a23260359"
```

#### Market Methods
* [get_fee_maker](https://docs.uniswap.io/)
```python
uniswap_wrapper.get_fee_maker()
```

* [get_fee_taker](https://docs.uniswap.io/)
```python
uniswap_wrapper.get_fee_taker()
```

* [get_eth_token_input_price](https://github.com/Uniswap/contracts-vyper/blob/master/contracts/uniswap_exchange.vy#L416)
```python
# Get the public price for ETH to Token trades with an exact input.
uniswap_wrapper.get_eth_token_input_price(bat, 1*10**18)
uniswap_wrapper.get_eth_token_input_price(dai, 5*10**18)
```

* [get_token_eth_input_price](https://github.com/Uniswap/contracts-vyper/blob/master/contracts/uniswap_exchange.vy#L437)
```python
# Get the public price for token to ETH trades with an exact input.
uniswap_wrapper.get_token_eth_input_price(bat, 1*10**18)
uniswap_wrapper.get_token_eth_input_price(dai, 5*10**18)
```

* [get_eth_token_output_price](https://github.com/Uniswap/contracts-vyper/blob/master/contracts/uniswap_exchange.vy#L426)
```python
# Get the public price for ETH to Token trades with an exact output
uniswap_wrapper.get_eth_token_output_price(bat, 1*10**18)
uniswap_wrapper.get_eth_token_output_price(dai, 5*10**18)
```

* [get_token_eth_output_price](https://github.com/Uniswap/contracts-vyper/blob/master/contracts/uniswap_exchange.vy#L448)
```python
# Get the public price for token to ETH trades with an exact output.
uniswap_wrapper.get_token_eth_output_price(bat, 1*10**18)
uniswap_wrapper.get_token_eth_output_price(dai, 5*10**18)
```

#### ERC20 Pool Methods
* [get_eth_balance](https://docs.uniswap.io/smart-contract-integration/vyper)
```python
# Get the balance of ETH in an exchange contract.
uniswap_wrapper.get_eth_balance(bat)
```

* [get_token_balance](https://github.com/Uniswap/contracts-vyper/blob/master/contracts/uniswap_exchange.vy#L469)
```python
# Get the balance of a token in an exchange contract.
uniswap_wrapper.get_token_balance(bat)
```

* [get_exchange_rate](https://github.com/Uniswap/uniswap-frontend/blob/master/src/pages/Pool/AddLiquidity.js#L351)
```python
# Get the balance of a token in an exchange contract.
uniswap_wrapper.get_exchange_rate(bat)
```

#### Liquidity Methods

* [add_liquidity](https://github.com/Uniswap/contracts-vyper/blob/master/contracts/uniswap_exchange.vy#L48)
```python
# Add liquidity to the pool.
uniswap_wrapper.add_liquidity(bat, 1*10**18)
```

* [remove_liquidity](https://github.com/Uniswap/contracts-vyper/blob/master/contracts/uniswap_exchange.vy#L83)
```python
# Remove liquidity from the pool.
uniswap_wrapper.removeliquidity(bat, 1*10**18)
```

#### Trading
* make_trade
  * eth_to_token_input
    * [ethToTokenSwapInput](https://github.com/Uniswap/contracts-vyper/blob/master/contracts/uniswap_exchange.vy#L127)
    * [ethToTokenTransferInput](https://github.com/Uniswap/contracts-vyper/blob/master/contracts/uniswap_exchange.vy#L162)
  * token_to_eth_input
    * [tokenToEthSwapInput](https://github.com/Uniswap/contracts-vyper/blob/master/contracts/uniswap_exchange.vy#L202)
    * [tokenToEthTransferInput](https://github.com/Uniswap/contracts-vyper/blob/master/contracts/uniswap_exchange.vy#L232)
  * token_to_token_input
    * [tokenToTokenSwapInput](https://github.com/Uniswap/contracts-vyper/blob/master/contracts/uniswap_exchange.vy#L271)
    * [tokenToTokenTransferInput](https://github.com/Uniswap/contracts-vyper/blob/master/contracts/uniswap_exchange.vy#L307)
```python
# Make a trade based on the input parameters
uniswap_wrapper.make_trade(eth, bat, 1*10**18) # calls _eth_to_token_input
uniswap_wrapper.make_trade(bat, eth, 1*10**18) # calls _token_to_eth_input
uniswap_wrapper.make_trade(bat, dai, 1*10**18) # calls _token_to_token_input
uniswap_wrapper.make_trade(eth, bat, 1*10**18, "0x123...") # calls _eth_to_token_input
```

* make_trade_output
  * eth_to_token_swap_output
    * [ethToTokenSwapOutput](https://github.com/Uniswap/contracts-vyper/blob/master/contracts/uniswap_exchange.vy#L167)
    * [ethToTokenTransferOutput](https://github.com/Uniswap/contracts-vyper/blob/master/contracts/uniswap_exchange.vy#L197)
  * token_to_eth_swap_output
    * [tokenToEthSwapOutput](https://github.com/Uniswap/contracts-vyper/blob/master/contracts/uniswap_exchange.vy#L237)
    * [tokenToEthTransferOutput](https://github.com/Uniswap/contracts-vyper/blob/master/contracts/uniswap_exchange.vy#L266)
  * token_to_token_swap_output
    * [tokenTotokenSwapOutput](https://github.com/Uniswap/contracts-vyper/blob/master/contracts/uniswap_exchange.vy#L312)
    * [tokenTotokenTransferOutput](https://github.com/Uniswap/contracts-vyper/blob/master/contracts/uniswap_exchange.vy#L349))
```python
# Make a trade where the output qty is known based on the input parameters
uniswap_wrapper.make_trade_output(eth, bat, 1*10**18) # calls _eth_to_token_swap_output
uniswap_wrapper.make_trade_output(bat, eth, 1*10**18) # calls _token_to_eth_swap_output
uniswap_wrapper.make_trade_output(bat, dai, 1*10**18, "0x123...") # calls _token_to_token_swap_output
```

## Testing
Unit tests are under development using the pytest framework. Contributions are welcome!

Test are run on the Rinkeby network.

To run the full test suite and ignore warnings, in the project directory run:

```
python -m pytest -W ignore::DeprecationWarning
```

## Ownership Disclosure
* I own some BAT and DAI tokens that are seen in the examples above. These tokens are used only for example purposes and are not meant to be an endorsement. I am not affiliated with BAT, Brave, Basic Attention Token, Brave Browser, DAI, Maker, MakerDAO, or any subsidiaries.

## Changelog
_0.3.3_
* Provide token inputs as addresses instead of names

_0.3.2_
* Add ability to transfer tokens after a trade
* Add tests for this new functionality

_0.3.1_
* Add tests for all types of trades

_0.3.0_
* Add ability to make all types of trades
* Add example to README

_0.2.1_
* Add liquidity tests

_0.2.0_
* Add liquidity and ERC20 pool methods

_0.1.1_
* Major README update

_0.1.0_
* Add market endpoints
* Add tests for market endpoints