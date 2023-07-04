FROM python

RUN pip install CherryPy
RUN pip install requests

COPY FacadeService.py .

ENTRYPOINT ["python", "FacadeService.py"]