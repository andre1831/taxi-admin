from django.db import models
from django.utils import timezone
import datetime
import pytz
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
import random
import string
from pymongo import MongoClient
from django.conf import settings
