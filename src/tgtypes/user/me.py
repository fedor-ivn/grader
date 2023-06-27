from dataclasses import dataclass
from tgtypes.user.user import User


@dataclass
class Me(User):
    can_join_groups: bool = False
    can_read_all_group_messages: bool = False
    supports_inline_queries: bool = False
