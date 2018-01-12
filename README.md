# rcv-connector_acl_converter
A simple python script to convert Exchange Receive Connector IP Lists to F5 External Data Group Lists.

Usage:
```
python convert_acl.py -i sample_content.csv -o external_dgl.txt
```

Requires Python 2.7

Export all IP Addresses configured on a Receive Connector using PowerShell:
```
Get-ReceiveConnector “Company internal SMTP Relaying Connector” | select -ExpandProperty RemoteIPRanges | Export-csv c:\RelayConnector1.csv
```
