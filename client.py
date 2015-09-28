#!/usr/bin/env python
# -*- coding: utf-8 -*-
################################################################################
#
# Copyright (c) 2015 .com, Inc. All Rights Reserved
#
################################################################################
"""
description:
author: liufengxu
date: 2015-09-28 23:18:31
last modified: 2015-09-28 23:25:46
version:
"""

import logging
from xmlrpclib import ServerProxy
import sys


def main():
    logging.basicConfig(level=logging.INFO, format="%(levelname)s: "
                        "%(asctime)s: %(filename)s: %(lineno)d * "
                        "%(thread)d %(message)s",
                        datefmt="%Y-%m-%d %H:%M:%S")
    # s = ServerProxy("http://127.0.0.1:8080")
    s = ServerProxy("http://101.200.198.128:8888")
    x = int(sys.argv[1])
    y = int(sys.argv[2])
    print s.add(x, y)

if __name__ == '__main__':
    main()
