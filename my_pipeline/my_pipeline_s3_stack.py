import aws_cdk as cdk
from constructs import Construct
from aws_cdk import (
    Duration,
    Stack,
    aws_s3 as s3,
)

class S3Stack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # S3
        bucket_source_images = s3.Bucket(self, 'source-images',
            encryption=s3.BucketEncryption.KMS,
            block_public_access=s3.BlockPublicAccess.BLOCK_ALL,
            removal_policy=cdk.RemovalPolicy.RETAIN,
            object_ownership=s3.ObjectOwnership.BUCKET_OWNER_PREFERRED,
            enforce_ssl=True,
        )

        bucket_scripts = s3.Bucket(self, 'scripts',
            encryption=s3.BucketEncryption.KMS,
            block_public_access=s3.BlockPublicAccess.BLOCK_ALL,
            removal_policy=cdk.RemovalPolicy.RETAIN,
            object_ownership=s3.ObjectOwnership.BUCKET_OWNER_PREFERRED,
            enforce_ssl=True,
        )

        bucket = s3.Bucket(self, 'configs',
            encryption=s3.BucketEncryption.KMS,
            block_public_access=s3.BlockPublicAccess.BLOCK_ALL,
            removal_policy=cdk.RemovalPolicy.RETAIN,
            object_ownership=s3.ObjectOwnership.BUCKET_OWNER_PREFERRED,
            enforce_ssl=True,
        )

