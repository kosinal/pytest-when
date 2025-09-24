import abc
from unittest.mock import MagicMock
from pytest_when.when import _TargetMethodReturn, _CallLazyValue


class ThenResponse(abc.ABC):
    def then_return(self, value: _TargetMethodReturn) -> MagicMock:
        """Return value in case the called_with specification will match the call."""
        raise NotImplementedError("Not implemented")

    def then_call(self, callable_: _CallLazyValue) -> MagicMock:
        """Call the callable_ in case the called_with specification will match the call.

        Callable shouldn't contain any args.
        In case the callable needs args, kwargs - use functools.partial
        to convert the callable into arg-less one, i.e.

        Example:
        >>> (
        >>>    when(example_module, "some_foo")
        >>>    .called_with()
        >>>    .then_call(functools.partial(foo_patched, *foo_args, **foo_kwargs)
        >>> )

        """
        raise NotImplementedError("Not implemented")

    def then_raise(self, exc: BaseException) -> MagicMock:
        """Raise exc in case the called_with specification will match the call."""
        raise NotImplementedError("Not implemented")

class WhenResponse(abc.ABC):

    def called_with(
        self,
        *args,
        **kwargs,
    ) -> ThenResponse:
        """Specify args and kwargs for which mock should be activated.

        Example:
        >>> when(Klass1, "some_class_method").called_with(
        >>>     "a",
        >>>     when.markers.any,
        >>>     kwarg1="b",
        >>>     kwarg2=when.markers.any,
        >>> ).then_return("Mocked")

        In this case the "Mocked" will be returned only if `some method`
        will be called with:
        "a" - as first argument,
        any second argument,
        kwarg1 = "b" (only),
        any kwarg2 kwarg

        """
        raise NotImplementedError("Not implemented")
