FROM python

RUN pip install CherryPy

COPY PersistenciaContatoService.py .

EXPOSE 8083

ENTRYPOINT ["python", "PersistenciaContatoService.py"]