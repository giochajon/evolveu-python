import psycopg2
import multip

try:
    connection = psycopg2.connect(user = "postgres",password = "postgres",host = "192.168.1.74",port = "5432",database = "cgyinfo")
    cursor = connection.cursor()
    cursor2 = connection.cursor()
    # Print PostgreSQL Connection properties
    #print ( connection.get_dsn_parameters(),"\n")
    

    # Print PostgreSQL version
    #cursor.execute("SELECT version();")
    cursor.execute("select comm_code, multipolygon from census2018")
    #record = cursor.fetchone()
    records = cursor.fetchall()
    for record in records:
    	x = record[0]
    	y = record[1]
    	z = multip.multip2google(y)
    	w = multip.getcenter(z)
    	cursor2.execute("UPDATE census2018 SET gcoord=(%s) WHERE comm_code = (%s)", (z,x,));
    	cursor2.execute("UPDATE census2018 SET gcenter=(%s) WHERE comm_code = (%s)", (w,x,));
    	connection.commit()






    
    
except (Exception, psycopg2.Error) as error :
    print ("Error while connecting to PostgreSQL", error)
finally:
    #closing database connection.
        if(connection):
            cursor.close()
            cursor2.close()
            connection.close()
            print("PostgreSQL connection is closed")