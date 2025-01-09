# ETL LIst
#image for DOcker 
from streamlit import *
from pandas import *
write('My Project Auto')

data ={
    'Task':['Extract', 'Transform', 'Load'],
    'Status':['Completed', 'InProgress', 'Pending']
}

data_frame =  DataFrame(data)

write('ETL PIPline Execuation Status',data_frame)