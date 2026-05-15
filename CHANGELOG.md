# Changelog

## 2026-05-15

### Documentacion

- Reescritura de documentos Markdown a formato legible y consistente, sin iconos.
- Actualizacion de `ROADMAP.md` con estado real del repositorio y plan V5 a V8.
- Creacion de `RELEASE_CHECKLIST.md` con criterios operativos de salida.
- Alineacion de `README.md` con la madurez actual del repositorio.
- Refuerzo de `README.md` para evaluacion tecnica de reclutadores (quickstart, resultados, metricas y enlaces de arquitectura).
- Creacion de `docs/ARQUITECTURA_FLUJO.md` con diagrama textual de flujo end-to-end.

### Calidad y validacion

- Correccion de lint en `buscador_privado_aumentado.py` por variable ambigua (`E741`).
- Correccion de tipado en `base_skill.py` para cumplir con mypy (`dict[str, Any]`).
- Verificacion local de pruebas: `36 passed`.

### CI

- Mejora del workflow `.github/workflows/validacion.yml`:
- Activacion de ejecucion manual con `workflow_dispatch`.
- Cache de dependencias `pip` en `actions/setup-python`.
- Ejecucion de Ruff y mypy via `python -m` para mayor portabilidad.

### Entorno local

- Limpieza de residuos de instalacion `~treamlit` en el entorno Python local para eliminar warnings de `pip`.
