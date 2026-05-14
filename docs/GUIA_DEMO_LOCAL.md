# Guía Demo Local

## Instalación de dependencias de desarrollo

```bash
python -m pip install -e ".[dev]"
```

## Ejecución de tests

```bash
python -m pytest -q
```

## Ejecución de demo V2

```bash
python demos/demo_puerta_aprobacion_humana.py
```

## Ejecución por CLI local

Bloqueo por falta de aprobación humana:

```bash
python ejemplos/cli_puerta_aprobacion_humana.py --accion aprobar_pago --descripcion "Pago urgente" --solicitante finanzas
```

Aprobación explícita de acción sensible:

```bash
python ejemplos/cli_puerta_aprobacion_humana.py --accion aprobar_pago --descripcion "Pago urgente" --solicitante finanzas --aprobador direccion --aprobada
```

## Evidencia de salida

La demo V2 guarda una evidencia reproducible en:

- `evidencias/salidas/demo_puerta_aprobacion_humana_v2.json`

## Criterio de demos futuras

Las demos deberán funcionar en local sin depender de APIs externas para su validación básica.

## Proveedor LLM opcional en fases futuras

Groq podrá añadirse como proveedor LLM opcional en iteraciones posteriores, sin romper el flujo local-first.

## Alcance V0/V1/V2

- V0 valida estructura de repositorio, documentación base y contrato común mínimo.
- V1 añade utilidades de validación y trazabilidad local.
- V2 incorpora la primera skill funcional con control humano explícito.

Publicado bajo licencia Creative Commons CC BY-SA 4.0 International.  
© 2025 – Txema Ríos. Todos los derechos compartidos.