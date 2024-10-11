
resource "aws_lambda_function" "aggregation_function" {
  filename         = "lambda_function.zip"
  function_name    = "AggregationFunction"
  role             = aws_iam_role.lambda_role.arn
  handler          = "lambda_function.lambda_handler"
  runtime          = "python3.8"
  timeout          = 30

  source_code_hash = filebase64sha256("lambda_function.zip")

  environment {
    variables = {
      DYNAMODB_TABLE = aws_dynamodb_table.aggregated_data.name
    }
  }
}

resource "aws_lambda_event_source_mapping" "lambda_kinesis" {
  event_source_arn = aws_kinesis_stream.fishing_data_stream.arn
  function_name    = aws_lambda_function.aggregation_function.arn
  starting_position = "LATEST"
}

resource "aws_iam_policy_attachment" "lambda_dynamodb_policy_attachment" {
  name       = "lambda_dynamodb_policy_attachment"
  roles      = [aws_iam_role.lambda_role.name]
  policy_arn = "arn:aws:iam::aws:policy/AmazonDynamoDBFullAccess"
}
