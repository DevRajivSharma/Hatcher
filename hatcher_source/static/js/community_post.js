
document.addEventListener("DOMContentLoaded", function () {
    document.querySelectorAll(".like-btn").forEach(button => {
        button.addEventListener("click", function (e) {
            e.preventDefault();
            
            const postId = this.getAttribute("data-post-id");
            const icon = this.querySelector("i");

            // Toggle the like icon appearance
           console.log(icon.classList)
           

            // Send AJAX request to toggle like
            fetch(`/community_post/toggle_like/${postId}/`, {
                method: "POST",
                headers: {
                    "X-CSRFToken": "{{ csrf_token }}",
                    "Content-Type": "application/json",
                },
                

            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    if (data.liked) {
                        icon.classList.remove("not-liked");
                        icon.classList.add("liked");
                    } else {
                        icon.classList.remove("liked");
                        icon.classList.add("not-liked");
                    }  // Update the `data-liked` attribute
                } else {
                    console.error("Error toggling like status.");
                }
            })
            .catch(error => console.error("Request failed:", error));
        });
    });
});
