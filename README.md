# example-aws-sam-app

This project contains source code and supporting files for a serverless application that you can deploy with the SAM CLI. It includes the following files and folders.

- hello_world - Code for the application's Lambda function.
- events - Invocation events that you can use to invoke the function.
- tests - Unit tests for the application code. 
- template.yaml - A template that defines the application's AWS resources.

## Run locally

```bash
example-aws-sam-app$ sam local invoke HelloWorldFunction --event events/event.json
```

## Build

```bash
example-aws-sam-app$ sam build
```

## Deploy 

```bash
example-aws-sam-app$ sam deploy 
```

## Tests

Tests are defined in the `tests` folder in this project. Use PIP to install the test dependencies and run tests.

```bash
example-aws-sam-app$ pip install -r tests/requirements.txt --user
# unit test
example-aws-sam-app$ python -m pytest tests/unit -v
```

## Resources

See the [AWS SAM developer guide](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/what-is-sam.html) for an introduction to SAM specification, the SAM CLI, and serverless application concepts.

Next, you can use AWS Serverless Application Repository to deploy ready to use Apps that go beyond hello world samples and learn how authors developed their applications: [AWS Serverless Application Repository main page](https://aws.amazon.com/serverless/serverlessrepo/)
