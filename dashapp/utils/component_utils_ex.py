from .common import *
from .config import ROUTE_PREFIX
# from .component_utils_old import *

## class for antd input components (ex.: select, multiselect, segmented, etc.)
class InputComponent():
    def __init__(self):
        pass

    def _add_label(self, label, component, type='stack'):
        filter_label_style = {'margin': '0px', 
                              'padding': '0px', 
                              'padding-left': '5px', 
                              'font-size': '12px'}
        label = "\xa0" if label == '' else label
        if type == 'stack':
            return dmc.Stack([fac.AntdText(label, style=filter_label_style, type='secondary'), component], spacing='2.5px')
        elif type == 'group':
            return dmc.Group([fac.AntdText(label, style=filter_label_style, type='secondary'), component], position='apart', style={'width': '100%'})
    
    def select(self, id, default_value, options, optionFilterProp = 'label', allowClear = True, mode = None, style = {}, label=None, placeholder='Select a value', **kwargs):
        component = fac.AntdSelect(
            id = id,
            options = options,
            defaultValue = default_value,
            style = style,
            optionFilterProp = optionFilterProp,
            optionFilterMode='case-insensitive',
            allowClear = allowClear,
            mode = mode,
            placeholder = placeholder,
            locale='en-us',
            maxTagCount = 'responsive',
            **kwargs
        )

        if label:
            component = self._add_label(label, component)
        
        return component
    
    def treeselect(self, id, default_value, options, label=None, optionFilterProp = 'value', allowClear = True, style = {}, multiple = True, treeCheckable = True, showCheckedStrategy = 'show-parent', maxTagCount = 'responsive', placeholder='Select a value', **kwargs):
        # validate options format to see if it matches the format required by AntdTreeSelect
        component = fac.AntdTreeSelect(
            id = id,
            treeData = options,
            defaultValue = default_value,
            style = style,
            treeNodeFilterProp = optionFilterProp,
            treeNodeFilterMode = 'case-insensitive',
            allowClear = allowClear,
            multiple = multiple,
            treeCheckable = treeCheckable,
            showCheckedStrategy = showCheckedStrategy,
            maxTagCount = maxTagCount,
            placeholder = placeholder,
            locale='en-us',
            autoClearSearchValue=False,
            **kwargs
        )

        if label:
            component = self._add_label(label, component)

        return component
    
    def segmented(self, id, default_value, options, label=None, style = {}, **kwargs):
        component = fac.AntdSegmented(
            id = id,
            options = options,
            defaultValue = default_value,
            style = style,
            **kwargs
        )

        if label:
            component = self._add_label(label, component)
        
        return component

    def number(self, id, default_value, min, max, step, label=None, style = {}, **kwargs):
        component = fac.AntdInputNumber(
            id = id,
            defaultValue = default_value,
            min = min,
            max = max,
            step = step,
            style = style,
            **kwargs
        )

        if label:
            component = self._add_label(label, component)
        
        return component

    def text(self, id, default_value, label=None, placeholder=None, style = {}, addonAfter=None, addonBefore=None, **kwargs):
        component = fac.AntdInput(
            placeholder=placeholder,
            id = id,
            defaultValue = default_value,
            style = style,
            addonAfter = addonAfter,
            addonBefore = addonBefore,
            **kwargs
        )

        if label:
            component = self._add_label(label, component)
        
        return component

    def date():
        pass

    def daterange():
        pass

    def switch(self, id, default_value, label=None, style = {}, size='default', **kwargs):
        component = fac.AntdSwitch(
                id = id,
                checked=default_value,
                style=style,
                size=size,
                **kwargs
            )
        
        if label:
            component = self._add_label(label, component, type='group')

        return component

class TextComponent():
    def __init__(self):
        pass

class LayoutComponent():
    def __init__(self):
        pass

class TableComponent():
    def __init__(self):
        pass

