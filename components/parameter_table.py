import streamlit as st
import pandas as pd
import plotly.express as px

def render_parameter_table(df: pd.DataFrame, selected_network: str = None):
    if selected_network:
        df = df[df['network'] == selected_network]
    
    # Add filter controls
    col1, col2 = st.columns(2)
    with col1:
        selected_module = st.selectbox(
            "Filter by Module",
            options=['All'] + sorted(df['module'].unique().tolist())
        )
    
    with col2:
        governance_filter = st.selectbox(
            "Governance Changeable",
            options=['All', 'Yes', 'No']
        )
    
    # Apply filters
    if selected_module != 'All':
        df = df[df['module'] == selected_module]
    
    if governance_filter != 'All':
        df = df[df['changeable_via_governance'] == (governance_filter == 'Yes')]
    
    # Display table
    st.dataframe(
        df[['module', 'parameter', 'value', 'changeable_via_governance']],
        use_container_width=True,
        hide_index=True
    )

def render_parameter_comparison(df: pd.DataFrame):
    # Pivot the dataframe to compare values across networks
    pivot_df = df.pivot(
        index=['module', 'parameter'],
        columns='network',
        values='value'
    ).reset_index()
    
    # Highlight differences
    def highlight_differences(row):
        if len(row.unique()) > 1:
            return ['background-color: #8A2BE2;opacity: 0.3'] * len(row)
        return [''] * len(row)
    
    styled_df = pivot_df.style.apply(
        highlight_differences,
        subset=pivot_df.columns[2:]
    )
    
    st.dataframe(
        styled_df,
        use_container_width=True
    )
