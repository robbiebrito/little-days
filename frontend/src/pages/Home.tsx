
import Header from "../components/Header"
import WeekOverview from "../components/WeekOverview"
import ModuleOverview from "../components/ModuleOverview"

function Home() {
  return (
    <div className="home" id="home">

      <Header />

      <main className="home-content">
        <section className="welcome">

          <div className="welcome-content">
            <span className="date">YOUR LITTLE CORNER OF THE WORLD ♡</span>

            <h1>Hello, lovely!</h1>

            <p className="subtitle">
              A new day, a new chance to enjoy the little things.
            </p>
          </div>

          <div className="welcome-decoration">
            <span>🌷</span>
            <span>☁️</span>
            <span>♡</span>
          </div>

        </section>

        <WeekOverview />
        <ModuleOverview />

      </main>

    </div>
  )
}

export default Home
