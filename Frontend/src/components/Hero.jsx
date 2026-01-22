import { useEffect, useState } from "react";

import bg1 from "../assets/bg1.webp";
import bg2 from "../assets/bg2.webp";
import bg3 from "../assets/bg3.webp";
import bg4 from "../assets/bg4.webp";

const backgrounds = [bg1, bg2, bg3, bg4];

function Hero() {
  const [current, setCurrent] = useState(0);

  useEffect(() => {
    const interval = setInterval(() => {
      setCurrent(prev => (prev + 1) % backgrounds.length);
    }, 4000); // change every 4 seconds

    return () => clearInterval(interval);
  }, []);

  return (
    <section
      style={{
        position: "relative",
        height: "100vh",
        overflow: "hidden",
      }}
    >
      {/* BACKGROUND SLIDES */}
      {backgrounds.map((bg, index) => (
        <div
          key={index}
          style={{
            position: "absolute",
            inset: 0,
            backgroundImage: `url(${bg})`,
            backgroundSize: "cover",
            backgroundPosition: "center",
            opacity: index === current ? 1 : 0,
            transition: "opacity 1.2s ease-in-out",
          }}
        />
      ))}

      {/* DARK OVERLAY */}
      <div
        style={{
          position: "absolute",
          inset: 0,
          backgroundColor: "rgba(0,0,0,0.45)",
          zIndex: 1,
        }}
      />

      {/* CONTENT */}
      <div
        style={{
          position: "relative",
          zIndex: 2,
          height: "100%",
          display: "flex",
          alignItems: "center",
          padding: "0 80px",
          color: "#fff",
          maxWidth: "700px",
        }}
      >
        <div>
          <h1 style={{ fontSize: "3.2rem", marginBottom: "20px" }}>
            Fashion Trends <br /> Across the Globe
          </h1>

          <p style={{ fontSize: "1.2rem", lineHeight: "1.6", opacity: 0.9 }}>
            Discover how style evolves from Indian streets to global runways.
            Curated trends, cultural stories, and modern fashion insights.
          </p>

          <div style={{ marginTop: "30px" }}>
            <button
              style={{
                padding: "14px 28px",
                fontSize: "1rem",
                borderRadius: "8px",
                border: "none",
                cursor: "pointer",
                backgroundColor: "#fff",
                color: "#000",
                marginRight: "14px",
              }}
            >
              Explore Trends
            </button>

            <button
              style={{
                padding: "14px 28px",
                fontSize: "1rem",
                borderRadius: "8px",
                border: "1px solid #fff",
                backgroundColor: "transparent",
                color: "#fff",
                cursor: "pointer",
              }}
            >
              India & Global
            </button>
          </div>
        </div>
      </div>
    </section>
  );
}

export default Hero;
