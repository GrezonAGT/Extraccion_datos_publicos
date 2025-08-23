import { useState, useEffect } from 'react';
import './App.css';
import { useFetch } from './useFetch';
import SearchBar from './components/SearchBar';
import Tabla from './components/Tabla';

function App() {

  //Usamos useFetch creado por nosotros para obtener la infomacion de la API
  const { data } = useFetch("http://127.0.0.1:8000/resources");
  const [expandedRow, setExpandedRow] = useState(null);
  const [searchTerm, setSearchTerm] = useState("");

  const toggleRow = (index) => {
    setExpandedRow(expandedRow === index ? null : index);
  };

  // Filtrar los proyectos según búsqueda por título
  const filteredData = data?.filter((user) =>
    user.titulo_proyecto?.toLowerCase().includes(searchTerm.toLowerCase()) 
  );

  return (
    <div className="App">
      <h1>Proyectos de Investigación e Innovación evaluados y aprobados desde el año 2009</h1>

      <SearchBar searchTerm={searchTerm} setSearchTerm={setSearchTerm} />

      <div className="card">
        <Tabla data={filteredData} expandedRow={expandedRow} toggleRow={toggleRow}/>
      </div>
    </div>
  );
}
export default App;
