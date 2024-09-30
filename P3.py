from dash import dcc,html
import dash
import pandas as pd
import plotly.express as px

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


# background color, font style and font family
darkbg = '#181818'  
fontcolor = '#FFFFFF'    
headingfontstyle = 'Helvetica'
tablebackground = '#77cea1'


# credit rating classification by gender
cr_rating_gender = bankdf.groupby(['Credit Rating','Gender']).size().reset_index(name = 'count')

cr_rating_gender = cr_rating_gender.sort_values(by = 'Credit Rating',ascending = True)

cr_rating_gender_bar = px.bar(cr_rating_gender, x = 'Credit Rating', y = 'count', 
                              color = 'Gender', barmode = 'group', color_discrete_map = {'Male':'lightgreen',
                                                                                        'Female':'lightblue'})

cr_rating_gender_bar.update_layout(
   title = {
      'text':'Credit Rating by Gender',
      'x':0.5,
      'xanchor': 'center',
      'yanchor':'top'
   },
   xaxis_title = 'Credit Rating',
   yaxis_title = '',
   plot_bgcolor = darkbg,
   paper_bgcolor = darkbg,
   font_color = fontcolor,
   xaxis = dict(showgrid = False),
   yaxis = dict(showgrid = False)
)

# churn rates accross countries
churn_rates_by_country = bankdf[bankdf['Exited'] == 1].groupby('Geography')['Exited'].count() / \
                         bankdf.groupby('Geography')['Exited'].count()*100

churn_rates_by_country = churn_rates_by_country.reset_index(name = 'Exit Rate')
churn_rates_by_country

churn_pie = px.pie(churn_rates_by_country, names = 'Geography', values = 'Exit Rate', hole = 0.5)

churn_pie.update_layout(
  title ={
    'text':'Churn Rates by Country',
    'xanchor':'center',
    'x':0.5,
    'yanchor':'top'
  },
  plot_bgcolor = darkbg,
  paper_bgcolor = darkbg,
  font_color = fontcolor
)

#register page
dash.register_page(__name__)

# layout
layout = html.Div(
    children = [
      html.Div(
        children  = dcc.Graph(figure = churn_pie, id = 'chart3'),
        style = {
          'float':'left',
          'width':'50%',
          'display':'inline-block',
          'margin':'10px 0px 0px 0px',
          'padding':'0'
        }
      ),
            html.Div(
        children  = dcc.Graph(figure = cr_rating_gender_bar, id = 'chart3'),
        style = {
          'float':'right',
          'width':'50%',
          'display':'inline-block',
          'margin':'10px 0px 0px 0px',
          'padding':'0'
        }
      )
    ]
)