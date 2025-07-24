def singleton(the_class):
    instances = {}

    def get_class(*args, **kwargs):
        if the_class not in instances:
            instances[the_class] = the_class(*args, **kwargs)
        return instances[the_class]

    # print(the_class)
    return get_class


@singleton
class AppSettings:
    _instance = None

    def __init__(self, *args, **kwargs):
        print("OI")
        self.tema = "Tema escuro"
        self.font = "18px"


@singleton
class Teste:
    def __init__(self):
        print("Olá")


if __name__ == "__main__":
    as1 = AppSettings()
    as1.tema = "Tema claro"
    print(as1.tema)

    as2 = AppSettings()
    print(as2.tema)

    t1 = Teste()
    t2 = Teste()
    print(t1 == t2)
