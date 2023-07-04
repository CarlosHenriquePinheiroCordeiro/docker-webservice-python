FROM python

RUN pip install CherryPy
RUN pip install requests
RUN pip install pymongo

COPY PersistenciaContatoService.py .

ENTRYPOINT ["python", "PersistenciaContatoService.py"]