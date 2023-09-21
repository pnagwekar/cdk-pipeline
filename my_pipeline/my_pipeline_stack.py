import aws_cdk as cdk
from constructs import Construct
from aws_cdk.pipelines import CodePipeline, CodePipelineSource, ShellStep
from my_pipeline.my_pipeline_app_stage import MyPipelineAppStage
from aws_cdk.pipelines import ManualApprovalStep

class MyPipelineStack(cdk.Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        pipeline =  CodePipeline(self, "Pipeline",
                        pipeline_name="CDKPipeline",
                        synth=ShellStep("Synth",
                            input=CodePipelineSource.git_hub("pnagwekar/cdk-pipeline", "main"),
                            commands=["npm install -g aws-cdk",
                                "python -m pip install -r requirements.txt",
                                "cdk synth"]
                        )
                    )

        testing_stage = pipeline.add_stage(MyPipelineAppStage(self, "infrastructure-Deploy",
            env=cdk.Environment(account="299344511603", region="us-east-1")))

        testing_stage.add_post(ManualApprovalStep('approval'))
