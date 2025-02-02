import os
import sqlite3
import pandas as pd
from datetime import datetime

class Database:
    def __init__(self):
        self.conn = sqlite3.connect('celestia.db')
        self.create_tables()

    def create_tables(self):
        with self.conn:
            # Parameters table
            self.conn.execute("""
                CREATE TABLE IF NOT EXISTS parameters (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    network TEXT,
                    module TEXT,
                    parameter TEXT,
                    value TEXT,
                    timestamp TIMESTAMP,
                    changeable_via_governance BOOLEAN
                )
            """)

            # Parameter history table
            self.conn.execute("""
                CREATE TABLE IF NOT EXISTS parameter_history (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    network_name TEXT,
                    parameter_name TEXT,
                    old_value TEXT,
                    new_value TEXT,
                    changed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)

    def store_parameters(self, network: str, parameters: list):
        with self.conn:
            for param in parameters:
                # First get the existing value if any
                cursor = self.conn.execute("""
                    SELECT value FROM parameters 
                    WHERE network = ? AND module = ? AND parameter = ?
                    ORDER BY timestamp DESC LIMIT 1
                """, (network, param['module'], param['parameter']))

                existing = cursor.fetchone()

                # Insert new parameter value
                self.conn.execute("""
                    INSERT INTO parameters 
                    (network, module, parameter, value, timestamp, changeable_via_governance)
                    VALUES (?, ?, ?, ?, ?, ?)
                """, (
                    network,
                    param['module'],
                    param['parameter'],
                    param['value'],
                    datetime.now(),
                    param['changeable_via_governance']
                ))

                # If value changed, record in history
                if existing and existing[0] != param['value']:
                    self.conn.execute("""
                        INSERT INTO parameter_history 
                        (network_name, parameter_name, old_value, new_value)
                        VALUES (?, ?, ?, ?)
                    """, (
                        network,
                        f"{param['module']}.{param['parameter']}",
                        existing[0],
                        param['value']
                    ))

    def get_parameters(self, network: str = None) -> pd.DataFrame:
        query = """
            SELECT * FROM parameters 
            WHERE timestamp = (
                SELECT MAX(timestamp) 
                FROM parameters p2 
                WHERE parameters.network = p2.network 
                AND parameters.module = p2.module 
                AND parameters.parameter = p2.parameter
            )
        """
        if network:
            query += " AND network = ?"
            params = (network,)
        else:
            params = None

        return pd.read_sql_query(query, self.conn, params=params)

    def get_parameter_history(self, network: str, start_time: datetime, parameter_filter: str = None) -> pd.DataFrame:
        """Get parameter history with filtering options"""
        query = """
            SELECT 
                network_name,
                parameter_name,
                old_value,
                new_value,
                changed_at
            FROM parameter_history
            WHERE network_name = ?
            AND changed_at >= ?
        """

        params = [network, start_time]

        if parameter_filter:
            query += " AND LOWER(parameter_name) LIKE LOWER(?)"
            params.append(f"%{parameter_filter}%")

        query += " ORDER BY changed_at DESC"

        return pd.read_sql_query(query, self.conn, params=tuple(params))

    def query(self, query: str, params: tuple = None) -> pd.DataFrame:
        """Execute a custom query and return results as a DataFrame"""
        return pd.read_sql_query(query, self.conn, params=params)

    def close(self):
        self.conn.close()