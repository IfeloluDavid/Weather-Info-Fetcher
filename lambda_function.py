import json
import urllib.request

def lambda_handler(event, context):
    # Get the city parameter from the query string
    city = event["queryStringParameters"].get("city", "London")  # Default to London if no city is provided
    api_key = "INSERT API KEY"
    base_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    try:
        with urllib.request.urlopen(base_url) as response:
            data = json.load(response)
        
        if data.get("cod") != 200:
            return {
                "statusCode": 400,
                "body": json.dumps({"error": data.get("message", "Error fetching data")})
            }
        
        weather_info = {
            "city": data["name"],
            "temperature": data["main"]["temp"],
            "description": data["weather"][0]["description"]
        }

        return {
            "statusCode": 200,
            "body": json.dumps(weather_info)
        }
    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }
