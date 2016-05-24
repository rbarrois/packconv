Packconv: a package converter
=============================

**Note: This project is currently only a design draft; no actual code exists.**

Packconv converts packages from language-specific formats to distribution-specific versions.

The supported source formats are:

* Python (*sdist*, *wheel*)

The supported target package managers are:

* Portage

Usage
-----

.. code-block:: sh

    $ cd my-overlay
    $ packconv python:Django
    >>> Finding latest version for python:Django
    >>> Parsing metadata for Django==1.9.5
    >>> Importing to dev-python/django/django-1.9.5.ebuild
    >>> Computing files hash
    >>> Building package
    >>> Done.

Configuration
-------------

``packconv`` uses a configuration file in ``.packconv/config``:

.. code-block:: ini

    [targets]
    ; Generate portage packages in the local folder 
    portage = .

    [portage]
    default-keywords = amd64 ~arm64

    [python]

It also manages package name mappings (when the upstream name does not match the distribution guidelines):

.. code-block:: ini

    # .packconv/portage
    [system]
    gcc = sys-devel/gcc

    [python]
    myapp = app-misc/myapp
    python-ldap = dev-python/ldap

Finally, it is also possible to specify dependencies on "system" packages:

.. code-block:: ini

    # .packconv/systemdeps
    [python]
    myapp = gcc openldap
