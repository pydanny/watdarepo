#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_watdarepo
----------------------------------

Tests for `watdarepo` module.
"""

import unittest

from watdarepo import identify_vcs
from watdarepo.main import UnknownVCS


class TestIdentifyVcs(unittest.TestCase):

    def test_git(self):
        repo_url = "git@github.com:pydanny/watdarepo.git"
        self.assertEqual(identify_vcs(repo_url), "git")
        repo_url = "https://github.com/pydanny/watdarepo.git"
        self.assertEqual(identify_vcs(repo_url), "git")

    def test_hg(self):
        repo_url = "ssh://hg@bitbucket.org/pydanny/static"
        self.assertEqual(identify_vcs(repo_url), "hg")

    def test_svn(self):
        # easy check
        repo_url = "http://svn.code.sf.net/p/docutils/code/trunk"
        self.assertEqual(identify_vcs(repo_url), "svn")

        # Throw an error because it can't find the Repo host
        repo_url = "docutils.svn.sourceforge.net"
        with self.assertRaises(UnknownVCS):
            self.assertEqual(identify_vcs(repo_url), "svn")

        # make a guess
        self.assertEqual(identify_vcs(repo_url, guess=True), "svn")


if __name__ == '__main__':
    unittest.main()
