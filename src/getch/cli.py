from . import config
from . import shell

import click
import os

@click.command()
@click.option(
    '--alias', '-a', required=True, help='Node name.'
)
@click.option(
    '--cli', '-c', help='Run a command in lncli.'
)
@click.option(
    '--start', '-s', is_flag=True, help='Start lnd.'
)
@click.option(
    '--kill', '-k', is_flag=True, help='Kill all lnd instances.'
)
@click.version_option(version='0.1.0-beta', prog_name='Getch')

def main(alias: str, cli: str, start: bool, kill: bool) -> None:
    '''
    Manage multiple Lightning nodes in a simple way.
    '''
    if (kill == True):
        os.system('pkill lnd')    
        click.echo('- [!] All lnd instances have been killed.')
        raise click.Abort()
    
    if (str(alias).title() in ['Basic', 'Bitcoin', 'Bitcoind']):
        click.echo('- [!] %s reserved word.' % (alias))
        raise click.Abort()
    
    path = os.path.expanduser('~/.getch')
    if (os.path.exists(path) == False):
        os.mkdir(path)
        os.mkdir(path + '/nodes')
    
    file = ('%s/getch.conf' % (path))
    if (os.path.exists(file) == False):
        os.popen('touch %s' % (file))

    conf = config.load(file)
    if not (alias in conf.keys()):
        click.echo('- [!] This alias does not exist in the settings.')
        raise click.Abort()
    else:
        conf[alias].update(conf['Basic'])
        conf[alias].update(conf['Bitcoin'])
        conf[alias].update(conf['Bitcoind'])
    
    for x, y in conf[alias].items():
        if ('$alias' in y):
            node = alias.lower().encode()
            conf[alias][x] = y.replace(
                '$alias', path + '/nodes/' + node.hex()
            )

    conf = conf[alias]
    if (os.path.exists(conf['datadir']) == False):
        os.mkdir(conf['datadir'])
    config.dump(
        conf, conf['datadir'] + '/lnd.conf'
    )

    sh = shell.Shell(conf)
    if isinstance(cli, str):
        sh.cli(cli)
    
    elif (start == True):
        sh.start()
