import pandas as pd
import plotly.express as px
import dash
from dash import dash_table
from dash import dcc,html,Input,Output
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import plotly.graph_objects as go

# background color, font style and font family
darkbg = '#181818'  
fontcolor = '#FFFFFF'  
headingfontstyle = 'Helvetica' 
bordercolor1 = 'rgb(17,226,213)'
bordercolor2 = 'rgb(248,249,168)'

bankdf = pd.read_csv(r'C:\Users\Virgil\Downloads\Bank churn\Bank_Churn.csv')

# renaming columns
bankdf.rename(columns = {'CreditScore':'Credit Score','NumOfProducts' : 'Num Of Products',
                       'HasCrCard' : 'Has Cr Card', 'IsActiveMember': 'Is Active Member', 
                       'EstimatedSalary' : 'Estimated Salary'},inplace = True)

# credit rating column
def credit_rating(Score):
  if Score >= 800:
     return 'Excellent'
  elif Score >= 740:
    return 'Very Good'
  elif Score >= 670:
    return 'Good'
  elif Score >= 580:
    return 'Fair'
  else:
    return 'Very Poor'

bankdf['Credit Rating'] = bankdf['Credit Score'].apply(credit_rating)


# Create the Dash app
bank_app = dash.Dash(__name__, use_pages = True)

# App layout
bank_app.layout = html.Div(
    style={
        'backgroundColor': darkbg,  # Changed 'background-color' to 'backgroundColor'
        'textAlign':'center',
        'height': '100vh',
        'width': '100vw',
        'padding': '20px',
        'marginTop': '-15px',  
        'marginLeft': '-10px',
        'margin':'-10px'  # Ensures padding and border are included in total width and height
    },
    children=[  
        
        # Framework for main app
        html.Div(
            "Maven's Bank Customer Churn Analysis", # title
            style={ 
                'textAlign': 'center',
                'color': fontcolor,
                'fontSize': '30px',
                'backgroundColor': darkbg,
                'fontWeight': 'bold',
                'fontFamily': headingfontstyle,
                'marginTop': '15px' , # Changed 'margin-top' to 'marginTop'
                'padding':'20px',
                'border':'10px solid',
                'borderImage':f'linear-gradient(to right,{bordercolor1},{bordercolor2})1',
                'borderRadius':'500px',
                'display':'inline-block'
                
            }
        ),
        html.Div(
            [dcc.Link(page['name'] + " | ", href=page['path'],
                      style = {
                        'color':fontcolor,
                        'fontWeight':'bold',
                        'fontSize':'18px',
                        'fontFamily':headingfontstyle,
                        'backgroundColor':darkbg,
                        'borderRadius':'20px',
                        'margin':'5px',
                        'display':'inline-block',
                        'transition':'0.3s'
                      })
             for page in dash.page_registry.values()
             ],
             style = {
               'position': 'absolute',  # Absolute positioning for top-right alignment
               'top': '20px',  # Distance from the top
               'right': '20px',  # Distance from the right
               'display': 'flex',
               'justifyContent': 'flex-end',  # Align links to the right
               'alignItems': 'center'
               }
        ),
        html.Hr(style={'border': 'none', 'margin': '0', 'padding': '0'}),
        dash.page_container
    ]
)



if __name__ == '__main__':
    bank_app.run(debug=True, port=8055)

