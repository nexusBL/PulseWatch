import { useEffect, useState } from "react";

import api from "./api";
import Header from "./components/Header";
import UrlForm from "./components/UrlForm";
import StatusTable from "./components/StatusTable";

function App() {
  const [statusData, setStatusData] = useState([]);

  const fetchStatus = async () => {
    try {
      const response = await api.get("/urls/status");
      setStatusData(response.data);
    } catch (err) {
      console.error("Fetch Status Error:", err);
    }
  };

  const handleDelete = async (id) => {
    try {
      await api.delete(`/urls/${id}`);
      fetchStatus();
    } catch (err) {
      console.error("Delete Error:", err);
    }
  };

  useEffect(() => {
    fetchStatus();

    const interval = setInterval(() => {
      fetchStatus();
    }, 5000);

    return () => clearInterval(interval);
  }, []);

  return (
    <div style={{ padding: "2rem" }}>
      <Header />

      <UrlForm onAdd={fetchStatus} />

      <br />

      <StatusTable
        data={statusData}
        onDelete={handleDelete}
      />
    </div>
  );
}

export default App;