echo "Building postgres"
cd db/postgres
./build.sh
echo "Building core-engine"
cd ../../core_engine
./build.sh
echo "Building datahub"
cd ../datahub
./build.sh
echo "Building label studio"
cd ../label_studio
./build.sh
echo "Building docs"
cd ../docs
./build.sh
echo "All images built"
docker rmi $(docker images | grep "<none>" | awk '{print $3}')