function Footer() {
  return (
    <footer
      style={{
        padding: "30px 80px",
        borderTop: "1px solid #eee",
        marginTop: "60px",
        color: "#666",
        fontSize: "0.9rem",
      }}
    >
      © {new Date().getFullYear()} Fashion Trend Platform · India & Global
    </footer>
  );
}

export default Footer;
