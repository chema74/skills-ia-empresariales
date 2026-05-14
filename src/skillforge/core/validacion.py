"""Utilidades de validacion para contratos comunes."""

from skillforge.core.contratos import ResultadoSkill


ESTADOS_VALIDOS = {"ok", "error", "advertencia"}


def validar_resultado_skill(resultado: ResultadoSkill) -> tuple[bool, list[str]]:
    """Valida reglas minimas del contrato ResultadoSkill."""

    errores: list[str] = []

    if not resultado.nombre_skill.strip():
        errores.append("nombre_skill no puede estar vacio")

    if resultado.estado not in ESTADOS_VALIDOS:
        errores.append("estado no permitido en contrato")

    if "mensaje" not in resultado.salida:
        errores.append("salida debe incluir la clave 'mensaje'")

    if not resultado.trazas:
        errores.append("trazas debe contener al menos un registro")

    return len(errores) == 0, errores