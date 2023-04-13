require 'aws-sdk-s3'

client = Aws::S3::Client.new

signer = Aws::S3::Presigner.new
url, headers = signer.presigned_request(
  :get_object, bucket: "bucket", key: "key"
)