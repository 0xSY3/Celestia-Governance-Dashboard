# Celestia Governance Dashboard

A comprehensive network governance and parameter monitoring platform for Celestia networks, providing advanced blockchain configuration insights and real-time network analysis.

## Overview

This dashboard offers real-time monitoring and analysis of Celestia network parameters across mainnet, mocha, and arabica networks. It provides a user-friendly interface for tracking governance parameters, comparing cross-network configurations, and analyzing parameter changes over time.

## Key Features

- **Multi-Network Support**: Monitor parameters across mainnet, mocha, and arabica networks
- **Real-time Parameter Tracking**: Live updates of network parameters every 5 minutes
- **Cross-Network Comparison**: Side-by-side parameter comparison with variance highlighting
- **Parameter History**: Track and visualize parameter changes over time
- **Network Status Monitoring**: Real-time network health and availability checks
- **Advanced Filtering**: Filter parameters by module and governance changeability
- **Data Export**: Download parameter data and comparisons in CSV format

## Technology Stack

- **Frontend**: Streamlit
- **Backend**: Python 3.11
- **Database**: SQLite
- **API Integration**: gRPC, REST
- **Data Visualization**: Plotly
- **Parameter Tracking**: Custom tracking system

## Installation

1. Clone the repository:
```bash
git clone https://github.com/your-username/celestia-governance-dashboard.git
cd celestia-governance-dashboard
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up the database:
```bash
python database.py
```

4. Start the application:
```bash
streamlit run main.py
```

## Usage

1. **View Network Parameters**:
   - Select a network from the dropdown menu
   - Use filters to find specific parameters
   - Export parameter data as CSV

2. **Compare Networks**:
   - Navigate to the "Network Comparison" tab
   - Parameters with different values are highlighted
   - Download comparison data

3. **Track Parameter History**:
   - Access the "Parameter History" tab
   - Filter by time range and parameter name
   - View historical changes across networks

4. **Monitor Network Status**:
   - Real-time status indicators for each network
   - Connection health monitoring
   - Automatic refresh every 5 minutes

## Network Support

- **Mainnet**: Production network
- **Mocha**: Public testnet
- **Arabica**: Development testnet

## Development

### Prerequisites
- Python 3.11+
- Streamlit
- gRPC tools
- SQLite3

### Setup Development Environment

1. Install development dependencies:
```bash
pip install -r requirements-dev.txt
```

2. Generate gRPC files:
```bash
python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. celestia_proto/*.proto
```

3. Run tests:
```bash
pytest tests/
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## Acknowledgments

- Celestia Network for providing the infrastructure and documentation
- Community contributors and testers

## Contact

For questions and support, please open an issue in the GitHub repository.
