import { useState } from "react";
import api from "../api";

function UrlForm({ onAdd }) {
  const [url, setUrl] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();

    if (!url.trim()) return;

    try {
      await api.post("/urls/", {
        url,
      });

      setUrl("");
      onAdd();
    } catch (err) {
      alert(
        err.response?.data?.detail ||
          "Failed to add URL"
      );
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <input
        type="text"
        placeholder="https://example.com"
        value={url}
        onChange={(e) =>
          setUrl(e.target.value)
        }
      />

      <button type="submit">
        Add URL
      </button>
    </form>
  );
}

export default UrlForm;