"""Demo V8: adaptadores LLM opcionales con fallback local."""

import json
import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from skillforge.skills import SolicitudComposicionLLM, evaluar_compositor_llm_opcional


def _serializar(resultado: object) -> dict[str, object]:
    return {
        "nombre_skill": resultado.nombre_skill,
        "estado": resultado.estado,
        "salida": resultado.salida,
        "trazas": resultado.trazas,
        "advertencias": resultado.advertencias,
    }


def main() -> None:
    os.environ["SKILLFORGE_ENABLE_MOCK_GROQ"] = "0"
    run_fallback = evaluar_compositor_llm_opcional(
        SolicitudComposicionLLM(
            accion="componer_texto",
            descripcion="demo_v8",
            solicitante="orquestador",
            contexto={},
            prompt="Resume riesgos operativos en una frase.",
            proveedor_preferido="mock_groq",
        )
    )

    os.environ["SKILLFORGE_ENABLE_MOCK_GROQ"] = "1"
    run_proveedor = evaluar_compositor_llm_opcional(
        SolicitudComposicionLLM(
            accion="componer_texto",
            descripcion="demo_v8",
            solicitante="orquestador",
            contexto={},
            prompt="Redacta cierre ejecutivo para comite de riesgo.",
            proveedor_preferido="mock_groq",
        )
    )

    evidencia = {
        "v8": {
            "fallback_local": _serializar(run_fallback),
            "proveedor_opcional_habilitado": _serializar(run_proveedor),
        }
    }

    ruta = ROOT / "evidencias" / "salidas" / "demo_v8_adaptadores_llm.json"
    ruta.parent.mkdir(parents=True, exist_ok=True)
    ruta.write_text(json.dumps(evidencia, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps({"evidencia_generada": str(ruta.name)}, ensure_ascii=False))


if __name__ == "__main__":
    main()
