#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Author: ewkoll ideath@operatorworld.com
Date: 2023-09-17 21:43:37
LastEditors: ewkoll
LastEditTime: 2023-09-20 17:15:25
Description: 
Copyright (c) 2023 by ewkoll email: ideath@operatorworld.com, All Rights Reserved.
'''
from dotenv import load_dotenv
load_dotenv()

import os
from koca.server import create_app
from config import Config

app = create_app(Config[os.getenv('FLASK_ENV') or 'production'])

if app and __name__ == '__main__':
    app.run(host=os.getenv('FLASK_RUN_HOST'), port=os.getenv('FLASK_RUN_PORT'), debug=os.getenv('FLASK_DEBUG'))