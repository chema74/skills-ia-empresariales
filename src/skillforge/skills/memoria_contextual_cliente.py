"""Skill 04: Memoria Contextual de Cliente (V1 local)."""

from dataclasses import dataclass, field
from datetime import datetime

from skillforge.core.contratos import EntradaSkill, ResultadoSkill
from skillforge.skills.base_skill import SkillBase


@dataclass
class EventoCliente:
    """Evento contextual asociado a un cliente."""

    fecha: str
    tipo: str
    detalle: str
    origen: str


@dataclass
class SolicitudMemoriaCliente(EntradaSkill):
    """Entrada para consolidar memoria contextual de cliente."""

    cliente_id: str = ""
    eventos: list[EventoCliente] = field(default_factory=list)
    responsable_actual: str | None = None
    prioridad_actual: str | None = None


class MemoriaContextualClienteSkill(SkillBase):
    """Consolida eventos de cliente y detecta conflictos basicos."""

    def __init__(self) -> None:
        super().__init__(nombre_skill="memoria_contextual_cliente")

    def ejecutar(self, entrada: SolicitudMemoriaCliente) -> ResultadoSkill:
        trazas: list[str] = []
        advertencias: list[str] = []
        self.nueva_traza(trazas, "inicio_memoria_cliente")

        if not entrada.cliente_id.strip():
            self.nueva_traza(trazas, "cliente_id_vacio")
            return self.construir_resultado(
                estado="error",
                salida={"mensaje": "cliente_id es obligatorio"},
                trazas=trazas,
                advertencias=advertencias,
            )

        if not entrada.eventos:
            self.nueva_traza(trazas, "sin_eventos")
            return self.construir_resultado(
                estado="error",
                salida={"mensaje": "No hay eventos para consolidar memoria"},
                trazas=trazas,
                advertencias=advertencias,
            )

        eventos_validos: list[tuple[datetime, EventoCliente]] = []
        for e in entrada.eventos:
            try:
                fecha_dt = datetime.fromisoformat(e.fecha)
                eventos_validos.append((fecha_dt, e))
            except ValueError:
                advertencias.append(f"fecha invalida ignorada: {e.fecha}")

        if not eventos_validos:
            self.nueva_traza(trazas, "eventos_invalidos")
            return self.construir_resultado(
                estado="error",
                salida={"mensaje": "Todos los eventos tienen fecha invalida"},
                trazas=trazas,
                advertencias=advertencias,
            )

        eventos_ordenados = [e for _, e in sorted(eventos_validos, key=lambda x: x[0])]
        self.nueva_traza(trazas, "eventos_ordenados")

        tipos = {e.tipo.strip().lower() for e in eventos_ordenados if e.tipo.strip()}
        if "queja" in tipos and "cierre" in tipos:
            advertencias.append("se detecta mezcla de eventos de queja y cierre: revisar consistencia")

        ultima_interaccion = eventos_ordenados[-1]
        timeline = [
            {
                "fecha": e.fecha,
                "tipo": e.tipo,
                "detalle": e.detalle,
                "origen": e.origen,
            }
            for e in eventos_ordenados
        ]

        self.nueva_traza(trazas, "memoria_consolidada")
        return self.construir_resultado(
            estado="ok",
            salida={
                "mensaje": "Memoria contextual consolidada en local",
                "cliente_id": entrada.cliente_id,
                "total_eventos": len(eventos_ordenados),
                "ultima_interaccion": {
                    "fecha": ultima_interaccion.fecha,
                    "tipo": ultima_interaccion.tipo,
                    "detalle": ultima_interaccion.detalle,
                },
                "responsable_actual": entrada.responsable_actual,
                "prioridad_actual": entrada.prioridad_actual,
                "timeline": timeline,
            },
            trazas=trazas,
            advertencias=advertencias,
        )


def evaluar_memoria_contextual_cliente(entrada: SolicitudMemoriaCliente) -> ResultadoSkill:
    """API funcional para compatibilidad con uso directo."""

    return MemoriaContextualClienteSkill().ejecutar(entrada)