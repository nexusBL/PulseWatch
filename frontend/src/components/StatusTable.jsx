function StatusTable({ data, onDelete }) {
  return (
    <table border="1" cellPadding="10">
      <thead>
        <tr>
          <th>URL</th>
          <th>Status</th>
          <th>Status Code</th>
          <th>Response Time (ms)</th>
          <th>Last Checked</th>
          <th>Actions</th>
        </tr>
      </thead>

      <tbody>
        {data.map((item) => (
          <tr key={item.id}>
            <td>{item.url}</td>

            <td>
              {item.is_up ? "🟢 UP" : "🔴 DOWN"}
            </td>

            <td>
              {item.status_code ?? "-"}
            </td>

            <td>
              {item.response_time
              ? `${item.response_time} ms`
              : "-"}
            </td>

            <td>
              {item.checked_at
                ? new Date(
                    item.checked_at
                  ).toLocaleString()
                : "-"}
            </td>

            <td>
              <button
                onClick={() =>
                  onDelete(item.id)
                }
              >
                Delete
              </button>
            </td>
          </tr>
        ))}
      </tbody>
    </table>
  );
}

export default StatusTable;