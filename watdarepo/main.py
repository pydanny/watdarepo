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
    unicode = str  # pragma: no cover


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


def identify_vcs_vs_alias(repo_url, guess=False, repo_aliases=REPO_ALIASES):
    for repo_alias in repo_aliases:
        if repo_url.startswith(repo_alias):
            return repo_alias

        if repo_url.endswith(repo_alias):
            return repo_alias

        # Guessing in this loop
        if guess and repo_alias in repo_url:
            return repo_alias

    return None


def identify_vcs(repo_url, guess=False, repo_aliases=REPO_ALIASES):
    """
    Determines the type of repo that `repo_url` represents.
    :param repo_url: Repo URL of unknown type.
    :returns: VCS type (git, hg, etc) or raises UnknownVCS exception.
    """
    repo_url = unicode(repo_url)

    # Do basic alias check
    vcs = identify_vcs_vs_alias(repo_url, guess=guess, repo_aliases=repo_aliases)
    if vcs:
        return vcs

    # remove prefix and try again
    no_prefix = ''.join(repo_url.split("//")[1:])
    vcs = identify_vcs_vs_alias(no_prefix, guess=guess, repo_aliases=repo_aliases)
    if vcs:
        return vcs

    if guess:
        if "bitbucket" in repo_url:
            return "hg"

    raise UnknownVCS


def identify_hosting_service(repo_url, hosting_services=HOSTING_SERVICES):
    """
    Determines the hosting service of `repo_url`.
    :param repo_url: Repo URL of unknown type.
    :returns: Hosting service or raises UnknownHostingService exception.
    """
    repo_url = unicode(repo_url)

    for service in hosting_services:
        if service in repo_url:
            return service

    raise UnknownHostingService


def watdarepo(repo_url, mode='d', guess=False, repo_aliases=REPO_ALIASES, hosting_services=HOSTING_SERVICES):
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
        repo_data['vcs'] = identify_vcs(repo_url, repo_aliases=repo_aliases)
    except UnknownVCS:
        repo_data['vcs'] = None

    # Get the hosting service
    try:
        repo_data['hosting_service'] = identify_hosting_service(repo_url, hosting_services=hosting_services)
    except UnknownHostingService:
        repo_data['hosting_service'] = None

    # If mode is 'c' or 'o', return an object representation of data.
    if mode in ('c', 'o'):
        # Define the c/o response class
        Repo = type(str('Repo'), (object,), repo_data)
        # Return the c/o response object
        return Repo()

    # return dictionary representation of data.
    return repo_data

