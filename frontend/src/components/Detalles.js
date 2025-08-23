function Detalles({ user }) {
  return (
    <div className="detalles">
      <h3>Detalles del Proyecto</h3>
      <p><b>Id del proyecto:</b> {user.id}</p>
      <p><b>Código Proyecto:</b> {user.codigo_proyecto}</p>
      <p><b>Título:</b> {user.titulo_proyecto}</p>
      <p><b>Fecha Registro:</b> {user.fecha_registro}</p>
      <p><b>Nombre Programa CTI:</b> {user.nme_prog_cti}</p>
      <p><b>Área Temática:</b> {user.area_tematica}</p>
      <p><b>Ciudad:</b> {user.nme_ciudad_pry}</p>
    </div>
  );
}

export default Detalles;
