#!/usr/bin/env python3

import sys

def test_major_version():
    assert sys.version_info.major == 3

def test_minor_version():
    assert sys.version_info.minor in {7, 8}