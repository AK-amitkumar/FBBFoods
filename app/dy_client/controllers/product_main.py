# -*- encoding: utf-8 -*-
# ===================================================
# phone: 10086 
# email: tangdayi520@126.com
# projectname: FBBFoods
# file_name: foods_main 
# author: tangdayi
# data: 2018年04月02日 23时27分
# ===================================================


import logging
import os
import requests
import json
import time
import random
import string
import datetime
import jinja2
from jinja2 import Environment, FileSystemLoader
from odoo import http, SUPERUSER_ID, exceptions
from odoo.http import content_disposition, dispatch_rpc, request

import sys

from tools.ydt.utils import today

path = os.path.realpath(os.path.join(os.path.dirname(__file__), '..', 'templates'))

reload(sys)  # Python2.5 初始化后会删除 sys.setdefaultencoding 这个方法，我们需要重新载入
sys.setdefaultencoding('utf-8')

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
# path = BASE_DIR + "/templates"
templateLoader = FileSystemLoader(searchpath=path)

# templateLoader = jinja2.PackageLoader('app.dy_client', "templates")

env = Environment(loader=templateLoader, autoescape=True)

logger = logging.getLogger(__name__)


class ProductController(http.Controller):
    """
    前端数据接口访问
    商品详情
    """

    @http.route('/fbb/introduction', type='http', auth='public')
    def introduction(self, **post):
        """
        商品详情
        :param post:
        :return:
        """
        data = {}
        template_list = env.get_template("home/introduction.html")
        html = template_list.render(data=data)
        return html

