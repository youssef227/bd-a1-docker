FROM ubuntu:latest

RUN apt-get update && \
    apt-get install -y python3 python3-pip && \
    pip3 install pandas numpy seaborn matplotlib scikit-learn scipy

RUN mkdir /home/doc-bd-a1

COPY dataset.csv /home/doc-bd-a1

WORKDIR /home/doc-bd-a1

CMD ["bash"]
