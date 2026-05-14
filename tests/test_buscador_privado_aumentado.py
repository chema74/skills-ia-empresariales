from skillforge.skills import DocumentoPrivado, SolicitudBusquedaPrivada, evaluar_buscador_privado_aumentado


def test_buscador_privado_ok_con_citas() -> None:
    corpus = [
        DocumentoPrivado(doc_id="D1", titulo="Riesgo", contenido="Revision humana de riesgo operativo.", fuente="politica"),
        DocumentoPrivado(doc_id="D2", titulo="Ventas", contenido="Seguimiento comercial semanal.", fuente="ventas"),
    ]
    entrada = SolicitudBusquedaPrivada(
        accion="buscar",
        descripcion="test",
        solicitante="qa",
        contexto={},
        consulta="riesgo humana",
        corpus=corpus,
        top_k=1,
    )

    resultado = evaluar_buscador_privado_aumentado(entrada)

    assert resultado.estado == "ok"
    assert resultado.salida["total_resultados"] == 1
    assert resultado.salida["resultados"][0]["doc_id"] == "D1"
    assert len(resultado.salida["resultados"][0]["citas"]) >= 1


def test_buscador_privado_error_consulta_vacia() -> None:
    entrada = SolicitudBusquedaPrivada(
        accion="buscar",
        descripcion="test",
        solicitante="qa",
        contexto={},
        consulta="",
        corpus=[DocumentoPrivado(doc_id="D1", titulo="A", contenido="B", fuente="x")],
    )

    resultado = evaluar_buscador_privado_aumentado(entrada)

    assert resultado.estado == "error"
    assert "consulta vacia" in resultado.salida["mensaje"].lower()