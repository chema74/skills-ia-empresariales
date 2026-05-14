"""Demo local para Skill 05 Pulso de Riesgo."""

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from skillforge.skills import FactorRiesgo, SolicitudPulsoRiesgo, evaluar_pulso_riesgo


def main() -> None:
    factores: list[FactorRiesgo] = []
    for linea in (ROOT / "ejemplos" / "factores_demo_pulso_riesgo.txt").read_text(encoding="utf-8").splitlines():
        if not linea.strip():
            continue
        nombre, severidad, peso = [x.strip() for x in linea.split("|", maxsplit=2)]
        factores.append(FactorRiesgo(nombre=nombre, severidad=int(severidad), peso=float(peso)))

    entrada = SolicitudPulsoRiesgo(
        accion="calcular_pulso_riesgo",
        descripcion="Demo local skill 05",
        solicitante="oficina_riesgos",
        contexto={"periodo": "mensual"},
        factores=factores,
        umbral_medio=35.0,
        umbral_alto=70.0,
    )

    resultado = evaluar_pulso_riesgo(entrada)
    salida = {
        "nombre_skill": resultado.nombre_skill,
        "estado": resultado.estado,
        "salida": resultado.salida,
        "trazas": resultado.trazas,
        "advertencias": resultado.advertencias,
    }

    print(json.dumps(salida, ensure_ascii=False, indent=2))
    ruta = ROOT / "evidencias" / "salidas" / "demo_pulso_riesgo_v1.json"
    ruta.parent.mkdir(parents=True, exist_ok=True)
    ruta.write_text(json.dumps(salida, ensure_ascii=False, indent=2), encoding="utf-8")


if __name__ == "__main__":
    main()