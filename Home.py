import dash
from dash import dcc,html

# background color, font style and font family
darkbg = '#181818'  
fontcolor = '#FFFFFF'  
headingfontstyle = 'Helvetica' 
bordercolor1 = 'rgb(17,226,213)'
bordercolor2 = 'rgb(248,249,168)'

# image url
img_url = 'https://ibb.co/fprVJmK'


# Register home page
dash.register_page(__name__, path='/')

# Layout
layout = html.Div(
    style={
        'display': 'flex',                # Use flexbox for layout
        'flexDirection': 'column',        # Arrange items vertically (image first, then text)
        'alignItems': 'center',           # Center items horizontally
        'padding': '20px'                 # Add padding around the layout
    },
    children=[
        # Container for the image
        html.Div(
            children=[
                html.Img(
                    src='https://i.ibb.co/3NS5Kt8/file.png',  # Image URL
                    alt='file',
                    style={
                        'height': '500px',      # Set the height of the image
                        'width': '70%',         # Set the width of the image
                        'borderRadius': '1%',   # Rounded corners
                        'display': 'block',     # Ensure the image is displayed as a block element
                        'margin': '0 auto' ,     # Center the image
                        'marginTop':'-40px'
                    }
                )
            ]
        ),
        # Container for the text
        html.Div(
            children=[
                "This dashboard presents insights from the Bank Customer Churn dataset, "
                "highlighting key factors contributing to customer retention and churn. "
                "Using demographic, transaction, and account data, we have identified "
                "trends in customer behavior that can help banks minimize churn and enhance customer satisfaction."
            ],
            style={
                'fontSize': '15px',                  # Set font size
                'padding': '10px',                   # Padding around text
                'marginTop': '-60px',                 # Add space between image and text
                'color': fontcolor,                  # Text color
                'fontFamily': headingfontstyle,      # Font family for the text
                'textAlign': 'center',               # Center the text
                'width': '70%'                       # Match the width of the image container
            }
        )
    ]
)

