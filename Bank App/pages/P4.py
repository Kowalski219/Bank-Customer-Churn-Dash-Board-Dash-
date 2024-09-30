import pandas as pd
from dash import dcc,html
import dash
import plotly.express as px
import plotly.graph_objects as go


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

# credit score and balance of customers
crs_bal = px.scatter(bankdf, x = 'Credit Score', y = 'Balance', color = 'Exited')

# tenure for churned and non churned customers
tenure_churn = bankdf[bankdf['Exited'] == 1]['Tenure']
tenure_churn = tenure_churn.rename('Tenure_Churn')

tenure_not_churn = bankdf[bankdf['Exited'] == 0]['Tenure']
tenure_not_churn = tenure_not_churn.rename('Tenure_Not_Churn')

# histogram for churned customers
tenure_churn_trace = go.Histogram(
    x= tenure_churn,
    opacity=0.6,
    name='Teenure of Churned Customers',
    marker=dict(color='red'),
    nbinsx=30
)

# histogram for non-churned customers
tenure_not_churn_trace = go.Histogram(
    x=tenure_not_churn,
    opacity=0.3,
    name='Tenure of Non-Churned Customers',
    marker=dict(color='green'),
    nbinsx=30
)

# layout
layout = go.Layout(
    title='Tenure Distribution of Churned vs. Non-Churned Customers',
    xaxis=dict(title='Tenure'),
    yaxis=dict(title='Count'),
    barmode='overlay'  # to Overlay the two histograms
)

# background color, font style and font family
darkbg = '#181818'  
fontcolor = '#FFFFFF'    
headingfontstyle = 'Helvetica'
tablebackground = '#77cea1'


# Create the figure
tenure_churn = go.Figure(data=[tenure_not_churn_trace, tenure_churn_trace], layout=layout)

tenure_churn.update_layout (
  xaxis = dict(showgrid = False),
  yaxis = dict(showgrid = False),
  font_color = fontcolor,
  paper_bgcolor = darkbg,
  plot_bgcolor = darkbg
)

crs_bal.update_layout(
  title = {'text':'Relationship between current bank balance & credit score',
           'x':0.5,
           'xanchor':'center'},
           paper_bgcolor = darkbg,
           plot_bgcolor = darkbg,
           font_color = fontcolor,
           xaxis = dict(showgrid = False),
           yaxis = dict(showgrid = False)
)

# register page
dash.register_page(__name__)

# layout
layout = html.Div(
  children = [
    html.Div(
      children = dcc.Graph(figure = crs_bal, id = 'chart4'),
      style = {
        'float':'left',
        'width':'50%',
        'display':'inline-block',
        'padding':'0',
        'margin':'10px 0 0 0'


      }
    ),
    html.Div(
      children = dcc.Graph(figure = tenure_churn, id = 'chart5'),
      style = {
        'float':'right',
        'width':'50%',
        'margin':'10px 0 0 0',
        'padding':'0',
        'display':'inline-block'
      }
    )
  ]
)
