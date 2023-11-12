def quadrat_summe_prozedural(n):
    # Prozedurale Lösung
    result = 0
    for i in range(n + 1):
        result += i ** 2
    return result


class QuadratSummeObjektorientiert:
    # Objektorientierte Lösung
    def __init__(self, n):
        self.n = n

    def berechne_quadrat_summe(self):
        result = 0
        for i in range(self.n + 1):
            result += i ** 2
        return result


def quadrat_summe_funktional(n):
    # Funktionale Lösung
    return sum(map(lambda x: x ** 2, range(n + 1)))