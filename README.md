# SAED-Security-At-Edge
SAED is a edge-based platform that enables smart and personalized semantic Enterprise Search service on the cloud
## Introduction
This is an open-source program that offers intelligence in the form of semantic and personalized search at the edge tier
while maintaining privacy of the search on the cloud tier. 
 
## SAED Running Instructions
Here, we uploaded only the plain-text dataset for simplicity of the usage.
1. Download "GoogleNews-vectors-negative300.bin" from [here] (https://drive.google.com/file/d/0B7XkCwpI5KDYNlNUTTlSS21pQmM/edit). and save it in the parent folder "SAED-Security-At-Edge"
2. Open the context_detection_extended.py and input your search query in line, 30.
3. In the executable file, edit line 145 to acess the "GoogleNews-vectors-negative300.bin" file.
4. Save the python file. 
5. Execute it from the terminal. if it needs persmission, please provide that accordingly. 
6. An output file named as weighted_query_"QUERY"_.txt will be formed. 

Assume, the search has been accomplished using the extended query. Cloud outputted search result is available now.
Now, Ranking unit will be utilized to rank the search result. 

7. We have provided a dummy resultant file "demo_initial_result.csv" in the repository.
8. Download BBC dataset (Demo query is considered from BBC dataset). In addition, download link for RFC dataset is also provided. 
9. Modify the following lines of RankingUnit.py:
    i.  Line 28: provide the query that has been already expanded. (It is already loaded with query "windows operating system") 
    ii. Line 17 and 73: provide the link of downloaded dataset.
    
10.Execute RankingUnit.py to get the final search result.
