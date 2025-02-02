import streamlit as st
import pandas as pd
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

# Page config must be the first Streamlit command
st.set_page_config(
    page_title="Celestia Governance Dashboard",
    page_icon="🌌",
    layout="wide"
)

from database import Database
from rest_client import RestClient
from styles import apply_custom_styles
from components.network_status import render_network_status
from components.parameter_table import render_parameter_table, render_parameter_comparison
from components.comparison_view import render_comparison_charts
from components.parameter_history import render_parameter_history

# Initialize clients
db = Database()
rest_client = RestClient()

# Apply custom styles
apply_custom_styles()

# Header
st.title("🌌 Celestia Governance Dashboard")
st.markdown("Real-time governance parameter monitoring and analysis across Celestia networks")

# Network status and initial parameter fetch
networks = ['mainnet', 'mocha', 'arabica']
network_status = {}
parameters_fetched = False

for network in networks:
    network_status[network] = rest_client.get_network_status(network)
    if network_status[network]:
        logging.info(f"Fetching parameters for {network}")
        parameters = rest_client.fetch_parameters(network)
        if parameters:
            db.store_parameters(network, parameters)
            parameters_fetched = True
            logging.info(f"Successfully stored parameters for {network}")
        else:
            logging.warning(f"No parameters fetched for {network}")
    else:
        logging.warning(f"{network} network is unavailable")

render_network_status(network_status)

# Main content
tab1, tab2, tab3, tab4 = st.tabs(["Parameters", "Network Comparison", "Analysis", "Parameter History"])

# Network selection and parameter fetch section
with tab1:
    st.subheader("Network Parameters")
    selected_network = st.selectbox(
        "Select Network",
        options=networks,
        key="params_network"
    )

    # Check network status first
    if not network_status[selected_network]:
        st.error(f"⚠️ {selected_network.title()} network is currently unavailable. Please try another network or check back later.")
    else:
        # Fetch and display parameters
        parameters_df = db.get_parameters(selected_network)
        if not parameters_df.empty:
            render_parameter_table(parameters_df, selected_network)
        else:
            with st.spinner(f"Fetching parameters from {selected_network}..."):
                try:
                    logging.info(f"Attempting to fetch parameters for {selected_network}")
                    params = rest_client.fetch_parameters(selected_network)
                    if params:
                        logging.info(f"Successfully fetched {len(params)} parameters")
                        db.store_parameters(selected_network, params)
                        parameters_df = db.get_parameters(selected_network)
                        render_parameter_table(parameters_df, selected_network)
                    else:
                        st.error(
                            "Unable to fetch parameters. Please try again in a few minutes. "
                            "If the issue persists, try a different network."
                        )
                except Exception as e:
                    logging.error(f"Error fetching parameters: {str(e)}")
                    st.error(
                        "An error occurred while fetching parameters. "
                        "The error has been logged for investigation."
                    )

with tab2:
    # Comparison view
    st.subheader("Cross-Network Comparison")
    all_parameters_df = db.get_parameters()
    if all_parameters_df.empty:
        st.info("No parameters available for comparison. Please wait while we fetch data from the networks...")
        parameters_fetched = False
        for network in networks:
            if network_status[network]:
                params = rest_client.fetch_parameters(network)
                if params:
                    db.store_parameters(network, params)
                    parameters_fetched = True
        if parameters_fetched:
            all_parameters_df = db.get_parameters()
            render_parameter_comparison(all_parameters_df)
        else:
            st.error("Unable to fetch parameters from any network. Please try again later.")
    else:
        render_parameter_comparison(all_parameters_df)

with tab3:
    # Analysis view
    all_parameters_df = db.get_parameters()
    if not all_parameters_df.empty:
        render_comparison_charts(all_parameters_df)
    else:
        st.info("No parameters available for analysis. Please select a network first.")

with tab4:
    # Parameter History view
    render_parameter_history()

# Footer
st.markdown("---")
st.markdown(
    """
    <div style='text-align: center'>
        <p>Data refreshes automatically every 5 minutes | 
        <a href='https://docs.celestia.org/'>Documentation</a> | 
        <a href='https://github.com/celestiaorg'>GitHub</a></p>
    </div>
    """,
    unsafe_allow_html=True
)

# Automatic refresh
if 'last_refresh' not in st.session_state:
    st.session_state.last_refresh = pd.Timestamp.now()

if (pd.Timestamp.now() - st.session_state.last_refresh).total_seconds() > 300:
    st.session_state.last_refresh = pd.Timestamp.now()
    st.experimental_rerun()