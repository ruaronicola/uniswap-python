from setuptools import setup, find_packages

setup(
    name="uniswap-python",
    version="0.7.2",
    description="An unofficial Python wrapper for the decentralized exchange Uniswap",
    author="Shane Fontaine, Erik Bjäreholt",
    author_email="shane6fontaine@gmail.com, erik@bjareho.lt",
    url="https://github.com/shanefontaine/uniswap-python",
    packages=find_packages(),
    package_data={"uniswap": ["assets/*.abi", "assets/*/*.abi"]},
    license="MIT",
    install_requires=[
        "web3>=6.0,<7.0",
        "click>=8.0.3,<9.0.0",
        "python-dotenv",
        "typing-extensions"
    ],
    python_requires=">=3.7.2,<4",
)
