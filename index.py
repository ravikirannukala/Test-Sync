from botocore.vendored import requests
import json
import datetime
import cx_Oracle


def handler(event, context):
    response = requests.get('http://www.mocky.io/v2/5ae856682d0000d2077b47dd',stream=True)
    contentType = response.headers['content-type']
    data = response.json()
    cnx = cx_Oracle.connect('hack', 'researchhack',
                                  host='myreaserch.cfe6bx1xwtmf.ap-southeast-2.rds.amazonaws.com:1521/ORCL')
    cur = cnx.cursor()
    # Reset Identity Coulmn
    statement = "insert into `developer_details` (`id`,`name`) VALUES (%s,%s)"
    for i in data['records']:
        print i['id'] + i['name']
        cur.execute(statement,(i['id'],i['name']))
    result = cur.fetchall()
    cnx.commit()
    cnx.close()
    return {'statusCode': 200,
            'body': json.dumps(result),
            'headers': {'Content-Type': 'application/json'}}
