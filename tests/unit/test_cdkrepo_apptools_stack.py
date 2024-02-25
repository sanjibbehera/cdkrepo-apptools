import aws_cdk as core
import aws_cdk.assertions as assertions

from cdkrepo_apptools.cdkrepo_apptools_stack import CdkrepoApptoolsStack

# example tests. To run these tests, uncomment this file along with the example
# resource in cdkrepo_apptools/cdkrepo_apptools_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = CdkrepoApptoolsStack(app, "cdkrepo-apptools")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
