import { useEffect, useState } from "react";
import Hero from "./components/Hero";
import TrendList from "./components/TrendList";
import Footer from "./components/Footer";

function App() {
  const [trends, setTrends] = useState([]);

  useEffect(() => {
    fetch(`${import.meta.env.VITE_API_BASE_URL}/api/trends/`)
      .then(res => res.json())
      .then(data => setTrends(data))
      .catch(err => console.error(err));
  }, []);

  return (
    <div style={{ fontFamily: "system-ui, sans-serif", color: "#111" }}>
      <Hero />
      <TrendList trends={trends} />
      <Footer />
    </div>
  );
}

export default App;
