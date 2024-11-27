import os
import sys
import json
import certifi
import pandas as pd
import numpy as np

from dotenv import load_dotenv
load_dotenv()

MONGO_DB_URL = os.getenv("MONGODB_URL")
print(MONGO_DB_URL)