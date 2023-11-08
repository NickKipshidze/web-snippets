export default function TasksCard(props: any) {
    return <div className="tasks-card">
        {props.children}
        <button>+</button>
    </div>
}