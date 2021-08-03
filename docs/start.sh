docker run -d \
    -p 8081:80 \
    -e SPEC_URL=http://127.0.0.1:7000/openapi.json \
    -e PAGE_TITLE="osairis API Docs" \
    -e PAGE_FAVICON="https://media.istockphoto.com/vectors/blue-moebius-strip-or-moebius-band-vector-id585291060?k=6&m=585291060&s=612x612&w=0&h=Mmwq27FbLgP_SR5xm5mdDrArMd1NvafMSrDFJLOQgwU=" \
    --name osairis-docs redocly/redoc