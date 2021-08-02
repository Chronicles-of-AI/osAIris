echo "Starting label-studio"
cd label_studio
./start.sh
echo "Starting postgres"
cd ../db/postgres
./start.sh
echo "Starting core-engine"
cd ../../core_engine
./start.sh $1
echo "Starting datahub"
sleep 10
cd ../datahub
./start.sh $1
echo "Starting docs"
cd ../docs
./start.sh
echo "All containers up."