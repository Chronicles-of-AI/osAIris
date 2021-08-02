echo $1
if [ $1 == "aws" ]
then
    docker run -d \
        -p 5000:5000 \
        -e AWS_SECRET_ACCESS_KEY=${AWS_SECRET_ACCESS_KEY} \
        -e AWS_ACCESS_KEY_ID=${AWS_ACCESS_KEY_ID} \
        -e AWS_DEFAULT_REGION="us-east-2" \
        -v "$(pwd)":/app \
        --env-file env_var \
        --network synapse-bridge \
        --name synapse-core synapse-core
elif [ $1 == "gcp" ]
then
    docker run -d \
        -p 5000:5000 \
        -e AWS_DEFAULT_REGION="us-east-2" \
        -e GOOGLE_APPLICATION_CREDENTIALS="/app/data/google_credential.json" \
        -v "$(pwd)":/app \
        -v ${GOOGLE_APPLICATION_CREDENTIALS}:/app/data/google_credential.json \
        --env-file env_var \
        --network synapse-bridge \
        --name synapse-core synapse-core
else
    echo "Cloud platform provided is neither aws or gcp"
fi