## ADDED Requirements

### Requirement: Generación de documentos Markdown
El sistema SHALL proveer cinco documentos Markdown que simulan la documentación oficial de AluraBank (Privacidad, Términos, FAQ, Seguridad, Tarifas) para ser consumidos por el pipeline RAG.

#### Scenario: Los documentos se encuentran disponibles en el sistema de archivos
- **WHEN** se inicie la indexación de la base vectorial del RAG
- **THEN** el sistema leerá correctamente los 5 archivos Markdown que contienen las políticas y reglas del banco.

### Requirement: Casos lógicos en los documentos
Los documentos SHALL incluir reglas de negocio condicionales (ej. retiros gratis solo para nivel Premium, coberturas por fraude condicionadas a tiempos de reporte).

#### Scenario: El RAG se enfrenta a una regla condicional
- **WHEN** un documento especifica que "el límite es X si se usa PIN, pero Y si se usa biometría"
- **THEN** esa información debe estar redactada explícitamente en el Markdown para que el modelo la extraiga.
