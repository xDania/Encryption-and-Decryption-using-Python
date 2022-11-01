# Encryption and Decryption using Python
<img src="https://user-images.githubusercontent.com/78479020/199277605-114c381a-cd70-46ff-a1cd-b65da9a62fbf.png" width=90% height=60%>

## Project idea
Encryption and Decryption using Python where the user can encrypt and decrypt the text they want. First by clicking on Create Secret Messages a window will pop up with two text boxes where the user type the text they want to encrypt then type the key and click on encrypt and it will show the encrypted message, for the decryption it is the same but the user should decrypt a message that is encrypted earlier and choose the decrypt option. 

## Install 
```
pip install pybase64
pip install mysql-connector-python
pip install mysql-connector
```
# Database
Here is a database that store the encryption and decryption messages
## storing ecryption in the database 
```
      def stor_data():

            connection = mysql.connector.connect(host='127.0.0.1',
                                                 database='pypro',
                                                 user='root',
                                                 password='12345678')
            mycursor = connection.cursor()

            sql = "INSERT INTO info (text1,text2) VALUES (%s,%s)"

            info = (str(message2), str(encry))

            mycursor.execute(sql, info)

            connection.commit()

```
## storing decryption in the database 
        def stor_data2():

            connection = mysql.connector.connect(host='127.0.0.1',
                                                 database='pypro',
                                                 user='root',
                                                 password='12345678')
            mycursor = connection.cursor()

            sql = "INSERT INTO info (text1,text2) VALUES (%s,%s)"

            info = (str(message1), str(decry))

            mycursor.execute(sql, info)

            connection.commit()
           
            
## Output 


https://user-images.githubusercontent.com/78479020/199266304-0602bda1-a5db-4491-8cb7-89c54d2142a5.mov


## References 
https://www.youtube.com/watch?v=y9cbTf1CLt8
