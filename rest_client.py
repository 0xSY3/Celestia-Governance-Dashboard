import requests
import logging
from typing import List, Dict, Optional
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

class RestClient:
    def __init__(self):
        self.endpoints = {
            'mainnet': [
                'https://api.celestia.nodestake.top',
                'https://api.celestia.nodeist.net',
                'https://celestia-api.lavenderfive.com'
            ],
            'mocha': [
                'https://api-mocha.pops.one',
                'https://api-1.celestia.nodes.guru'
            ],
            'arabica': [
                'https://api.celestia-arabica-11.com'
            ]
        }
        
        # Configure session with retries
        self.session = requests.Session()
        retries = Retry(total=3, backoff_factor=0.5, status_forcelist=[500, 502, 503, 504])
        self.session.mount('https://', HTTPAdapter(max_retries=retries))
    
    def get_network_status(self, network: str) -> bool:
        """Check if network endpoints are accessible"""
        for endpoint in self.endpoints.get(network, []):
            try:
                response = self.session.get(f"{endpoint}/cosmos/base/tendermint/v1beta1/syncing", timeout=10)
                return response.status_code == 200
            except Exception as e:
                logging.warning(f"Failed to connect to {endpoint}: {str(e)}")
                continue
        return False

    def _format_value(self, value: any) -> str:
        """Format parameter values for display"""
        if isinstance(value, (dict, list)):
            return str(value)
        return str(value)

    def fetch_parameters(self, network: str) -> List[Dict]:
        """Fetch governance parameters from network using REST API"""
        parameters = []
        
        for endpoint in self.endpoints.get(network, []):
            try:
                # Query parameters from different modules
                parameter_endpoints = {
                    'auth': '/cosmos/auth/v1beta1/params',
                    'bank': '/cosmos/bank/v1beta1/params',
                    'staking': '/cosmos/staking/v1beta1/params',
                    'slashing': '/cosmos/slashing/v1beta1/params',
                    'gov': '/cosmos/gov/v1beta1/params/voting',
                    'distribution': '/cosmos/distribution/v1beta1/params',
                    'mint': '/cosmos/mint/v1beta1/params'
                }

                for module, path in parameter_endpoints.items():
                    try:
                        response = self.session.get(f"{endpoint}{path}", timeout=15)
                        if response.status_code == 200:
                            data = response.json()
                            if 'params' in data:
                                params_data = data['params']
                                for key, value in params_data.items():
                                    parameters.append({
                                        'module': module,
                                        'parameter': key,
                                        'value': self._format_value(value),
                                        'changeable_via_governance': True
                                    })
                                logging.info(f"Successfully fetched {module} parameters")
                    except Exception as e:
                        logging.error(f"Error fetching {module} parameters: {str(e)}")
                        continue

                if parameters:  # If we got parameters, break the endpoint loop
                    break

            except Exception as e:
                logging.error(f"Failed to connect to {endpoint}: {str(e)}")
                continue

        return parameters
