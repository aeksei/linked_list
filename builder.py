from driver import JsonFileDriver


class DriverBuilder:
    def build(self):
        return None


class JsonFileBuilder(DriverBuilder):
    def build(self):
        filename = input('Введите название json файла: (.json)')
        filename = filename if filename else 'tmp'
        filename = filename.strip()
        if not filename.endswith('.json'):
            filename += '.json'

        return JsonFileDriver(filename)


class FabricDriverBuilder:
    @staticmethod
    def get_driver():
        driver_name = input("Введите название драйвера: ")
        driver_name = driver_name if driver_name else 'json_file'

        drivers = {
            'json_file': JsonFileBuilder
        }

        return drivers[driver_name]().build()


if __name__ == '__main__':
    driver = FabricDriverBuilder.get_driver()
