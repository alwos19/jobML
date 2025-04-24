from pydataxm.pydatasimem import ReadSIMEM

dataset_id = 'AECA28'
fecha_inicio = '2013-01-01'
fecha_fin = '2025-03-31'

generacion = ReadSIMEM(dataset_id, fecha_inicio, fecha_fin)

# Recuperar datos
data = generacion.main(filter=False)

data.to_excel('Data\VertimientosHidricos.xlsx', index=False)