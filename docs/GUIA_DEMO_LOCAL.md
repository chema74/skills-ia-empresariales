# Guia Demo Local

## Instalacion de dependencias de desarrollo

```bash
python -m pip install -e ".[dev]"
```

## Ejecucion de tests

```bash
python -m pytest -q
```

## Ejecucion de demo V2

```bash
python demos/demo_puerta_aprobacion_humana.py
```

## Ejecucion por CLI local

Bloqueo por falta de aprobacion humana:

```bash
python ejemplos/cli_puerta_aprobacion_humana.py --accion aprobar_pago --descripcion "Pago urgente" --solicitante finanzas
```

Aprobacion explicita de accion sensible:

```bash
python ejemplos/cli_puerta_aprobacion_humana.py --accion aprobar_pago --descripcion "Pago urgente" --solicitante finanzas --aprobador direccion --aprobada
```

## Evidencia de salida

La demo V2 guarda una evidencia reproducible en:

- `evidencias/salidas/demo_puerta_aprobacion_humana_v2.json`

## Criterio de demos futuras

Las demos deben funcionar en local sin depender de APIs externas para su validacion basica.

## Proveedor LLM opcional en fases futuras

Groq puede anadirse como proveedor LLM opcional en iteraciones posteriores, sin romper el flujo local-first.

## Alcance V0 V1 V2

- V0 valida estructura de repositorio, documentacion base y contrato comun minimo.
- V1 anade utilidades de validacion y trazabilidad local.
- V2 incorpora la primera skill funcional con control humano explicito.

Publicado bajo licencia Creative Commons CC BY-SA 4.0 International.
(c) 2025 - Txema Rios. Todos los derechos compartidos.
