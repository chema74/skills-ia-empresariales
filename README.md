# Skills IA Empresariales

Biblioteca modular en castellano de skills IA empresariales reutilizables, auditables y demostrables.

## Para reclutadores tecnicos

Repositorio de ingenieria IA aplicada orientado a producto:

- Arquitectura modular de 10 skills empresariales.
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

El repositorio se encuentra en estado operativo local-first con las 10 skills previstas implementadas y validadas.

Resumen de avance:

- V0: estructura base, documentacion inicial, contrato comun minimo y test de humo.
- V1: nucleo comun de validacion y trazabilidad reutilizable.
- V2: primera skill funcional con control humano explicito.
- V3: implementacion del catalogo empresarial en modulos independientes.
- V4: demos locales y evidencias reproducibles para validacion tecnica.

Las siguientes iteraciones se gestionan desde V5 en adelante en `ROADMAP.md`.

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

## Arranque rapido en 2 minutos

```bash
python -m pip install -e ".[dev]"
python -m ruff check src tests
python -m mypy src
python -m pytest -q
```

## Resultados verificables

Casos de uso demostrables con salida reproducible:

- Demos ejecutables: `demos/demo_*.py` (10 escenarios).
- Evidencias generadas: `evidencias/salidas/demo_*.json` (10 salidas).
- Flujo integrado multi-skill: `tests/integracion/test_flujo_integrado.py`.

Ejemplos directos:

- `demos/demo_pulso_riesgo.py` -> `evidencias/salidas/demo_pulso_riesgo_v1.json`
- `demos/demo_forjador_informes.py` -> `evidencias/salidas/demo_forjador_informes_v1.json`
- `demos/demo_puerta_aprobacion_humana.py` -> `evidencias/salidas/demo_puerta_aprobacion_humana_v2.json`

## Metricas de calidad (estado actual)

- `ruff`: en verde.
- `mypy`: en verde (`18` ficheros revisados).
- `pytest`: en verde (`36` tests).
- CI activa en `.github/workflows/validacion.yml`.

## Arquitectura y flujo

- `docs/ARQUITECTURA.md`
- `docs/ARQUITECTURA_FLUJO.md`

## Nota de seguridad por diseno

La arquitectura aplica seguridad por diseno mediante validacion, trazabilidad y limites explicitos. Las decisiones de alto impacto requieren revision humana.

## Aclaracion profesional

Este proyecto no sustituye revision profesional en ambitos regulados (legal, fiscal, sanitario, financiero o equivalentes).

Publicado bajo licencia Creative Commons CC BY-SA 4.0 International.
(c) 2025 - Txema Rios. Todos los derechos compartidos.
