FROM python

RUN pip install CherryPy

COPY FacadeService.py .

EXPOSE 8081

ENTRYPOINT ["python", "FacadeService.py"]