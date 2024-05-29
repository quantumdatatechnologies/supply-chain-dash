## Dash Libraries
import dash
# from dash_extensions.enrich import DashProxy, Serverside, MultiplexerTransform
from dash import html, dcc, clientside_callback, ctx, callback
import dash_cytoscape as cyto
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate
import dash_bootstrap_components as dbc
import dash_mantine_components as dmc
from dash_iconify import DashIconify
import feffery_antd_components as fac
import feffery_utils_components as fuc
import dash_loading_spinners as dls

## Plotly Libraries
import plotly.express as px
import plotly.io as pio
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from plotly.utils import PlotlyJSONEncoder
import cufflinks as cf

## Generic Libraries
from datetime import datetime, date, timedelta
import time
import numpy as np
import pandas as pd
import pickle
import os, sys
import json
import functools
import copy
import ast
import math
import urllib.parse
import uuid
import copy

PAGE_LAYOUT_STYLE = {}

from .config import LOCAL_DEV
if LOCAL_DEV:
    def get_uploads_folder():
        parent_dir = os.path.abspath(os.path.join(os.getcwd(), '.'))
        return  parent_dir + '/app'

# ## QML Libraries
# from .psi_config import LOCAL_DEV

# if not LOCAL_DEV:
#     import os, sys; sys.path.insert(0, os.environ.get('QUANTUM_ML_HOME', default='/home/qdt/quantum_ml')); from quantum_ml.common import *
#     from quantum_ml.utils.timeseries_utils import *
#     from quantum_ml.financial_prepare import *

#     # Connect to the Azure Redis server
#     rds = redis.StrictRedis(host=AZURE_REDIS_HOST, password=AZURE_REDIS_PWD,
#                                  port=AZURE_REDIS_PORT, ssl=True)
# else:
#     # Connect to the local Redis server
#     rds = redis.StrictRedis(host='localhost', port=6379, db=0)

def initialize_log_txt():
    """
    Initialize the log.txt file.
    """
    with open('log.txt', 'w') as f:
        f.write('')
    log = '** Initialized log.txt **'
    update_log(log)

def update_log(text):
    """
    Update the log.txt file with the given text.
    """
    print(text)
    with open('log.txt', 'a') as f:
        f.write(text + '\n')

def initialize_local_cache():
    """
    Initialize the local cache.
    """
    global LOCAL_APP_CACHE
    LOCAL_APP_CACHE = {}
    log = '** Initialized local cache **'
    update_log(log)

initialize_local_cache()
initialize_log_txt()

def redis_cache_callback(func=None, return_key=False, module_name=True, expiration_time=None, logging=True):
    """
    A decorator for caching Dash callback outputs in a Redis store.

    :param func: The callback function to be wrapped.
    :param return_key: If True, the cache key is appended to the output as the last element.
    :param module_name: If True, includes the module name in the cache key.
    :param expiration_time: The expiration time (in seconds) for the cache.
    """
    if func is None:
        return functools.partial(redis_cache_callback, return_key=return_key, expiration_time=expiration_time)

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        if logging:
            t = time.time()
        if module_name:
            key = f"{func.__module__}-{func.__name__}-{str(args)}-{str(kwargs)}"
        else:
            key = f"{func.__name__}-{str(args)}-{str(kwargs)}"
        # data = redis_client.get(key)
        data = LOCAL_APP_CACHE.get(key) 

        if data is None:
            data = func(*args, **kwargs)
            # serialized_data = pickle.dumps(data)
            # redis_client.set(key, serialized_data, ex=expiration_time)
            LOCAL_APP_CACHE[key] = data
            if logging:
                t1 = time.time()
                log = f"Redis cache miss for {key} in {t1 - t} seconds"
                update_log(log)
            if return_key:
                return data + [key]
            else:
                return data

        deserialized_data = data #pickle.loads(data)
        if logging:
            t1 = time.time()
            log = f"Redis cache hit for {key} in {t1 - t} seconds"
            update_log(log)
        if return_key:
            deserialized_data = list(deserialized_data) if isinstance(deserialized_data, tuple) else deserialized_data
            return deserialized_data + [key]
        else:
            return deserialized_data

    return wrapper

def get_redis_data(key):
    # data = redis_client.get(key)
    data = LOCAL_APP_CACHE.get(key)
    if data is None:
        return None
    return data #pickle.loads(data)