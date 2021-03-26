FROM python:3.6
WORKDIR /mnt/scripts/
RUN pip install requests
RUN pip install telegram-send

# COPY . .
# RUN python setup.py install
# RUN python -m unittest
# ENTRYPOINT ["tri_ad"]
