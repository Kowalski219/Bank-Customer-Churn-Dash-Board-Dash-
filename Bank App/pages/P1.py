import dash
from dash import dcc,html,dash_table
import pandas as pd
import numpy as np
import plotly.graph_objects as go

# background color, font style and font family
darkbg = '#181818'  
fontcolor = '#FFFFFF'  
headingfontstyle = 'Helvetica'
tablebackground = '#77cea1'

# register the page
dash.register_page(__name__)

# Read the dataset
bankdf = pd.read_csv(r'C:\Users\Virgil\Downloads\Bank churn\Bank_Churn.csv')

# layout
layout = html.Div(
    style={
        'backgroundColor': darkbg,
        'height': '100vh',
        'width': '100vw',
        'display': 'flex',
        'flexDirection': 'row',  # Make elements appear side by side
        'justifyContent': 'flex-start',  # Align items to the left
        'alignItems': 'flex-start',
        'padding': '10px',
    },
    
    children=[

        # Container for the objectives text
        html.Div(
            style={
                'backgroundColor': darkbg,
                'width': '20%',  # Set the width for the text container
                'padding': '10px',
                'marginRight': '20px',  # Add some space between the text and table
                'textAlign': 'left'
            },
            children=[
                html.H1(
                    'Objectives',
                    style={
                        'color': fontcolor,
                        'fontSize': '25px',
                        'fontFamily': headingfontstyle,
                        'fontWeight': 'bold',
                        'textAlign':'center'
                    }
                ),
                html.Div(
                    children=[
                        html.Div(
                            children=[
                                html.Ol([
                                    html.Li(
                                        'What is the average account balance and tenure for different age groups',
                                        style={
                                            'textAlign': 'left',
                                            'backgroundColor': darkbg,
                                            'fontSize': '15px',
                                            'color': fontcolor,
                                            'fontFamily': headingfontstyle
                                        }
                                    ),
                                    html.Br(),
                                    html.Li(
                                        'The distribution of salaries for churned vs. non-churned customers to identify salary ranges where churn is higher.',
                                        style={
                                            'textAlign': 'left',
                                            'color': fontcolor,
                                            'fontFamily': headingfontstyle,
                                            'fontSize': '15px'
                                        }
                                    ),
                                    html.Br(),
                                    html.Li(
                                        'Countries with the highest churn rates',
                                        style = {
                                            'textAlign':'left',
                                            'color':fontcolor,
                                            'fontFamily':headingfontstyle,
                                            'fontSize':'15px'
                                        }
                                    ),

                                    html.Br(),
                                      
                                    html.Li(
                                        'The relationship between credit score and account balance',
                                        style={
                                            'textAlign': 'left',
                                            'color': fontcolor,
                                            'fontFamily': headingfontstyle,
                                            'fontSize': '15px'
                                        }
                                    ),
                                    html.Br(),
                                      
                                    html.Li(
                                        'Churn rates across countries',
                                        style={
                                            'textAlign': 'left',
                                            'color': fontcolor,
                                            'fontFamily': headingfontstyle,
                                            'fontSize': '15px'
                                        }
                                    ),
                                     html.Br(),
                                       html.Li(
                                               'The distribution of tenure for churned vs. non-churned customers',
                                               style = {
                                                       'texxtAlign':'left',
                                                       'color':fontcolor,
                                                       'fontFamily':headingfontstyle,
                                                       'fontSize':'15px'
                                                       }
                                       ),
                                          html.Br(),
                                          html.Li(
                                                  'How product usage impacts churn rates',
                                                  style = {
                                                          'textAlign':'Left',
                                                          'color':fontcolor,
                                                          'fontFamily':headingfontstyle,
                                                          'fontSize':'15px'
                                                  }
                                          )

                                             
                                ])
                            ]
                        )
                    ]
                )
            ]
        ),

        # Container for the heading and data table
        html.Div(
            style={
                'width': '60%',  # Adjust the table container width
                'backgroundColor': darkbg,
                'overflowX': 'hidden',  # Disable horizontal scroll for the table
                'padding': '10px',
                
                # Add marginLeft to move the table container to the right
                'marginLeft': '200px',  # Move the table further right
            },
            children=[
                # Heading section for the data table, directly above the table
                html.H1(
                    'Data Table',
                    style={
                        'color': fontcolor,
                        'fontSize': '20px',
                        'textAlign': 'center',
                        'marginTop': '20px',
                        'fontFamily': headingfontstyle,
                    }
                ),
                html.Div(
                    style={
                        'width': '100%',  # Ensure full width for the table container
                        'backgroundColor': darkbg,
                        'overflowX': 'hidden',  # Disable horizontal scrolling
                        'overflowY': 'hidden',  # No vertical scroll in container
                        'padding': '5px',
                    },
                    children=[
                        dash_table.DataTable(
                            id='table1',
                            columns=[{'name': i, 'id': i} for i in bankdf.columns],
                            data=bankdf.to_dict('records'),
                            page_size=10,
                            filter_action='native',
                            row_selectable='multi',
                            style_table={
                                'overflowY': 'auto',  # Enable vertical scroll for table only
                                'maxHeight': '300px',
                            },
                            style_data={
                                'color': fontcolor,
                                'backgroundColor': darkbg,
                                'fontSize': '10px',
                            },
                            style_header={
                                'backgroundColor': tablebackground,
                                'fontWeight': 'bold',
                                'textAlign': 'center',
                                'fontFamily': headingfontstyle,
                                'padding': '10px',
                                'border': '1px solid white',
                            },
                            style_cell={
                                'textAlign': 'center',
                                'fontFamily': headingfontstyle,
                                'color': fontcolor,
                                'border': '1px solid white',
                            }
                        )
                    ]
                )
            ]
        )
    ]
)

    
