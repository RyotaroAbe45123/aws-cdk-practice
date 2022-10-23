import os

import aws_cdk as cdk
from constructs import Construct
from aws_cdk import (
    aws_lambda as _lambda,
    aws_dynamodb as dynamodb
)
from aws_cdk.aws_apigateway import (
    RestApi,
    LambdaIntegration
) 

class AWSService(Construct):
    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        #  create dynamo table
        table = dynamodb.Table(
            self, "usertable",
            table_name= 'Users',
            partition_key=dynamodb.Attribute(
                name="id",
                type=dynamodb.AttributeType.STRING
            )
        )

        # create Lambda Function
        getAllLambda = _lambda.Function(self, 'ApiLambda',
            handler='lambda_handler.handler',
            function_name='usersFunction',
            runtime=_lambda.Runtime.PYTHON_3_7,
            code=_lambda.Code.from_asset('resources'))

        getAllLambda.add_environment("TABLE_NAME", table.table_name)
        
        # Grant Permission to Lambda function
        table.grant_read_write_data(getAllLambda)

        # create API Gateway
        api = RestApi(self, "users-api")
        
        users = api.root.add_resource("users")
        get_users_integration = LambdaIntegration(getAllLambda)
        users.add_method("GET", get_users_integration)