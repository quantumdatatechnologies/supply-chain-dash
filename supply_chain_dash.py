import os

from dashapp.utils.config import ROUTE_PREFIX
from dashapp.utils.common import *
from dashapp.appshell.layout import app_layout
from dashapp.appshell.callbacks import register_appshell_callbacks
from dashapp.pages.pathing.callbacks import register_callbacks as register_pathing_callbacks

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
DSS_APP_DIR = os.path.join(CURRENT_DIR, 'dashapp')
PAGES_DIR = os.path.join(DSS_APP_DIR, 'pages')
ASSETS_DIR = os.path.join(DSS_APP_DIR, 'assets')

app = dash.Dash(__name__, use_pages=True, pages_folder=PAGES_DIR, assets_folder = ASSETS_DIR, routes_pathname_prefix=ROUTE_PREFIX)

app.title = 'CINDE'
app.layout = app_layout
app.config.suppress_callback_exceptions = True

register_appshell_callbacks(app)

if __name__ == '__main__':
    app.run_server(debug=False, port=8052, host='0.0.0.0', threaded=True)