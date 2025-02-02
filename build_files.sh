#!/bin/bash

# Install Python dependencies
pip install -r requirements.txt

# Create necessary directories
mkdir -p ~/.streamlit

# Create Streamlit config
cat > ~/.streamlit/config.toml << EOF
[server]
headless = true
port = $PORT
enableCORS = false
address = "0.0.0.0"
EOF

# Create streamlit credentials
cat > ~/.streamlit/credentials.toml << EOF
[general]
email = ""
EOF

# Start the Streamlit app
streamlit run main.py
