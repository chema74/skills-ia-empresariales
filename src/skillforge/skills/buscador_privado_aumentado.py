"""Skill 06: Buscador Privado Aumentado (V1 local)."""

from dataclasses import dataclass, field

from skillforge.core.contratos import EntradaSkill, ResultadoSkill
from skillforge.skills.base_skill import SkillBase


@dataclass
class DocumentoPrivado:
    """Documento interno indexable en memoria local."""

    doc_id: str
    titulo: str
    contenido: str
    fuente: str


@dataclass
class SolicitudBusquedaPrivada(EntradaSkill):
    """Entrada para busqueda local sobre corpus privado."""

    consulta: str = ""
    corpus: list[DocumentoPrivado] = field(default_factory=list)
    top_k: int = 3


class BuscadorPrivadoAumentadoSkill(SkillBase):
    """Realiza busqueda lexical local y devuelve citas internas."""

    def __init__(self) -> None:
        super().__init__(nombre_skill="buscador_privado_aumentado")

    def ejecutar(self, entrada: SolicitudBusquedaPrivada) -> ResultadoSkill:
        trazas: list[str] = []
        advertencias: list[str] = []
        self.nueva_traza(trazas, "inicio_busqueda_privada")

        if not entrada.consulta.strip():
            self.nueva_traza(trazas, "consulta_vacia")
            return self.construir_resultado(
                estado="error",
                salida={"mensaje": "Consulta vacia: define terminos de busqueda"},
                trazas=trazas,
                advertencias=advertencias,
            )

        if not entrada.corpus:
            self.nueva_traza(trazas, "corpus_vacio")
            return self.construir_resultado(
                estado="error",
                salida={"mensaje": "Corpus vacio: no hay documentos internos"},
                trazas=trazas,
                advertencias=advertencias,
            )

        tokens = [t.lower() for t in entrada.consulta.split() if t.strip()]
        resultados: list[tuple[int, DocumentoPrivado, list[str]]] = []

        for doc in entrada.corpus:
            texto = f"{doc.titulo} {doc.contenido}".lower()
            coincidencias = [tok for tok in tokens if tok in texto]
            score = len(coincidencias)
            if score > 0:
                citas = self._extraer_citas(doc.contenido, coincidencias)
                resultados.append((score, doc, citas))

        self.nueva_traza(trazas, "ranking_calculado")
        resultados.sort(key=lambda x: x[0], reverse=True)
        top_k = max(1, entrada.top_k)
        top = resultados[:top_k]

        if not top:
            advertencias.append("sin resultados para la consulta en el corpus privado")

        items = [
            {
                "doc_id": doc.doc_id,
                "titulo": doc.titulo,
                "fuente": doc.fuente,
                "score": score,
                "citas": citas,
            }
            for score, doc, citas in top
        ]

        self.nueva_traza(trazas, "respuesta_generada")
        return self.construir_resultado(
            estado="ok",
            salida={
                "mensaje": "Busqueda privada completada en local",
                "consulta": entrada.consulta,
                "total_resultados": len(items),
                "resultados": items,
            },
            trazas=trazas,
            advertencias=advertencias,
        )

    def _extraer_citas(self, contenido: str, tokens: list[str], max_citas: int = 2) -> list[str]:
        lineas = [l.strip() for l in contenido.splitlines() if l.strip()]
        citas: list[str] = []
        for linea in lineas:
            lmin = linea.lower()
            if any(tok in lmin for tok in tokens):
                citas.append(linea[:160])
            if len(citas) >= max_citas:
                break
        return citas


def evaluar_buscador_privado_aumentado(entrada: SolicitudBusquedaPrivada) -> ResultadoSkill:
    """API funcional para compatibilidad con uso directo."""

    return BuscadorPrivadoAumentadoSkill().ejecutar(entrada)