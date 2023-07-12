const API = "http://192.168.100.5:8000";

const commentForm = document.getElementById("comment-form");

commentForm.addEventListener("submit", async (event) => {
    event.preventDefault();

    const content = document.getElementById("content").value;
    const author = document.getElementById("author").value;

    const data = {
        "content": content,
        "author": author
    };

    try {
        const response = await fetch(API + "/comments/new", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(data)
        });

        if (response.ok) {
            const result = await response.json();
            console.log(result);
            location.reload();
        }
    } catch (error) {
        console.log("Error:", error.message);
    }
});

const checkAPIStatus = async () => {
    try {
        const response = await fetch(API);

        if (response.ok) {
            console.log("API is up and running");
        } else {
            console.log("API is down");
            window.location.href = "./error.html";
        }
    } catch (error) {
        console.log("API is down");
        window.location.href = "./error.html";
    }
};

async function getComments() {
    const response = await fetch(API + "/comments");
    const comments = response.json();

    return comments;
}

async function outputComments() {
    const commentsContainer = document.getElementById("comments");
    const comments = await getComments();

    for (comment of comments.reverse()) {
        commentsContainer.innerHTML += `
            <div class="comment">
                <h1>${comment.author}</h1>
                <p>${comment.content}</p>
            </div>
        `;
    }
}

checkAPIStatus();
outputComments();