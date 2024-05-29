from dashapp.utils.config import *
from dashapp.utils.common import *
from dashapp.utils.component_utils import *

def url(path):
    return (ROUTE_PREFIX + path).replace('//', '/')

def create_title(text, id=None):
    return dmc.Title(order=1, id=id, children=text, style={"marginTop": "2rem"}, align="center")

def create_head(text):
    return dmc.Text(align="center", children=text, style={"marginTop": "1rem"})

def Tile(icon, heading, description, href):
    return dcc.Link(dmc.Card(
                radius="md",
                p="xl",
                withBorder=True,
                m=5,
                children=[
                    dmc.Group([
                            DashIconify(
                                icon=icon, height=20, color=dmc.theme.DEFAULT_COLORS["indigo"][5]
                            ),
                            dmc.ThemeIcon(
                                DashIconify(icon="akar-icons:arrow-up-right", width=20),
                                size="sm",
                                variant="light",
                                color='blue'
                            ),
                        ], position='apart', align='apart'),
                    dmc.Text(heading, size="lg", mt="md"),
                    dmc.Divider(
                        style={"width": 50},
                        size="sm",
                        color=dmc.theme.DEFAULT_COLORS["indigo"][5],
                        my=10,
                    ),
                    dmc.Text(description, size="sm", color="dimmed", mt="sm"),
                ],
                style={'height': '100%'}
            ), href=url(href))

def AntDTile(icon, heading, description, href):
    return dcc.Link(
        fac.AntdCard(
                headStyle={"display": "none"},
                title=None,
                hoverable=True,
                children=[
                    dmc.SimpleGrid(
                        cols=1,
                        spacing=0,
                        children = [
                            fac.AntdIcon(
                                icon=icon,
                                style = {"fontSize": "40px"}
                            ),
                            fac.AntdTitle(heading, level=4),
                            dmc.Divider(style={"width": "50px"}, size="sm", my=10),
                            fac.AntdText(description, type="secondary")
                        ]
                    ),
                ],
                className='antd-tile',
                style={'height': '100%',
                        'width': '350px',
                        'align': 'center',
                        'position': 'center',
                        'flexDirection': 'column',}
            ), href=url(href),)
                #target="_blank")

def create_tile_content(content: dict):
    card_content = [(v['icon'], v['name'], v['description'], v['path']) for k,v in content.items() if 'description' in v]
    return card_content