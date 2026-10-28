"""stringops: what it declares, and what its actions do."""

import app as M


def test_the_app_declares_every_action_and_its_blok():
    declaration = M.app.registry.to_implement_agent_input().model_dump(mode="json", exclude_none=True)
    interfaces = {implementation["interface"] for implementation in declaration["implementations"]}
    assert interfaces == {
        "concatenate", "change_case", "reverse", "repeat", "replace", "strip",
        "count", "length", "split", "join", "is_palindrome", "words",
    }
    # A Literal is a choice port.
    [change_case] = [i for i in declaration["implementations"] if i["interface"] == "change_case"]
    [case] = [arg for arg in change_case["definition"]["args"] if arg["key"] == "case"]
    assert case["kind"] == "ENUM"
    assert [choice["value"] for choice in case["choices"]] == ["upper", "lower", "title", "swap"]
    assert case["default"] == "upper"


def test_the_actions_do_what_they_say():
    assert M.concatenate("a", "b") == "a b"
    assert M.change_case("Hello", "swap") == "hELLO"
    assert M.reverse("abc") == "cba"
    assert M.repeat("ab", 3, "-") == "ab-ab-ab"
    assert M.count("banana", "an") == 2
    assert M.split("a b c") == ["a", "b", "c"]
    assert M.join(["a", "b"], ",") == "a,b"
    assert M.is_palindrome("Anna")
    assert list(M.words("one two")) == ["one", "two"]
