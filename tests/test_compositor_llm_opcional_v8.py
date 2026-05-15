from skillforge.skills import SolicitudComposicionLLM, evaluar_compositor_llm_opcional


def test_compositor_fallback_local_por_defecto() -> None:
    resultado = evaluar_compositor_llm_opcional(
        SolicitudComposicionLLM(
            accion="componer_texto",
            descripcion="v8",
            solicitante="qa",
            contexto={},
            prompt="Genera un resumen de riesgo operativo.",
            proveedor_preferido="mock_groq",
        )
    )

    assert resultado.estado == "ok"
    assert resultado.salida["uso_fallback_local"] is True
    assert resultado.salida["proveedor_efectivo"] == "local_reglas"
    assert "fallback" in " ".join(resultado.advertencias).lower()


def test_compositor_prompt_vacio_devuelve_error() -> None:
    resultado = evaluar_compositor_llm_opcional(
        SolicitudComposicionLLM(
            accion="componer_texto",
            descripcion="v8",
            solicitante="qa",
            contexto={},
            prompt="",
        )
    )

    assert resultado.estado == "error"
    assert "prompt vacio" in resultado.salida["mensaje"].lower()


def test_compositor_con_proveedor_mock_habilitado(monkeypatch: object) -> None:
    monkeypatch.setenv("SKILLFORGE_ENABLE_MOCK_GROQ", "1")
    resultado = evaluar_compositor_llm_opcional(
        SolicitudComposicionLLM(
            accion="componer_texto",
            descripcion="v8",
            solicitante="qa",
            contexto={},
            prompt="Genera dos lineas de cierre comercial.",
            proveedor_preferido="mock_groq",
        )
    )

    assert resultado.estado == "ok"
    assert resultado.salida["uso_fallback_local"] is False
    assert resultado.salida["proveedor_efectivo"] == "mock_groq"
