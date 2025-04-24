from pydataxm.pydatasimem import ReadSIMEM

datasets = {'AECA28':'VertimientosHidricos','B0E933':'ReservasHidraulicasEnergía'}
fecha_inicio = '2013-01-01'
fecha_fin = '2025-03-31'

for dataset_id in datasets:

    generacion = ReadSIMEM(dataset_id, fecha_inicio, fecha_fin)
    data = generacion.main(filter=False)

    data.to_excel(f'Data\{datasets[dataset_id]}.xlsx', index=False)