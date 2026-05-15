import pytest

from skillforge.skills import (
    DocumentoPrivado,
    EventoCliente,
    FactorRiesgo,
    ReglaNormativa,
    SolicitudAprobacion,
    SolicitudBusquedaPrivada,
    SolicitudEnrutamiento,
    SolicitudForjadorInformes,
    SolicitudLecturaDocumental,
    SolicitudMemoriaCliente,
    SolicitudPulsoRiesgo,
    SolicitudRadarAnomalias,
    SolicitudVerificacionNormativa,
    SolicitudVozMarca,
    evaluar_buscador_privado_aumentado,
    evaluar_enrutador_inteligente,
    evaluar_forjador_informes,
    evaluar_lector_inteligente_documental,
    evaluar_memoria_contextual_cliente,
    evaluar_puerta_aprobacion_humana,
    evaluar_pulso_riesgo,
    evaluar_radar_anomalias,
    evaluar_verificador_normativo,
    evaluar_voz_marca_inteligente,
)


@pytest.mark.parametrize(
    ("nombre", "resultado"),
    [
        (
            "lector_inteligente_documental",
            evaluar_lector_inteligente_documental(
                SolicitudLecturaDocumental(
                    accion="leer",
                    descripcion="regresion",
                    solicitante="qa",
                    contexto={},
                    texto_documento="Linea 1\n\nLinea 2",
                )
            ),
        ),
        (
            "radar_anomalias",
            evaluar_radar_anomalias(
                SolicitudRadarAnomalias(
                    accion="detectar_anomalias",
                    descripcion="regresion",
                    solicitante="qa",
                    contexto={},
                    serie=[10, 11, 10, 50],
                )
            ),
        ),
        (
            "forjador_informes",
            evaluar_forjador_informes(
                SolicitudForjadorInformes(
                    accion="forjar_informe",
                    descripcion="regresion",
                    solicitante="qa",
                    contexto={},
                    titulo="Informe Regresion",
                    hallazgos=["Hallazgo valido"],
                )
            ),
        ),
        (
            "memoria_contextual_cliente",
            evaluar_memoria_contextual_cliente(
                SolicitudMemoriaCliente(
                    accion="consolidar_memoria",
                    descripcion="regresion",
                    solicitante="qa",
                    contexto={},
                    cliente_id="CLI-001",
                    eventos=[
                        EventoCliente(
                            fecha="2026-05-01T10:00:00",
                            tipo="contacto",
                            detalle="primer contacto",
                            origen="crm",
                        )
                    ],
                )
            ),
        ),
        (
            "pulso_riesgo",
            evaluar_pulso_riesgo(
                SolicitudPulsoRiesgo(
                    accion="calcular_riesgo",
                    descripcion="regresion",
                    solicitante="qa",
                    contexto={},
                    factores=[FactorRiesgo(nombre="operativo", severidad=6, peso=2.0)],
                )
            ),
        ),
        (
            "buscador_privado_aumentado",
            evaluar_buscador_privado_aumentado(
                SolicitudBusquedaPrivada(
                    accion="buscar",
                    descripcion="regresion",
                    solicitante="qa",
                    contexto={},
                    consulta="procedimiento",
                    corpus=[
                        DocumentoPrivado(
                            doc_id="DOC-1",
                            titulo="Manual",
                            contenido="Procedimiento interno de aprobacion",
                            fuente="kb",
                        )
                    ],
                )
            ),
        ),
        (
            "enrutador_inteligente",
            evaluar_enrutador_inteligente(
                SolicitudEnrutamiento(
                    accion="enrutar",
                    descripcion="regresion",
                    solicitante="qa",
                    contexto={},
                    intencion="Necesito un informe de riesgo",
                )
            ),
        ),
        (
            "voz_marca_inteligente",
            evaluar_voz_marca_inteligente(
                SolicitudVozMarca(
                    accion="adaptar_texto",
                    descripcion="regresion",
                    solicitante="qa",
                    contexto={},
                    texto="Tenemos una actualizacion de servicio.",
                )
            ),
        ),
        (
            "verificador_normativo",
            evaluar_verificador_normativo(
                SolicitudVerificacionNormativa(
                    accion="verificar_normativa",
                    descripcion="regresion",
                    solicitante="qa",
                    contexto={},
                    texto_objetivo="Este texto incluye consentimiento expreso.",
                    reglas=[
                        ReglaNormativa(
                            codigo="RG-1",
                            descripcion="Debe incluir consentimiento",
                            requerido="consentimiento",
                        )
                    ],
                )
            ),
        ),
        (
            "puerta_aprobacion_humana",
            evaluar_puerta_aprobacion_humana(
                SolicitudAprobacion(
                    accion="aprobar_pago",
                    descripcion="regresion",
                    solicitante="qa",
                    contexto={},
                    aprobada=True,
                    aprobador="direccion",
                )
            ),
        ),
    ],
)
def test_regresion_contrato_salida_base_en_todas_las_skills(nombre: str, resultado: object) -> None:
    assert resultado.nombre_skill == nombre
    assert resultado.estado in {"ok", "error", "advertencia"}
    assert isinstance(resultado.salida, dict)
    assert isinstance(resultado.salida.get("mensaje"), str)
    assert resultado.salida["mensaje"].strip() != ""
    assert isinstance(resultado.trazas, list)
    assert len(resultado.trazas) >= 1
    assert isinstance(resultado.advertencias, list)


@pytest.mark.parametrize(
    "resultado",
    [
        evaluar_lector_inteligente_documental(
            SolicitudLecturaDocumental(
                accion="leer",
                descripcion="regresion_error",
                solicitante="qa",
                contexto={},
                texto_documento="",
            )
        ),
        evaluar_radar_anomalias(
            SolicitudRadarAnomalias(
                accion="detectar_anomalias",
                descripcion="regresion_error",
                solicitante="qa",
                contexto={},
                serie=[1, 2],
            )
        ),
        evaluar_forjador_informes(
            SolicitudForjadorInformes(
                accion="forjar_informe",
                descripcion="regresion_error",
                solicitante="qa",
                contexto={},
            )
        ),
    ],
)
def test_regresion_contrato_en_errores_mantiene_estructura(resultado: object) -> None:
    assert resultado.estado == "error"
    assert isinstance(resultado.salida.get("mensaje"), str)
    assert resultado.salida["mensaje"].strip() != ""
    assert isinstance(resultado.trazas, list)
    assert len(resultado.trazas) >= 1
