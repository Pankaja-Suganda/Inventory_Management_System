FROM python:3.9
LABEL maintainer="Inventory-Management-System"

ENV PYTHONUNBUFFERED 1

# COPY manage.py gunicorn-cfg.py requirements.txt .ims_env ./
# COPY app app
# COPY authentication authentication
# COPY core core
# COPY customer customer
# COPY dashboard dashboard
# COPY invoice invoice
# COPY materials materials
# COPY pre_sales_order pre_sales_order
# COPY purchase_order purchase_order
# COPY quotation quotation
# COPY sales_order sales_order
# COPY stock stock
# COPY supplier supplier
COPY . .


EXPOSE 8000

RUN pip install virtualenv

RUN python -m virtualenv ims_env
RUN ./ims_env/Scripts/activate


RUN pip install --upgrade pip
RUN pip install -r requirements.txt

RUN python manage.py makemigrations
RUN python manage.py migrate
