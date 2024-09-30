import dash 
from dash import dcc,html
import pandas as pd
import plotly.express as px


# background color, font style and font family
darkbg = '#181818'  
fontcolor = '#FFFFFF'    
headingfontstyle = 'Helvetica'
tablebackground = '#77cea1'


bankdf = pd.read_csv(r'C:\Users\Virgil\Downloads\Bank churn\Bank_Churn.csv')


# renaming columns
bankdf.rename(columns = {'CreditScore':'Credit Score','NumOfProducts' : 'Num Of Products',
                       'HasCrCard' : 'Has Cr Card', 'IsActiveMember': 'Is Active Member', 
                       'EstimatedSalary' : 'Estimated Salary'},inplace = True)

# product usage vs churn rate
pro_churn = bankdf[bankdf['Exited']== 1].groupby('Num Of Products')['Exited'].count().reset_index(name = 'Num Exited')

pro_churn_bar = px.bar(pro_churn, x = 'Num Of Products', y = 'Num Exited',color_discrete_sequence=['lightgreen'])
pro_churn_bar.update_layout(
    title = {'text': 'Impact of churn rate by number of products used',
             'x' : 0.5,
             'xanchor':'center'},
             xaxis_title = 'Number of Products',
             yaxis_title = 'Churn',
             paper_bgcolor = darkbg,
             plot_bgcolor = darkbg,
             xaxis = dict(showgrid = False),
             yaxis = dict(showgrid = False),
             font_color = fontcolor
)

# register page
dash.register_page(__name__)

# layout
layout = html.Div(
    children = [
        html.Div (
            children = dcc.Graph(figure = pro_churn_bar, id = 'chart5'),
            style = {
                'color':fontcolor,
                'margin':'10px 0 0 0'
            }
        )
    ]
)