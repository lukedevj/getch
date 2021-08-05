# Getch

Manage multiple Lightning nodes in a simple way.

[Buy me a coffee ☕︎](https://coinos.io/lukedev)

## Install

* Require `Python >= 3.6`
* Require `Lnd`
* Clone Repository 

```bash
$ cd getch/
$ python3 setup.py install --user
$ mkdir ~/.getch
$ mv ./getch.conf ~/.getch/getch.conf
```

Verify it's installed:
```bash
$ getch --help
```

## How to use?

First we will have to analyze the `cat ./getch.conf` configuration file and we can see that the configuration file is very similar to the `cat ~/.lnd/lnd.conf` configuration file, because they are the same configurations, each [Alias] is a "node" that has its own settings, there are reserved words like Basic, Bitcoin and Bitcoind, which are used to apply a global setting to all nodes, as you can see there is a special `$alias` character it takes the name of the key and replacing `$alias` with the key for example `Bob`, in [Bitcoin] you can configure some things, in [Bitcoind] it will be the ZMQ and RPC settings of your `bitcoind` you can find these settings in the file `cat ~/.bitcoin/bitcoin.conf`.

### Creating a new node?

In order for you to create a new node, it is first necessary to configure it in the configuration file, Example:

```bash
$ nano ~/.getch/getch.conf
```

```bash
[Luke]
alias = 'Luke'
listen = 9377
rpclisten = '127.0.0.1:10011'
restlisten = '127.0.0.1:8980'
externalip = '127.0.0.1:9201'
```

After that let's start lnd with these settings `getch -a Luke -s` open a new tab in the terminal, `getch -a Luke -c "create"` to create a new wallet.

### Executing commands.
```bash
$ getch -a Luke -c "getinfo"
{
    "version": "0.13.99-beta commit=v0.13.0-beta-195-ga427451b",
    "commit_hash": "a427451b7500979be5a6a4833c63026867cf23c3",
    "identity_pubkey": "03a04b1259522e9d0a8e9d088aead406ca7d9751246561997d979c2bd4bd77657a",
    "alias": "Alice",
    "color": "#3399ff",
    "num_pending_channels": 0,
    "num_active_channels": 0,
    "num_inactive_channels": 0,
    "num_peers": 0,
    "block_height": 232,
    "block_hash": "71a41a6a599799fefe8ae4004d3992711caeda795993142b74accd3015498982" 
....}
```

### Killing all nd instances.
```bash
$ getch -a "" -k
```
