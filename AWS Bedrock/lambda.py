import json
import boto3

s3 = boto3.client('s3')

bedrock = boto3.client(
    service_name='bedrock', 
    region_name='us-east-1'
)

bedrock_runtime = boto3.client(
    service_name='bedrock-runtime',
    region_name='us-east-1'
)

def bedrockDemo(event, context):
    s3_bucket = event["Records"][0]["s3"]["bucket"]["name"]
    s3_file = event["Records"][0]["s3"]["object"]["key"]

    data = s3.get_object(Bucket=s3_bucket, Key=s3_file)
    contents = data['Body'].read()
    text = contents.decode("utf-8")

    modelId = "ai21.j2-ultra-v1" #In my AWS account - user ak2024_temp. Delete after test. Also delete bucket txt files.
    prompt="I am giving you an article at the end of the prompt, summarize the article. {}".format(text)
    
    body = json.dumps(
        {
            "prompt": prompt, 
            "maxTokens": 2049,
            "temperature": 0.7,
            "topP": 1,
            "stopSequences":[],
            "countPenalty":{"scale":0},
            "presencePenalty":{"scale":0},
            "frequencyPenalty":{"scale":0}
        }
    )

    response = bedrock_runtime.invoke_model(
        body=body,
        modelId=modelId,
        accept='application/json',
        contentType='application/json'
    )
    response_body = json.loads(response.get('body').read())

    answer = json.dumps(response_body.get("completions")[0].get("data").get("text"))
    print("Summarizing the article ------")
    print(answer)
    
    return {
        'statusCode': 200,
        'body': json.dumps({ "Answer": answer })
    }