from .utils import *


def register_callbacks(app):
    @app.callback(Output('sankey_fig', 'figure'),
                  Input('snapshot-date-select', 'value'),
                  prevent_initial_call=True
                  )
    def update_sankey(selected_date):
        sankey_df, colors_mapping = get_sankey_data(pathing_df, selected_data=selected_date)
        sankey_fig = get_sankey(df=sankey_df, flow_order=['source_location', 'destination_location'],
                                value_col='in_transit',
                                suffix_name='', colors_mapping=colors_mapping)
        return sankey_fig
