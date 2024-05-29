import pandas as pd

LOCAL_DEV = True
ROUTE_PREFIX = '/supply-chain-dash/'
VERSION = 'v0.0.1'

PAGES = {
    'Home': {
        'path': '/',
        'name': 'Home',
        'icon': 'antd-home',
    },
    'Supply Chain Pathing': {
        'path': '/supply-chain-pathing',
        'name': 'Supply Chain Pathing',
        'icon': 'antd-catalog',
        'description': 'A historical visualization of the supply chain pathing'
    },
    'Simulation Engine': {
        'path': '/simulation-engine',
        'name': 'Simulation Engine',
        'icon': 'antd-cluster',
        'description': 'Simulate various supply chain scenarios'
    }
}

NAV_ICONS = {k: v['icon'] for k, v in PAGES.items()}