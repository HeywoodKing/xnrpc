#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
test
"""
__author__ = "Xiong Neng"

import unittest

if __name__ == '__main__':
    loader = unittest.TestLoader()
    start_dir = './test'
    suite = loader.discover(start_dir)
    runner = unittest.TextTestRunner()
    runner.run(suite)

