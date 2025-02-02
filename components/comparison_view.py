import streamlit as st
import plotly.express as px
import pandas as pd

def render_comparison_charts(df: pd.DataFrame):
    # Create comparison visualizations
    st.subheader("Parameter Analysis")
    
    # Count parameters by module
    module_counts = df.groupby(['network', 'module']).size().reset_index(name='count')
    
    fig = px.bar(
        module_counts,
        x='module',
        y='count',
        color='network',
        barmode='group',
        title='Parameters by Module Across Networks',
        template='plotly_dark'
    )
    
    fig.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(color='white')
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    # Governance changeable parameters
    governance_counts = df.groupby(['network', 'changeable_via_governance']).size().reset_index(name='count')
    
    fig2 = px.pie(
        governance_counts,
        values='count',
        names='changeable_via_governance',
        facet_col='network',
        title='Governance Changeable Parameters Distribution',
        template='plotly_dark'
    )
    
    fig2.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(color='white')
    )
    
    st.plotly_chart(fig2, use_container_width=True)
