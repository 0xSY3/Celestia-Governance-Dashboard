import grpc
import json
from concurrent import futures
from typing import List, Dict, Optional
import logging
from google.protobuf.json_format import MessageToDict
from celestia_proto.cosmos.params.v1beta1 import params_pb2, params_pb2_grpc

class GrpcClient:
    def __init__(self):
        self.endpoints = {
            'mainnet': [
                'celestia.grpc.kjnodes.com:443',
                'celestia-grpc.chainode.tech:443',
                'celestia-grpc.noders.services:11090'
            ],
            'mocha': [
                'celestia-testnet-grpc.itrocket.net:443',
                'grpc-celestia-testnet.cryptech.com.ua:443'
            ],
            'arabica': [
                'grpc.celestia-arabica-11.com:443'
            ]
        }

        # Hardcoded parameters that aren't available via gRPC
        self.hardcoded_params = [
            {
                'module': 'blob',
                'parameter': 'SquareSizeUpperBound',
                'value': '128',
                'changeable_via_governance': False,
                'description': 'Hardcoded maximum square size which limits the number of shares per row or column for the original data square (not yet extended).'
            },
            {
                'module': 'blob',
                'parameter': 'SubtreeRootThreshold',
                'value': '64',
                'changeable_via_governance': False,
                'description': 'See ADR-013 for more details.'
            },
            {
                'module': 'consensus',
                'parameter': 'MaxTxSize',
                'value': '2 MiB',
                'changeable_via_governance': False
            },
            {
                'module': 'consensus',
                'parameter': 'TimeoutPropose',
                'value': '3500 ms',
                'changeable_via_governance': False
            },
            {
                'module': 'consensus',
                'parameter': 'TimeoutCommit',
                'value': '4200 ms',
                'changeable_via_governance': False
            },
            {
                'module': 'consensus',
                'parameter': 'UpgradeHeightDelay',
                'value': '100800 blocks',
                'changeable_via_governance': False
            },
            {
                'module': 'consensus',
                'parameter': 'MaxBlockSizeBytes',
                'value': '100 MiB',
                'changeable_via_governance': False
            }
        ]

    def get_network_status(self, network: str) -> bool:
        """Check if network endpoints are accessible"""
        for endpoint in self.endpoints.get(network, []):
            try:
                options = [
                    ('grpc.enable_http_proxy', 0),
                    ('grpc.enable_retries', 1),
                    ('grpc.keepalive_timeout_ms', 10000),
                    ('grpc.ssl_target_name_override', endpoint.split(':')[0])
                ]
                credentials = grpc.ssl_channel_credentials()
                channel = grpc.secure_channel(endpoint, credentials, options=options)
                future = grpc.channel_ready_future(channel)
                future.result(timeout=10)
                return True
            except Exception as e:
                logging.warning(f"Failed to connect to {endpoint}: {str(e)}")
                continue
        return False

    def fetch_parameters(self, network: str) -> List[Dict]:
        """Fetch all parameters, including hardcoded ones"""
        parameters = self.hardcoded_params.copy()  # Start with hardcoded parameters

        # Queryable parameters mapping
        param_mapping = {
            'auth': {
                'MaxMemoCharacters': True,
                'SigVerifyCostED25519': True,
                'SigVerifyCostSecp256k1': True,
                'TxSigLimit': True,
                'TxSizeCostPerByte': False
            },
            'bank': {
                'SendEnabled': False,
                'DefaultSendEnabled': True
            },
            'staking': {
                'UnbondingTime': True,
                'MaxValidators': True,
                'MaxEntries': True,
                'HistoricalEntries': True,
                'BondDenom': False,
                'MinCommissionRate': True
            },
            'slashing': {
                'SignedBlocksWindow': True,
                'MinSignedPerWindow': True,
                'DowntimeJailDuration': True,
                'SlashFractionDoubleSign': True,
                'SlashFractionDowntime': True
            },
            'distribution': {
                'CommunityTax': True,
                'BaseProposerReward': True,
                'BonusProposerReward': True,
                'WithdrawAddrEnabled': True
            }
        }

        for endpoint in self.endpoints.get(network, []):
            try:
                channel = grpc.secure_channel(
                    endpoint,
                    grpc.ssl_channel_credentials(),
                    options=[
                        ('grpc.enable_http_proxy', 0),
                        ('grpc.enable_retries', 1),
                        ('grpc.keepalive_timeout_ms', 10000),
                        ('grpc.ssl_target_name_override', endpoint.split(':')[0])
                    ]
                )

                stub = params_pb2_grpc.QueryStub(channel)

                for subspace, params in param_mapping.items():
                    for param_name, is_changeable in params.items():
                        try:
                            request = params_pb2.QueryParamsRequest(
                                subspace=subspace,
                                key=param_name
                            )
                            response = stub.Params(
                                request,
                                timeout=15,
                                metadata=[('x-cosmos-block-height', 'latest')]
                            )

                            if response and response.param:
                                param_value = MessageToDict(response.param)
                                value = param_value.get('value', '')

                                parameters.append({
                                    'module': subspace,
                                    'parameter': param_name,
                                    'value': value,
                                    'changeable_via_governance': is_changeable
                                })
                                logging.info(f"Successfully fetched {subspace}.{param_name}")
                        except Exception as e:
                            logging.error(f"Error fetching {subspace}.{param_name}: {str(e)}")
                            continue

                if parameters:  # If we got parameters, break the endpoint loop
                    break

            except Exception as e:
                logging.error(f"Failed to connect to {endpoint}: {str(e)}")
                continue

        return parameters