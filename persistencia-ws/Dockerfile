FROM python

RUN pip install CherryPy
RUN pip install requests
RUN pip install pymongo

COPY PersistenciaContatoService.py .

EXPOSE 8081

ENTRYPOINT ["python", "PersistenciaContatoService.py"]