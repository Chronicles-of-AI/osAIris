echo "Starting label-studio"
cd label_studio
./start.sh
echo "Starting postgres"
cd ../db/postgres
./start.sh
echo "Starting core-engine"
cd ../../core_engine
./start.sh
echo "Starting datahub"
cd ../datahub
./start.sh
echo "Starting docs"
cd ../docs
./start.sh
echo "All containers up."