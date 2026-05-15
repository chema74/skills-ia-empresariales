# Release Checklist

## Objetivo

Esta checklist define los controles minimos para considerar una version lista para publicar.

## Checklist previa a release

1. Calidad estatica en verde
- Ejecutar `ruff check src tests`.
- Ejecutar `mypy src`.
- Confirmar que no hay errores pendientes.

2. Tests automaticos en verde
- Ejecutar `python -m pytest -q`.
- Confirmar 0 fallos y 0 errores.

3. Entorno reproducible
- Validar instalacion limpia con `python -m pip install -e ".[dev]"`.
- Confirmar que el proyecto arranca en entorno nuevo.

4. Contrato comun estable
- Verificar que todas las skills usan `EntradaSkill`.
- Verificar que todas las skills devuelven `ResultadoSkill`.

5. Demos funcionales
- Ejecutar demos principales en `demos/`.
- Ejecutar CLI relevante en `ejemplos/`.
- Confirmar que la salida coincide con el comportamiento esperado.

6. Evidencias actualizadas
- Regenerar evidencias en `evidencias/salidas/` si hubo cambios funcionales.
- Revisar coherencia entre evidencias y resultados actuales.

7. Documentacion consistente
- Revisar `README.md`, `ROADMAP.md`, `RESUMEN_EJECUTIVO.md` y `CATALOGO_TECNICO.md`.
- Confirmar que estado y alcance son coherentes entre documentos.

8. Seguridad y gobernanza minima
- Confirmar ausencia de secretos y claves reales en el repositorio.
- Verificar uso de `.env.example` como plantilla.
- Confirmar revision humana activa en acciones sensibles.

9. Higiene de repositorio
- Ejecutar `git status`.
- Verificar que no hay archivos temporales, caches o artefactos no deseados.

10. Criterio de cierre de version
- Registrar una nota corta de release con:
- Cambios principales.
- Riesgos conocidos.
- Validaciones ejecutadas.

## Criterio de salida

La version se considera lista solo cuando los 10 puntos anteriores estan completos y verificados.
