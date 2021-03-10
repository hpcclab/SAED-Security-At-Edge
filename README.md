# SAED-Security-At-Edge
SAED is an edge-based platform that offers intelligence in the form of privacy-preserving semantic and personalized search at the edge tier to augment the capabilities of the Enterprise Search services on the cloud. SAED can be plugged in to any cloud-based enterprise search solution (e.g., AWS Kendra) and extend their smartness and privacy wihtout enforcing any change on them. SAED is the first platform that develops the idea of **logical partitioning of applications across edge-to-cloud continuum** in the context of a privacy-preserving search application. In particular, to preserve the user's privacy, SAED decouples the intelligence aspect of the semantic search algorithm (and performs it on a trusted edge tier) from its pattern matching aspect (that is performed on the untrusted public cloud tier).

## Availability
SAED is an open-source program that was developed at HPCC lab, University of Louisiana Lafayette. Details of its theory, implementation, and evaluation have been published in 21st IEEE/ACM International Symposium on Cluster, Cloud, and Grid Computing (CCGrid 2021) in Melbourne, Australia. 
The research paper is also available on the arXiv repository:
https://arxiv.org/abs/2102.13367

Users of this open-source platform are requested to cite the following paper in their publications:
 ````
 @inproceedings{zobaedsaed2021,
  title={SAED: Edge-Based Intelligence for Privacy-Preserving Enterprise Search on the Cloud},
  author={Zobaed, Sakib M, and Amini Salehi, Mohsen and Buyya, Rajkumar}
  booktitle={Proceedings of the 21st International Symposium on Cluster, Cloud, and Grid Computing},
  series={CCGRID'21},
  year={2021},
  month={May}
}
 ````
 
## Architecture

Architectural overview of the SAED system within edge tier and as part of the three-tier enterprise search service is hown below. SAED provides semantic search via identifying the query context and combining that with the user’s interests. Then, Query Expansion and Weighting unit of SAED, respectively, incorporate the semantic and assure the relevancy of the results. Solid and dashed lines indicate the interactions from user to the cloud tier and from the cloud tier to the user respectively.
<p align="center"><img src="archi.png"></p>

## SAED Running Instructions

Here, we uploaded only the plain-text dataset for simplicity of the usage.
1. Download "GoogleNews-vectors-negative300.bin" from [here] (https://drive.google.com/file/d/0B7XkCwpI5KDYNlNUTTlSS21pQmM/edit). and save it in the parent folder "SAED-Security-At-Edge".
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
