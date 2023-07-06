// uvicorn URL here
const API = "http://0.0.0.0";

const commentsContainer = document.getElementById("chat");
const messageInput = document.getElementById("message-input");
const usernameInput = document.getElementById("username-input");
let comments = [];

// Working on fixing this
(async function updateChat() {
    const data = await fetch(API + "/comments")
        .then(function (response) {
            if (response.ok) {
                return response.json()
            } else {
                console.log("Something's fucked up");
            }
        });

    if (comments.length < data.length) {
        commentsContainer.innerHTML = "";

        for (comment of data) {
            commentsContainer.innerHTML += `
                <div class="comment">
                    <h1>${comment.user}</h1>
                    <p>${comment.content}<p>
                </div>
            `;
        }
        comments = data;

        commentsContainer.scrollTop = commentsContainer.scrollHeight;
    }

    setTimeout(updateChat, 1000);
})();

messageInput.addEventListener("keydown", function (event) {
    if (event.key === "Enter") {
        event.preventDefault();
        const message = messageInput.value;
        const user = usernameInput.value;

        fetch(API + "/comment", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                user: user,
                content: message
            })
        })

        messageInput.value = "";
    }
});
