
function WeekOverview() {
  const days = [
    { day: "MON", icon: "☀️", temperature: "24°" },
    { day: "TUE", icon: "🌤️", temperature: "22°" },
    { day: "WED", icon: "☁️", temperature: "20°" },
    { day: "THU", icon: "🌷", temperature: "23°" },
    { day: "FRI", icon: "☀️", temperature: "25°" },
    { day: "SAT", icon: "🌤️", temperature: "26°" },
    { day: "SUN", icon: "☀️", temperature: "27°" }
  ]

  return (
    <section className="week-overview">

      <div className="week-text">
        <span className="week-label">YOUR WEEK AT A GLANCE</span>

        <h2>A fresh week, a fresh start ♡</h2>

        <p>
          Make room for the little things that make you happy.
        </p>
      </div>

      <div className="weather-content">

        <div className="weather-main">
          <span className="weather-icon">☀️</span>

          <div>
            <strong>24°</strong>
            <p>Sunny and lovely</p>
          </div>
        </div>

        <div className="weather-days">
          {days.map((item) => (
            <div className="weather-day" key={item.day}>
              <span>{item.day}</span>
              <span>{item.icon}</span>
              <strong>{item.temperature}</strong>
            </div>
          ))}
        </div>

      </div>

    </section>
  )
}

export default WeekOverview
