#!/usr/bin/env python

import argparse
import json
import sys

from distlib import locators as distlib_locators
from distlib import metadata as distlib_metadata

from . import base


def load_package(args):
    locator = distlib_locators.PyPIRPCLocator(args.pypi_url)
    distribution = locator.locate(args.package)
    if distribution is None:
        raise base.LoadingError("No package found for %s" % args.package)

    data = base.PackageData(
        name=distribution.name,
        version=distribution.version,
        download_url=distribution.download_url,
        homepage=getattr(distribution.metadata, 'home_page', None),
        description=distribution.metadata.summary,
        license=distribution.metadata.license,
        build_deps=list(distribution.metadata.build_requires),
        run_deps=list(distribution.metadata.run_requires),
    )
    json.dump(data._asdict(), sys.stdout, indent=2)


def main(argv=None):
    if argv is None:
        argv = sys.argv

    parser = argparse.ArgumentParser(usage="Load metadata information about a package from a PyPI repository")
    parser.add_argument('--pypi-url', default="https://pypi.python.org/pypi/", help="PyPI index to use")
    parser.add_argument('package', help="Package to import")

    args = parser.parse_args(argv[1:])

    try:
        load_package(args)
    except base.LoadingError as e:
        sys.stderr.write('LoadingError: %s\n' % e)
        sys.exit(1)


if __name__ == '__main__':
    main()
