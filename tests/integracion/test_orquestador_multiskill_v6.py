from skillforge.skills import (
    PIPELINE_CLIENTE_COMUNICACION,
    PIPELINE_CUMPLIMIENTO_PUBLICACION,
    PIPELINE_RIESGO_INFORME,
    SolicitudOrquestacion,
    evaluar_orquestador_multiskill,
)


def test_pipeline_riesgo_informe_e2e_ok() -> None:
    resultado = evaluar_orquestador_multiskill(
        SolicitudOrquestacion(
            accion="orquestar",
            descripcion="v6_riesgo",
            solicitante="orquestador",
            contexto={"canal": "interno"},
            pipeline_id=PIPELINE_RIESGO_INFORME,
            entrada_pipeline={
                "intencion": "Necesito evaluar riesgo operativo y generar informe ejecutivo",
                "titulo": "Informe Riesgo V6",
                "factores": [
                    {"nombre": "continuidad", "severidad": 8, "peso": 4.0},
                    {"nombre": "cumplimiento", "severidad": 7, "peso": 3.0},
                ],
            },
        )
    )

    assert resultado.estado in {"ok", "advertencia"}
    assert resultado.salida["pipeline_id"] == PIPELINE_RIESGO_INFORME
    assert resultado.salida["total_pasos"] == 3
    assert any("inicio_pipeline:riesgo_informe" in traza for traza in resultado.trazas)
    assert any("fin_pipeline:riesgo_informe" in traza for traza in resultado.trazas)
    pasos = resultado.salida["pasos"]
    assert pasos[0]["paso"] == "enrutamiento"
    assert pasos[1]["paso"] == "pulso_riesgo"
    assert pasos[2]["paso"] == "forjador_informes"


def test_pipeline_cumplimiento_publicacion_e2e_con_bloqueo() -> None:
    resultado = evaluar_orquestador_multiskill(
        SolicitudOrquestacion(
            accion="orquestar",
            descripcion="v6_cumplimiento",
            solicitante="cumplimiento",
            contexto={"canal": "externo"},
            pipeline_id=PIPELINE_CUMPLIMIENTO_PUBLICACION,
            entrada_pipeline={
                "texto_objetivo": "Comunicacion sin consentimiento y con promesa garantizado.",
                "reglas": [
                    {
                        "codigo": "RG-CONSENT",
                        "descripcion": "Debe incluir consentimiento",
                        "requerido": "consentimiento",
                        "severidad": "alta",
                    },
                    {
                        "codigo": "RG-PROMESA",
                        "descripcion": "No promesas absolutas",
                        "prohibido": "garantizado",
                        "severidad": "media",
                    },
                ],
            },
        )
    )

    assert resultado.estado == "advertencia"
    assert resultado.salida["pipeline_id"] == PIPELINE_CUMPLIMIENTO_PUBLICACION
    assert resultado.salida["total_pasos"] == 2
    pasos = resultado.salida["pasos"]
    assert pasos[0]["paso"] == "verificador_normativo"
    assert pasos[1]["paso"] == "puerta_aprobacion_humana"
    assert pasos[1]["estado"] == "advertencia"


def test_pipeline_cliente_comunicacion_e2e_ok() -> None:
    resultado = evaluar_orquestador_multiskill(
        SolicitudOrquestacion(
            accion="orquestar",
            descripcion="v6_cliente",
            solicitante="cx",
            contexto={"segmento": "enterprise"},
            pipeline_id=PIPELINE_CLIENTE_COMUNICACION,
            entrada_pipeline={
                "cliente_id": "CLI-77",
                "eventos": [
                    {
                        "fecha": "2026-05-10T10:00:00",
                        "tipo": "reunion",
                        "detalle": "revision trimestral",
                        "origen": "crm",
                    }
                ],
                "tono_objetivo": "ejecutivo",
                "palabras_clave_marca": ["servicio", "continuidad"],
                "texto_base": "Seguimos acompanando la operacion con foco en continuidad del servicio.",
            },
        )
    )

    assert resultado.estado in {"ok", "advertencia"}
    assert resultado.salida["pipeline_id"] == PIPELINE_CLIENTE_COMUNICACION
    assert resultado.salida["total_pasos"] == 2
    pasos = resultado.salida["pasos"]
    assert pasos[0]["paso"] == "memoria_contextual_cliente"
    assert pasos[1]["paso"] == "voz_marca_inteligente"


def test_pipeline_no_soportado_devuelve_error() -> None:
    resultado = evaluar_orquestador_multiskill(
        SolicitudOrquestacion(
            accion="orquestar",
            descripcion="v6_error",
            solicitante="qa",
            contexto={},
            pipeline_id="pipeline_desconocido",
            entrada_pipeline={},
        )
    )

    assert resultado.estado == "error"
    assert "no soportado" in resultado.salida["mensaje"].lower()
    assert isinstance(resultado.salida["pipelines_disponibles"], list)
