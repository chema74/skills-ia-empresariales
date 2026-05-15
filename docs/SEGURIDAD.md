# Seguridad

## Seguridad por diseno

El proyecto incorpora seguridad por diseno como criterio transversal desde la definicion de contratos hasta la ejecucion local.

## Validacion de entradas

Toda entrada debe validarse por tipo, formato y limites antes de procesarse.

## Control de salidas

Las salidas deben seguir contratos explicitos y registrar advertencias cuando existan incertidumbres.

## Trazabilidad

Las ejecuciones deben conservar trazas locales para permitir auditoria, depuracion y revision de decisiones.

## Separacion logica local y proveedor LLM

La logica de negocio local y la integracion con proveedores LLM se mantienen separadas para reducir acoplamiento y riesgo operativo.

## No incluir claves reales

No se deben almacenar claves reales en el repositorio. Solo se permite el uso de `.env.example` como plantilla.

## Revision humana para acciones sensibles

Las acciones de impacto deben pasar por control y aprobacion humana documentada.

## Limites del proyecto

Este repositorio no pretende cubrir por si solo requisitos legales o regulatorios completos de cada sector.

## Alcance de seguridad

No se promete seguridad absoluta; se establecen medidas de validacion, trazabilidad, revision humana y limites explicitos.

Publicado bajo licencia Creative Commons CC BY-SA 4.0 International.
(c) 2025 - Txema Rios. Todos los derechos compartidos.
