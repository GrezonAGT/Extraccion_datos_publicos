import Detalles from "./Detalles";

function Filas({ user, index, expandedRow, toggleRow }) {
  return (
    <>
      <tr
        onClick={() => toggleRow(index)}
        style={{
          cursor: "pointer",
          background: expandedRow === index ? "#f0f0f0" : "white"
        }}
      >
        <td>{user.codigo_proyecto}</td>
        <td>{user.titulo_proyecto}</td>
        <td>{user.fecha_registro}</td>
        <td>{user.nme_ciudad_pry}</td>
      </tr>

      {expandedRow === index && (
        <tr>
          <td colSpan="6">
            <Detalles user={user} />
          </td>
        </tr>
      )}
    </>
  );
}

export default Filas;
