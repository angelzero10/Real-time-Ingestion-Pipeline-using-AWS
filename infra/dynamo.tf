

resource "aws_dynamodb_table" "aggregated_data" {
  name         = "AggregatedData"
  billing_mode = "PAY_PER_REQUEST"
  hash_key     = "County"
  range_key    = "Timestamp"

  attribute {
    name = "County"
    type = "S"
  }

  attribute {
    name = "Timestamp"
    type = "S"
  }
}
