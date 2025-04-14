function addComment() {
    const commentSection = document.getElementById("comments-section");
    const newComment = document.createElement("div");
    newComment.classList.add("comment-box");
    newComment.innerHTML = `
      <div class="comment-header">
        <span>user_id - ${new Date().toLocaleString()}</span>
        <span class="heart">&#10084;</span>
      </div>
      <div class="comment-body">
        New comment added!
      </div>
    `;
    commentSection.appendChild(newComment);
  }
  