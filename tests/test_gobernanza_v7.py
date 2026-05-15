from skillforge.core.gobernanza import cargar_politicas, cargar_registro_cambios


def test_carga_politicas_versionadas() -> None:
    politicas = cargar_politicas()

    assert "aprobar_pago" in politicas
    assert politicas["aprobar_pago"].version == "v1.0.0"
    assert politicas["aprobar_pago"].requiere_aprobacion is True
    assert "direccion" in politicas["aprobar_pago"].roles_aprobadores


def test_carga_registro_cambios_gobernanza() -> None:
    cambios = cargar_registro_cambios()

    assert len(cambios) >= 1
    primer_cambio = cambios[0]
    assert primer_cambio["version"] == "v1.0.0"
    assert "politicas de aprobacion" in primer_cambio["descripcion"].lower()
