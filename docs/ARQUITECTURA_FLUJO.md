# Arquitectura y Flujo

## Componentes

- `src/skillforge/core`: contratos, validacion y trazabilidad comun.
- `src/skillforge/skills`: implementacion de skills empresariales.
- `demos/`: ejecuciones de referencia por skill.
- `evidencias/salidas/`: resultados JSON reproducibles.
- `tests/`: pruebas unitarias e integracion.

## Flujo de ejecucion

1. Cliente o proceso invoca una skill con una `EntradaSkill`.
2. La skill valida entrada y genera trazas locales.
3. La logica de negocio produce `ResultadoSkill`.
4. El resultado pasa por validacion de contrato.
5. Se devuelve salida estructurada con estado, trazas y advertencias.
6. Opcionalmente se persiste evidencia en JSON para auditoria.

## Diagrama textual

```text
[Solicitud]
    |
    v
[EntradaSkill] --> [SkillBase] --> [Skill concreta]
                      |               |
                      |               v
                      |          [Salida de negocio]
                      v               |
               [Validacion contrato]  |
                      |               |
                      +-------> [ResultadoSkill]
                                  |   |   |
                                  |   |   +--> advertencias
                                  |   +------> trazas
                                  +----------> estado + salida
                                              |
                                              v
                                    [Evidencia JSON opcional]
```
