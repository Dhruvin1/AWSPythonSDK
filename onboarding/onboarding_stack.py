from aws_cdk import (
    # Duration,
    Stack,
    aws_ec2 as ec2,
    # aws_sqs as sqs,
)
from constructs import Construct

class OnboardingStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here

        # example resource
        # queue = sqs.Queue(
        #     self, "OnboardingQueue",
        #     visibility_timeout=Duration.seconds(300),
        # )
        self.vpc = ec2.Vpc(self, 'ecs-vpc-ngw',
            cidr = '10.1.0.0/16',
            max_azs=3,
            nat_gateways = 1,
            subnet_configuration = [
                ec2.SubnetConfiguration(
                    subnet_type=ec2.SubnetType.PUBLIC,
                    cidr_mask=24,
                    name = 'ecs-vpc-public'
                ),
                ec2.SubnetConfiguration(
                    subnet_type=ec2.SubnetType.PRIVATE_WITH_NAT,
                    cidr_mask = 24,
                    name = 'ecs-vpc-private'
                )    
            ]
        )
