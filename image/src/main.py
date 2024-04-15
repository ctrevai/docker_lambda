# basic lambda function handler send back hello world
import numpy as np


def lambda_handler(event, context):
    arr = np.random.randint(0, 10, (3, 3))
    return {
        'statusCode': 200,
        'body': 'Hello from Lambda! again!',
        'array': arr.tolist()}
