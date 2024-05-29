from dashapp.utils.common import *
from dashapp.utils.component_utils import *
from dashapp.utils.config import *

i = InputComponent()
ui = UIComponent()

header_title = ui.header_title(bigTitle='CINDE', smallTitle='CINDE', version=VERSION, img_path='assets/logo.png', img_height=None, theme_toggle=True, secondary_logo='assets/light-theme-logo.png')
header_group = ui.group([header_title], position='apart')

app_layout = html.Div(
                        [
                            ui.appshell_layout(header=header_group, nav_icons=NAV_ICONS, horizontal=False), 
                            # additional_logo,
                            fuc.FefferyKeyPress(
                                    id='fs-key-press',
                                    keys='ctrl.s',
                                    pressedCounts=0
                                ),
                            dcc.Store(id='theme-store', data='light'),
                            dcc.Store(id='theme-empty', data=''),
                        ],
                        style={'height': '100vh'}
                    )