# MedApp

#Prerequisites-
1. Download and install Python - https://www.python.org/ftp/python/3.11.0/python-3.11.0-amd64.exe
2. Download and install Anaconda (package manager) - https://repo.anaconda.com/archive/Anaconda3-2022.10-Windows-x86_64.exe
3. Download and insall MySQL and MSQL Workbench - https://dev.mysql.com/downloads/file/?id=514518

Open MySQL workbench and connect to the local instance
then create a database called 'medapp' and create two tables in that database using the SQL scripts

Open Anaconda prompt and navigate to the folder where the repo is cloned
create an new virtual environment using ```conda create --name env1```
then install Flask using ```conda install -c anaconda flask``` and
install mysqldb module using ```pip install flask-mysqldb```

Now run the application using ```python app.py```

