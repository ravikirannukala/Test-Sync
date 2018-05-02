from botocore.vendored import requests
import json
import datetime
import mysql.connector


def handler(event, context):
    response = requests.get('http://www.mocky.io/v2/5ae856682d0000d2077b47dd',stream=True)
    contentType = response.headers['content-type']
    data = response.json()
    print data
    for i in data['records']:
        print "myid" + i['id']
        print "myname" + i['name']
    cnx = mysql.connector.connect(user='ravi', password='test1234',
                                  host='devdb.cfe6bx1xwtmf.ap-southeast-2.rds.amazonaws.com',
                                  database='developer')
    cur = con.cursor()
    # Reset Identity Coulmn
    statement = 'select * from developer'
    cur.execute(statement)
    result = cur.fetchall()
    output = result.json()
    print result
    cnx.close()
    return {'statusCode': 200,
            'body': json.dumps(output),
            'headers': {'Content-Type': 'application/json'}}
