# EC2-Scheduler-Lambda
AWS Lambda function for stopping and starting tagged EC2 instances on a specified schedule

Usage:
Create two function on AWS Lambda for each script. 

Create an appropriate IAM role for Lamda to use having at least start/stop permissions

Specify the stop and start schedule in Lambda as a cron expression. (Refer: https://docs.aws.amazon.com/lambda/latest/dg/tutorial-scheduled-events-schedule-expressions.html)
