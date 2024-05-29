from .utils import *

card_content = create_tile_content(PAGES)

tiles = [
    AntDTile(icon, heading, description, href)
    # Tile(icon, heading, description, href)

    for icon, heading, description, href in card_content
]

header_container = dmc.Container(
                size="lg",
                # mt=10,
                children=[
                    dmc.Group(
                        [
                            create_title(
                                "Welcome to the CINDE Application!",
                                id="features",
                            ),
                            # dmc.Space(h=10, w=10),
                            # create_head("Predicting safety stock levels for MARS sites across the US."),
                        ],
                        position="center",
                    ),
                ],
            )

tile_container = dmc.Container(
                size="lg",
                px=0,
                py=0,
                my=40,
                children=[
                    dmc.SimpleGrid(
                        cols=3,
                        # mt=100,
                        breakpoints=[
                            {"maxWidth": "xs", "cols": 1},
                            {"maxWidth": "xl", "cols": 1},
                        ],
                        children=tiles,
                        style={'justify-content': 'center'}
                    ),
                ],
            )

layout = html.Div(
    [   
        fac.AntdImage(src='assets/cover_photo.png', preview=False, height=300),
        dmc.Center(html.Div([header_container, tile_container]), style={'padding': '10px'}),
        html.Div(id='page-content', style={'padding': '10px'})
    ],
)