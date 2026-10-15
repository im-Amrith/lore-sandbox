from unittest import mock

from api import handlers


def test_mixed_case_code_is_looked_up_unchanged():
    with mock.patch.object(handlers, "cache") as cache, mock.patch.object(handlers, "get_link") as get_link:
        cache.get.return_value = None
        get_link.return_value = "https://example.com"
        assert handlers.redirect("Xk9fT2a") == (302, "https://example.com")
        get_link.assert_called_once_with("Xk9fT2a")
