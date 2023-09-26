from fastapi import FastAPI, HTTPException

from fastapi.middleware.cors import CORSMiddleware

from pydantic import BaseModel

import mysql.connector


 

app = FastAPI()

 

origins = ["http://localhost:3000",

           "http://3.26.145.126:3000" # Add the actual URL of your frontend

# Add other allowed origins if needed

]

app.add_middleware(

    CORSMiddleware,

    allow_origins=origins,

    allow_credentials=True,

    allow_methods=["*"],

    allow_headers=["*"],

)

 

class EmployeeCreate(BaseModel):

    Sign_up_as: str

    Salutation: str

    First_name: str

    Last_name: str

    Contact_number: str

    Email_id: str

    Address: str

    Login_username: str

    Login_password: str

 

def connect_to_mysql_server():

    try:

        host = 'fsa.cbukmbi4p5zb.ap-southeast-2.rds.amazonaws.com'

        user = 'admin'

        password = 'password12345'

        database = 'fsa_database'

 

        connection = mysql.connector.connect(

            host=host,

            user=user,

            password=password,

            database=database

        )

 

        if connection.is_connected():

            print("Connected to MySQL server!")

            return connection

 

    except mysql.connector.Error as err:

        print("Error:", err)

        return None

   

def insert_data(connection, registration):

    try:

        if connection.is_connected():

            cursor = connection.cursor()

            query = "INSERT INTO registration (Sign_up_as, Salutation, First_name, Last_name, Contact_number, Email_id, Address, Login_username, Login_password) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);"

            values = (registration.Sign_up_as, registration.Salutation, registration.First_name, registration.Last_name, registration.Contact_number, registration.Email_id, registration.Address, registration.Login_username, registration.Login_password)

            cursor.execute(query, values)

            connection.commit()

            cursor.close()

            return True

    except mysql.connector.Error as err:

       

        print("Error:", err)

        return False

   

 

 

def query_data(connection):

    results = []

    try:

        if connection.is_connected():

            cursor = connection.cursor()

            query = "SELECT * FROM registration;"

            cursor.execute(query)

            results = cursor.fetchall()  # Read the result set

            cursor.close()

    except mysql.connector.Error as err:

        print("Error:", err)

 

    return results

 

@app.get("/")

def read_root():

    return {"Hello": "World"}

 

   

 

@app.post("/create_data")

async def create_employee(registration: EmployeeCreate):

    connection = connect_to_mysql_server()

 

    if connection:

        success = insert_data(connection, registration)

        if success:

            return {"message": "created successfully"}

        else:

            raise HTTPException(status_code=500, detail="Failed to create employee")

    else:

        raise HTTPException(status_code=500, detail="Database connection error")

   

 

class LoginCredentials(BaseModel):

    Login_username: str

    Login_password: str

 

@app.post("/login")

async def login_user(credentials: LoginCredentials):

    connection = connect_to_mysql_server()

 

    if connection:

        user_data = fetch_user_by_username_and_password(connection, credentials.Login_username, credentials.Login_password)

       

        if user_data:

            return {"message": "Login successful"}

        else:

            raise HTTPException(status_code=401, detail="Invalid credentials")

    else:

        raise HTTPException(status_code=500, detail="Database connection error")

 

def fetch_user_by_username_and_password(connection, username, password):

    user_data = {}

    try:

        if connection.is_connected():

            cursor = connection.cursor(dictionary=True)

            query = "SELECT * FROM registration WHERE Login_username = %s AND Login_password = %s;"

            cursor.execute(query, (username, password))

            user_data = cursor.fetchone()

            cursor.close()

    except mysql.connector.Error as err:

        print("Error:", err)

 

    return user_data

 

class RegisterCreate(BaseModel):

    Child_Name: str

    Age: int

    Gender: str

    Child_Address: str

    Date_Of_Birth: str

    Parent_Name: str

    Parent_Contact: str

    Passport_Photo: str

    Adhar_Card: str

    Choice_Of_Academy: str

    Batchs: str

    Subscription: str

    Fees_Structure: int

    Sports_played_by_the_child_currently: str

    Any_Formal_Coaching_taken_for_the_football: str

    Academy: str

    Duration: str

    Position_played: str

    Any_major_injuries_fractures_in_the_past:str

    Fracture: str

    Any_Allergies: str

    Allergies: str

    Prevailing_ailments_medical_conditions: str

    Blood_Pressure: str

    Allergic_rhinitis: str

    Breathing_difficulty: str

   

   

 

def insert_register(connection, register):

    try:

        if connection.is_connected():

            cursor = connection.cursor()

            query = "INSERT INTO Child (Child_Name, Date_Of_Birth, Age, Gender, Child_Address, Parent_Name, Parent_Contact, Passport_Photo, Adhar_Card, Choice_Of_Academy, Batchs, Subscription, Fees_Structure, Sports_played_by_the_child_currently, Any_Formal_Coaching_taken_for_the_football, Academy, Duration, Position_played, Any_major_injuries_fractures_in_the_past, Fracture, Any_Allergies, Allergies, Prevailing_ailments_medical_conditions, Blood_Pressure, Allergic_rhinitis, Breathing_difficulty) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"

            values = (register.Child_Name, register.Date_Of_Birth, register.Age, register.Gender, register.Child_Address, register.Parent_Name, register.Parent_Contact, register.Passport_Photo, register.Adhar_Card, register.Choice_Of_Academy, register.Batchs, register.Subscription, register.Fees_Structure, register.Sports_played_by_the_child_currently, register.Any_Formal_Coaching_taken_for_the_football, register.Academy, register.Duration, register.Position_played, register.Any_major_injuries_fractures_in_the_past, register.Fracture, register.Any_Allergies, register.Allergies, register.Prevailing_ailments_medical_conditions, register.Blood_Pressure, register.Allergic_rhinitis, register.Breathing_difficulty)

            cursor.execute(query, values)

            connection.commit()

            cursor.close()

            return True

    except mysql.connector.Error as err:

        print("Error:", err)

        return False

   

 

def query_register(connection):

    results = []

    try:

        if connection.is_connected():

            cursor = connection.cursor()

            query = "SELECT * FROM Child;"

            cursor.execute(query)

            results = cursor.fetchall()

            cursor.close()

    except mysql.connector.Error as err:

        print("Error:", err)

 

    return results

 

@app.post("/Register_data")

async def create_register(register: RegisterCreate):

    connection = connect_to_mysql_server()

 

    if connection:

        success = insert_register(connection, register)  # Use insert_register here

        if success:

            return {"message": "Registration created successfully"}

        else:

            raise HTTPException(status_code=500, detail="Failed to create registration")

    else:

        raise HTTPException(status_code=500, detail="Database connection error")

 