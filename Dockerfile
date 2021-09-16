FROM python:3.6.15-slim-buster

WORKDIR /app

RUN apt-get update
RUN apt-get install git -y
RUN apt-get install -y libglib2.0-0 libsm6 libxrender1 libxext6
RUN apt-get install python3-tk -y
RUN git clone https://github.com/nodefluxio/vortex.git
RUN cd vortex && git checkout drop-enforce && pip install --ignore-installed --timeout=10000 ./src/runtime[all]

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 80

CMD ["/bin/bash"]