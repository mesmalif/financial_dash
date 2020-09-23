import dash_html_components as html
import dash_core_components as dcc


def Header(app):
    return html.Div([get_header(app), html.Br([]), get_menu()])


def get_header(app):
    header = html.Div(
        [
            html.Div(
                [
                    html.Img(
                        src=app.get_asset_url("dash-financial-logo.png"),
                        className="logo",
                    ),
                    html.A(
                        html.Button("Learn More", id="learn-more-button"),
                        href="https://plot.ly/dash/pricing/",
                    ),
                ],
                className="row",
            ),
            html.Div(
                [
                    html.Div(
                        [html.H5("Calibre Financial Index Fund Investor Shares")],
                        className="seven columns main-title",
                    ),
                    html.Div(
                        [
                            dcc.Link(
                                "Full View",
                                href="/dash-financial-report/full-view",
                                className="full-view-link",
                            )
                        ],
                        className="five columns",
                    ),
                ],
                className="twelve columns",
                style={"padding-left": "0"},
            ),
        ],
        className="row",
    )
    return header


def get_menu():
    menu = html.Div(
        [
            dcc.Link(
                "Overview",
                href="/dash-financial-report/overview",
                className="tab first",
            ),
            dcc.Link(
                "Price Performance",
                href="/dash-financial-report/price-performance",
                className="tab",
            ),
            dcc.Link(
                "Portfolio & Management",
                href="/dash-financial-report/portfolio-management",
                className="tab",
            ),
            dcc.Link(
                "Fees & Minimums", href="/dash-financial-report/fees", className="tab"
            ),
            dcc.Link(
                "Distributions",
                href="/dash-financial-report/distributions",
                className="tab",
            ),
            dcc.Link(
                "News & Reviews",
                href="/dash-financial-report/news-and-reviews",
                className="tab",
            ),
        ],
        className="row all-tabs",
    )
    return menu


def make_dash_table(df):
    """ Return a dash definition of an HTML table for a Pandas dataframe """
    table = []
    for index, row in df.iterrows():
        html_row = []
        for i in range(len(row)):
            html_row.append(html.Td([row[i]]))
        table.append(html.Tr(html_row))
    return table

def SumValuesInList(data_list):
    sum = 0
    for data in data_list:
        sum += data

    return sum

def StoreData(df, x_axis_data):
    store_data = []
    for data in x_axis_data:
        filtered_df = df[df.item == str(data)]
        column_data_list = filtered_df['values'].tolist()
        values_sum = SumValuesInList(column_data_list)
        store_data.append(values_sum)

    return store_data

def CompileData(store_a_data, store_b_data, x_axis_data):
    fig_data = []
    if store_a_data:
        fig_data.append(
            {
                'x':x_axis_data,
                'y':store_a_data,
                'marker': {
                    'color': '#97151c',
                    'line': {
                        'color': 'rgb(255, 255, 255)',
                        "width": 2,
                    }
                },
                'name': 'Store A Data',
                'type': 'bar',
            }
        )

    if store_b_data:
        fig_data.append(
            {
                'x': x_axis_data,
                'y': store_b_data,
                'marker': {
                    'color': '#dddddd',
                    'line': {
                        'color': 'rgb(255, 255, 255)',
                        "width": 2,
                    }
                },
                'name': 'Store B Data',
                'type': 'bar',
            }
        )
    figure = {
        'data': fig_data,
        'layout': {
            'autosize': False,
            'bargap': 0.35,
            'font': {
                "family": "Raleway", "size": 10
            },
            'height': 200,
            'hovermode': "closest",
            'legend': {
                "x": -0.0228945952895,
                "y": -0.189563896463,
                "orientation": "h",
                "yanchor": "top",
            },
            'margin': {
                "r": 0,
                "t": 20,
                "b": 10,
                "l": 10,
            },
            'showlegend': True,
            'title': "",
            'width': 330,
            'xaxis': {
                "autorange": True,
                "range": [-0.5, 4.5],
                "showline": True,
                "title": "",
                "type": "category",
            },
            'yaxis': {
                "autorange": True,
                "range": [0, 22.9789473684],
                "showgrid": True,
                "showline": True,
                "title": "",
                "type": "linear",
                "zeroline": False,
            },

        }
    }

    return figure

def BarGraphFigure(selected_df, selected_option):
    x_axis_data = selected_df.item.unique()
    store_a_data = None
    store_b_data = None
    if len(selected_option) > 1:
        store_a_data = StoreData(selected_df[selected_df.store == 'Store A'], x_axis_data)
        store_b_data = StoreData(selected_df[selected_df.store == 'Store B'], x_axis_data)
    else:
        if selected_option[0] == 'A':
            store_a_data = StoreData(selected_df[selected_df.store == 'Store A'], x_axis_data)
        else:
            store_b_data = StoreData(selected_df[selected_df.store == 'Store B'], x_axis_data)

    figure = CompileData(store_a_data, store_b_data, x_axis_data)

    return figure
