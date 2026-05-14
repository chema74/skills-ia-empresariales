from skillforge.core.trazabilidad import agregar_traza_local, crear_traza_local


def test_crear_traza_local() -> None:
    traza = crear_traza_local("test_evento")

    assert traza.startswith("local|")
    assert traza.endswith("|test_evento")


def test_agregar_traza_local() -> None:
    trazas: list[str] = []

    actualizadas = agregar_traza_local(trazas, "paso_1")

    assert len(actualizadas) == 1
    assert actualizadas[0].endswith("|paso_1")