import boto3
import pprint
from botocore.config import Config
import configparser

config = configparser.ConfigParser()
config.read('config.ini')


my_config = Config(
    region_name = config['AWS link up']['region_name']
)

kendra = boto3.client('kendra', config=my_config,
                      aws_access_key_id=config['AWS link up']['aws_access_key_id'],
                      aws_secret_access_key=config['AWS link up']['aws_secret_access_key']                   
                      )


fi= open (config['DEFAULT']['Weighted_query'], 'r')
all_wq=fi.readlines()
all_filtered_w_q=[]
for i in all_wq:
    all_filtered_w_q.append(i[:i.index(":")]) 


with open(config['DEFAULT']['initial_ranking_file'], 'w') as fii:    
    for query in all_filtered_w_q:
    
        index_id=config['AWS link up']['amazon_index_id']
    
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
    


