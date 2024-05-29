from dashapp.pages.home.utils import *
from dashapp.utils.config import *

def AntDTileCatalog(category, heading, description, href, star_color=None):
    return fac.AntdCard(
        headStyle={"display": "none"},
        title=None,
        hoverable=True,
        children=[
            dmc.SimpleGrid(
                cols=1,
                spacing=0,
                children=[
                    dmc.Group([
                        fac.AntdTag(content=category, color=categories_mapping_color[category]),
                        dmc.ActionIcon(DashIconify(icon="ph:star-fill", width=20),
                                       n_clicks=0,
                                       variant="subtle",
                                       color=star_color[heading],
                                       id={'type': 'card-star',
                                           'index': heading}
                                       ),
                    ],
                        position='apart',
                        style={'margin-bottom': '20px'}
                    ),

                    dcc.Link([
                        fac.AntdTitle(heading, level=4),
                        dmc.Divider(style={"width": "50px"}, size="sm", my=10),
                        fac.AntdText(description, type="secondary")], href=url(href),
                    )  # target="_blank")
                ]
            ),
        ],
        className='antd-tile',
        style={'height': '100%',
               'width': '350px',
               'align': 'center',
               'position': 'center',
               'flexDirection': 'column', }
    )


def create_tile_content_catalog(content: dict):
    card_content = [(v['category'], v['name'], v['description'], v['path']) for k, v in content.items() if
                    'description' in v]
    return card_content


def return_app_cards_list(app_dic, stored_color):
    card_content = create_tile_content_catalog(app_dic)

    tiles = [
        AntDTileCatalog(category, heading, description, href, star_color=stored_color)
        # Tile(icon, heading, description, href)

        for category, heading, description, href in card_content
    ]

    return tiles


def search_not_found(text):
    message = html.Div([  # DashIconify(icon="nonicons:not-found-16"),
        text],
        style={'padding-top': '20px', 'font-size': 'larger'}
    )
    return message
