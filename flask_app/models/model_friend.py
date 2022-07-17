# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL

#model the class after the appropriate table from our database
#Note: we will need to call on the connectToMySQL function every time we want
#to execute a query because our connection closes as soon as the query
#finishes executing.
class Friend:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.occupation = data['occupation']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    #Now we use class methods to query our database
    @classmethod
    def create_one(cls, data):
        query = "INSERT INTO friends (first_name, last_name, occupation, created_at, updated_at) VALUES (%(first_name)s, %(last_name)s, %(occupation)s, NOW(), NOW() );"
        return connectToMySQL("basic_python_project_db").query_db(query, data);

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM friends"
        # Make sure to call the connectToMySQL function with the schema and table you are targeting
        results = connectToMySQL('basic_python_project_db').query_db(query)
        #Create an empty list to append our instances to
        friends = []
        # Iterate over the db results and create instances of friends with cls
        for friend in results:
            friends.append(cls(friend))
        return friends
        
