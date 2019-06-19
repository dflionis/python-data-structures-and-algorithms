"""An example of building out linked list functionality by hand
"""


class Link:
    """Represents a single link for use within a linked list

    Attributes:
        link_id: An integer that uniquely identifies the link
        link_data: Data of any type that represents the paylod of the link
        next: A link object that the current link points to
    """
    def __init__(self, link_id, link_data):
        self.link_id = link_id
        self.link_data = link_data
        self.next = None

    def display_link(self):
        """Prints the link to standard output using the following format:
           {link_id,data}
        """
        print("{" + str(self.link_id) + "," + str(self.link_data) + "} ")


class LinkList:
    """A class for building linked lists

    Attributes:
        first: The first link in the linked list
    """
    def __init__(self):
        self.first = None

    def is_empty(self):
        """Returns True if the linked list is empty, otherwise False

        Returns:
            A boolean representing whether or not the linked list is empty
        """
        return self.first is None

    def insert_first(self, link_id, link_data):
        """Takes a link and inserts it to the front of the linked list.

        Args:
            link_id: An integer representing a unique identifier of a link.
            link_data: A piece of data of any type representing the "payload"
                of the link object
        """
        new_link = Link(link_id, link_data)
        new_link.next = self.first
        self.first = new_link

    def delete_first(self):
        """Removes the first link from the linked list

        Returns:
            The link object that has been removed
        """
        temp = self.first
        self.first = self.first.next
        return temp

    def display_list(self):
        """Prints a textual representation of the linked list to standard
           output.
        """
        print('List (first-->last): ')
        current = self.first
        while current is not None:
            current.display_link()
            current = current.next
        print('')


class LinkListApp:
    """A wrapper class for testing Linked List functionality
    """
    @staticmethod
    def test_linked_list():
        """Tests various linked list functionality as a proof of concept
        """
        the_list = LinkList()
        the_list.insert_first(22, 2.99)
        the_list.insert_first(44, 4.99)
        the_list.insert_first(66, 6.99)
        the_list.insert_first(88, 8.99)

        the_list.display_list()

        while not the_list.is_empty():
            a_link = the_list.delete_first()
            print('Deleted ')
            a_link.display_link()
            print('')

        the_list.display_list()


if __name__ == '__main__':
    LinkListApp.test_linked_list()
