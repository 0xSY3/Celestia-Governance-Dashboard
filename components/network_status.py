import streamlit as st

def render_network_status(status_dict):
    st.markdown("""
        <style>
        .network-status {
            display: flex;
            justify-content: space-between;
            padding: 10px;
            background: rgba(26, 28, 35, 0.95);
            border-radius: 5px;
            margin: 10px 0;
        }
        </style>
    """, unsafe_allow_html=True)

    cols = st.columns(len(status_dict))
    
    for i, (network, status) in enumerate(status_dict.items()):
        with cols[i]:
            st.markdown(
                f"""
                <div class="network-status">
                    <span>{network.title()}</span>
                    <span class="status-indicator {'status-online' if status else 'status-offline'}"></span>
                </div>
                """,
                unsafe_allow_html=True
            )
