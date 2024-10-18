import mysql.connector
from tkinter import messagebox

def Save_Data_MySql(B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R):
    try:
        mydb = mysql.connector.connect(
            host="localhost",
            user = "root",
            password = "345345",
            )
        mycursor = mydb.cursor()
        print("Connected to the database")

    except:
        messagebox.showerror("Error", "Could not connect to the database")

    try:
        command = "CREATE DATABASE Heart_Data"
        mycursor.execute(command)

        command = "USE Heart_Data"
        mycursor.execute(command)

        command = "CREATE TABLE Data (User int auto_increment primary key, Name varchar(50), Date varchar(100), DOB varchar(100), Age varchar(100), Sex varchar(100), Cp varchar(100), trestbps varchar(100), Chol varchar(100), Fbs varchar(100), Restecg varchar(100), Thalach varchar(100), Exang varchar(100), Oldpeak varchar(100), Slope varchar(100), Ca varchar(100), Thal varchar(100), Result varchar(100))"
        mycursor.execute(command)

        command = "INSERT INTO Data (Name, Date, DOB, Age, Sex, Cp, trestbps, Chol, Fbs, Restecg, Thalach, Exang, Oldpeak, Slope, Ca, Thal, Result) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        mycursor.execute(command,(B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R))
        mydb.commit()
        mydb.close()
        messagebox.showinfo("Success", "Data saved to the database")

       
    except:
        mycursor.execute("USE Heart_Data")
        mydb = mysql.connector.connect(
            host="localhost",
            user = "root",
            password = "345345",
            database = "Heart_Data"
            )
        mycursor = mydb.cursor()

        command = "INSERT INTO Data (Name, Date, DOB, Age, Sex, Cp, trestbps, Chol, Fbs, Restecg, Thalach, Exang, Oldpeak, Slope, Ca, Thal, Result) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        mycursor.execute(command,(B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R))
        mydb.commit()
        mydb.close()
        messagebox.showinfo("Success", "Data saved to the database")



 # ebox.showerror("Error", "Could not save data to the database")


# Save_Data_MySql('Nabin Katwal', '08/08/2022' , '1989', '44', '1', '1', '33', '33', '1', '1', '33', '1', '33.0', '0', '2', '1', '0' )

