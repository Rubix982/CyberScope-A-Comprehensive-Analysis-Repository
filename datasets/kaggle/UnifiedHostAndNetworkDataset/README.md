# Unified Host And Network Dataset

The Unified Host and Network Dataset is a subset of network and computer (host) events collected from the Los Alamos National Laboratory enterprise network over the course of approximately 90 days.

The host event logs originated from most enterprise computers running the Microsoft Windows operating system on Los Alamos National Laboratory’s (LANL) enterprise network. The network event data originated from many of the internal enterprise routers within the LANL enterprise network.

The data values have been de-identified (anonymized) to protect the security of LANL’s operational IT environment. The identities match across both the host and network data allowing the two data elements to be used together for analysis and research. In some cases, including well-known network ports, system-level users names (not associated to people), and system-level hosts, the values were not deidentified. In addition, in some cases hosts were combined where they represented well-known redundant services including the Active Directory servers, LANL’s email servers, and LANL’s automated vulnerability scanning systems.

For a detailed description of the data, see [citing](https://csr.lanl.gov/data/2017/#citing).

The network and host event data are currently available as multiple files each containing one day of events, which can be accessed through the links below, respectively:

- [Netflow](https://csr.lanl.gov/data-fence/1738281337/_84wzULUsJzOaAsV7NvJR8KIBOw=/unified-host-network-dataset-2017/netflow.html)
- [HostEvents](https://csr.lanl.gov/data-fence/1738281337/_84wzULUsJzOaAsV7NvJR8KIBOw=/unified-host-network-dataset-2017/wls.html)

To download all the individual files for the network and host event data respectively:

```sh
for i in $(seq -w 2 90); do wget -c https://csr.lanl.gov/data/unified-host-network-dataset-2017/1738281337/_84wzULUsJzOaAsV7NvJR8KIBOw=/netflow/netflow_day-$i.bz2; done
for i in $(seq -w 1 90); do wget -c https://csr.lanl.gov/data/unified-host-network-dataset-2017/1738281337/_84wzULUsJzOaAsV7NvJR8KIBOw=/wls/wls_day-$i.bz2; done
```

## Network Event Data

The data is provided in CSV format, one record per line. The network events represent bi-directional events where possible. It is in the form of:

Time, Duration, SrcDevice, DstDevice, Protocol, SrcPort, DstPort, SrcPackets, DstPackets, SrcBytes, DstBytes

The following table contains a description of each field:

Field Name	Description
Time	The start time of the event in epoch time format
Duration	The duration of the event in seconds.
SrcDevice	The device that likely initiated the event.
DstDevice	The receiving device.
Protocol	The protocol number.
SrcPort	The port used by the SrcDevice.
DstPort	The port used by the DstDevice.
SrcPackets	The number of packets the SrcDevice sent during the event.
DstPackets	The number of packets the DstDevice sent during the event.
SrcBytes	The number of bytes the SrcDevice sent during the event.
DstBytes	The number of bytes the DstDevice sent during the event.
A sample of the network event data is shown below:

```text
761,4434,Comp132598,Comp817788,6,Port12597,22,89159,85257,15495068,69768940
764,13161,Comp178973,Comp164069,17,137,137,325,0,30462,0
765,14369,Comp492856,Mail,6,Port30344,443,227,214,32300,9844
765,14431,Comp782574,Mail,6,Port28068,443,1637,3313,75302,1220077
765,17056,Comp378125,Mail,6,Port28068,443,3848,4096,177008,1441295
765,17087,Comp378125,Mail,6,Port41392,443,571,275,60842,12650
765,18105,Comp492856,Mail,6,Port30344,443,292,298,40698,13708
765,18633,Comp378125,Mail,6,Port41392,443,622,310,70370,20963
765,22042,Comp782574,Mail,6,Port28068,443,2142,4299,98532,1423831
```

## Host Event Data

The host event data set is a subset of host event logs collected from all computers running the Microsoft Windows operating system on LANL’s enterprise network. The data is provided in JSON format, one record per line.

The following table contains the Event IDs included from the event logs of Windows computers in the released dataset and a brief description of each:

EventID	Description
4768	Kerberos authentication ticket was requested (TGT)
4769	Kerberos service ticket was requested (TGS)
4770	Kerberos service ticket was renewed
4774	An account was mapped for logon
4776	The domain controller attempted to validate the credentials for an account
4624	An account was successfully logged on
4625	An account failed to logon on
4634	An account was logged off
4647	User initiated logon
4648	A logon was attempted using explicit credentials
4672	Special privileges assigned to a new logon
4800	The workstation was locked
4801	The workstation was unlocked
4802	The screensaver was invoked
4803	The screensaver was dismissed
4688	Process start
4689	Process end
4608	Windows is starting up
4609	Windows is shutting down
1100	Event logging service has shut down (often recorded instead of EventID 4609)

Each record in the event data set will have some of the following event attributes as described below:

- **Time**
    - The epoch time of the event in seconds.
- **EventID**
    - Four digit integer corresponding to the event id of the record.
- **LogHost**
    - The hostname of the computer that the event was recorded on. In the case of directed authentication events, the LogHost will correspond to the computer that the authentication event is terminating at (destination computer).
- **LogonType**
    - Integer corresponding to the type of logon, see Table 2.
- **LogonTypeDescription**
    - Description of the LogonType, see Table 2.
- **UserName**
    - The user account initiating the event. If the user ends in $, then it corresponds to a computer account for the specified computer.
- **DomainName**
    - Domain name of UserName.
- **LogonID**
    - A semi-unique (unique between current sessions and LogHost) number that identifies the logon session just initiated. Any events logged subsequently during this logon session should report the same Logon ID through to the logoff event.
- **SubjectUserName**
    - For authentication mapping events, the user account specified by this field is mapping to the user account in UserName.
- **SubjectDomainName**
    - Domain name of SubjectUserName.
- **SubjectLogonID**
    - See LogonID.
- **Status**
    - Status of the authentication request. “0x0” means success otherwise failure.
- **Source**
    - For authentication events, this will correspond to the the computer where the authentication originated (source computer), if it is a local logon event then this will be the same as the LogHost.
- **ServiceName**
    - The account name of the computer or service the user is requesting the ticket for.
- **Destination**
    - This is the server the mapped credential is accessing. This may indicate the local computer when starting another process with new account credentials on a local computer.
- **AuthenticationPackage**
    - The type of authentication occurring including Negotiate, Kerberos, NTLM plus a few more.
- **FailureReason**
    - The reason for a failed logon.
- **ProcessName**
    - The process executable name, for authentication events this is the process that processed the authentication event. ProcessNames may include the file type extensions (i.e exe).
- **ProcessID**
    - A semi-unique (unique between currently running processes AND LogHost) value that identifies the process. Process ID allows you to correlate other events logged in association with the same process through to the process end.
- **ParentProcessName**
    - The process executable that started the new process. ParentProcessNames often do not have file extensions like ProcessName but can be compared by removing file extensions from the name.
- **ParentProcessID**
    - Identifies the exact process that started the new process. Look for a preceding event 4688 with a ProcessID that matches this ParentProcessID.

A sample of the host event data is shown below,

```json
{"EventID": 4769, "UserName": "User624729", "ServiceName": "Comp883934$", "DomainName": "Domain002", "Status": "0x0", "Source": "Comp309534", "Computer": "ActiveDirectory", "Time": 2}
{"EventID": 4776, "UserName": "Scanner", "DomainName": "Domain002", "Status": "0x0", "Computer": "ActiveDirectory", "AuthenticationPackage": "MICROSOFT_AUTHENTICATION_PACKAGE_V1_0", "Time": 2}
{"EventID": 4672, "UserName": "ActiveDirectory$", "LogonID": "0x2e66398d", "DomainName": "Domain002", "Computer": "ActiveDirectory", "Time": 2}
{"EventID": 4624, "UserName": "ActiveDirectory$", "LogonID": "0x2e66398d", "DomainName": "Domain002", "LogonTypeDescription": "Network", "Computer": "ActiveDirectory", "AuthenticationPackage": "Kerberos", "Time": 2, "LogonType": 3}
{"EventID": 4634, "UserName": "ActiveDirectory$", "LogonID": "0x2e66398d", "DomainName": "Domain002", "LogonTypeDescription": "Network", "Computer": "ActiveDirectory", "Time": 2, "LogonType": 3}
{"EventID": 4624, "UserName": "User380010", "LogonID": "0x9f17415", "DomainName": "Domain002", "LogonTypeDescription": "Network", "Computer": "Comp966305", "AuthenticationPackage": "Kerberos", "Time": 2, "LogonType": 3}
{"EventID": 4634, "UserName": "User380010", "LogonID": "0x9f17415", "DomainName": "Domain002", "LogonTypeDescription": "Network", "Computer": "Comp966305", "Time": 2, "LogonType": 3}
{"EventID": 4624, "UserName": "User096622", "LogonID": "0x9f17637", "DomainName": "Domain002", "LogonTypeDescription": "Network", "Computer": "Comp966305", "AuthenticationPackage": "Kerberos", "Time": 2, "LogonType": 3}
{"EventID": 4634, "UserName": "User096622", "LogonID": "0x9f17637", "DomainName": "Domain002", "LogonTypeDescription": "Network", "Computer": "Comp966305", "Time": 2, "LogonType": 3}
{"EventID": 4624, "UserName": "User233472", "LogonID": "0x9f17fe4", "DomainName": "Domain002", "LogonTypeDescription": "Network", "Computer": "Comp966305", "AuthenticationPackage": "Kerberos", "Time": 2, "LogonType": 3}
```

## Citing

If you use this data in a publication please cite the following paper:

M. Turcotte, A. Kent and C. Hash, “Unified Host and Network Data Set”, in Data Science for Cyber-Security. November 2018, 1-22

```text
@inbook{doi:10.1142/9781786345646_001,
  author = {Melissa J. M. Turcotte and Alexander D. Kent and Curtis Hash},
  title = {Unified Host and Network Data Set},
  booktitle = {Data Science for Cyber-Security},
  chapter = {Chapter 1},
  pages = {1-22},
  year = {2018},
  month = {nov},
  publisher = {World Scientific},
  doi = {10.1142/9781786345646_001},
  URL = {https://www.worldscientific.com/doi/abs/10.1142/9781786345646_001},
  eprint = {https://www.worldscientific.com/doi/pdf/10.1142/9781786345646_001},
}
```

## License

CC0

To the extent possible under law, Los Alamos National Laboratory has waived all copyright and related or neighboring rights to Unified Host and Network DataSet. This work is published from: United States.

## Notes

This data set and associated research have been approved by the LANL Human Subject Research Review Board under approval LANL 14-07 X and has been approved for public release under approval LA-UR-17-20763

## Contact

For questions, feedback, or updates and future news related to events with regards to this dataset please send an e-mail to cyberdata@lanl.gov.
