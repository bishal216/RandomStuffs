from flask import Flask, request, render_template, jsonify,url_for,redirect
from pymongo import MongoClient
from elasticsearch import Elasticsearch

# Set up MongoDB client
connection_string = 'mongodb+srv://Bellatrix:Hello123@bookdb.ynryira.mongodb.net/?retryWrites=true&w=majority'
mongo_client = MongoClient(connection_string)
mongo_db = mongo_client['sample_restaurants']
mongo_collection = mongo_db['restaurants']

# # Set up Elasticsearch client
es_client = Elasticsearch(hosts=[{'host':'localhost','port':9200,'scheme':'https'}],
                           basic_auth= ('elastic','7azPaAh4Jn-9=0q6Nsnt'),
                           verify_certs=False)
index_name = "restaurant"

index_body = {
    "mappings": {
        "properties": {
            "name": {"type": "text"},
            "address": {
                "properties": {
                    "building": {"type": "text"},
                    "coord": {"type": "geo_point"},
                    "street": {"type": "text"},
                    "zipcode": {"type": "text"},
                    "borough": {"type": "text"}
                }
            },
            "cuisine": {"type": "text"}
        }
    }
}
if not es_client.indices.exists(index = index_name):
    es_client.indices.create(index=index_name, body=index_body)
    Mentries = mongo_collection.find()
    
    documents = []
    for entry in Mentries:
        doc = {
        "name": entry["name"],
        "borough": entry["borough"],
        "cuisine": entry["cuisine"],
        "address": {
            "building": entry["address"]["building"],
            "street": entry["address"]["street"],
            "zipcode": entry["address"]["zipcode"]            
        }
        }
        documents.append(doc)
    # Index transformed data into Elasticsearch index
    for i, doc in enumerate(documents):
        es_client.index(index=index_name, id=i, body=doc)

# Set up Flask app
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/all')
def dispAll():
    entries = mongo_collection.find()
    return render_template('entries.html', entries=entries)

@app.route('/submit', methods=['POST'])
def submit():
    query = request.form['query']
    return redirect(url_for('search',query=query))

@app.route('/search', methods=['GET', 'POST'])
def search():
    data = request.args.get('query')
    query = {
        "query": {
            "match": {
                "cuisine": data
            }
        }
    }
    result = es_client.search(index=index_name, body=query)
    hits = result["hits"]["hits"]
    response = [
        {
            "name": hit["_source"]["name"],
            "cuisine": hit["_source"]["cuisine"],
            "borough": hit["_source"]["borough"],
            "address": hit["_source"]["address"]
        }
        for hit in hits
    ]   
    return render_template('entries.html', entries=response) 
    # return jsonify({"restaurants": response}), 200

if __name__ == '__main__':
    app.run(debug=True)