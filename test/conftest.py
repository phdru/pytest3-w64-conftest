
connectionShortcuts = {
    'mysql': 'mysql://test@localhost/test',
    'postgres': 'postgres:///test',
    'sqlite': 'sqlite:/:memory:',
}


def pytest_addoption(parser):
    """Add the SQLObject options"""
    parser.addoption(
        '-D', '--Database',
        action="store", dest="Database", default='sqlite',
        help="The database to run the tests under (default sqlite).  "
        "Can also use an alias from: %s"
        % (', '.join(connectionShortcuts.keys())))

option = None


def pytest_configure(config):
    """Make cmdline arguments available to dbtest"""
    global option
    option = config.option
