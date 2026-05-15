# V8 Adaptadores LLM Opcionales

## Objetivo

Habilitar integracion con proveedor LLM opcional sin romper ejecucion local-first.

## Componentes

- Capa de adaptadores: `src/skillforge/core/adaptadores_llm.py`
- Skill de uso: `src/skillforge/skills/compositor_llm_opcional.py`

## Adaptadores implementados

1. `mock_groq`
- Proveedor opcional simulado.
- Se habilita con `SKILLFORGE_ENABLE_MOCK_GROQ=1`.

2. `local_reglas`
- Fallback local garantizado.
- Siempre disponible y sin dependencias externas.

## Contrato comun de adaptador

Respuesta tipada `RespuestaAdaptadorLLM` con:

- `proveedor`
- `estado`
- `texto`
- `tokens_estimados`
- `error` opcional

## Fallback garantizado

Funcion `generar_con_fallback(...)`:

1. Intenta proveedor preferido.
2. Si falla o no esta disponible, activa `local_reglas`.
3. Devuelve salida valida para mantener operacion local intacta.

## Validacion automatica

- `tests/test_adaptadores_llm_v8.py`
- `tests/test_compositor_llm_opcional_v8.py`

## Demo y evidencia

- Demo: `demos/demo_v8_adaptadores_llm.py`
- Evidencia: `evidencias/salidas/demo_v8_adaptadores_llm.json`
