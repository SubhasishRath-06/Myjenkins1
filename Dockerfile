#docker image 
FROM python:3.9.19-slim
RUN pip install streamlit 
WORKDIR /var 
COPY dkrETL.py .
EXPOSE 8501
# run a file in cmd
CMD ["streamlit","run","dkrETL.py"]