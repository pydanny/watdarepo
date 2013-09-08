===============================
watdarepo
===============================

.. image:: https://badge.fury.io/py/watdarepo.png
    :target: http://badge.fury.io/py/watdarepo
    
.. image:: https://travis-ci.org/pydanny/watdarepo.png?branch=master
        :target: https://travis-ci.org/pydanny/watdarepo

.. image:: https://pypip.in/d/watdarepo/badge.png
        :target: https://crate.io/packages/watdarepo?version=latest

.. image:: https://coveralls.io/repos/audreyr/cookiecutter/badge.png?branch=master
        :target: https://coveralls.io/r/audreyr/cookiecutter?branch=master


Determines type and host of a repo. 

* Free software: BSD license
* Documentation: http://watdarepo.rtfd.org.

Features
--------

Works to some degree with the following VCS:

* Git
* Mercurial
* SVN
* BZR

Works to some degree with the following hosting services:

* GitHub
* BitBucket
* GitLab
* Gitorious
* Sourceforge

Usage
-----

::

    >>> from watdarepo import watdarepo
    >>> watdarepo("https://github.com/pydanny/watdarepo")
    {
        u'vcs': u'git',
        u'hosting_service': u'github',
        u'repo_url': u'https://github.com/pydanny/watdarepo'
    }

Related Projects
-----------------

* **Dulwich** is a Python Git API and does not have any discovery features.
* **VCS** works with both Git and Mercurial, incorporates Dulwich, but does not appear to have any discovery features.
