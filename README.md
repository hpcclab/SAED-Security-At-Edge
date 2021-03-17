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

Architectural overview of SAED within the edge tier and (as part of the three-tier enterprise search service) is shown below. SAED provides semantic search via identifying the query context (Context Identifier module) and combining that with the user’s interests (Interest Detector module). Then, the Query Expansion module and the Weighting unit of SAED, respectively, incorporate the semantic and assure the relevancy of the results. Solid and dashed lines indicate the interactions from the user to the cloud tier and from the cloud tier to the user, respectively.
<p align="center"><img src="archi.png"></p>

## SAED Running Instructions

Here, we uploaded only the plain-text dataset for simplicity of the usage.
1. Clone this project in your machine via git clone.
2. Download pre-trained "GoogleNews-vectors-negative300.bin" W2V model from [here](https://drive.google.com/file/d/0B7XkCwpI5KDYNlNUTTlSS21pQmM/edit).
3. Download ```BBC``` dataset (Demo query is considered from BBC dataset). In addition, download link for RFC dataset is also provided.
4. Open ```config.csv file``` to provide dataset name (BBC/RFC), W2V model location, AWS region, access key id, secret access key, kendra index id. We have already loaded a demo query and user interest, and initial ranking file.     
5. Run ```context_detection_extended.py```. If it needs execution persmission, please provide that accordingly. 
   1. Example: ```chmod a+x context_detection_extended.py``` 
               ```python3 context_detection_extended.py```
6. An output file named as ```weighted_query_"QUERY"_.txt``` will be formed. 
7. Update ```config.csv``` file with the newly generated weighted query file. Note that, we have already provided a demo file based on the demo query and interest.
8. We have provided an interface to facilitate search through AWS Kendra. Run ```Search_through_kendra.py```. If it needs execution persmission, please provide that accordingly. Before running the file, please check ```config.csv``` again and make sure that AWS related information have been provided correctly. 
   1. Example: ```chmod a+x Search_through_kendra.py```
   2. ```python3 Search_through_kendra.py```      
9. After running the file, Cloud (AWS Kendra) outputted search result is saved in ```initial_ranking.csv``` file.
10. Now, Ranking unit will be utilized to get the final search result. Run ```RankingUnit.py```. If it needs execution persmission, please provide that accordingly. 
   1. Example: ```chmod a+x RankingUnit.py```
11. The final search result will be shown in the terminal. 
