import streamlit as st
#from src.graph_controls import graph_controls
from src.graphs import graph_controls
from src.utility import load_dataframe
from streamlit.components.v1 import iframe

def views(link):
    """
    Helper function for directing users to various pages.
    :param link: str, option selected from the radio button
    :return:
    """
    if link == 'Home':
        st.header("Welcome to UWS-AHL")
        st.write("Developer:Shahadate Rezvy")
        st.subheader("Getting started")
        st.sidebar.subheader("Upload your data")
        uploaded_file = st.sidebar.file_uploader(label="Upload your csv or excel file here.",
                                                 accept_multiple_files=False,
                                                 type=['csv', 'xlsx'])


        if uploaded_file is not None:
            df, columns,df_average,df_std = load_dataframe(uploaded_file=uploaded_file)

            st.sidebar.subheader("Visualize your data")

            show_data = st.sidebar.checkbox(label='Show data')

            if show_data:
                try:
                    st.subheader("Data view")
                    number_of_rows = st.sidebar.number_input(label='Select number of rows', min_value=2)

                    st.dataframe(df.head(number_of_rows))
                except Exception as e:
                    print(e)

            #st.sidebar.subheader("Theme selection")

            #theme_selection = st.sidebar.selectbox(label="Select your themes",
                                                   #options=['plotly', 
                                                            #'plotly_white',
                                                            #'ggplot2',
                                                           # 'seaborn',
                                                            #'simple_white'
                                                          # ])
            st.sidebar.subheader("Chart selection")
            chart_type = st.sidebar.selectbox(label="Select your chart type.",
                                              options=['Scatter plots',
                                                       'Box plots',
                                                       'Violin plots',
                                                       #'Density contour',
                                                       #'Sunburst',
                                                       'Pie Charts',
                                                       #'Density heatmaps',
                                                       #'Sunburst',
                                                       #'Histogram',
                                                       #'Tree maps',
                                                       'custom'
                                                        ])  # 'Line plots',

            #graph_controls(chart_type=chart_type, df=df, dropdown_options=columns, template=theme_selection)
            
            graph_controls(chart_type=chart_type, df=df, df_average=df_average, df_std=df_std, dropdown_options=columns, template='plotly')
