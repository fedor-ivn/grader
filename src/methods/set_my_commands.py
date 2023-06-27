from methods.method import Method
from content import EmptyRequestContent
from uri.method_uri import MethodURI
from methods.raw_method import RawMethod
from uri.uri import URI
from tgtypes.bool_response import BoolResponse


class SetMyCommands(Method[BoolResponse]):
    def call(self, bot: URI) -> BoolResponse:
        return BoolResponse(
            response=RawMethod(
                EmptyRequestContent(),
            ).call(MethodURI("setmycommands", bot))
        )
