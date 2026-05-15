# Skills IA Empresariales

Biblioteca modular en castellano de skills IA empresariales reutilizables, auditables y demostrables.

## Para reclutadores tecnicos

Repositorio de ingenieria IA aplicada orientado a producto:

- Arquitectura modular de skills empresariales y de plataforma.
- Contrato comun tipado para interoperabilidad.
- Validacion estatica y pruebas automatizadas.
- Demos y evidencias reproducibles en local.

## Problema que resuelve

Este repositorio define una base tecnica para construir capacidades IA reutilizables que puedan funcionar de forma independiente o integradas en agentes mayores. No es una coleccion de prompts y no es un agente monolitico.

## Principios tecnicos

- Modularidad por skill con contratos comunes.
- Enfoque free-first y local-first.
- Trazabilidad, validacion y revision humana en acciones sensibles.
- Limites explicitos sobre automatizacion y alcance.
- Compatibilidad con Python 3.11.

## Estado actual

El repositorio se encuentra en estado operativo local-first con roadmap V0-V8 completada.

Resumen de avance:

- V0: estructura base, documentacion inicial, contrato comun minimo y test de humo.
- V1: nucleo comun de validacion y trazabilidad reutilizable.
- V2: primera skill funcional con control humano explicito.
- V3: implementacion del catalogo empresarial en modulos independientes.
- V4: demos locales y evidencias reproducibles para validacion tecnica.
- V5: endurecimiento de calidad, regresion de contratos y evidencias de integracion.
- V6: orquestador multi-skill con 3 pipelines empresariales.
- V7: gobernanza versionada y checklist de auditoria tecnica por release.
- V8: capa de adaptadores LLM opcionales con fallback local garantizado.

## Skills implementadas

01. Lector Inteligente Documental
02. Radar de Anomalias
03. Forjador de Informes
04. Memoria Contextual de Cliente
05. Pulso de Riesgo
06. Buscador Privado Aumentado
07. Enrutador Inteligente
08. Voz de Marca Inteligente
09. Verificador Normativo
10. Puerta de Aprobacion Humana

Capacidades de plataforma adicionales:

- Orquestador multi-skill (`orquestador_multiskill`).
- Compositor con adaptadores LLM opcionales (`compositor_llm_opcional`).

## Arranque rapido en 2 minutos

```bash
python -m pip install -e ".[dev]"
python -m ruff check src tests
python -m mypy src
python -m pytest -q
```

## Resultados verificables

Casos de uso demostrables con salida reproducible:

- Demos ejecutables: `demos/demo_*.py`.
- Evidencias generadas: `evidencias/salidas/demo_*.json`.
- Flujos integrados multi-skill: `tests/integracion/`.

## Metricas de calidad (estado actual)

- `ruff`: en verde.
- `mypy`: en verde (`22` ficheros revisados).
- `pytest`: en verde (`69` tests).
- CI activa en `.github/workflows/validacion.yml`.

## Arquitectura y flujo

- `docs/ARQUITECTURA.md`
- `docs/ARQUITECTURA_FLUJO.md`
- `docs/V6_PIPELINES.md`
- `docs/V8_ADAPTADORES_LLM.md`

## Nota de seguridad por diseno

La arquitectura aplica seguridad por diseno mediante validacion, trazabilidad y limites explicitos. Las decisiones de alto impacto requieren revision humana.

## Aclaracion profesional

Este proyecto no sustituye revision profesional en ambitos regulados (legal, fiscal, sanitario, financiero o equivalentes).

Publicado bajo licencia Creative Commons CC BY-SA 4.0 International.
(c) 2025 - Txema Rios. Todos los derechos compartidos.
