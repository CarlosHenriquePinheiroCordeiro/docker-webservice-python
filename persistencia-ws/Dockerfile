FROM python

RUN pip install CherryPy
RUN pip install requests
RUN pip install pymongo

COPY PersistenciaContatoService.py .
COPY contatos.txt .

EXPOSE 8083

ENTRYPOINT ["python", "PersistenciaContatoService.py"]