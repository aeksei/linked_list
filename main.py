from linked_list import LinkedList, ObservedLinkedList
from builder import FabricDriverBuilder


def main():
    driver = FabricDriverBuilder.get_driver()
    # l = LinkedList(driver=driver)
    l = ObservedLinkedList(driver=driver)
    l.append(5)
    l.append(10)

    l[0] = 100


if __name__ == '__main__':
    main()
