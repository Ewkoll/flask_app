#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Author: ewkoll ideath@operatorwrold.com
Date: 2023-09-18 10:48:34
LastEditors: ewkoll
LastEditTime: 2023-09-18 19:32:17
Description: 
Copyright (c) 2023 by ewkoll email: ideath@operatorwrold.com, All Rights Reserved.
'''
from koca import bex, Result

@bex.route(bex_name="echo")
def echo(request):
    
    return Result().success("success", request)


@bex.route()
def amlRiskListRecall(request):
    
    return Result().success("amlRiskListRecall Finish")
