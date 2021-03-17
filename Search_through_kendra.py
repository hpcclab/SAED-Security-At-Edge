import boto3
import pprint
import pandas as pd
from botocore.config import Config

df=pd.read_csv('config.csv',header=None)


my_config = Config(
    region_name = df.iloc[3][1]
)

kendra = boto3.client('kendra', config=my_config,
                      aws_access_key_id=df.iloc[4][1],
                      aws_secret_access_key=df.iloc[5][1]                     
                      )


fi= open ("Weighted_query_internet.txt", 'r')
all_wq=fi.readlines()
all_filtered_w_q=[]
for i in all_wq:
    all_filtered_w_q.append(i[:i.index(":")]) 


with open("initial_ranking.csv", 'w') as fii:    
    for query in all_filtered_w_q:
    
        index_id=df[1][6]
    
        response=kendra.query(
                QueryText = query,
                IndexId = index_id)
        
        print ('\nSearch results for query: ' + query + '\n')        
        
        for query_result in response['ResultItems']:
        
            #print('-------------------')
            #print('Type: ' + str(query_result['Type']))
                
    
        
            if query_result['Type']=='DOCUMENT':
                if 'DocumentTitle' in query_result:
                    document_title = query_result['DocumentTitle']['Text']
                    fii.write(document_title+',')
                    
     
            print ('------------------\n\n')  
    


