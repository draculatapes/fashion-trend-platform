function TrendCard({ trend }) {
  return (
    <div
      style={{
        padding: "20px",
        borderRadius: "14px",
        border: "1px solid #eee",
        backgroundColor: "#fafafa",
      }}
    >
      <h3 style={{ marginBottom: "8px" }}>{trend.title}</h3>

      <p style={{ color: "#555", fontSize: "0.9rem" }}>
        Region: {trend.region}
      </p>

      <p style={{ color: "#777", fontSize: "0.85rem" }}>
        Category: {trend.category}
      </p>

      <span
        style={{
          display: "inline-block",
          marginTop: "12px",
          padding: "4px 10px",
          fontSize: "0.75rem",
          borderRadius: "20px",
          backgroundColor: "#111",
          color: "#fff",
        }}
      >
        {trend.status}
      </span>
    </div>
  );
}

export default TrendCard;
