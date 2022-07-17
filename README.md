# Flask Set Up Instructions
In this example my project name is, **basic_python_project**

## Create new project folder and set up virtual environmnent
1. In terminal, navigate to where you want to place your project folder and create project directory `mkdir basic_python_project`
2. Navigate to newly created project folder, `cd basic_python_project`
3. Set up virtual environment. In this case we will be using flask, and mysql. `pipenv install PyMySQL flask`. _Double check that you are in the project folder when you do this!_
4. Create a **.gitignore** file
5. Create **mysqlconnection.py** file.
```py
# a cursor is the object we use to interact with the database
import pymysql.cursors # DELETE COMMENT WHEN RESOLVED See 'reportMissingModuleSource' https://github.com/microsoft/pylance-release/blob/main/DIAGNOSTIC_SEVERITY_RULES.md#diagnostic-severity-rules

class MySQLConnection:
    def __init__(self,db):
        connection = pymysql.connect(host = 'localhost',
                                    user='root',
                                    password='rootroot',
                                    db=db,
                                    charset='utf8mb4',
                                    cursorclass=pymysql.cursors.DictCursor,
                                    autocommit=True)
        # Establish connection to the database
        self.connection = connection

    def query_db(self, query, data=None):
        with self.connection.cursor() as cursor:
            try:
                query = cursor.mogrify(query, data)
                print("Running Query:", query)

                cursor.execute(query, data)
                if query.lower().find("insert") >= 0:
                    #Insert queries will return the ID NUMBER of the row

                    self.connection.commit()
                    return cursor.lastrowid
                elif query.lower().find("select") >= 0:
                    #Select queries will return the data in a list of dictionaries

                    result = cursor.fetchall()
                    return result
                else:
                    # Update and Delete quereies will return nothing
                    self.connection.commit()
            
            except Exception as e:
                # if the query fails, the method will return False
                print("Something went wrong", e)
                return False
            finally:
                # Close the connection
                self.connection.close()

# connectToMySQL receives the database we're using and uses it to create an 
# instance of MySQL CONNECTION
def connectToMySQL(db):
    return MySQLConnection(db)
```

