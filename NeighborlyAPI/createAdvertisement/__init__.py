import azure.functions as func
import pymongo
import requests

def main(req: func.HttpRequest) -> func.HttpResponse:

    request = req.get_json()

    if request:
        try:
            url = "mongodb://dbsa:jXW5MVLsyMHOc1fHuu2tKQsOVyR7DPMCVjJa4Yeu57AliT9UbamL0CgVuLaOno2OlsmJIlwC4wB8ACDbHtzcSw==@dbsa.mongo.cosmos.azure.com:10255/?ssl=true&retrywrites=false&replicaSet=globaldb&maxIdleTimeMS=120000&appName=@dbsa@"  # TODO: Update with appropriate MongoDB connection information
            client = pymongo.MongoClient(url)
            database = client['project2']
            collection = database['advertisements']

            rec_id1 = collection.insert_one(eval(request))
            logic_app_url = "https://prod-91.eastus.logic.azure.com:443/workflows/c0c21e51dc1940849c07195cde9601be/triggers/manual/paths/invoke?api-version=2016-10-01&sp=%2Ftriggers%2Fmanual%2Frun&sv=1.0&sig=RJATPSSxVg-Zp9hqQd4RuDmIh6Gy_w2mIlwMGKARafo"
            response = requests.get(logic_app_url)
            return func.HttpResponse(req.get_body())

        except ValueError:
            print("could not connect to mongodb")
            return func.HttpResponse('Could not connect to mongodb', status_code=500)

    else:
        return func.HttpResponse(
            "Please pass name in the body",
            status_code=400
        )