# 🌌 Celestia Network Parameter Dashboard

A comprehensive governance and parameter monitoring platform for Celestia networks, providing real-time insights into network configurations across mainnet, mocha, and arabica networks.

## Overview

This dashboard provides a real-time view of Celestia network parameters, enabling users to monitor and compare configurations across different networks. Built with Streamlit and powered by gRPC, it offers an intuitive interface for tracking governance parameters and network status.

## Key Features

- **Multi-Network Monitoring**: Track parameters across mainnet, mocha, and arabica networks
- **Real-time Updates**: Automatic parameter refresh every 5 minutes
- **Network Comparison**: Side-by-side parameter analysis with variance highlighting
- **Parameter History**: Track changes in network parameters over time
- **Advanced Filtering**: Filter by module and governance changeability
- **Data Export**: Download parameter data in CSV format
- **Network Health**: Real-time status monitoring of each network

## Live Demo

Visit the live dashboard at: [Celestia Parameter Dashboard](https://celestia-governance-dashboard.replit.app/)

## Technology Stack

- **Frontend**: Streamlit
- **Backend**: Python 3.11
- **Database**: SQLite3
- **API Integration**: gRPC, REST
- **Data Visualization**: Plotly
- **Deployment**: Vercel

## Deployment

### Prerequisites

- Python 3.11+
- Git
- Vercel CLI (optional)

### Deploy on Vercel

1. Fork this repository
2. Connect your Vercel account to GitHub
3. Import the repository in Vercel:
   - Select the repository
   - Framework Preset: Other
   - Build Command: Leave blank (uses `vercel.json` configuration)
   - Output Directory: `.`
   - Install Command: Leave blank (uses `vercel.json` configuration)

### Local Development

1. Clone the repository:
```bash
git clone https://github.com/yourusername/celestia-parameter-dashboard.git
cd celestia-parameter-dashboard
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Start the application:
```bash
streamlit run main.py
```

## Usage

### Parameter Monitoring

1. Select a network (mainnet, mocha, or arabica)
2. View current parameter values
3. Filter parameters by module
4. Toggle governance-changeable parameters

### Network Comparison

1. Navigate to the "Network Comparison" tab
2. View side-by-side parameter comparisons
3. Identify variations highlighted in purple
4. Export comparison data as CSV

### Parameter History

1. Access the "Parameter History" tab
2. Select time range and network
3. Filter by parameter name
4. Download historical data

## Network Parameters

### Currently Monitored Parameters

- **Auth**: MaxMemoCharacters, TxSigLimit, TxSizeCostPerByte, etc.
- **Bank**: SendEnabled, DefaultSendEnabled
- **Staking**: UnbondingTime, MaxValidators, MaxEntries, etc.
- **Slashing**: SignedBlocksWindow, MinSignedPerWindow, etc.
- **Distribution**: CommunityTax, BaseProposerReward, etc.

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Celestia Network for providing the infrastructure
- Community contributors and testers

## Support

For questions and support:
- Open an issue in the GitHub repository
- Join the Celestia Discord community

---
Made with ❤️ for the Celestia community
