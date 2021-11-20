FROM python:buster
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . .
RUN git clone https://github.com/x-hw/amazing-qr.git
RUN python prepare_library.py
WORKDIR /app/amazing-qr
RUN python setup.py install
WORKDIR /app
ENTRYPOINT ["python"]
CMD ["main.py"]
