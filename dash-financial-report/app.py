# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from pages import (
    overview,
    pricePerformance,
    portfolioManagement,
    feesMins,
    distributions,
    newsReviews,
)
from utils import BarGraphFigure

app = dash.Dash(
    __name__, meta_tags=[{"name": "viewport", "content": "width=device-width"}]
)
server = app.server

app.config.suppress_callback_exceptions = True

# Describe the layout/ UI of the app
app.layout = html.Div(
    [dcc.Location(id="url", refresh=False), html.Div(id="page-content")]
)

# Update page
@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def display_page(pathname):
    if pathname == "/dash-financial-report/price-performance":
        return pricePerformance.create_layout(app)
    elif pathname == "/dash-financial-report/portfolio-management":
        return portfolioManagement.create_layout(app)
    elif pathname == "/dash-financial-report/fees":
        return feesMins.create_layout(app)
    elif pathname == "/dash-financial-report/distributions":
        return distributions.create_layout(app)
    elif pathname == "/dash-financial-report/news-and-reviews":
        return newsReviews.create_layout(app)
    elif pathname == "/dash-financial-report/full-view":
        return (
            overview.create_layout(app),
            pricePerformance.create_layout(app),
            portfolioManagement.create_layout(app),
            feesMins.create_layout(app),
            distributions.create_layout(app),
            newsReviews.create_layout(app),
        )
    else:
        return overview.create_layout(app)

#  Callback to update bar graphs on dropdown value change
@app.callback(
    output=Output("graph-1", "figure"),
    inputs=[
        Input("options-dropdown", "value")
    ],
)
def update_bar_chart(selected_option):
    if selected_option == 'A':
        y_data = [
            [
                "21.67",
                "11.26",
                "15.62",
                "8.37",
                "11.11",
            ],
            [
                "21.83",
                "11.41",
                "15.79",
                "8.50",
            ]
        ]
    else:
        y_data = [
            [
                "11.67",
                "5.26",
                "20.62",
                "18.37",
                "9.11",
            ],
            [
                "11.83",
                "21.41",
                "18.79",
                "12.50",
            ]
        ]

    fig = BarGraphFigure(y_data)

    return fig


if __name__ == "__main__":
    app.run_server(debug=True)
