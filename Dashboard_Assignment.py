import pandas as pd
import plotly.express as px
import plotly.figure_factory as ff
import streamlit as st

df = pd.read_csv('fifa_eda.csv')
df['International Reputation'] = df['International Reputation'].astype(str)
df['Skill Moves'] = df['Skill Moves'].astype(str)
df['Joined'] = df['Joined'].astype(str)
st.markdown(
    """
    <style>
    body {
        background-color: #6495ED;
    }
    </style>
    """,
    unsafe_allow_html=True
)

## Data Describtion Page
def DataDescription():
    st.title('Data Description Page')
    st.markdown('#### Sample rows of the Data')
    st.write(df.sample(5))
    
    st.markdown('#### Data Description')
    st.write(df.describe())
    
    st.markdown('#### Null Values')
    st.write(df.isnull().sum())
    
    st.markdown('#### Data Types')
    st.write(df.dtypes)
## Numerical Charts Page
def NumericalCharts():
    ### Histogram Plot ###
    st.title('Numerical Charts Page')
    st.sidebar.subheader('Histogram Plot')
    hist_col = st.sidebar.selectbox('Choose Historam Column',['Age','Overall','Potential','Value','Wage','Height','Weight','Release Clause'])
    hist_fig = px.histogram(data_frame=df,x=hist_col,text_auto=True,color_discrete_sequence=['#4d0000'])
    st.markdown('#### Histogram of '+hist_col+' Column')
    st.plotly_chart(hist_fig)
    ### Box Plot ###
    st.sidebar.subheader('Box Plot')
    Box_col = st.sidebar.selectbox('Choose Box Column',['Age','Overall','Potential','Value','Wage','Height','Weight','Release Clause'])
    color_Box = st.sidebar.checkbox('AddColor')
    if color_Box:
        c_Box = st.sidebar.selectbox('Select Color : ',['Nationality','Club','Preferred Foot','International Reputation','Skill Moves','Position','Joined','Contract Valid Until'])
        box_fig = px.box(data_frame=df,x=Box_col,color = c_Box,color_discrete_sequence=px.colors.qualitative.Set1)
        st.markdown('#### BoxPlot of '+Box_col+' Column')
        st.plotly_chart(box_fig)
    else:
        box_fig = px.box(data_frame=df,x=Box_col,color_discrete_sequence=px.colors.qualitative.Set1)
        st.markdown('#### BoxPlot of '+Box_col+' Column')
        st.plotly_chart(box_fig)
        
   ### Scatter Plot ###
    st.sidebar.subheader('Scatter Plot')
    scatt_X = st.sidebar.selectbox('Choose Scatter X Col : ',['Age','Overall','Potential','Value','Wage','Height','Weight','Release Clause'])
    scatt_Y = st.sidebar.selectbox('Choose Scatter Y Col : ',['Age','Overall','Potential','Value','Wage','Height','Weight','Release Clause'])
    color_scatter = st.sidebar.checkbox('Add Color')
    if color_scatter:
        c_scatter = st.sidebar.selectbox('Choose Color : ',['Nationality','Club','Preferred Foot','International Reputation','Skill Moves','Position','Joined','Contract Valid Until'])
        Scatt_fig = px.scatter(data_frame=df,x=scatt_X,y=scatt_Y,color = c_scatter,color_discrete_sequence=px.colors.qualitative.Set1)
        st.markdown('#### Scatter Plot Between '+ scatt_X +' & '+scatt_Y)
        st.plotly_chart(Scatt_fig)
    else:
            Scatt_fig = px.scatter(data_frame=df,x=scatt_X,y=scatt_Y,color_discrete_sequence=px.colors.qualitative.Set1)
            st.markdown('#### Scatter Plot Between '+ scatt_X +' & '+scatt_Y)
            st.plotly_chart(Scatt_fig)
    ### Line Plot ###
    st.sidebar.subheader('Line Plot')
    line_X = st.sidebar.selectbox('Choose Line X Col : ',['Contract Valid Until','Joined'])
    line_Y = st.sidebar.selectbox('Choose Line Y Col : ',['Age','Overall','Potential','Value','Wage','Height','Weight','Release Clause'])
    color_line = st.sidebar.checkbox('Add Line')
    df_line = df.groupby(line_X).sum()[line_Y]
    if color_line:
        line_color = st.sidebar.selectbox('Choose Other line Col : ',['Age','Overall','Potential','Value','Wage','Height','Weight','Release Clause'])
        df_line = df.groupby(line_X).sum()[[line_Y,line_color]]
        line_fig = px.line(data_frame=df_line,color_discrete_sequence=px.colors.qualitative.Set1)
        st.markdown('#### Line Plot Between '+ line_X +' & ['+line_Y+' , '+line_color+']')
        st.plotly_chart(line_fig)
    else:
        line_fig = px.line(data_frame=df_line,color_discrete_sequence=['#990000'])
        st.markdown('#### Line Plot Between '+ line_X +' & '+line_Y)
        st.plotly_chart(line_fig)
    ### Correlation Matrix
    st.sidebar.subheader('Correlation Matrix')
    corr_vars = st.sidebar.multiselect('Choose Corr Variables : ',['Age','Overall','Potential','Value','Wage','Height','Weight','Release Clause'])
    fig_corr = px.imshow(df[corr_vars].corr(),text_auto=True,color_continuous_scale=['#000000','#990000'])
    st.markdown('#### Correlation Matrix')
    st.plotly_chart(fig_corr)
