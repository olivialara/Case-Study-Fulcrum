import streamlit as st
import pandas as pd
import numpy as np
#plotly imports
import plotly.express as px
import plotly.io as pio
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import json

st.title("Fulcrum Case Study: POMS")
# st.header("Search By Punk ID")
st.subheader("Data visualizations to summarize POMS policies.")

#image = Image.open('images/cryptopunks-image.jpg')

def graph_policy_breakdown_by_insurance_type():
    data = {'Insurance Type': ['Commercial', 'Auto', 'Home', 'Life'],
            'Percentage': [.59, .22, .15, .04],
            'Format': ['59%', '22%', '15%', '4%'],
            'Count': [1475, 550, 375, 100]
        }
    df = pd.DataFrame(data)

    fig = px.bar(df, 
             x= "Insurance Type",
             y= "Count",
             text = 'Format',
             color_discrete_sequence = ['#056374']
            )
            
    fig.update_layout(title = 'Policy Breakdown', title_x=.5, height=400)

    fig.update_traces(
    hovertemplate='<b>Insurance Type: %{x}</b><br>Count: %{y}<br>Percentage: %{text}'
    )

    return fig

def graph_monthly_trends():
    data = {'Date': ['Jan', 'Feb', 'March', 'April', 'May', 'June', 'July', 
                           'Aug', 'Sep', 'Oct',
                           'Nov', 'Dec'],
        'Format': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
        '2024': [145, 204, 336, 207, 159, 97, 72, 85, 96, 150, 170, 112],
        '2023': [101, 188, 207, 156, 105, 35, 90, 77, 101, 119, 101, 80]
       }

    df = pd.DataFrame(data)
    fig = go.Figure()

    fig.add_trace(
    go.Scatter(
        x=df['Date'],
        y=df['2023'],
        marker = {'color': '#dc3828'},
        name="Prev. Year" 
    ))

    fig.add_trace(
    go.Bar(
        x=df['Date'],
        y=df['2024'],
        marker = {'color': '#056374'},
        name="2024" 
    ))

    fig.update_layout(title = 'Monthly Trends', 
                  title_x=.5, 
                  xaxis_title="Month", 
                  yaxis_title="New Policies Generated",
                  hovermode='x unified',
                  height=400
                 )
    return fig

def graph_policy_breakdown_by_state():
    states = pd.read_csv('insurance-policy-count-by-state.csv') 
    code = {'Alabama': 'AL',
        'Alaska': 'AK',
        'Arizona': 'AZ',
        'Arkansas': 'AR',
        'California': 'CA',
        'Colorado': 'CO',
        'Connecticut': 'CT',
        'Delaware': 'DE',
        'District of Columbia': 'DC',
        'Florida': 'FL',
        'Georgia': 'GA',
        'Hawaii': 'HI',
        'Idaho': 'ID',
        'Illinois': 'IL',
        'Indiana': 'IN',
        'Iowa': 'IA',
        'Kansas': 'KS',
        'Kentucky': 'KY',
        'Louisiana': 'LA',
        'Maine': 'ME',
        'Maryland': 'MD',
        'Massachusetts': 'MA',
        'Michigan': 'MI',
        'Minnesota': 'MN',
        'Mississippi': 'MS',
        'Missouri': 'MO',
        'Montana': 'MT',
        'Nebraska': 'NE',
        'Nevada': 'NV',
        'New Hampshire': 'NH',
        'New Jersey': 'NJ',
        'New Mexico': 'NM',
        'New York': 'NY',
        'North Carolina': 'NC',
        'North Dakota': 'ND',
        'Ohio': 'OH',
        'Oklahoma': 'OK',
        'Oregon': 'OR',
        'Pennsylvania': 'PA',
        'Rhode Island': 'RI',
        'South Carolina': 'SC',
        'South Dakota': 'SD',
        'Tennessee': 'TN',
        'Texas': 'TX',
        'Utah': 'UT',
        'Vermont': 'VT',
        'Virginia': 'VA',
        'Washington': 'WA',
        'West Virginia': 'WV',
        'Wisconsin': 'WI',
        'Wyoming': 'WY'}
    states['Code'] = states['State'].map(code)

    fig = px.choropleth(states,
        locations='Code',
        color='2024',
        color_continuous_scale='bluyl',
        hover_name='State',
        locationmode='USA-states',
        hover_data=["2024"],
        labels={'2024':'Count', 'Code': 'Abbv.'},
        scope='usa',
        height=800,
        width=1200
        )

    fig.add_scattergeo(
        locations=states['Code'],
        locationmode='USA-states',
        text=states['2024'],
        hoverinfo='skip',
        mode='text',
        showlegend=False
        )

    fig.update_layout(font=dict(
        size=10, 
        #color="black"
        )),


    fig.update_traces(hovertemplate='<b>State: %{state}</b><br>Policy Count: %{2024}')

    fig.update_layout(
        title=dict(text="Active Policies by State", 
               #font=dict(size=18), 
               x=0.5))
    return fig


st.write(graph_policy_breakdown_by_insurance_type())
st.write(graph_policy_breakdown_by_state())
st.write(graph_monthly_trends())