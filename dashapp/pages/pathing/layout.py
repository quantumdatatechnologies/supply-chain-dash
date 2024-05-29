from .utils import *

ui = UIComponent()
ic = InputComponent()

date_list = pathing_df['snapshot_date'].unique().tolist()
date_options = [{'label': i, 'value': i} for i in date_list]
date_label = fac.AntdText('Snapshot Date', style=dict(color='var(--sub_text)'))
date_dropdown = ic.select(id='snapshot-date-select', options=date_options, default_value='2024-01-26', label=date_label,
                          mode='single',
                          style={'width': '100%'})

brand_list = ['Combos']
brand_options = [{'label': i, 'value': i} for i in brand_list]
brand_label = fac.AntdText('Brand', style=dict(color='var(--sub_text)'))
brand_dropdown = ic.select(id='brand-select', options=brand_options, default_value=brand_list[0], label=brand_label, mode='single',
                           style={'width': '100%'})

select_group = dmc.SimpleGrid(cols=4,
                              children=[date_dropdown, brand_dropdown],
                              style={'margin-bottom': '20px'})

filter_content = dmc.SimpleGrid(
    id='r-filter-group',
    cols=1,
    children=[
        select_group,
    ],
    spacing=10,
    verticalSpacing=10,
    style={'width': '100%'}
)

filter_card = ui.simple_antd_card(filter_content, className='filter-card')

sankey_df, colors_mapping = get_sankey_data(pathing_df)

sankey_fig = get_sankey(df=sankey_df, flow_order=['source_location', 'destination_location'], value_col='in_transit',
           suffix_name='', colors_mapping=colors_mapping)

sankey_graph = dcc.Graph(figure=sankey_fig,
                  config={'displaylogo': False, 'modeBarButtonsToRemove': ['lasso2d', 'pan'], 'displayModeBar': False},
                  id='sankey_fig',
                  style=dict(width='100%', height=''))

chart_grid = dmc.Grid(
    children=[
        dmc.Col([sankey_graph], span=12),
    ],
    gutter=15
)

card_content = dmc.SimpleGrid(
    cols=1,
    children=[
        filter_card,
        chart_grid,
    ],
    style={'width': '100%', 'padding': '5px'}
)

layout = html.Div(
    [
        fac.AntdText("Materials Movement", className='title'),
        dmc.Space(h=20),
        card_content,
    ],
    style=PAGE_LAYOUT_STYLE
)