## Categorical Charts Page
def CategoricalCharts():
    st.title('Categorical Charts Page')
    ### Count Plot ###
    st.sidebar.subheader('Count Plot')
    count_col = st.sidebar.selectbox('Choose Count Column :',
    ['Nationality','Club','Preferred Foot','International Reputation','Skill Moves','Position','Joined','Contract Valid Until'])
    ##Color part
    color_count = st.sidebar.checkbox('Add Color')
    if color_count :
        c_count = st.sidebar.selectbox('Choose Color',['Nationality','Club','Preferred Foot','International Reputation','Skill Moves','Position','Joined','Contract Valid Until'])
        count_fig = px.histogram(data_frame=df,x=count_col,color=c_count,color_discrete_sequence=px.colors.qualitative.Set1)
        st.markdown('#### Count Plot of '+count_col+' Column')
        st.plotly_chart(count_fig)
    else:
        count_fig = px.histogram(data_frame=df,x=count_col,color_discrete_sequence=['#990000'])
        st.markdown('#### Count Plot of '+count_col+' Column')
        st.plotly_chart(count_fig) 
                                       
    ### Bar Plot ###
    st.sidebar.subheader('Bar Plot')
    bar_X = st.sidebar.selectbox('Choose Bar X Col : ',['Nationality','Club','Preferred Foot','International Reputation','Skill Moves','Position','Joined','Contract Valid Until'])
    bar_Y = st.sidebar.selectbox('Choose Bar Y Col : ',['Age','Overall','Potential','Value','Wage','Height','Weight','Release Clause'])
    color_bar = st.sidebar.checkbox('Select Color')
    if color_bar :
        c_bar = st.sidebar.selectbox('Choose Color',['Nationality','Club','Preferred Foot','International Reputation','Skill Moves','Position','Joined','Contract Valid Until'])
        Bar_fig = px.bar(data_frame=df,x=bar_X,y=bar_Y,color=c_bar,barmode='group',color_discrete_sequence=px.colors.qualitative.Set1)
        st.markdown('#### Bar Plot Between '+ bar_X +' & '+bar_Y)
        st.plotly_chart(Bar_fig)
    else:
        Bar_fig = px.bar(data_frame=df,x=bar_X,y=bar_Y,color_discrete_sequence=['#990000'])
        st.markdown('#### Bar Plot Between '+ bar_X +' & '+bar_Y)
        st.plotly_chart(Bar_fig)
    
    ### Violen Plot ###
    st.sidebar.subheader('Violen Plot')
    Violen_X = st.sidebar.selectbox('Choose Violen X Col : ',['Nationality','Club','Preferred Foot','International Reputation','Skill Moves','Position','Joined','Contract Valid Until'])
    Violen_Y = st.sidebar.selectbox('Choose Violen Y Col : ',['Age','Overall','Potential','Value','Wage','Height','Weight','Release Clause'])
    color_Violen = st.sidebar.checkbox('select Color')
    if color_Violen :
        c_Violen = st.sidebar.selectbox('Choose Color',['Nationality','Club','Preferred Foot','International Reputation','Skill Moves','Position','Joined','Contract Valid Until'])
        Violen_fig = px.violin(data_frame=df,x=Violen_X,y=Violen_Y,color=c_Violen,color_discrete_sequence=px.colors.qualitative.Set1)
        st.markdown('#### Violen Plot Between '+ Violen_X +' & '+Violen_Y)
        st.plotly_chart(Violen_fig)
    else:
        Violen_fig = px.violin(data_frame=df,x=Violen_X,y=Violen_Y,color_discrete_sequence=['#990000'])
        st.markdown('#### Violen Plot Between '+ Violen_X +' & '+Violen_Y)
        st.plotly_chart(Violen_fig)  
    
    ### Strip Plot ###
    st.sidebar.subheader('Strip Plot')
    Strip_X = st.sidebar.selectbox('Choose Strip X Col : ',['Nationality','Club','Preferred Foot','International Reputation','Skill Moves','Position','Joined','Contract Valid Until'])
    Strip_Y = st.sidebar.selectbox('Choose Strip Y Col : ',['Age','Overall','Potential','Value','Wage','Height','Weight','Release Clause'])
    color_Strip = st.sidebar.checkbox('SelectColor')
    if color_Strip :
        c_Strip = st.sidebar.selectbox('ChooseColor',['Nationality','Club','Preferred Foot','International Reputation','Skill Moves','Position','Joined','Contract Valid Until'])
        Strip_fig = px.strip(data_frame=df,x=Strip_X,y=Strip_Y,color=c_Strip,color_discrete_sequence=px.colors.qualitative.Set1)
        st.markdown('#### Strip Plot Between '+ Strip_X +' & '+Strip_Y)
        st.plotly_chart(Strip_fig)
    else:
        Strip_fig = px.strip(data_frame=df,x=Strip_X,y=Strip_Y,color_discrete_sequence=['#990000'])
        st.markdown('#### Strip Plot Between '+ Strip_X +' & '+Strip_Y)
        st.plotly_chart(Strip_fig) 
dic = {
    'Data Description':DataDescription,
    'Numerical Charts':NumericalCharts,
    'Categorical Charts':CategoricalCharts
}
st.sidebar.subheader('Pages Names')
user_choice = st.sidebar.selectbox('Choose Page : ',dic.keys())
dic[user_choice]()
