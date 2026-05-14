"""Clase base para implementar skills reutilizables."""

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
        salida: dict,
        trazas: list[str],
        advertencias: list[str] | None = None,
    ) -> ResultadoSkill:
        """Crea y valida un ResultadoSkill estandar."""

        resultado = ResultadoSkill(
            nombre_skill=self.nombre_skill,
            estado=estado,
            salida=salida,
            trazas=trazas,
            advertencias=advertencias or [],
        )

        es_valido, errores = validar_resultado_skill(resultado)
        if not es_valido:
            self.nueva_traza(trazas, "resultado_con_errores_de_contrato")
            resultado.estado = "error"
            resultado.advertencias.extend(errores)
            resultado.salida["mensaje"] = "Resultado invalido por reglas de contrato"

        return resultado