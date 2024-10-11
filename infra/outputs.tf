output "kinesis_stream_name" {
  value = aws_kinesis_stream.fishing_data_stream.name
}

output "lambda_function_name" {
  value = aws_lambda_function.aggregation_function.function_name
}

output "dynamodb_table_name" {
  value = aws_dynamodb_table.aggregated_data.name
}
