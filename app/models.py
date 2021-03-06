# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from mongoengine import Document, fields, DynamicDocument
from datetime import datetime as dt, timedelta
import logging
logger = logging.getLogger("support")
import sys, os
reload(sys)
sys.setdefaultencoding("utf-8")

# Create your models here.
class RegisterModel(Document):
    device_model = fields.StringField()    
    time_stamp = fields.DateTimeField()
    device_imei1 = fields.StringField()
    device_imei2 = fields.StringField()
    device_brand = fields.StringField()
    diagnose_data = fields.ListField()
