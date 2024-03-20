# AWS Infrastructure for Generating Thumbnails

In this repository, you will find the definition of a basic infrastructure on AWS using AWS CloudFormation for thumbnail generation. It utilizes a serverless infrastructure with a Lambda function that responds to the POST event of the bucket where the image to be thumbnailized arrives.

## Test

### thumbnail_generator.py

This code is a test of the lambda function locally.

## Resources

### S3Bucket

This resource defines an S3 bucket in AWS.

### ThumbnailFunction 

This resource defines a Lambda function in AWS, which acts as an image thumbnail generator.

### LambdaExecutionRole

This resource defines the execution role for the Lambda function.

### S3EventPermission

This resource defines permissions for the S3 bucket to notify the Lambda function when an object is created.

### ThumbnailFunctionTrigger

This resource defines the notification configuration of the S3 bucket to invoke the Lambda function when an object is created.
