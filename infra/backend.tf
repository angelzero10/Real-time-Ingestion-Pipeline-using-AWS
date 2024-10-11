terraform {
  backend "s3" {
    bucket = "luis-ayala-pipeline-20241011-terraform"
    key    = "terraform.tfstate"
    region = "ap-northeast-1"
  }
}
