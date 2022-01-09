from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any, Optional


class Handler(ABC):
    """
    The Handler interface declares a method for building the chain of handlers.
    It also declares a method for executing a request.
    """

    @abstractmethod
    def set_next(self, handler: Handler) -> Handler:
        pass

    @abstractmethod
    def handle(self, request) -> Optional[str]:
        pass


class AbstractHandler(Handler):
    """
    The default chaining behavior can be implemented inside a base handler
    class.
    """

    _next_handler: Handler = None

    def set_next(self, handler: Handler) -> Handler:
        self._next_handler = handler
        # Returning a handler from here will let us link handlers in a
        # convenient way like this:
        # monkey.set_next(squirrel).set_next(dog)
        return handler

    @abstractmethod
    def handle(self, request: Any) -> str:
        if self._next_handler:
            return self._next_handler.handle(request)

        return None


"""
All Concrete Handlers either handle a request or pass it to the next handler in
the chain.
"""


class BalanceHandler(AbstractHandler):
    def handle(self, request: Any) -> str:
        if request<10:
            return f"Balance not enough"
        else:
            return super().handle(request)


class BuyHandler(AbstractHandler):
    def handle(self, request: Any) -> str:
        if request<20:
            return f"no available thread"
        else:
            return super().handle(request)


class OrderHandler(AbstractHandler):
    def handle(self, request: Any) -> str:
        if request<30:
            return f"time passed"
        else:
            return super().handle(request)


def client_code(handler: Handler) -> None:
    """
    The client code is usually suited to work with a single handler. In most
    cases, it is not even aware that the handler is part of a chain.
    """
    # example={
    #     'total':15,
    #     'available_concurrency':20,
    #     'time':1
    # }
    example=[5,15,21]
    for i in example:
        result = handler.handle(i)
        print(result)
    # result = handler.handle(example)
    # print(result)


if __name__ == "__main__":
    balance = BalanceHandler()
    buy = BuyHandler()
    order = OrderHandler()

    balance.set_next(buy).set_next(order)

    # The client should be able to send a request to any handler, not just the
    # first one in the chain.
    client_code(balance)
