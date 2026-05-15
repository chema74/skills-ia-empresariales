from skillforge.core.adaptadores_llm import (
    ADAPTADORES_REGISTRADOS,
    AdaptadorLocalReglas,
    AdaptadorMockGroq,
    RespuestaAdaptadorLLM,
    generar_con_fallback,
    listar_adaptadores,
)


def test_listar_adaptadores_contiene_mock_y_local() -> None:
    adaptadores = listar_adaptadores()
    assert "local_reglas" in adaptadores
    assert "mock_groq" in adaptadores


def test_contrato_respuesta_local_reglas() -> None:
    adaptador = AdaptadorLocalReglas()
    respuesta = adaptador.generar(prompt="Resumen de incidencias operativas")

    assert isinstance(respuesta, RespuestaAdaptadorLLM)
    assert respuesta.proveedor == "local_reglas"
    assert respuesta.estado == "ok"
    assert isinstance(respuesta.texto, str)
    assert respuesta.tokens_estimados >= 1


def test_contrato_respuesta_mock_groq_no_disponible() -> None:
    adaptador = AdaptadorMockGroq()
    respuesta = adaptador.generar(prompt="Texto de prueba")

    assert isinstance(respuesta, RespuestaAdaptadorLLM)
    assert respuesta.proveedor == "mock_groq"
    assert respuesta.estado in {"ok", "error"}
    assert isinstance(respuesta.tokens_estimados, int)


def test_fallback_local_garantizado_cuando_proveedor_no_esta() -> None:
    respuesta, uso_fallback = generar_con_fallback(
        prompt="Necesito un resumen ejecutivo",
        proveedor_preferido="proveedor_no_existente",
    )

    assert uso_fallback is True
    assert respuesta.proveedor == "local_reglas"
    assert respuesta.estado == "ok"


def test_registro_adaptadores_tiene_objetos_validos() -> None:
    assert "local_reglas" in ADAPTADORES_REGISTRADOS
    assert "mock_groq" in ADAPTADORES_REGISTRADOS
    assert hasattr(ADAPTADORES_REGISTRADOS["local_reglas"], "generar")
    assert hasattr(ADAPTADORES_REGISTRADOS["mock_groq"], "generar")
