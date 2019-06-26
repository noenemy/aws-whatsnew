import boto3
import json

dynamodb = boto3.resource('dynamodb', region_name='ap-northeast-2')

def create_table ():
    table = dynamodb.create_table(
        TableName='whatsnew_archive',
        KeySchema=[
            {
                'AttributeName': 'year',
                'KeyType': 'HASH'  #Partition key
            },
            {
                'AttributeName': 'title',
                'KeyType': 'RANGE'  #Sort key
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'year',
                'AttributeType': 'N'
            },
            {
                'AttributeName': 'title',
                'AttributeType': 'S'
            }
        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 10,
            'WriteCapacityUnits': 10
        }
    )
    
def scan_table_allpages(table_name, filter_key=None, filter_value=None):
    
    table = dynamodb.Table(table_name)

    if filter_key and filter_value:
        filtering_exp = Key(filter_key).eq(filter_value)
        response = table.scan(FilterExpression=filtering_exp)
    else:
        response = table.scan()

    items = response['Items']
    while True:
        print len(response['Items'])
        if response.get('LastEvaluatedKey'):
            response = table.scan(ExclusiveStartKey=response['LastEvaluatedKey'])
            items += response['Items']
        else:
            break

    return items
    
def add_new_article(table_name, title, year, url, posted_date):
    
    
    table = dynamodb.Table(table_name)
    
    response = table.put_item(
       Item={
            'year': year,
            'title': title,
            'url': url,
            'posted_date': posted_date
        }
    )


'''
create_table()
'''

add_new_article('whatsnew_archive', 'Amazon FSx for Windows File Server now enables you to use a single AWS Managed AD with file systems across VPCs or accounts', 2019, 'https://aws.amazon.com/about-aws/whats-new/2019/06/amazon-fsx-for-windows-file-server-now-enables-you-to-use-a-single-aws-managed-ad-with-file-systems-across-vpcs-or-accounts/', '2019-06-25')

rows = scan_table_allpages('whatsnew_archive')
for row in rows:
    print row
