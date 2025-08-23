function Detalles({ user }) {
  return (
    <div className="detalles">
      <h3>Detalles del Proyecto</h3>
      <p><b>Id del proyecto:</b> {user.proyecto_id}</p>
      <p><b>Id de la convocatoria:</b> {user.convocatoria_id}</p>
      <p><b>Año convocatoria:</b> {user.convocatoria_id}</p>
      <p><b>Descripción convocatoria:</b> {user.desc_convocatoria}</p>
      <p><b>Código Proyecto:</b> {user.codigo_proyecto}</p>
      <p><b>Título:</b> {user.titulo_proyecto}</p>
      <p><b>Fecha Registro:</b> {user.fecha_registro}</p>
      <p><b>Fecha Aprobación:</b> {user.fecha_aprobacion}</p>
      <p><b>Entidad que Ejecuta:</b> {user.entidad_ejecuta}</p>
      <p><b>Tipo de Financiación:</b> {user.tipo_financiacion}</p>
      <p><b>Descripción Financiación:</b> {user.desc_financiacion}</p>
      <p><b>Nombre Programa CTI:</b> {user.nme_prog_cti}</p>
      <p><b>Área Temática:</b> {user.area_tematica}</p>
      <p><b>Estado del Proyecto:</b> {user.estado_proyecto}</p>
      <p><b>Tipo Proyecto:</b> {user.nme_tipo_proyecto}</p>
      <p><b>Ciudad:</b> {user.nme_ciudad_pry}</p>
    </div>
  );
}

export default Detalles;
