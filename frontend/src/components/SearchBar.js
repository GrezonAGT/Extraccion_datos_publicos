function SearchBar({ searchTerm, setSearchTerm }) {
  return (
    <input
      type="text"
      placeholder="Buscar por palabra clave en el título"
      value={searchTerm}
      onChange={(e) => setSearchTerm(e.target.value)}
      style={{ marginBottom: "15px", padding: "8px", width: "50%" }}
    />
  );
}

export default SearchBar;
