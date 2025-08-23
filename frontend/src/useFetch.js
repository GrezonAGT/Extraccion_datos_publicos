import { useState, useEffect } from "react";

export function useFetch(url) {
  const [data, setData] = useState(null);

  useEffect(() => {
    fetch(url)
      .then((response) => response.json())
      .then((data) => {
        // Formatear fechas al estilo YYYY-MM-DD
        const formattedData = data.map(item => ({
          ...item,
          fecha_registro: item.fecha_registro?.split("T")[0],
          fecha_aprobacion: item.fecha_aprobacion?.split("T")[0],
        }));
        setData(formattedData);
      });
  }, [url]);

  return { data };
}