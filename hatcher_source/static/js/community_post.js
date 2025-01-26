function like_toggle(e) {
    // Find the closest <p> element that contains the data-post-id attribute
    const postElement = e.target.closest('[data-post-id]');
    
    if (!postElement) {
        console.error("Post element not found.");
        return;
    }
    
    const postId = postElement.getAttribute("data-post-id"); // Access the data-post-id from the closest <p>
    // alert("Id is " + postId);  // Verify that postId is correctly retrieved
    
    const icon = postElement.querySelector("i"); // Get the icon inside the clicked element
    const slike = postElement.querySelector('span'); // Get the span inside the clicked element

    // Send AJAX request to toggle like
    fetch(`/community_post/toggle_like/${postId}/`, {
        method: "POST",
        headers: {
            "X-CSRFToken": "{{ csrf_token }}",
            "Content-Type": "application/json",
        }
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            if (data.liked) {
                icon.classList.remove("not-liked");
                icon.classList.add("liked");
                slike.innerHTML = +(slike.innerHTML) + 1;
            } else {
                icon.classList.remove("liked");
                icon.classList.add("not-liked");
                slike.innerHTML = +(slike.innerHTML) - 1;
            }
        } else {
            console.error("Error toggling like status.");
        }
    })
    .catch(error => console.error("Request failed:", error));
}




const my_post = document.getElementById('my-post');
const container1 = document.querySelector('.container1');

my_post.addEventListener('click', () => {
    fetch('/community_post/my_post', {
      headers: { 'X-Requested-With': 'XMLHttpRequest' }
    })
    .then(response => response.text()) // Parse plain HTML as text
    .then(html => {
      container1.innerHTML = html;
    })
    .catch(error => {
      console.error('Error fetching posts:', error);
    });
  });



function delete_post(id){
    fetch(`/community_post/delete_post/?post_id=${id}`, {
        headers: { 'X-Requested-With': 'XMLHttpRequest' }
    })
    .then(response => response.text()) // Parse plain HTML as text
    .then(html => {
    container1.innerHTML = html;
    })
    .catch(error => {
    console.error('Error fetching posts:', error);
    });
}
