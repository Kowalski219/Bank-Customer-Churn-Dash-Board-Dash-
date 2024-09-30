import plotly.express as px
import pandas as pd 
import dash
from dash import dcc,html
import numpy as np
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

# background color, font style and font family
darkbg = '#181818'  
fontcolor = '#FFFFFF'    
headingfontstyle = 'Helvetica'
tablebackground = '#77cea1'

# credit rating classification by gender
cr_rating_gender = bankdf.groupby(['Credit Rating','Gender']).size().reset_index(name = 'count')



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


bankdf['Credit Rating'] = bankdf['Credit Score'].apply(credit_rating)

# Reordering the columns
columns_order = [
    'CustomerId', 'Surname', 'Credit Score', 'Credit Rating', 'Geography',
    'Gender', 'Age', 'Tenure', 'Balance', 'Num Of Products', 'Has Cr Card',
    'Is Active Member', 'Estimated Salary', 'Exited'
]


# avg credit score
avg_cr_score = round(bankdf['Credit Score'].mean())
print('The average credit score is', avg_cr_score)

# total male
total_male = bankdf[bankdf['Gender'] == 'Male']['Gender'].count()

# total female
total_female = bankdf[bankdf['Gender'] == 'Female']['Gender'].count()

# how many men have are above the avg credit score
above_avg_cr_score_male = bankdf[bankdf['Gender']=='Male'][bankdf['Credit Score'] > avg_cr_score].shape[0]

# how many female have are above the avg credit score
above_avg_cr_score_female = bankdf[bankdf['Gender']=='Female'][bankdf['Credit Score'] > avg_cr_score].shape[0]


# perc above avg cr score male
perc_above_avg_cr_score_male = round((above_avg_cr_score_male / total_male) * 100)


# perc above avg cr score female
perc_above_avg_cr_score_female =round ((above_avg_cr_score_female / total_female) * 100)

# avg age
avg_age = round(bankdf['Age'].mean())
print('The average age is: ', avg_age)




# Maximum age
max_age = bankdf['Age'].max()

# Minimum age
min_age = bankdf['Age'].min()

# Determine the number of intervals
n = bankdf['Age'].count()
k = int(np.log2(n)) + 1


# Age range
age_range = max_age - min_age
print('The age range is:', age_range)

# Interval width
interval_width = age_range / k

# Create intervals
intervals = pd.interval_range(start=min_age, freq=interval_width, closed='left', periods=k)

# Assign data to intervals
bankdf['Age Group'] = pd.cut(bankdf['Age'], bins=intervals, include_lowest=True)

# Format intervals as strings
intervals_list = [f"{round(interval.left)}-{round(interval.right)}" for interval in intervals]

# Map intervals to their formatted string representations
interval_mapping = {interval: f"{round(interval.left)}-{round(interval.right)}" for interval in intervals}
bankdf['Age Group'] = bankdf['Age Group'].map(interval_mapping)

print("Formatted Intervals:")
for interval in intervals_list:
    print(interval)

# average balance for different age groups
avg_bank_bal_per_age_group = bankdf.groupby('Age Group')[['Balance','Tenure']].mean().reset_index()
avg_bank_bal_per_age_group ['Tenure'] = avg_bank_bal_per_age_group ['Tenure'].round()

# line chart for avg bank balance per age group
avg_bal_age = px.line(avg_bank_bal_per_age_group, x = 'Age Group', y = 'Balance', color = 'Tenure')

# updating the chart to remove grid lines 
avg_bal_age.update_layout(
   title = {
      'text': 'Avg Bank Balance For Each Age Group',
      'xanchor': 'center',
      'yanchor':'top',
      'x':0.5
   },
   xaxis = dict(showgrid = False),
   yaxis = dict(showgrid = False),
   plot_bgcolor = darkbg,
   paper_bgcolor = darkbg,
   font_color = fontcolor
)

red = '#FF4533'
lightgreen = '#A0FEAD'

# salary for churned and non churned customers
salary_churn = bankdf[bankdf['Exited'] == 1]['Estimated Salary']
salary_not_churn = bankdf[bankdf['Exited'] == 0]['Estimated Salary']


# histogram for churned customers
churn_trace = go.Histogram(
    x=salary_churn,
    opacity=0.6,
    name='Churned Customers',
    marker=dict(color= red),
    nbinsx=30
)

# histogram for non-churned customers
non_churn_trace = go.Histogram(
    x=salary_not_churn,
    opacity=0.3,
    name='Non-Churned Customers',
    marker=dict(color=lightgreen),
    nbinsx=30
)

# layout
layout = go.Layout(
    title='Salary Distribution of Churned vs. Non-Churned Customers',
    xaxis=dict(title='Estimated Salary'),
    yaxis=dict(title='Count'),
    barmode='overlay'  # to Overlay the two histograms
)

# Create the figure
chun_non_chun = go.Figure(data=[churn_trace, non_churn_trace], layout=layout)

chun_non_chun.update_layout(
   plot_bgcolor = darkbg,
   paper_bgcolor = darkbg,
   font_color = fontcolor,
   xaxis = dict(showgrid = False),
   yaxis = dict(showgrid = False)
)





# register page
dash.register_page(__name__)

