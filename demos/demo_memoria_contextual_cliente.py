"""Demo local para Skill 04 Memoria Contextual de Cliente."""

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from skillforge.skills import EventoCliente, SolicitudMemoriaCliente, evaluar_memoria_contextual_cliente


def main() -> None:
    eventos: list[EventoCliente] = []
    for linea in (ROOT / "ejemplos" / "eventos_demo_memoria_cliente.txt").read_text(encoding="utf-8").splitlines():
        if not linea.strip():
            continue
        fecha, tipo, detalle, origen = [x.strip() for x in linea.split("|", maxsplit=3)]
        eventos.append(EventoCliente(fecha=fecha, tipo=tipo, detalle=detalle, origen=origen))

    entrada = SolicitudMemoriaCliente(
        accion="consolidar_memoria_cliente",
        descripcion="Demo local skill 04",
        solicitante="equipo_customer_success",
        contexto={"canal": "mixto"},
        cliente_id="CL-2026-001",
        eventos=eventos,
        responsable_actual="account_manager_01",
        prioridad_actual="alta",
    )

    resultado = evaluar_memoria_contextual_cliente(entrada)
    salida = {
        "nombre_skill": resultado.nombre_skill,
        "estado": resultado.estado,
        "salida": resultado.salida,
        "trazas": resultado.trazas,
        "advertencias": resultado.advertencias,
    }

    print(json.dumps(salida, ensure_ascii=False, indent=2))
    ruta = ROOT / "evidencias" / "salidas" / "demo_memoria_contextual_cliente_v1.json"
    ruta.parent.mkdir(parents=True, exist_ok=True)
    ruta.write_text(json.dumps(salida, ensure_ascii=False, indent=2), encoding="utf-8")


if __name__ == "__main__":
    main()