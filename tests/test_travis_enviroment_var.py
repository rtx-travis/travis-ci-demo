#!/usr/bin/env python3

import sys
import os

pathlist = os.path.realpath(__file__).split(os.path.sep)
travis_index = pathlist.index("travis-ci-demo")
env_var_txt_filepath = os.path.sep.join([*pathlist[:(travis_index + 1)], "env_var.txt"])

def test_env_var_txt():
    with open(env_var_txt_filepath,"r") as fid:
        env_var = fid.readline().strip()
    assert env_var == "asdf"