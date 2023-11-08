import styles from "./page.module.css"
import TasksCard from "@/components/tasks-card"

export default function Home() {
  return (
    <>
      <TasksCard>
        <h1>November 8</h1>
        <h3>Subtitle</h3>
        <div>
          <input type="checkbox" />
          <p>Item 1</p>
        </div>
        <div>
          <input type="checkbox" />
          <p>Item 2</p>
        </div>
        <div>
          <input type="checkbox" />
          <p>Item 3</p>
        </div>
      </TasksCard>
      <button className="add-day-btn">+</button>
    </>
  )
}
