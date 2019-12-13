from typing import Dict, Tuple, Sequence

ConnectionOptions = Dict[str, str]
Address = Tuple[str, int]
Server = Tuple[Address, ConnectionOptions]


def broadcast_message(message: str, servers: Sequence[Server]) -> None:
    print(message)
    print(servers)


# The static type checker will treat the previous type signature as
# being exactly equivalent to this one.
def broadcast_message(
    message: str, servers: Sequence[Tuple[Tuple[str, int], Dict[str, str]]]
) -> None:
    print(message)
    print(servers)
