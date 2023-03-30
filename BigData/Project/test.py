# from elasticsearch import Elasticsearch

# # Create Elasticsearch client instance
# es_client = Elasticsearch(['https://localhost:9200/'],
#                            http_auth= ('elastic','7azPaAh4Jn-9=0q6Nsnt'),
#                            verify_certs=False)

# # Delete all documents in all indices
# es_client.delete_by_query(index="_all", body={"query": {"match_all": {}}})

# # Delete all indices
# es_client.indices.delete(index="restaurant")


from elasticsearch import Elasticsearch

es_client = Elasticsearch(hosts=[{'host':'localhost','port':9200,'scheme':'https'}],
                           http_auth= ('elastic','7azPaAh4Jn-9=0q6Nsnt'),
                           verify_certs=False)

index_name = 'restaurant'

# Define search query to retrieve all documents
query = {"query": {"match_all": {}}}

# Execute the search
result = es_client.search(index=index_name, body=query, size=10000)

# Print the documents
for hit in result['hits']['hits']:
    print(hit['_source'])
    
count = es_client.count(index=index_name)['count']

# print the count
print(f'The number of documents in the index is: {count}')