# pahe 1 layout
layout = html.Div(
    children = [
        # Card visuals container
        html.Div(
            style = {
                'display':'flex',
                'flexDirection':'row',
                'alignItems':'center',
                'justifyContent':'flex-start',
                'width':'100%'
            },
            children = [
                html.Div(
                    children = [
                        html.Div(
                            children = 'Total Male',
                            style = {
                                'color':fontcolor,
                                'fontFamily':headingfontstyle,
                                'fontSize':'20px',
                                'padding':'5px',
                                'fontWeight':'bold',
                                'marginRight':'45px',
                                'textAlign':'center'
                            }
                        ),
                        html.Div(
                            children = f'{total_male}',
                            style = {
                                'color':fontcolor,
                                'backgroundColor':darkbg,
                                'fontFamily':headingfontstyle,
                                'fontWeight':'bold',
                                'padding':'5px',
                                'marginRight':'45px',
                                'textAlign':'center',
                                'fontSize':'15px'
                            }
                        )
                    ],
                    style = {
                        'display':'flex',
                        'flexDirection':'column',
                        'alignItems':'center'
                    }
                ),
                html.Div(
                    children = [
                        html.Div(
                            children = 'Total Female',
                            style = {
                                'textAlign':'center',
                                'fontFamily':headingfontstyle,
                                'color':fontcolor,
                                'fontSize':'20px',
                                'padding':'5px',
                                'marginRight':'45px',
                                'backgroundColor':darkbg,
                                'fontWeight':'bold'
                            }
                        ),
                        html.Div(
                            children = f'{total_female}',
                            style = {
                                'textAlign':'center',
                                'color':fontcolor,
                                'fontWeight':'bold',
                                'backgroundColor':darkbg,
                                'padding':'5px',
                                'marginRight':'45px',
                                'fontFamily':headingfontstyle,
                                'fontSize':'15px'
                            }
                        )
                    ],
                    style ={
                        'display':'flex',
                        'flexDirection':'column',
                        'alignItems':'center'
                    }
                ),
                html.Div(
                    children = [
                        html.Div(
                            children = 'Avg Age',
                            style ={
                                'textAlign':'center',
                                'color':fontcolor,
                                'fontFamily':headingfontstyle,
                                'padding':'5px',
                                'fontWeight':'bold',
                                'marginRight':'45px',
                                'fontSize':'20px'
                            }
                        ),
                        html.Div(
                            children = f'{avg_age}',
                            style = {
                                'textAlign':'center',
                                'color':fontcolor,
                                'fontFamily':headingfontstyle,
                                'fontWeight':'bold',
                                'padding':'5px',
                                'marginRight':'45px',
                                'fontSize':'15px'
                            }
                        )
                    ],
                    style = {
                        'display':'flex',
                        'flexDirection':'column',
                        'alignItems':'center'
                    }
                ),
                html.Div(
                    children = [
                        html.Div(
                            children = 'Avg Credit Score',
                            style = {
                                'textAlign':'center',
                                'color':fontcolor,
                                'fontFamily':headingfontstyle,
                                'fontWeight':'bold',
                                'marginRight':'45px',
                                'padding':'5px',
                                'fontSize':'20px'
                            }
                        ),
                        html.Div(
                            children = f'{avg_cr_score}',
                            style = {
                                'textAlign':'center',
                                'color':fontcolor,
                                'fontSize':'15px',
                                'marginRight':'45px',
                                'padding':'5px',
                                'fontFamily': headingfontstyle,
                                'fontWeight':'bold'
                            }
                        )
                    ],
                    style = {
                        'display':'flex',
                        'flexDirection':'column',
                        'alignItems':'center'
                    }
                ),
                html.Div(
                    children = [
                        html.Div(
                            children = '% Above Avg Credit Score (male)',
                            style = {
                                'textAlign':'center',
                                'color':fontcolor,
                                'fontSize':'20px',
                                'fontFamily':headingfontstyle,
                                'fontWeight':'bold',
                                'padding':'5px',
                                'marginRight':'45px'
                            }
                        ),
                        html.Div(
                            children = f'{perc_above_avg_cr_score_male}',
                            style = {
                                'textAlign':'center',
                                'color':fontcolor,
                                'fontFamily':headingfontstyle,
                                'fontWeight':'bold',
                                'padding':'5px',
                                'marginRight':'45px',
                                'fontSize':'15px'
                            }
                        )
                    ],
                    style = {
                        'display':'flex',
                        'flexDirection':'column',
                        'alignItems':'center'
                    }
                ),
                html.Div(
                    children = [
                        html.Div(
                            children = '% Above Avg Credit Score (female)',
                            style = {
                                'textAlign':'center',
                                'fontFamily':headingfontstyle,
                                'color':fontcolor,
                                'padding':'5px',
                                'marginRight':'45px',
                                'fontSize':'20px',
                                'fontWeight':'bold'
                            }
                        ),
                        html.Div(
                            children = f'{perc_above_avg_cr_score_female}',
                            style = {
                                'textAlign':'center',
                                'color':fontcolor,
                                'fontSize':'15px',
                                'fontWeight':'bold',
                                'marginRight':'45px',
                                'padding':'5px',
                                'fontFamily':headingfontstyle
                            }
                        )
                    ],
                    style = {
                        'display':'flex',
                        'flexDirection':'column',
                        'alignItems':'center'
                    }
                )
            ]
        ),

        # Charts container
        html.Div(
            children = [
                html.Div(
                    children = dcc.Graph(figure=avg_bal_age, id='chart1'),
                    style = {
                        'width':'50%',
                        'display':'inline-block',
                        'margin':'10px 0px 0px 0px',
                        'padding':'0',
                        'float':'left'
                    }
                ),
                html.Div(
                  children = dcc.Graph(figure = chun_non_chun, id ='chart2'),
                  style = {
                    'width' : '50%',
                    'display':'inline-block',
                    'margin':'10px 0px 0px 0px',
                    'padding':'0',
                    'float':'right'

                  }
                )
            ]
        )
    ]
)
