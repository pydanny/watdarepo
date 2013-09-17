#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_watdarepo
----------------------------------

Tests for `watdarepo` module.
"""

import sys
import unittest

from watdarepo import identify_hosting_service
from watdarepo import identify_vcs
from watdarepo import watdarepo
from watdarepo.main import UnknownHostingService
from watdarepo.main import UnknownVCS

if sys.version_info[:2] < (2, 7):
    import unittest2 as unittest
else:
    import unittest


class TestIdentifyVcs(unittest.TestCase):

    def test_git(self):
        repo_url = "git@github.com:pydanny/watdarepo.git"
        self.assertEqual(identify_vcs(repo_url), "git")
        repo_url = "https://github.com/pydanny/watdarepo.git"
        self.assertEqual(identify_vcs(repo_url), "git")

    def test_hg(self):
        repo_url = "ssh://hg@bitbucket.org/pydanny/static"
        self.assertEqual(identify_vcs(repo_url), "hg")

        repo_url = "http://bitbucket.org/pydanny/static"
        with self.assertRaises(UnknownVCS):
            identify_vcs(repo_url)
        self.assertEqual(identify_vcs(repo_url, guess=True), "hg")

    def test_svn(self):
        # easy check
        repo_url = "http://svn.code.sf.net/p/docutils/code/trunk"
        self.assertEqual(identify_vcs(repo_url), "svn")

        # Throw an error because it can't find the Repo host
        repo_url = "docutils.svn.sourceforge.net"
        with self.assertRaises(UnknownVCS):
            identify_vcs(repo_url)

        # make a guess
        self.assertEqual(identify_vcs(repo_url, guess=True), "svn")


class TestIdentifyHostingService(unittest.TestCase):

    def test_github(self):
        repo_url = "git@github.com:pydanny/watdarepo.git"
        self.assertEqual(identify_hosting_service(repo_url), "github")
        repo_url = "https://github.com/pydanny/watdarepo.git"
        self.assertEqual(identify_hosting_service(repo_url), "github")

    def test_gitlab(self):
        repo_url = "http://demo.gitlab.com/"
        self.assertEqual(identify_hosting_service(repo_url), "gitlab")

    def test_gitorious(self):
        repo_url = "git://gitorious.org/gitorious/mainline.git"
        self.assertEqual(identify_hosting_service(repo_url), "gitorious")
        repo_url = "http://git.gitorious.org/gitorious/mainline.git"
        self.assertEqual(identify_hosting_service(repo_url), "gitorious")

    def test_bitbucket(self):
        repo_url = "https://bitbucket/pydanny/static/"
        self.assertEqual(identify_hosting_service(repo_url), "bitbucket")

    def test_sourceforge(self):
        pass

    def test_failure(self):
        with self.assertRaises(UnknownHostingService):
            identify_hosting_service("American Hotdogs!")


class TestWatDaRepo(unittest.TestCase):

    def test_github(self):
        repo_url = "git@github.com:pydanny/watdarepo.git"
        data = watdarepo(repo_url)
        self.assertEqual(data['vcs'], u'git')
        self.assertEqual(data['hosting_service'], u'github')

    def test_github_object_mode(self):
        repo_url = "git@github.com:pydanny/watdarepo.git"
        data = watdarepo(repo_url, mode='c')
        self.assertEqual(data.vcs, u'git')
        self.assertEqual(data.hosting_service, u'github')

    def test_unknown_vcs(self):
        repo_url = "http://not-identifiable-repo.com"
        data = watdarepo(repo_url)
        self.assertEqual(data['vcs'], None)

    def test_unknown_hosting_service(self):
        repo_url = "http://not-identifiable-repo.com"
        data = watdarepo(repo_url)
        self.assertEqual(data['hosting_service'], None)

if __name__ == '__main__':
    unittest.main()
