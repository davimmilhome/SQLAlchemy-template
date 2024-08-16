
# SQLAlchemy template

This is a template for connect and extract data from DBMS using SQLAlchemy and Pyodbc.

--- 
The program are structured at this way: 

<pre>

│   .env 
│   .env.example 
│   .gitignore 
│    main.py 
│    requirements.txt 
│
├───cfg 
│       database.py 
│
├───output 
│       .gitkeep
│ 
└───scripts
    │   .gitkeep
    │
    ├───python
    │       script_example.py
    │
    └───queries
            querie_example.py
            
</pre>

**Where:**

database.py - responsible for setup the connection with DB </br>

output/ -  used for put output files from your exctract  </br>

scripts -  folder that cotains your procedures, functions, querrys that will be called at the main.py </br>

main.py - Program start point </br>

.env - contains your connection and other envriomment variables. You will need to create that based on .env.example </br>

requirements.txt - python packages setup </br>

## Dependencies

 - SQLAlchemy
 - pyodbc
 - python-dotenv
 - pandas (optional)

## Using

Clone this project and install the dependencies at requirements.txt
</br>

Setup your querrys and call them on main.py using the connection as the example on code.
</br>

Treat your data using your procedures on scripts/
</br>

Save/export your data as you like :)
</br>

## Authors
Davi Milhome