class ChartComponent():
    def __init__(self):
        pass

    def graph(self, graph_id, fig=None, style={"width":"100%", "height":"100%"}, animate=False, className='', circle=True, responsive=True, loading=False):
        if 'width' not in style.keys():
            style['width'] = '100%'
        if 'height' not in style.keys():
            style['height'] = '100%'
        # style={"width":"100%", "height":"100%"}
        if fig != None:
            if animate:
                g = dcc.Graph(id=graph_id, figure=fig, style=style, animate=True,
                        animation_options={'frame': { 'redraw': True}}, className=className, responsive=responsive) 
            else:
                g = dcc.Graph(id=graph_id, figure=fig, style=style, className=className, responsive=responsive) 
        else:
            if animate:
                g = dcc.Graph(id=graph_id, style=style, animate=True,
                        animation_options={'frame': { 'redraw': True}}, className=className, responsive=responsive, figure={'data': [], 'layout': {}})
            else:
                g = dcc.Graph(id=graph_id, style=style, className=className, responsive=responsive, figure={'data': [], 'layout': {}})
        if loading:
            return dmc.Skeleton(children=[g], circle=circle, animate=True, visible=False, style={'height': '100%', 'width':'100%'})
        else:
            return g

class UIComponent():
    def __init__(self):
        pass

    def button(self, title, icon=None, **kwargs):
        if icon:
            return fac.AntdButton(title, icon=fac.AntdIcon(
                    icon=icon,
                    **kwargs
                ))
        else:
            return fac.AntdButton(title, **kwargs)

    def card(self, children, header=None, style={}, shadow=True, overflow=False):
        bodyStyle = {'margin': '0px', 'padding': '0px', 'margin-left': '2px', 'margin-right': '2px'}
        if overflow:
            bodyStyle.update({'overflow': 'scroll'})
        headStyle = {'padding': '0px', 'margin': '0px', 'min-height': '5px', 'box-sizing': 'content-box'}
        style.update({'border-radius': '3px', 'background-color': '#fffff9'})
        if shadow:
            style.update({'box-shadow': 'rgba(149, 157, 165, 0.2) 0px 8px 24px'})
        if header:
            card = fac.AntdCard(children, bordered=False, style=style, title=header, bodyStyle=bodyStyle, headStyle=headStyle)

        else:
            card = fac.AntdCard(children, bordered=False, style=style, bodyStyle=bodyStyle, headStyle={
                        'display': 'none'
                    })
            
        return card

    def modal():
        pass

    def drawer():
        pass

    def accordion():
        pass

    def tabs():
        pass

    def popover(self, target, content, placement='bottom', mouseLeaveDelay=0.1, trigger = 'click', **kwargs):
        return fac.AntdPopover(
            target,
            content = content,
            placement = placement,
            mouseLeaveDelay = mouseLeaveDelay,
            trigger = trigger,
            popupContainer = 'parent',
            # overlayInnerStyle = {'display': 'inline-block'},
            # overlayStyle = {'display': 'inline-block'},
            # style = {'display': 'inline-block'},
            **kwargs
        )
    
    def stack(self, children, spacing='2.5px', align='center', justify='center', style={}):
        return dmc.Stack(children, spacing=spacing, align=align, justify=justify, style=style)
    
    def group(self, children, position='apart', style={}):
        return dmc.Group(children, position=position, style=style)
    
    def header_title(self, bigTitle=None, smallTitle=None, version=None, logo_img=None):
        title_group = []

        if (bigTitle != None) & (smallTitle != None):
            title_text = html.Div(
                [
                    dmc.MediaQuery(
                        dmc.Title(bigTitle, order=2, style={'color':dmc.theme.DEFAULT_COLORS["blue"][6]}),
                        smallerThan="md",
                        styles={"display": "none"},
                    ),
                    dmc.MediaQuery(
                        dmc.Title(smallTitle, order=2, style={'color':dmc.theme.DEFAULT_COLORS["blue"][6]}),
                        largerThan="md",
                        styles={"display": "none"},
                    ),
                ],
                style={'padding': '5px', "textDecoration": "none", 'margin':'auto'},
                )
            
            title_group.append(title_text)

        if logo_img:
            # title_group.append(fac.AntdImage(src=logo_img, height=50))
            title_group.append(html.Img(src=logo_img, height=50, style={'padding': '5px'}))

        if version:
            title_group.append(dmc.Badge(version, size='lg', color='gray'))

        title = self.group(title_group, position='left')
        return title
    
    def appshell_layout(self, header, nav_icons=None, default_page='Home', horizontal=True):
        if nav_icons:
            if horizontal:
                menu = fac.AntdFooter(
                                        fac.AntdMenu(
                                            id='menu',
                                            theme='light',
                                            menuItems=[
                                                {
                                                    'component': 'Item',
                                                    'props': {
                                                        'key': name.lower(),
                                                        'title': name,
                                                        'icon': icon,
                                                        'href': name.lower().replace(' ', '-') if idx > 0 else ROUTE_PREFIX
                                                    }
                                                }
                                                for idx, name, icon in zip(range(len(nav_icons)), nav_icons.keys(), nav_icons.values())
                                            ],
                                            popupContainer='parent',
                                            mode='horizontal',
                                            style={
                                                'width': '100%',
                                                'height': '70px',
                                                'overflow': 'hidden auto',
                                                # 'align': 'center',
                                                # 'position': 'absolute',
                                                # 'text-align': 'center',
                                                'padding': '0px',
                                                'margin': '0px',
                                                # 'border-radius': '15px',
                                                # 'background-color': 'red',
                                            }
                                        ),
                                        style = {
                                            'position': 'fixed',
                                            'bottom': '0px',
                                            'left': '50%',
                                            'right': '25%',
                                            'margin-left': '-41.25%',
                                            'width': '82.5%',
                                            # 'height': '70px',
                                            'background-color': 'rgba(0,0,0,0)',
                                            'padding': '0px',
                                            'margin-bottom': '15px',
                                            # 'border-radius': '15px',
                                        }
                                    )
            else:
                menu = fac.AntdSider(
                                        fac.AntdMenu(
                                            id='menu',
                                            theme='light',
                                            menuItems=[
                                                {
                                                    'component': 'Item',
                                                    'props': {
                                                        'key': name.lower(),
                                                        'title': name,
                                                        'icon': icon,
                                                        'href': name.lower().replace(' ', '-') if idx > 0 else ROUTE_PREFIX
                                                    }
                                                }
                                                for idx, name, icon in zip(range(len(nav_icons)), nav_icons.keys(), nav_icons.values())
                                            ],
                                            popupContainer='parent',
                                            mode='inline',
                                            style={
                                                'width': '100%',
                                                'height': '100%',
                                                'overflow': 'hidden auto',
                                                # 'align': 'center',
                                                # 'position': 'absolute',
                                                # 'text-align': 'center',
                                                'padding': '0px',
                                                'margin': '0px',
                                                # 'border-radius': '15px',
                                                # 'background-color': 'red',
                                            }
                                        ),
                                        style = {
                                            'position': 'fixed',
                                            'left': '0px',
                                            'top': '0px',
                                            'bottom': '0px',
                                            'width': '100%',
                                            'background-color': 'rgba(0,0,0,0)',
                                            'padding': '0px',
                                            'margin-bottom': '15px',
                                            # 'border-radius': '15px',
                                        }
                                    )
        else:
            menu = html.Div(id='menu', style={'display': 'none'})

        layout = fuc.FefferyTopProgress(html.Div([
                dcc.Location(id='url', refresh=False),
                fuc.FefferyStyle(
                        rawStyle='''
                    .sider-demo .ant-layout-sider-trigger {
                    position: absolute !important;
                    }
                    '''
                ),

                html.Div(
                    [   fac.AntdLayout(
                            fac.AntdContent(
                                    header,
                                    style={'margin': '10px'}
                                ),
                            id = 'header',
                            style={'min-height': '70px'}
                        ),
                        fac.AntdLayout(
                            [   
                                fac.AntdContent(
                                    [dash.page_container],
                                    style={'height': '100%',
                                           'background': 'rgba(0,0,0,0)'}
                                ),
                                
                            ],
                            style={
                                'height': 'auto',
                                # 'overflow': 'scroll'
                            }
                        ),
                        menu
                    ],
                    id='page',
                    className='sider-demo',
                    style={
                        'height': '100%',
                        # 'border': '1px solid rgb(241, 241, 241)',
                    }
                )
            ],
            style={
                'height': '100%',
                'width': '100%',
                'min-height': '100vh',
                # 'background': 'black',
            }))
        
        return layout


