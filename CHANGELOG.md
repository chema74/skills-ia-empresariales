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

### V5 en progreso

- Nuevas pruebas de regresion de contratos para las 10 skills en `tests/test_regresion_contratos_skills.py`.
- Nueva prueba de integracion de cumplimiento y aprobacion humana en `tests/integracion/test_flujo_cumplimiento_aprobacion.py`.
- Nueva demo de integracion V5 en `demos/demo_v5_integracion.py`.
- Evidencias de integracion V5 publicadas:
- `evidencias/salidas/demo_v5_integracion_riesgo_informe.json`
- `evidencias/salidas/demo_v5_integracion_normativa_aprobacion.json`
- Validacion actualizada en local: `50 passed`.

### V6 completada

- Nuevo orquestador multi-skill: `src/skillforge/skills/orquestador_multiskill.py`.
- Tres plantillas de pipeline empresariales implementadas:
- `riesgo_informe`
- `cumplimiento_publicacion`
- `cliente_comunicacion`
- Trazabilidad de extremo a extremo agregada por pipeline y por paso.
- Exportes publicos del orquestador anadidos en `src/skillforge/skills/__init__.py`.
- Documentacion V6 publicada en `docs/V6_PIPELINES.md`.
- Demo V6 publicada en `demos/demo_v6_orquestador_multiskill.py`.
- Evidencias V6 generadas:
- `evidencias/salidas/demo_v6_pipeline_riesgo_informe.json`
- `evidencias/salidas/demo_v6_pipeline_cumplimiento_publicacion.json`
- `evidencias/salidas/demo_v6_pipeline_cliente_comunicacion.json`
- Pruebas de integracion V6:
- `tests/integracion/test_orquestador_multiskill_v6.py`
- Validacion actualizada en local: `57 passed`.
