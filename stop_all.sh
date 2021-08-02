echo "stoping postgres"
cd db/postgres
./stop.sh
echo "stoping core-engine"
cd ../../core_engine
./stop.sh
echo "stoping datahub"
cd ../datahub
./stop.sh
echo "stoping label-studio"
cd ../label_studio
./stop.sh
echo "stoping docs"
cd ../docs
./stop.sh
echo "All containers down"