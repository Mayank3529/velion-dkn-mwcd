document.addEventListener("submit", e => e.preventDefault());
const API = "http://127.0.0.1:5000/api/knowledge";

// HARD STOP for any form submission
window.addEventListener("submit", function (e) {
    e.preventDefault();
    e.stopPropagation();
});

// ---------------- LOGIN ----------------
function login() {
    const token = document.getElementById("token").value;
    if (!token) {
        alert("Please enter token");
        return;
    }
    localStorage.setItem("token", token);
    window.location.href = "upload.html";
}

// ---------------- LOGOUT ----------------
function logout() {
    localStorage.removeItem("token");
    window.location.href = "index.html";
}

// ---------------- UPLOAD ----------------
function upload() {
    const token = localStorage.getItem("token");
    if (!token) {
        alert("Please login again");
        return;
    }

    fetch(API, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "X-USER-TOKEN": token
        },
        body: JSON.stringify({
            title: document.getElementById("title").value,
            description: document.getElementById("description").value,
            contentType: document.getElementById("contentType").value
        })
    })
    .then(res => res.json())
    .then(data => {
        alert(data.message || "Uploaded successfully");
        document.getElementById("title").value = "";
        document.getElementById("description").value = "";
        document.getElementById("contentType").value = "";
    })
    .catch(() => alert("Upload failed"));
}

// ---------------- LOAD / SEARCH ----------------
function loadKnowledge() {
    console.log("Search clicked — page is NOT reloading");

    const token = localStorage.getItem("token");
    const query = document.getElementById("search").value;

    let url = "http://127.0.0.1:5000/api/knowledge";
    if (query) {
        url += "?q=" + encodeURIComponent(query);
    }

    fetch(url, {
        headers: {
            "X-USER-TOKEN": token
        }
    })
    .then(res => res.json())
    .then(data => {
        const results = document.getElementById("results");
        results.innerHTML = "";

        if (!Array.isArray(data) || data.length === 0) {
            results.innerHTML = "<p style='text-align:center;'>No results found</p>";
            return;
        }

        data.forEach(item => {
            results.innerHTML += `
                <div class="card result-card">
                    <h4>${item.title}</h4>
                    <p>${item.description}</p>
                    <span class="badge">${item.content_type}</span>
                </div>
            `;
        });
    });
}
