# Roadmap

## Estado actual (mayo 2026)

El repositorio se encuentra en estado funcional local-first con:

- 10 skills implementadas y validadas.
- Contrato comun estable (`EntradaSkill` y `ResultadoSkill`).
- Demos locales y evidencias reproducibles.
- Base de seguridad por diseno con trazabilidad y revision humana para acciones sensibles.

## V5 - Endurecimiento tecnico y calidad

Objetivo: aumentar fiabilidad operativa y mantenibilidad.

Estado: en progreso (2026-05-15).

- Elevar cobertura de pruebas unitarias y anadir pruebas de integracion entre skills.
- Incluir verificacion estatica en CI (`ruff`, `mypy`) con umbrales minimos definidos.
- Anadir pruebas de regresion para contratos de entrada/salida.
- Estandarizar mensajes de error y advertencias para facilitar observabilidad.

Criterio de cierre V5:

- CI en verde de forma estable.
- Sin errores criticos en linting y tipado estatico.
- Evidencias de pruebas de integracion publicadas.

## V6 - Orquestacion y flujos multi-skill

Objetivo: pasar de skills aisladas a flujos de trabajo coordinados.

Estado: completado (2026-05-15).

- Disenar un orquestador local para encadenar skills con reglas explicitas.
- Definir plantillas de pipeline para casos de uso empresariales frecuentes.
- Anadir trazabilidad de extremo a extremo en ejecuciones multi-skill.

Criterio de cierre V6:

- Al menos 3 pipelines multi-skill documentados y probados.
- Trazas completas por ejecucion con identificacion de cada paso.

## V7 - Gobernanza avanzada y auditoria

Objetivo: reforzar control, cumplimiento y capacidad de auditoria.

Estado: completado (2026-05-15).

- Extender controles de aprobacion humana con politicas por tipo de accion.
- Versionar politicas de validacion y registrar cambios de gobernanza.
- Incorporar checklists de auditoria tecnica para cada release.

Criterio de cierre V7:

- Politicas versionadas y trazables.
- Evidencias de auditoria publicadas para todos los flujos criticos.

## V8 - Integracion opcional con proveedores LLM

Objetivo: habilitar capacidades LLM sin romper el modo local-first.

Estado: completado (2026-05-15).

- Crear capa de adaptadores para proveedores externos opcionales.
- Mantener fallback local funcional cuando no haya conexion o proveedor.
- Definir pruebas de contrato para garantizar compatibilidad entre adaptadores.

Criterio de cierre V8:

- Integracion opcional activa con al menos un proveedor.
- Ejecucion local base intacta y validada sin dependencias externas.

## Mantenimiento continuo

- Revisar roadmap al cierre de cada version.
- Publicar fecha de ultima validacion en documentacion tecnica.
- Mantener consistencia entre estado real, catalogo tecnico y roadmap.

Publicado bajo licencia Creative Commons CC BY-SA 4.0 International.  
(c) 2025 - Txema Rios. Todos los derechos compartidos.
