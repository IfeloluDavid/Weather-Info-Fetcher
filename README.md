**Project Title: Weather Info Fetcher**

Objective: Create a serverless function that fetches and displays current weather information for a given city using a public weather API.

🔍 𝗛𝗲𝗿𝗲'𝘀 𝗵𝗼𝘄 𝗶𝘁 𝘄𝗼𝗿𝗸𝘀:

1️⃣ A static website hosted on an Amazon S3 bucket acts as the user interface, where users enter the name of a city.

2️⃣ The request is routed through an API Gateway, serving as the bridge between the user and backend.

3️⃣ A Lambda function is triggered, fetching the current weather information from OpenWeatherMap's public API.

4️⃣ The result? Instant weather updates delivered back to the user! 🌎🌧️🌞


![Weather Info Fetcher](https://github.com/user-attachments/assets/566a1f22-349e-4348-8c7c-4e1dcce023c0)

## Features
- Accepts a city name from the frontend.
- Retrieves real-time weather information such as temperature and description.
- Displays the information in a user-friendly interface.
- Uses AWS serverless architecture for seamless scalability.

## Prerequisites
- **AWS Account**: To set up Lambda, API Gateway, and S3.
- **Node.js & npm**: For testing and deployment.
- **OpenWeatherMap API Key**: Sign up at [OpenWeatherMap](https://openweathermap.org/api) to get an API key.
- **Basic knowledge of AWS services**.

---

## Steps to Build the Project

### 1. Set Up OpenWeatherMap API
1. Go to [OpenWeatherMap API](https://openweathermap.org/api).
2. Sign up or log in and generate an API key.
3. Keep the API key handy; you'll need it for the Lambda function.

---

### 2. Create the Backend with AWS Lambda
1. **Create a Lambda Function**:
   - Go to the [AWS Management Console](https://aws.amazon.com/console/).
   - Navigate to **Lambda** → **Create Function**.
   - Choose **Author from Scratch**.
   - Function Name: `weatherInfoFetcher`.
   - Runtime: **Python 3.9**.

2. **Write the Lambda Code**: Which is Part of the Files in the Repository

3. **Deploy the Lambda Function**:
   - Save and deploy the function.

4. **Test the Lambda Function**:
   - Test with the following `event`:
     ```json
     {
       "queryStringParameters": {
         "city": "London"
       }
     }
     ```

---

### 3. Configure API Gateway
1. **Create an API Gateway**:
   - Navigate to **API Gateway** → **Create API**.
   - Choose **HTTP API**.

2. **Configure Routes**:
   - Add a new route: `GET /Implementation`.
   - Integrate this route with your Lambda function.

3. **Deploy the API**:
   - Deploy the API to a stage (e.g., `prod`).
   - Note the API endpoint.
Configure the Method
Select the HTTP Method:
Click on the resource (e.g., /weather) that your Lambda function is linked to.
Select the HTTP method (e.g., GET) from the methods under that resource.
Check Method Request:
Click on Method Request.
Under URL Query String Parameters, add city as a parameter:
Click Add query string.
Enter city as the name and save.

4. Configure Integration Request
Click on Integration Request.
Mapping Query String to Lambda:
Scroll to the section Mapping Templates.
Ensure that the Lambda Function is selected as the integration type.
In the Mapping Templates section:
Click Add mapping template.
Enter application/json as the content type and click the checkmark.
Add the following JSON in the mapping template to pass query string parameters to the Lambda function:
json
Copy code
{
    "queryStringParameters": {
        "city": "$input.params('city')"
    }
}


5. Deploy the API
Once the changes are saved:
Click on Actions (top menu).
Select Deploy API.
Choose an existing stage (e.g., prod) or create a new stage (e.g., test).
Click Deploy
---

### 4. Create the Frontend
1. Create an `index.html` file with the file used

   Replace YOUR_API_GATEWAY_URL with your actual API Gateway URL.

Save the file.


Replace YOUR_API_GATEWAY_URL with your actual API Gateway URL.

Save the file.

### 5. Host the Frontend
Use AWS S3:

Create an S3 bucket.
Upload the index.html file.
Enable static website hosting.
Access the Frontend:

Use the S3 website URL to access your frontend.

### 6. Testing
Open your frontend in a browser.
Enter a city name and click "Fetch Weather".
Verify the displayed weather information.
Additional Notes
Ensure CORS is enabled in API Gateway.
Make sure your Lambda function has proper permissions.
For production, secure the API Gateway with authentication.
