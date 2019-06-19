"""Tests the Link and LinkList classes
"""
from src.linked_list import Link, LinkList


class TestLink:
    """Tests the Link class
    """
    @staticmethod
    def test_link_instantiation():
        """Tests the __init__ method
        """
        link = Link(42, 'some_data')
        assert link.link_id == 42
        assert link.link_data == 'some_data'
        assert link.next is None

    @staticmethod
    def test_display_link(capsys):
        """Tests the display_link method
        """
        link = Link(23, 'payload')
        link.display_link()
        out, _ = capsys.readouterr()
        expected_stdout = '{23,payload} \n'
        assert out == expected_stdout


class TestLinkList:
    """Tests the LinkList class
    """
    @staticmethod
    def test_link_list_instantiation():
        """Tests the __init__ method
        """
        link_list = LinkList()
        assert link_list.first is None

    class TestIsEmpty:
        """Tests the is_empty method
        """
        @staticmethod
        def test_is_empty_when_empty():
            """Tests the is_empty method when the link list is empty
            """
            link_list = LinkList()
            assert link_list.is_empty()

        @staticmethod
        def test_is_empty_when_not_empty():
            """Tests the is_empty method when the link list is not empty
            """
            link_list = LinkList()
            link_list.insert_first(23, 'payload')
            assert link_list.is_empty() is False

    @staticmethod
    def test_insert_first():
        """Tests the insert_first method
        """
        link_list = LinkList()
        link_list.insert_first(23, 'payload')
        assert link_list.first.link_id == 23
        assert link_list.first.link_data == 'payload'

    @staticmethod
    def test_delete_first():
        """Tests the delete_first method
        """
        link_list = LinkList()
        link_list.insert_first(23, 'payload')
        assert link_list.first is not None
        link_list.delete_first()
        assert link_list.first is None

    @staticmethod
    def test_display_list(capsys):
        """Tests the display_list method
        """
        link_list = LinkList()
        link_list.insert_first(100, 'payload')
        link_list.insert_first(101, 'another_payload')
        link_list.display_list()
        out, _ = capsys.readouterr()
        expected_stdout = (
            'List (first-->last): \n{101,another_payload} \n{100,payload} \n\n'
        )
        assert out == expected_stdout
