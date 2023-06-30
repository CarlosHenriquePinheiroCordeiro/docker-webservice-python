FROM python

RUN pip install CherryPy
RUN pip install requests

COPY BoContatoService.py .

EXPOSE 8082

ENTRYPOINT ["python", "BoContatoService.py"]