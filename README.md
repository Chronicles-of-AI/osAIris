# osAIris 🔱
## MLOps tool for ALL
## An answer to all your ML Problems.
Complete End-to-End Application for setting up and integrating with products for MLOps
## Offerings
## ML Capabilities
1. AWS Rekognition
2. AWS Comprehend
3. AWS SageMaker
4. GCP AutoML
5. GCP Vertex AI

## Integrations
1. Label Studio -- Annotation tool
2. Redoc --  API Documentations

## Setup Instructions
### Step 1: Clone the repository
```python
git clone git@github.com:Chronicles-of-AI/osAIris.git
```
### Step 2: Setup your cloud credentials
1. AWS: https://chroniclesofai.com/aws-cli-and-sdk-setup-for-devs/
2. GCP: https://chroniclesofai.com/vertex-ai-setup-for-devs/

### Step 3: Navigate to osAIris directory on your local system and build the containers 
Below command will build all the necessary docker containers
```python
sh build_all.sh
```

### Step 4: Wait for the docker images to be pulled/build.⏰

### Step 5: Start the containers 🏁
```python
sh start_all.sh
```

### Step 6: Verify the APIs on 🧐
Open up your browser and check the link below to verify the APIs.
```python
localhost:7000/docs
```

## Housekeeping 🛠

### Application logs 📝
We use python native logging mechanism. For application level logs run
```python
tail -f logs/debug.logs
```

### Docker logs 📊
Run below command to get docker logs
```python
docker compose logs -f
```

### Clean-up 🧴
Run below command to bring down all the Docker containers
```python
docker compose down
```

### Restart 🏁
Run below command to restart all your docker containers
```python
./restart_all.sh
```
