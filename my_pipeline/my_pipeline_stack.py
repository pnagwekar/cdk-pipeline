import aws_cdk as cdk
from constructs import Construct
from aws_cdk.pipelines import CodePipeline, CodePipelineSource, ShellStep
from my_pipeline.my_pipeline_app_dev_stage import MyPipelineAppDevStage
from aws_cdk.pipelines import ManualApprovalStep

class MyPipelineStack(cdk.Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        repoName = self.node.try_get_context("repoName")
        dev_info = self.node.try_get_context("dev")

        pipeline =  CodePipeline(self, "Pipeline",
                        pipeline_name="CDKPipeline",
                        synth=ShellStep("Synth",
                            input=CodePipelineSource.git_hub(repoName, "main"),
                            commands=["npm install -g aws-cdk",
                                "python -m pip install -r requirements.txt",
                                "cdk synth"]))

        testing_stage = pipeline.add_stage(MyPipelineAppDevStage(self, "infrastructure-Deploy",
            env=cdk.Environment(account=dev_info["account"], region=dev_info["region"])))

        testing_stage.add_post(ManualApprovalStep('approval'))
