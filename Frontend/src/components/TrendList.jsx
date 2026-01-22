import TrendCard from "./TrendCard";

function TrendList({ trends }) {
  return (
    <section style={{ padding: "40px 80px" }}>
      <h2 style={{ fontSize: "2rem", marginBottom: "24px" }}>
        Trending Right Now
      </h2>

      <div
        style={{
          display: "grid",
          gridTemplateColumns: "repeat(auto-fit, minmax(260px, 1fr))",
          gap: "24px",
        }}
      >
        {trends.map(trend => (
          <TrendCard key={trend.id} trend={trend} />
        ))}
      </div>
    </section>
  );
}

export default TrendList;
