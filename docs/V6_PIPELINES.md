# V6 Pipelines Multi-skill

## Objetivo

Definir flujos empresariales reutilizables que encadenan skills con trazabilidad completa de extremo a extremo.

## Orquestador

- Skill: `orquestador_multiskill`
- API funcional: `evaluar_orquestador_multiskill`
- Entrada: `SolicitudOrquestacion`
- Salida: `ResultadoSkill` con detalle de pasos ejecutados, estado por paso, trazas y advertencias.

## Pipelines disponibles

### 1. riesgo_informe

Secuencia:
1. `enrutador_inteligente`
2. `pulso_riesgo`
3. `forjador_informes`

Uso recomendado:
- Evaluacion de riesgo operativo con emision de informe ejecutivo.

### 2. cumplimiento_publicacion

Secuencia:
1. `verificador_normativo`
2. `puerta_aprobacion_humana`

Uso recomendado:
- Control de cumplimiento previo a publicacion de comunicacion externa.

### 3. cliente_comunicacion

Secuencia:
1. `memoria_contextual_cliente`
2. `voz_marca_inteligente`

Uso recomendado:
- Consolidacion de contexto de cliente y generacion de comunicacion de marca.

## Trazabilidad E2E

Cada ejecucion incorpora:

- Traza de inicio de pipeline.
- Trazas por inicio de cada paso.
- Trazas internas de cada skill prefijadas por paso.
- Traza de cierre con estado final del pipeline.

## Validacion automatica

Pruebas de integracion:

- `tests/integracion/test_orquestador_multiskill_v6.py`
- `tests/integracion/test_flujo_integrado.py`
- `tests/integracion/test_flujo_cumplimiento_aprobacion.py`
