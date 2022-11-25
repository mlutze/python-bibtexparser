from copy import copy, deepcopy

from bibtexparser.model import (
    Entry,
    ExplicitComment,
    Field,
    ImplicitComment,
    Preamble,
    String,
)


def test_entry_equality():
    # Equal to itself
    entry_1 = Entry(
        "article",
        "key",
        {"field": Field("field", "value", 1)},
        1,
        "raw",
    )
    assert entry_1 == entry_1
    # Equal to identical entry
    entry_2 = Entry(
        "article",
        "key",
        {"field": Field("field", "value", 1)},
        1,
        "raw",
    )
    assert entry_1 == entry_2
    # Not equal to entry with different entry-type
    entry_3 = Entry(
        "book",
        "key",
        {"field": Field("field", "value", 1)},
        1,
        "raw",
    )
    assert entry_1 != entry_3
    # Not equal to entry with different fields
    entry_4 = Entry(
        "article",
        "key",
        {"field": Field("field", "value", 1), "field2": Field("field2", "value", 2)},
        1,
        "raw",
    )
    assert entry_1 != entry_4


def test_entry_copy():
    entry_1 = Entry(
        "article",
        "key",
        {"field": Field("field", "value", 1)},
        1,
        "raw",
    )
    entry_2 = copy(entry_1)
    assert entry_1 == entry_2
    assert entry_1 is not entry_2
    assert entry_1.fields is entry_2.fields
    assert entry_1.fields == entry_2.fields


def test_entry_deepcopy():
    entry_1 = Entry("article", "key", {"field": Field("field", "value", 1)}, 1, "raw")
    entry_2 = deepcopy(entry_1)
    assert entry_1 == entry_2
    assert entry_1 is not entry_2
    assert entry_1.fields is not entry_2.fields
    assert entry_1.fields == entry_2.fields
    assert entry_1.fields["field"] is not entry_2.fields["field"]
    assert entry_1.fields["field"] == entry_2.fields["field"]


def test_string_equality():
    # Equal to itself
    string_1 = String(
        "key",
        "value",
        1,
        "raw",
    )
    assert string_1 == string_1
    # Equal to identical string
    string_2 = String(
        "key",
        "value",
        1,
        "raw",
    )
    assert string_1 == string_2
    # Not equal to string with different key
    string_3 = String(
        "key2",
        "value",
        1,
        "raw",
    )
    assert string_1 != string_3
    # Not equal to string with different value
    string_4 = String(
        "key",
        "value2",
        1,
        "raw",
    )
    assert string_1 != string_4


def test_string_copy():
    string_1 = String(
        "key",
        "value",
        1,
        "raw",
    )
    string_2 = copy(string_1)
    assert string_1 == string_2
    assert string_1 is not string_2


def test_string_deepcopy():
    string_1 = String(
        "key",
        "value",
        1,
        "raw",
    )
    string_2 = deepcopy(string_1)
    assert string_1 == string_2
    assert string_1 is not string_2


def test_preamble_equality():
    # Equal to itself
    preamble_1 = Preamble("value", 1, "raw")
    assert preamble_1 == preamble_1
    # Equal to identical preamble
    preamble_2 = Preamble("value", 1, "raw")
    assert preamble_1 == preamble_2
    # Not equal to preamble with different value
    preamble_3 = Preamble("value2", 1, "raw")
    assert preamble_1 != preamble_3


def test_preamble_copy():
    preamble_1 = Preamble("value", 1, "raw")
    preamble_2 = copy(preamble_1)
    assert preamble_1 == preamble_2
    assert preamble_1 is not preamble_2


def test_preable_deepcopy():
    preamble_1 = Preamble("value", 1, "raw")
    preamble_2 = deepcopy(preamble_1)
    assert preamble_1 == preamble_2
    assert preamble_1 is not preamble_2


def test_implicit_comment_equality():
    # Equal to itself
    comment_1 = ImplicitComment(
        start_line=1, comment="This is my comment", raw="#  This is my comment"
    )
    assert comment_1 == comment_1
    # Equal to identical comment
    comment_2 = ImplicitComment(
        start_line=1, comment="This is my comment", raw="#  This is my comment"
    )
    assert comment_1 == comment_2
    # Not equal to comment with different comment
    comment_3 = ImplicitComment(
        start_line=1, comment="This is my comment2", raw="#  This is my comment"
    )
    assert comment_1 != comment_3


def test_implicit_comment_copy():
    comment_1 = ImplicitComment(
        start_line=1, comment="This is my comment", raw="#  This is my comment"
    )
    comment_2 = copy(comment_1)
    assert comment_1 == comment_2
    assert comment_1 is not comment_2


def test_implicit_comment_deepcopy():
    comment_1 = ImplicitComment(
        start_line=1, comment="This is my comment", raw="#  This is my comment"
    )
    comment_2 = deepcopy(comment_1)
    assert comment_1 == comment_2
    assert comment_1 is not comment_2


def test_explicit_comment_equality():
    # Equal to itself
    comment_1 = ExplicitComment(
        start_line=1, comment="This is my comment", raw="#  This is my comment"
    )
    assert comment_1 == comment_1
    # Equal to identical comment
    comment_2 = ExplicitComment(
        start_line=1, comment="This is my comment", raw="#  This is my comment"
    )
    assert comment_1 == comment_2
    # Not equal to comment with different comment
    comment_3 = ExplicitComment(
        start_line=1, comment="This is my comment2", raw="#  This is my comment"
    )
    assert comment_1 != comment_3


def test_explicit_comment_copy():
    comment_1 = ExplicitComment(
        start_line=1, comment="This is my comment", raw="#  This is my comment"
    )
    comment_2 = copy(comment_1)
    assert comment_1 == comment_2
    assert comment_1 is not comment_2


def test_explicit_comment_deepcopy():
    comment_1 = ExplicitComment(
        start_line=1, comment="This is my comment", raw="#  This is my comment"
    )
    comment_2 = deepcopy(comment_1)
    assert comment_1 == comment_2
    assert comment_1 is not comment_2


def test_implicit_and_explicit_comment_equality():
    # Equal to itself
    comment_1 = ImplicitComment(
        start_line=1, comment="This is my comment", raw="#  This is my comment"
    )
    comment_2 = ExplicitComment(
        start_line=1, comment="This is my comment", raw="#  This is my comment"
    )
    assert comment_1 != comment_2
    assert comment_2 != comment_1