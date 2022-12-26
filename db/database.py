import boto3
from boto3.dynamodb.conditions import Key

from botocore.exceptions import ClientError


class DatabaseServices:
    def __init__(self, session: boto3.resource):
        self.session = session
        self.table = self.create_dynamodb_table()

    def create_dynamodb_table(self):
        table_name = 'cryptoNews'
        key_schema = [
            {
                'AttributeName': 'link',
                'KeyType': 'HASH'
            },
            {
                'AttributeName': 'title',
                'KeyType': 'RANGE'
            }
        ]
        attribute_definitions = [
            {
                'AttributeName': 'link',
                'AttributeType': 'S'
            },
            {
                'AttributeName': 'title',
                'AttributeType': 'S'
            },
        ]
        provisioned_throughput = {
            'ReadCapacityUnits': 5,
            'WriteCapacityUnits': 5
        }

        try:
            table = self.session.create_table(TableName=table_name,
                                              KeySchema=key_schema,
                                              AttributeDefinitions=attribute_definitions,
                                              ProvisionedThroughput=provisioned_throughput)
            table.wait_until_exists()
        except ClientError:
            table = self.session.Table(table_name)
        return table

    def check_if_news_is_processed(self, link: str) -> bool:
        return len(self.table.query(KeyConditionExpression=Key('link').eq(link))['Items']) > 0

    def add_news_to_table(self, news: list[str]) -> None:
        self.table.put_item(Item={'link': news[1], 'title': news[0]})
