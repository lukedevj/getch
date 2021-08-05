from os import system
from re import findall

class Shell:
    '''
        Interacts with "lnd" to execute CLI commands and initialize it.
    '''

    def __init__(self, config: dict):
        assert isinstance(config, dict), (
            'The config entry is not a dictionary.'
        )

        self.config, self.network = (
            config, 'mainnet'
        )
        networks = [
            'bitcoin.mainnet', 'bitcoin.testnet',
            'bitcoin.regtest', 'bitcoin.signet'
        ]
        for x, y in self.config.items():
            if (x in networks) and (y == '1'):
                self.network = x[8:] ; break
        
        self.macaroonpath = self.config['adminmacaroonpath']
        self.rpcserver = self.config['rpclisten']
        self.datadir = self.config['datadir']
    
    def start(self):
        command = 'lnd --configfile=%s/lnd.conf' % (self.datadir)
        system(command)
    
    def cli(self, args: str):
        command = f'lncli --network={self.network} --rpcserver={self.rpcserver} '
        command+= f'--macaroonpath={self.macaroonpath} --lnddir={self.datadir} {args}'
        system(command)