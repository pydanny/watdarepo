#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
watdarepo.main
-----------------

"""

from __future__ import unicode_literals
import sys

PY3 = sys.version > '3'

if PY3:
    unicode = str


class UnknownVCS(Exception):
    pass


class UnknownHostingService(Exception):
    pass

REPO_ALIASES = ("git", "hg", "svn", "bzr")
HOSTING_SERVICES = ("gitlab",
                    "github",
                    "bitbucket",
                    "gitorious",
                    "sourceforge")


class RepoData(object):
    """ Bunch class to provide an object representation
        instead of a dictionary representation.
    """

    def __init__(self, repo_data):
        self.update(repo_data)


def identify_vcs_vs_alias(repo_url, guess=False):
    for repo_alias in REPO_ALIASES:
        if repo_url.startswith(repo_alias):
            return repo_alias

        if repo_url.endswith(repo_alias):
            return repo_alias

        # Guessing in this loop
        if guess and repo_alias in repo_url:
            return repo_alias

    return None


def identify_vcs(repo_url, guess=False):
    """
    Determines the type of repo that `repo_url` represents.
    :param repo_url: Repo URL of unknown type.
    :returns: VCS type (git, hg, etc) or raises UnknownVCS exception.
    """
    repo_url = unicode(repo_url)

    # Do basic alias check
    vcs = identify_vcs_vs_alias(repo_url, guess=guess)
    if vcs:
        return vcs

    # remove prefix and try again
    no_prefix = ''.join(repo_url.split("//")[1:])
    vcs = identify_vcs_vs_alias(no_prefix, guess=guess)
    if vcs:
        return vcs

    raise UnknownVCS


def identify_hosting_service(repo_url):
    """
    Determines the hosting service of `repo_url`.
    :param repo_url: Repo URL of unknown type.
    :returns: Hosting service or raises UnknownHostingService exception.
    """
    repo_url = unicode(repo_url)

    for service in HOSTING_SERVICES:
        if service in repo_url:
            return service

    raise UnknownHostingService


def watdarepo(repo_url, mode='d', guess=False):
    """
    Gets vcs and hosting service for repo_urls
    :param repo_url: Repo URL of unknown type.
    :param mode: Return dictionary (default) or object
    :param guess: Whether or not to make guesses
    :returns: Hosting service or raises UnknownHostingService exception.
    """
    repo_url = unicode(repo_url)

    # Set the repo_url
    repo_data = {'repo_url': repo_url}

    # Get the VCS type
    try:
        repo_data['vcs'] = identify_vcs(repo_url)
    except UnknownVCS:
        repo_data['vcs'] = None

    # Get the hosting service
    try:
        repo_data['hosting_service'] = identify_hosting_service(repo_url)
    except UnknownHostingService:
        repo_data['hosting_service'] = None

    # If mode is 'c' or 'o', return an object representation of data.
    if mode in ('c', 'o'):
        return RepoData(repo_data)

    # return dictionary representation of data.
    return repo_data


if __name__ == "__main__":
    pass
