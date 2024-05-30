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
brand_dropdown = ic.select(id='brand-select', options=brand_options, default_value=brand_list[0], label=brand_label,
                           mode='single',
                           style={'width': '100%'})

comp_list = ['Comp1']
comp_options = [{'label': i, 'value': i} for i in comp_list]
comp_label = fac.AntdText('Comp', style=dict(color='var(--sub_text)'))
comp_dropdown = ic.select(id='comp-select', options=comp_options, default_value='Comp1', label=comp_label,
                          mode='single',
                          style={'width': '100%'})

sfg_list = ['SFG1']
sfg_options = [{'label': i, 'value': i} for i in sfg_list]
sfg_label = fac.AntdText('SFG', style=dict(color='var(--sub_text)'))
sfg_dropdown = ic.select(id='sfg-select', options=brand_options, default_value='SFG1', label=sfg_label, mode='single',
                         style={'width': '100%'})

item_list = ['Item1']
item_options = [{'label': i, 'value': i} for i in item_list]
item_label = fac.AntdText('Item', style=dict(color='var(--sub_text)'))
item_dropdown = ic.select(id='item-select', options=brand_options, default_value='Item1', label=item_label,
                          mode='single',
                          style={'width': '100%'})

zrep_list = ['ZREP1']
zrep_options = [{'label': i, 'value': i} for i in item_list]
zrep_label = fac.AntdText('ZREP', style=dict(color='var(--sub_text)'))
zrep_dropdown = ic.select(id='zrep-select', options=brand_options, default_value='ZREP1', label=zrep_label,
                          mode='single',
                          style={'width': '100%'})

select_group = dmc.SimpleGrid(cols=6,
                              children=[date_dropdown, brand_dropdown, comp_dropdown, sfg_dropdown,
                                        item_dropdown, zrep_dropdown
                                        ],
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
                         config={'displaylogo': False, 'modeBarButtonsToRemove': ['lasso2d', 'pan'],
                                 'displayModeBar': False},
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
