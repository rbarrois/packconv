
import collections

class LoadingError(Exception):
    """Base class for loading errors"""


PackageData = collections.namedtuple(
    'PackageData',
    [
        'name', 'version', 'download_url', 'homepage', 'description', 'license',
        'build_deps', 'run_deps',
    ])
