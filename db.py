import cx_Oracle
import os

# Set the path to your Oracle wallet directory
wallet_path = os.getenv('ORACLE_WALLET_PATH', '/path/to/wallet')

# Set the wallet password
wallet_password = os.getenv('ORACLE_WALLET_PASSWORD', 'your_wallet_password')

# Set the connection details
dsn = cx_Oracle.makedsn('hostname', 'port', service_name='service_name')

# Create a connection using the wallet
connection = cx_Oracle.connect(
    user=os.getenv('ORACLE_USERNAME', 'your_username'),
    password=os.getenv('ORACLE_PASSWORD', 'your_password'),
    dsn=dsn,
    encoding='UTF-8',
    nencoding='UTF-8',
    mode=cx_Oracle.SYSDBA,
    wallet_location=wallet_path,
    password=wallet_password
)

# Perform database operations here

# Close the connection
connection.close()