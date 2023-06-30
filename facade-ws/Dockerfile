FROM python

RUN pip install CherryPy
RUN pip install requests

COPY FacadeService.py .

EXPOSE 8081

ENTRYPOINT ["python", "FacadeService.py"]