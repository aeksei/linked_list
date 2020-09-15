from linked_list import LinkedList
from builder import FabricDriverBuilder


def main():
    driver = FabricDriverBuilder.get_driver()
    l = LinkedList(driver=driver)
    l.append(5)
    l.append(10)

    for value in l:
        print(value)

    l.write()


if __name__ == '__main__':
    main()
