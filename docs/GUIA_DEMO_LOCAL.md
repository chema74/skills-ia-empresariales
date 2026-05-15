# Guia Demo Local

## Instalacion de dependencias de desarrollo

```bash
python -m pip install -e ".[dev]"
```

## Ejecucion de validacion completa

```bash
python -m ruff check src tests
python -m mypy src
python -m pytest -q
```

## Demos clave por fase

```bash
python demos/demo_puerta_aprobacion_humana.py
python demos/demo_v6_orquestador_multiskill.py
python demos/demo_v7_auditoria_gobernanza.py
python demos/demo_v8_adaptadores_llm.py
```

## Ejecucion por CLI local (gobernanza V7)

Bloqueo por falta de aprobacion humana:

```bash
python ejemplos/cli_puerta_aprobacion_humana.py --accion aprobar_pago --descripcion "Pago urgente" --solicitante finanzas
```

Aprobacion explicita de accion sensible con rol y evidencia:

```bash
python ejemplos/cli_puerta_aprobacion_humana.py --accion aprobar_pago --descripcion "Pago urgente" --solicitante finanzas --aprobador direccion --rol-aprobador direccion --evidencia-id EV-001 --aprobada
```

## Evidencias de salida

Se generan evidencias reproducibles en:

- `evidencias/salidas/demo_puerta_aprobacion_humana_v2.json`
- `evidencias/salidas/demo_v6_pipeline_riesgo_informe.json`
- `evidencias/salidas/demo_v7_auditoria_gobernanza.json`
- `evidencias/salidas/demo_v8_adaptadores_llm.json`

## Alcance actual

- V0-V8 completadas.
- Ejecucion local base intacta y validada sin dependencias externas.
- Capa LLM opcional disponible con fallback local garantizado.

Publicado bajo licencia Creative Commons CC BY-SA 4.0 International.
(c) 2025 - Txema Rios. Todos los derechos compartidos.
