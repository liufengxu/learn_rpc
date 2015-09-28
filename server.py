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
date: 2015-09-28 23:17:18
last modified: 2015-09-28 23:47:28
version:
"""

import logging
from SimpleXMLRPCServer import SimpleXMLRPCServer


def add(x, y):
    return x + y


def main():
    logging.basicConfig(level=logging.INFO, format="%(levelname)s: "
                        "%(asctime)s: %(filename)s: %(lineno)d * "
                        "%(thread)d %(message)s",
                        datefmt="%Y-%m-%d %H:%M:%S")
    s = SimpleXMLRPCServer(('101.200.198.128', 8888))
    s.register_function(add)
    s.serve_forever()

if __name__ == '__main__':
    main()
