#!/bin/bash

# Copy the output files from the container to the local machine
docker cp kind_benz:/home/doc-bd-a1/res_dpre.csv D:/bigdata
docker cp kind_benz:/home/doc-bd-a1/eda-in-1.txt D:/bigdata
docker cp kind_benz:/home/doc-bd-a1/eda-in-2.txt D:/bigdata
docker cp kind_benz:/home/doc-bd-a1/eda-in-3.txt D:/bigdata
docker cp kind_benz:/home/doc-bd-a1/vis.png D:/bigdata
docker cp kind_benz:/home/doc-bd-a1/k.txt D:/bigdata

# Close the container
docker stop  kind_benz
