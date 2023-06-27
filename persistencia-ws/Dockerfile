FROM python

RUN pip install CherryPy

COPY PersistenciaContatoService.py .

EXPOSE 8081

ENTRYPOINT ["python", "PersistenciaContatoService.py"]