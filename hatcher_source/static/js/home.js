document.getElementById('search-box').addEventListener('click',()=>{
    const search_div = document.getElementById('search-div');
    const job_type_select = document.getElementById('job_type_select');
    search_div.classList.remove('visually-hidden');
    job_type_select.focus();
});