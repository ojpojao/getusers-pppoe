# GET USERS PPPOE ROUTEROS
This tiny script get all users Mikrotik RouterOS and exports to csv file

[![Build Status](https://travis-ci.org/ojpojao/getusers-pppoe.svg?branch=master)](https://travis-ci.org/ojpojao/getusers-pppoe)

## Requirements
- [Python](https://www.python.org/) >= 3.6
- [Pandas](https://pypi.org/project/pandas/) >= 1.2.4
- [RouterOS-api](https://pypi.org/project/RouterOS-api/) >= 0.17.0
- [Python3-virtualenv](https://pypi.org/project/virtualenv/)
- [git](https://git-scm.com/)
- Your Mikrotik RouterOS device must have the api enabled in ip->services


### Setup

- Ubuntu, Mint:
```console
sudo apt update && sudo apt install -y python3-pip git python3-venv
git clone https://github.com/ojpojao/olt8820g.git
cd pastinhas
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

```
- Fedora
```console
sudo dnf install -y git
git clone https://github.com/ojpojao/olt8820g.git
cd astinhas
python3 -m virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Run
In the main function, edit the host, username and password parameters according to your device. Then save and run the script.
```console
python main.py
```

