const image = document.querySelector(".hatcher-logo");
const timeline_hatcher = gsap.timeline({ defaults: { duration: 1, ease: "bounce.out"},repeat:-1 ,repeatDelay:2});

  timeline_hatcher.fromTo(
    image,
    {
      scale: 0.5
    },
    {
      scale: 1,
      ease: "bounce.out"
    }
  );

const price_cards = document.querySelectorAll(".price_card");
price_cards.forEach((card) => {
    card.addEventListener("mouseover", () => {
        gsap.to(card, {
            duration: 0.5,
            scale: 1.1,
            ease: "power2.out"
        });
        
    });
    card.addEventListener("mouseout", () => {
        gsap.to(card, {
            duration: 0.5,
            scale: 1,
            ease: "power2.out"
        });
    });
});

// Shake animation
const shake = document.querySelectorAll(".shake");

// Create a GSAP timeline
const timeline = gsap.timeline({ defaults: { duration: 0.8, ease: "power2.out"},repeat:-1 ,repeatDelay:0.5});

// Loop through each element and add animations to the timeline
shake.forEach((element) => {
    timeline.to(element, {
        scale: 1.1,
        ease: "power2.out"
    }).to(element, {
        scale: 1,
        ease: "power2.out"
    });
});


setInterval(function(){
    const word = document.getElementById("alternate_word");
    let val = word.innerText
    if (val == 'Learning'){
        word.style.color='rgb(85, 81, 255)';
        word.innerHTML='Growing ';
    }
    else if (val == 'Growing'){
        word.style.color='rgb(199, 185, 255)';
        word.innerHTML='Achieving ';
    }
    else if (val == 'Achieving'){
        word.style.color='rgb(15, 169, 88)';
        word.innerHTML='Exploring ';
    }
    else if (val == 'Exploring'){
        word.style.color='rgb(169, 84, 15)';
        word.innerHTML='Hiring ';
    }
    else{
        word.style.color='rgb(15, 169, 88)';
        word.innerHTML='Learning';
    }
},3000);