from dashapp.utils.common import *
from dashapp.utils.component_utils import *
from dashapp.utils.config import *

def register_appshell_callbacks(app):
    app.clientside_callback(
        """
        function(nClicks, currentTheme) {
            if (nClicks === undefined || nClicks === 0) {
                const initialTheme = currentTheme || 'light';
                const initialIconClass = initialTheme === 'dark' ? 'bi bi-brightness-high' : 'bi bi-moon';
                document.documentElement.setAttribute('data-theme', initialTheme);
                return [initialTheme, initialIconClass];
            }
            const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
            const newIconClass = newTheme === 'dark' ? 'bi bi-brightness-high' : 'bi bi-moon';
            document.documentElement.setAttribute('data-theme', newTheme);
            return [newTheme, newIconClass];
        }
        """,
        [Output("theme-store", "data"), Output('theme-icon', 'className')],
        Input('theme-button', 'nClicks'),
        State('theme-store', 'data')
    )

    app.clientside_callback(
        """
        function updateFullscreen(pressedCounts) {
            if (pressedCounts % 2 === 1) {
                return [
                    {'display': 'none'},
                    {'display': 'none'},
                    {'display': 'none'},
                    {'height': '100vh', 'border': '1px solid rgb(241, 241, 241)'}
                ];
            } else {
                return [
                    {'position': 'sticky', 'top': 0, 'zIndex': 1, 'width': '100%'},
                    {'overflow': 'hidden auto'},
                    {},
                    {'height': '100%', 'zIndex': 0}
                ];
            }
        }
        """,
        [
            Output('header', 'style'),
            Output('menu', 'style'),
            Output('sider', 'style'),
            Output('page', 'style')
        ],
        [Input('fs-key-press', 'pressedCounts')]
    )

    @app.callback(
        Output('menu', 'currentKey'),
        Input('url', 'pathname'),
        State('menu', 'currentKey')
    )

    def update_menu(pathname, current_key):
        root, path = pathname.split('/')[1], pathname.split('/')[2]
        key = 'home' if path == '' else path.replace('-', ' ')
        if key != current_key:
            return key
        else:
            raise PreventUpdate
