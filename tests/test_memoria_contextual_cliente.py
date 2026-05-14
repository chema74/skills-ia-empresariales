from skillforge.skills import EventoCliente, SolicitudMemoriaCliente, evaluar_memoria_contextual_cliente


def test_memoria_cliente_ok() -> None:
    entrada = SolicitudMemoriaCliente(
        accion="consolidar_memoria_cliente",
        descripcion="test",
        solicitante="qa",
        contexto={},
        cliente_id="CL-1",
        eventos=[
            EventoCliente(fecha="2026-01-01T10:00:00", tipo="alta", detalle="Alta", origen="crm"),
            EventoCliente(fecha="2026-01-02T10:00:00", tipo="contacto", detalle="Llamada", origen="ventas"),
        ],
    )

    resultado = evaluar_memoria_contextual_cliente(entrada)

    assert resultado.estado == "ok"
    assert resultado.salida["total_eventos"] == 2
    assert resultado.salida["timeline"][0]["tipo"] == "alta"


def test_memoria_cliente_error_sin_cliente_id() -> None:
    entrada = SolicitudMemoriaCliente(
        accion="consolidar_memoria_cliente",
        descripcion="test",
        solicitante="qa",
        contexto={},
        cliente_id="",
        eventos=[EventoCliente(fecha="2026-01-01T10:00:00", tipo="alta", detalle="Alta", origen="crm")],
    )

    resultado = evaluar_memoria_contextual_cliente(entrada)

    assert resultado.estado == "error"
    assert "cliente_id" in resultado.salida["mensaje"].lower()


def test_memoria_cliente_advertencia_conflicto() -> None:
    entrada = SolicitudMemoriaCliente(
        accion="consolidar_memoria_cliente",
        descripcion="test",
        solicitante="qa",
        contexto={},
        cliente_id="CL-2",
        eventos=[
            EventoCliente(fecha="2026-01-01T10:00:00", tipo="queja", detalle="Queja", origen="soporte"),
            EventoCliente(fecha="2026-01-03T10:00:00", tipo="cierre", detalle="Cierre", origen="soporte"),
        ],
    )

    resultado = evaluar_memoria_contextual_cliente(entrada)

    assert resultado.estado == "ok"
    assert any("mezcla" in adv for adv in resultado.advertencias)