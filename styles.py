import streamlit as st

def apply_custom_styles():
    st.markdown("""
        <style>
        /* Main container */
        .main {
            background-color: #0E1117;
        }
        
        /* Star field animation */
        @keyframes twinkle {
            0% { opacity: 0.3; }
            50% { opacity: 1; }
            100% { opacity: 0.3; }
        }
        
        .star-field {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            pointer-events: none;
            z-index: -1;
            background: 
                radial-gradient(1px 1px at 20px 30px, #fff, rgba(0,0,0,0)),
                radial-gradient(1px 1px at 40px 70px, #fff, rgba(0,0,0,0)),
                radial-gradient(1px 1px at 50px 160px, #fff, rgba(0,0,0,0)),
                radial-gradient(1px 1px at 90px 250px, #fff, rgba(0,0,0,0));
            background-repeat: repeat;
            animation: twinkle 4s infinite;
        }
        
        /* Custom card style */
        .stCard {
            border-radius: 10px;
            background: rgba(26, 28, 35, 0.95);
            padding: 20px;
            margin: 10px 0;
        }
        
        /* Parameter table styles */
        .dataframe {
            font-size: 14px;
            border-radius: 5px;
            overflow: hidden;
        }
        
        .dataframe th {
            background-color: #1A1C23;
            color: #8A2BE2;
            padding: 12px;
        }
        
        .dataframe td {
            padding: 10px;
        }
        
        /* Network status indicator */
        .status-indicator {
            display: inline-block;
            width: 10px;
            height: 10px;
            border-radius: 50%;
            margin-right: 5px;
        }
        
        .status-online {
            background-color: #00FF00;
        }
        
        .status-offline {
            background-color: #FF0000;
        }
        </style>
        <div class="star-field"></div>
    """, unsafe_allow_html=True)
