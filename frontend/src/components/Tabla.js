import Filas from "./Filas";

function Tabla({ data, expandedRow, toggleRow }) {
  return (
    <table border="1">
      <thead>
        <tr>
          <th>Código Proyecto</th>
          <th>Título</th>
          <th>Fecha Registro</th>
          <th>Ciudad</th>
        </tr>
      </thead>
      <tbody>
        {data?.map((user, index) => (
          <Filas
            key={index}
            user={user}
            index={index}
            expandedRow={expandedRow}
            toggleRow={toggleRow}
          />
        ))}
      </tbody>
    </table>
  );
}

export default Tabla;