"""Clase base para implementar skills reutilizables."""

from typing import Any

from skillforge.core.contratos import ResultadoSkill
from skillforge.core.trazabilidad import agregar_traza_local
from skillforge.core.validacion import validar_resultado_skill


class SkillBase:
    """Plantilla comun para construir skills empresariales."""

    nombre_skill: str

    def __init__(self, nombre_skill: str) -> None:
        self.nombre_skill = nombre_skill

    def nueva_traza(self, trazas: list[str], evento: str) -> list[str]:
        """Agrega una traza local a la ejecucion."""

        return agregar_traza_local(trazas, evento)

    def construir_resultado(
        self,
        estado: str,
        salida: dict[str, Any],
        trazas: list[str],
        advertencias: list[str] | None = None,
    ) -> ResultadoSkill:
        """Crea y valida un ResultadoSkill estandar."""

        salida_normalizada = dict(salida)
        salida_normalizada["mensaje"] = self._normalizar_mensaje(estado=estado, mensaje=salida.get("mensaje"))
        advertencias_normalizadas = self._normalizar_advertencias(advertencias or [])

        resultado = ResultadoSkill(
            nombre_skill=self.nombre_skill,
            estado=estado,
            salida=salida_normalizada,
            trazas=trazas,
            advertencias=advertencias_normalizadas,
        )

        es_valido, errores = validar_resultado_skill(resultado)
        if not es_valido:
            self.nueva_traza(trazas, "resultado_con_errores_de_contrato")
            resultado.estado = "error"
            resultado.advertencias.extend(self._normalizar_advertencias(errores))
            resultado.salida["mensaje"] = self._normalizar_mensaje(
                estado="error",
                mensaje="Resultado invalido por reglas de contrato",
            )

        return resultado

    def _normalizar_mensaje(self, estado: str, mensaje: Any) -> str:
        texto = str(mensaje or "").strip() or "sin detalle"
        prefijo_por_estado = {
            "ok": "OK",
            "error": "ERROR",
            "advertencia": "ADVERTENCIA",
        }
        prefijo = prefijo_por_estado.get(estado, "INFO")
        if texto.upper().startswith(f"{prefijo}:"):
            return texto
        return f"{prefijo}: {texto}"

    def _normalizar_advertencias(self, advertencias: list[str]) -> list[str]:
        normalizadas: list[str] = []
        for advertencia in advertencias:
            texto = advertencia.strip()
            if not texto:
                continue
            if texto.upper().startswith("WARN:"):
                normalizadas.append(texto)
            else:
                normalizadas.append(f"WARN: {texto}")
        return normalizadas
