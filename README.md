# vidar_config
Extracts Vidar config from Command &amp; Control servers for specific botnets

This script is capable of extracting information regarding specific botnets from Vidar Command & Control servers enabling researchers to track campaigns over time.

To find suitable botnets, head over to [Tria.ge Sandbox](https://tria.ge/s?q=family%3avidar). Currently, the extraction of the botnet from samples is unfortunately broken. Due to this, download the PCAP from the analysis of a Vidar sample and search for POST requests which contain an "X-Id" as header. 

![image](https://user-images.githubusercontent.com/9799160/221959914-260e47fd-8193-426f-a96d-49a6485af010.png)

Afterwards, open the script and replace the IP of "c2" and the ID with the X-Id you found.

![image](https://user-images.githubusercontent.com/9799160/221960247-11e74e9c-3f3c-414a-8f25-90b0d7495bb3.png)

Fire up the script and you should get an output similar to this one:

![image](https://user-images.githubusercontent.com/9799160/221960408-3a9a2659-f7d0-4778-84f3-cba4ac3b3ec7.png)


