"""Demo local para Skill 06 Buscador Privado Aumentado."""

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from skillforge.skills import DocumentoPrivado, SolicitudBusquedaPrivada, evaluar_buscador_privado_aumentado


def main() -> None:
    corpus: list[DocumentoPrivado] = []
    for linea in (ROOT / "ejemplos" / "corpus_demo_buscador_privado.txt").read_text(encoding="utf-8").splitlines():
        if not linea.strip():
            continue
        doc_id, titulo, contenido, fuente = [x.strip() for x in linea.split("|", maxsplit=3)]
        corpus.append(DocumentoPrivado(doc_id=doc_id, titulo=titulo, contenido=contenido, fuente=fuente))

    entrada = SolicitudBusquedaPrivada(
        accion="buscar_corpus_privado",
        descripcion="Demo local skill 06",
        solicitante="equipo_operaciones",
        contexto={"entorno": "interno"},
        consulta="riesgo revision humana contingencia",
        corpus=corpus,
        top_k=2,
    )

    resultado = evaluar_buscador_privado_aumentado(entrada)
    salida = {
        "nombre_skill": resultado.nombre_skill,
        "estado": resultado.estado,
        "salida": resultado.salida,
        "trazas": resultado.trazas,
        "advertencias": resultado.advertencias,
    }

    print(json.dumps(salida, ensure_ascii=False, indent=2))
    ruta = ROOT / "evidencias" / "salidas" / "demo_buscador_privado_aumentado_v1.json"
    ruta.parent.mkdir(parents=True, exist_ok=True)
    ruta.write_text(json.dumps(salida, ensure_ascii=False, indent=2), encoding="utf-8")


if __name__ == "__main__":
    main()