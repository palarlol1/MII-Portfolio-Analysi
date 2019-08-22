import dash
import dash_core_components as dcc
import dash_html_components as html
from services.portfolio_analysis import get_axis, get_pie_graph
import plotly.graph_objs as go

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

dates, value = get_axis()

pos, sizes = get_pie_graph()

app.layout = html.Div(
children = [
    html.H1(children = "MII Portfolio", style = {'text-align':'center'}),
    html.Hr(style={'height':'3px', 'border':'None', 'background-color':'blue', 'width':'85%'}),
    html.Div(children = dcc.Graph(
            id = 'Portfolio-Graph',
            figure = {'data':[{'x':dates, 'y':value, 'type':'line', 'name':'MII Portfolio'}],
                        'layout':{
                            'title':"Portfolio Tracker"
                        }
                    }
            ),
            style = {'width':'80%', 'margin':'auto','boder':'solid 3px blue'}
        )

    ]
)

if __name__ == '__main__':
    app.run_server(debug=True)
