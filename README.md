# vidar_config
Extracts Vidar config from Command &amp; Control servers for specific botnets

This script is capable of extracting information regarding specific botnets from Vidar Command & Control servers enabling researchers to track campaigns over time.

To find suitable botnets, head over to [Tria.ge Sandbox](https://tria.ge/s?q=family%3avidar). Currently, the extraction of the botnet from samples is unfortunately broken. Due to this, download the PCAP from the analysis of a Vidar sample and search for POST requests which contain an "X-Id" as header. 

Afterwards, open the script and replace the IP of "c2" and the ID with the X-Id you found.


