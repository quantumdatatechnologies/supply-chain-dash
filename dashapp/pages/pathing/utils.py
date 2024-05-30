from dashapp.pages.home.utils import *
from dashapp.utils.config import *

material_numbers = ['10218691',
'S7147400',
'10218581',
'10249308',
'10099128',
'S7147100',
'10099132',
'10099141',
'10205935',
'S7147500',
'10172051',
'10278409',
'10099135',
'S7147300',
'10210144',
'10099130',
'10179353',
'S1317100',
'S1317500',
'10266659',
'10231969',
'10250712',
'10201272',
'10280863',
'10280031',
'S4556600']


def get_pathing_df():
    CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
    DATA_DIR = os.path.join(CURRENT_DIR, 'data')
    MATERIAL_MOVEMENT_DIR = os.path.join(DATA_DIR, 'scheduled_intransit.csv')
    pathing_df = pd.read_csv(MATERIAL_MOVEMENT_DIR).dropna(subset=['source_location', 'destination_location'])
    # pathing_df['snapshot_date'] = pd.to_datetime(pathing_df['snapshot_date'])
    return pathing_df

pathing_df = get_pathing_df()

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


import datetime

import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import plotly.colors as pc


def get_sankey_data(pathing_df, selected_data='2024-01-26'):
    pathing_df['snapshot_date'] = pd.to_datetime(pathing_df['snapshot_date'])
    sankey_df = pathing_df[pathing_df['snapshot_date'] == np.datetime64(selected_data)]

    # sankey_df = sankey_df.groupby(['source_location', 'destination_location'])[['in_transit']].sum().reset_index()
    sankey_df = sankey_df[sankey_df['material_number'].isin(material_numbers)].groupby(
        ['material_number', 'source_location', 'destination_location'])[['in_transit']].sum().reset_index()
    sankey_df['proportion'] = sankey_df['in_transit'].clip(upper=np.percentile(sankey_df['in_transit'], 50))
    sankey_df['proportion'] = sankey_df['proportion'] / sankey_df['proportion'].sum()

    # sankey_df = sankey_df.nlargest(30, 'proportion')
    cols_order = ['source_location', 'destination_location']
    color_list = px.colors.qualitative.Plotly
    colors_mapping = {}
    unique_nodes = np.unique(sankey_df[cols_order].values)

    for i, node in enumerate(unique_nodes):
        color_index = i % len(color_list)
        colors_mapping[node] = color_list[color_index]

    # sankey_df = sankey_df.nlargest(50, 'proportion')
    return sankey_df, colors_mapping

def get_sankey(df, flow_order, value_col, suffix_name,
               fig_title='', theme='dark', colors_mapping=dict()):
    # -----------------------------------------#
    # Fill out steps 1-4 to spec your diagram: #
    # -----------------------------------------#

    # Step 1. Specify >=2 categorical columns in flow order
    cols = flow_order

    # Step 2. Specify a column for the flow volume value
    value = value_col
    real_value = 'in_transit'
    value_suffix = " {}".format(suffix_name)  # Specify (if any) a suffix for the value

    # Step 3. Set the plot's title
    title = fig_title

    # Step 4. (Optional) Customize layout, font, and colors
    width, height = 700, 500  # Set plot's width and height
    fontsize = 14  # Set font size of labels
    fontfamily = 'sans-serif'  # Set font family of plot's text

    # ---------------------------------------#
    # Code to create Sankey diagram begins!  #
    # ---------------------------------------#

    s = []  # This will hold the source nodes
    t = []  # This will hold the target nodes
    v = []  # This will hold the flow volumes between the source and target nodes
    v2 = []
    labels = np.unique(df[cols].values)  # Collect all the node labels

    # Get all the links between two nodes in the data and their corresponding values
    for c in range(len(cols) - 1):
        s.extend(df[cols[c]].tolist())
        t.extend(df[cols[c + 1]].tolist())
        v.extend(df[value].tolist())
        v2.extend(df[real_value].tolist())
    links = pd.DataFrame({"source": s, "target": t, "value": v, 'real_value': v2})

    links = links.groupby(["source", "target"], as_index=False).agg({"value": "sum", "real_value": "sum"})

    for l in range(len(labels)):
        links = links.replace({labels[l]: l})  # Replace node labels with the label's index

    print(labels)
    # Define a Plotly Sankey diagram
    fig = go.Figure(
        data=[
            go.Sankey(
                valuesuffix=value_suffix,
                node=dict(label=labels, color=[colors_mapping[labl] for labl in labels]
                          ),
                link=dict(
                    source=links["source"],
                    target=links["target"],
                    value=links["value"],
                    color=[colors_mapping[labels[i]] for i in links['source']],
                    label=links['real_value'],
                ),

            )
        ]
    )

    # fig.add_annotation(
    #     dict(font=dict(color="black", size=12), x=0.1, y=0.85, showarrow=False, text='<b>Search<br>advertising</b>'))
    #
    # fig.add_annotation(
    #     dict(font=dict(color="black", size=12), x=0.1, y=0.5, showarrow=False, text='<b>Search<br>software</b>'))

    # Customize plot based on earlier values
    fig.update_layout(
        title_text='<b>{}<b>'.format(title),
        title_x=0.5,
        font=dict(size=fontsize, family=fontfamily, color='black'),
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        margin=dict(l=0, r=30, t=30, b=30)
        # title={"y": 0.9, "x": 0.5, "xanchor": "center", "yanchor": "top"},  # Centers title
    )

    return fig


def create_filter_dropdown(
        dropdown_id: str,
        data: list,
        value=None,
        multi_state=False,
        clearable_state=False,
        placeholder="No Filters Added...",
        dd_style=None,
        class_name='single_select'
):
    """
    Returns a html.Div element with the header text and a dcc.dropdown for the given data
    """

    dropdown = dcc.Dropdown(
        id=dropdown_id,
        multi=multi_state,
        optionHeight=45,
        clearable=clearable_state,
        placeholder=placeholder,
        className=class_name,
        options=data,
        value=value,
        persistence=False,
        # persistence_type="session",
        style=dd_style,
    )

    return dropdown

# get_sankey(df=sankey_df, flow_order=cols_order, value_col='proportion',
#            suffix_name='', colors_mapping=colors_mapping)
